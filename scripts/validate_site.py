#!/usr/bin/env python3
"""Validate the exported portfolio without a browser."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
from lxml import html, etree
from PIL import Image
import json, re, sys

root=Path(__file__).resolve().parents[1]/'dist'
errors=[]
documents={}
for path in sorted(root.glob('*.html')):
    tree=html.document_fromstring(path.read_text())
    documents[path.name]=tree
    ids=[x.get('id') for x in tree.xpath('//*[@id]')]
    errors.extend(f'{path.name}: duplicate id {id}' for id,count in Counter(ids).items() if count>1)
    for name,xpath in [('h1','//h1'),('main','//main'),('description','//meta[@name="description"]'),('canonical','//link[@rel="canonical"]')]:
        if len(tree.xpath(xpath))!=1: errors.append(f'{path.name}: expected one {name}')
    if tree.xpath('//a//a | //a//button | //button//a'):
        errors.append(f'{path.name}: nested interactive element')
    for a in tree.xpath('//a[@target="_blank"]'):
        if 'noopener' not in a.get('rel',''):errors.append(f'{path.name}: external link lacks noopener')
    for image in tree.xpath('//img'):
        if 'alt' not in image.attrib:errors.append(f'{path.name}: image lacks alt')
        if image.get('src'):
            local=root/image.get('src')
            if local.is_file():
                with Image.open(local) as im:
                    expected=(image.get('width'),image.get('height'))
                    if all(expected) and tuple(map(int,expected))!=im.size:errors.append(f'{path.name}: wrong dimensions {local.name}')
    for button in tree.xpath('//button'):
        if not button.get('aria-label') and not ''.join(button.itertext()).strip():
            errors.append(f'{path.name}: unlabeled button')
    for element in tree.xpath('//*[@aria-controls] | //*[@aria-labelledby]'):
        for attr in ['aria-controls','aria-labelledby']:
            for id in element.get(attr,'').split():
                if id not in ids:errors.append(f'{path.name}: {attr} references absent {id}')
    for data in tree.xpath('//script[@type="application/ld+json"]/text()'):
        try:json.loads(data)
        except Exception:errors.append(f'{path.name}: invalid structured data')

local_refs=0
archive_data=root.parent/'scripts/additional_projects.json'
if archive_data.is_file():
    for project in json.loads(archive_data.read_text())['projects']:
        filename=project['slug']+'.html'
        page=documents.get(filename)
        if page is None:
            errors.append('Project archive: missing page '+filename)
            continue
        proofs=page.xpath('//figure[contains(concat(" ",normalize-space(@class)," ")," rx-proof ")]')
        if len(proofs)!=len(project['proofs']):errors.append(filename+': source-example count differs')
        for rendered,example in zip(proofs,project['proofs']):
            if ''.join(rendered.xpath('.//pre/code//text()'))!=example['code']:
                errors.append(filename+': source excerpt changed')
            if example['url'] not in rendered.xpath('.//a/@href'):
                errors.append(filename+': exact source link missing')

for name,tree in documents.items():
    for element in tree.xpath('//*[@href] | //*[@src] | //*[@data-zoom]'):
        for attr in ['href','src','data-zoom']:
            target=element.get(attr)
            if not target:continue
            u=urlsplit(target)
            if u.scheme or u.netloc:continue
            file=unquote(u.path) or name
            path=(root/file).resolve()
            if root.resolve() not in [path,*path.parents]:errors.append(f'{name}: escapes document root {target}');continue
            if not path.is_file():errors.append(f'{name}: missing resource {target}');continue
            local_refs+=1
            if u.fragment and path.suffix=='.html' and path.name in documents:
                if not documents[path.name].xpath('//*[@id=$id]',id=unquote(u.fragment)):
                    errors.append(f'{name}: absent fragment {target}')
for stylesheet in root.glob('*.css'):
    css=stylesheet.read_text()
    for item in re.findall(r'url\(([^)]+)\)',css):
        file=item.strip("'\"")
        if not file.startswith(('data:','https:','#')) and not (root/file).is_file():
            errors.append(f'{stylesheet.name}: missing '+file)
    if css.count('{')!=css.count('}'):errors.append(f'{stylesheet.name}: unmatched block braces')

engineering=documents.get('collabrium-engineering.html')
evidence_path=root.parent/'scripts/collabrium_evidence.json'
if engineering is not None and evidence_path.is_file():
    evidence=json.loads(evidence_path.read_text())
    proofs=engineering.xpath('//details[contains(concat(" ",normalize-space(@class)," ")," ce-proof ")]')
    if len(proofs)!=len(evidence['examples']):errors.append('Engineering: source-example count differs from evidence')
    for proof,example in zip(proofs,evidence['examples']):
        rendered=''.join(proof.xpath('.//pre/code//text()'))
        if rendered!=example['code']:errors.append('Engineering: source excerpt changed: '+example['id'])
        links=proof.xpath('.//a/@href')
        if not any('/'+evidence['commit']+'/' in link and link.endswith(f"#L{example['start_line']}-L{example['end_line']}") for link in links):
            errors.append('Engineering: exact source link missing: '+example['id'])
for name,tree in documents.items():
    for el in tree.xpath('//svg'):
        try:etree.fromstring(etree.tostring(el,with_tail=False))
        except Exception as e:errors.append(f'{name}: invalid SVG {e}')

def luminance(s):
    rgb=[int(s[i:i+2],16)/255 for i in [1,3,5]]
    rgb=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in rgb]
    return sum(c*w for c,w in zip(rgb,[.2126,.7152,.0722]))
for fg,bg in [('#62645e','#f8f7f3'),('#b84d2e','#f8f7f3'),('#fff3e8','#b84d2e'),('#adbaa5','#18201b')]:
    a,b=sorted([luminance(fg),luminance(bg)],reverse=True)
    ratio=(a+.05)/(b+.05)
    if ratio<4.5:errors.append(f'Low contrast: {fg} / {bg} = {ratio:.2f}')
fonts=list((root/'assets').glob('*.ttf'))
for font in fonts:
    if font.read_bytes()[:4] not in [b'\x00\x01\x00\x00',b'OTTO']:
        errors.append('Invalid font '+font.name)
for error in errors:print('ERROR',error)
print(json.dumps({'pages':len(documents),'local_references_checked':local_refs,'fonts':len(fonts),'total_asset_bytes':sum(p.stat().st_size for p in root.rglob('*') if p.is_file()),'errors':len(errors),'browser_qa':'unavailable'},indent=2))
sys.exit(bool(errors))

