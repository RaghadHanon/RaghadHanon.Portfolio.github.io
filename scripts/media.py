"""Real Collabrium recordings, product screens, and project documents."""
from components import *
from PIL import Image
import math
import json
import re

MEDIA=DIST/'assets/media'
RECORDINGS=[
    ('projects-tasks-demo.mp4','Project & work-item delivery','Follow project planning, work items, and the delivery workflow.','05:56'),
    ('tenant-teams-demo.mp4','Tenant, users & teams','Explore the organization workspace and the people and teams inside it.','03:26'),
    ('reports-demo.mp4','Reports & analytics','See the reporting workflow and the analytical views of project work.','04:14'),
    ('learning-hub-demo.mp4','Learning Hub','Explore roadmaps, courses, assignments, and shared learning resources.','03:13'),
    ('multi-tenant-architecture.mp4','Multi-Tenant Architecture','A visual overview of Collabrium’s tenant structure and role hierarchy.','00:48')
]
SCREENS = json.loads((ROOT/'scripts/module_screens.json').read_text())
PROMOS=[
    ('demo-1.webp','Meet Collabrium','Our graduation team and the platform we delivered.'),
    ('demo-2.webp','The challenge','The fragmented workflows that motivated the project.'),
    ('demo-3.webp','The solution','A connected workspace for the organization.'),
    ('demo-4.webp','The platform modules','The major parts of Collabrium in one overview.')
]

def media_image(path,alt,cls='',lazy=True):
    file=DIST/'assets'/path
    with Image.open(file) as im: width,height=im.size
    return f'<img src="assets/{path}" alt="{escape(alt,quote=True)}" width="{width}" height="{height}" class="{cls}" loading="{"lazy" if lazy else "eager"}" decoding="async">'

def video_gallery(prefix):
    cards=[]
    for i,(file,title,summary,duration) in enumerate(RECORDINGS):
        poster='assets/media/'+file.replace('.mp4','-poster.jpg')
        cards.append(f'''<article class="demo-card"><div class="video-frame"><video controls playsinline preload="none" poster="{poster}" width="1440" height="810" aria-labelledby="{prefix}-video-title-{i}"><source src="assets/media/{file}" type="video/mp4"><a href="assets/media/{file}">Download this recording</a></video><span class="video-duration mono" aria-hidden="true">{duration}</span></div><div class="demo-card-body"><span class="label">Original recording / {i+1:02}</span><h3 id="{prefix}-video-title-{i}">{title}</h3><p>{summary}</p></div></article>''')
    return '<div class="demo-grid">'+''.join(cards)+'</div><p class="media-footnote">Use the player’s full-screen control to inspect the interface in detail. Recordings play on request.</p>'

def screen_explorer(prefix):
    panels=[]
    buttons=[]
    for i,screen in enumerate(SCREENS):
        file,title,caption=screen['asset'],screen['group'],screen['caption']
        id=prefix+'-screen-'+str(i)
        panels.append(f'''<figure class="screen-panel" id="{id}"><button class="image-zoom" type="button" data-zoom="assets/{file}" data-caption="{escape(caption,quote=True)}" aria-label="Expand {escape(title,quote=True)} screenshot">{media_image(file,title+' — '+screen['screen_title'])}</button><figcaption><strong>{title}</strong><span>{caption}</span></figcaption></figure>''')
        buttons.append(f'<button type="button" class="screen-choice" data-screen-choice="{id}" aria-controls="{id}" aria-pressed="{str(i==0).lower()}">{title}</button>')
    return f'''<div class="screen-explorer" data-screen-explorer><div class="screen-choices" role="group" aria-label="Choose a Collabrium screen">{''.join(buttons)}</div><div class="screen-stage">{''.join(panels)}</div><p class="media-footnote">Categories match the folders in the original screens archive. Select a module to see its overview, then open the image for a closer look.</p></div>'''

def resources():
    docs=[
      ('docs/Collabrium-Thesis.pdf','docs/thesis-cover.webp','Final project thesis','272 pages / PDF','Requirements, system design, domain models, and the implementation walkthrough.','Read the thesis'),
      ('docs/Collabrium-Presentation.pptx','docs/presentation-cover.webp','Graduation project presentation','53 slides / PowerPoint','The updated graduation presentation, including platform workflows and product demonstrations.','Download the presentation')
    ]
    cards=[]
    for file,cover,title,label,description,action in docs:
        size=(205855172 if file.endswith('.pptx') else (DIST/'assets'/file).stat().st_size)/(1024*1024)
        cards.append(f'''<article class="resource-card"><a class="resource-preview" href="{'presentation.html' if file.endswith('.pptx') else 'assets/'+file}" target="_blank" rel="noopener" aria-label="{action}">{media_image(cover,title+' cover')}</a><div><span class="label">{label}</span><h3>{title}</h3><p>{description}</p><a class="resource-action" href="{'presentation.html' if file.endswith('.pptx') else 'assets/'+file}" target="_blank" rel="noopener">{action}<span>{size:.1f} MB</span>{arrow()}</a></div></article>''')
    return '<div class="resource-grid">'+''.join(cards)+'</div>'

def promo_gallery(prefix):
    cards=[]
    for file,title,caption in PROMOS:
        cards.append(f'''<figure class="promo-card"><button class="image-zoom" type="button" data-zoom="assets/media/{file}" data-caption="{escape(caption,quote=True)}" aria-label="Expand {escape(title,quote=True)} project image">{media_image('media/'+file,title)}</button><figcaption><strong>{title}</strong><span>{caption}</span></figcaption></figure>''')
    joined=''.join(cards)
    return f'<div class="promo-gallery" id="{prefix}-promos" tabindex="0" aria-label="Four Collabrium project story images">{joined}</div><p class="media-footnote">Four original project visuals. Open an image to read it at full size.</p>'

def home_media():
    return f'''<section class="section writing project-showcase" id="showcase" aria-labelledby="writing-title"><div class="wrap"><div class="section-head reveal"><div><div class="eyebrow">05 / Inside the product</div><h2 id="writing-title">A closer look at the work.</h2></div><p>Real workflows, original recordings, and the documents behind Collabrium. Explore the finished product and the thinking that shaped it.</p></div><div class="showcase-subhead"><div><span class="label">01 / Watch</span><h3>The platform in motion.</h3></div><a class="text-link" href="collabrium.html#demo">View the case study {arrow()}</a></div>{video_gallery('home')}<div class="showcase-subhead"><div><span class="label">02 / Explore</span><h3>The interface, up close.</h3></div><a class="text-link" href="collabrium.html#project-story">Meet the project {arrow()}</a></div>{screen_explorer('home')}<a class="text-link archive-all-link" href="collabrium.html#walkthrough">Explore all 202 screens {arrow('right')}</a><div class="showcase-subhead"><div><span class="label">03 / Read</span><h3>The research behind the build.</h3></div></div>{resources()}{linkedin_series()}</div></section>'''



def linkedin_series():
    links=['dQ93CzKb','d7pM5biD','daM3mNSy','dVii-Cc9','d34BXFRV','dQHDbSVw']
    titles=['Introducing Collabrium','Collabrium series · Part 02','Collabrium series · Part 03','Collabrium series · Part 04','From project setup to sprint delivery','Reports, analytics & AI insights']
    cards=''.join(f'<li>{ext("https://lnkd.in/p/"+link, f"<span class=\"mono\">{i+1:02}</span><span>{title}</span>","series-link")}</li>' for i,(link,title) in enumerate(zip(links,titles)))
    return '<div class="build-notes"><span class="label">Collabrium / LinkedIn series</span><h3>The development story, in order.</h3><ol class="linkedin-series">'+cards+'</ol></div>'

def full_screen_gallery():
    files=json.loads((ROOT/'scripts/all_screens.json').read_text())
    groups=sorted(set(f['group'] for f in files))
    result=[f'<p>All {len(files)} application screenshots from the project archive, organized by module. Open a module, then select any screen to view it at full size.</p>']
    for group in groups:
        items=sorted([f for f in files if f['group']==group],key=lambda f:f['title'].lower())
        title=group
        result.append(f'<details class="archive-group"><summary><strong>{escape(title)}</strong><span class="mono">{len(items)} screens</span></summary><div class="archive-grid">')
        for f in items:
            label=re.sub(r'(?<=[a-z])(?=[A-Z])',' ',Path(f['title']).stem)
            caption=title+' / '+label
            result.append(f'<figure><button class="image-zoom" type="button" data-zoom="assets/{f["asset"]}" data-caption="{escape(caption,quote=True)}" aria-label="Expand {escape(caption,quote=True)}">{media_image(f["asset"],caption)}</button><figcaption>{escape(label)}</figcaption></figure>')
        result.append('</div></details>')
    return ''.join(result)
