"""Shared static portfolio components."""
from pathlib import Path
from html import escape
import json
import os

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ORIGIN = os.environ.get('PORTFOLIO_URL', 'https://raghadhanon.github.io').rstrip('/')
EMAIL = 'raghadhanoon2015@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/raghad-hanon/'
GITHUB = 'https://github.com/RaghadHanon'
CF = 'https://codeforces.com/profile/Raghad185'
C = GITHUB + '/Collabrium/blob/01aa3dd11fe0b888f54de64314ec3ca2aeb4ca1a/'
A = GITHUB + '/Actify/blob/2d2204fc04000f73354a956c1841d26846cacb70/'
H = GITHUB + '/HotelBookingPlatform/blob/f469dcc3dafa81ccd2478bebfd161a4150f62b7d/'
REPORT_POST = 'https://www.linkedin.com/posts/raghad-hanon_collabrium-dataanalytics-reporting-activity-7512136188053389313-tXdt'
AGILE_POST = 'https://www.linkedin.com/posts/raghad-hanon_post-05-from-project-setup-to-sprint-delivery-activity-7490126858164789248-mgZ-'
HEBRON_POST = 'https://www.linkedin.com/posts/raghad-hanon_hello-lets-talk-about-the-hebron-code-jam-activity-7060148629621063680-W1Fo'

def arrow(kind='up'):
    d = {'up':'M5 15 15 5M5 5h10v10','right':'M4 10h12M11 5l5 5-5 5','down':'M10 3v14M5 12l5 5 5-5','left':'M16 10H4M9 5l-5 5 5 5'}[kind]
    return f'<svg class="arrow" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="{d}"/></svg>'

def ext(href,label,cls='',icon=True):
    return f'<a href="{escape(href,quote=True)}" class="{cls}" target="_blank" rel="noopener noreferrer">{label}{arrow() if icon else ""}</a>'

def tags(items):
    return '<div class="tags">'+''.join(f'<span class="tag">{escape(x)}</span>' for x in items)+'</div>'

def header(home=False):
    base = '' if home else 'index.html'
    return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap nav">
    <a class="wordmark" href="index.html" aria-label="Raghad Hanon, home"><span class="monogram" aria-hidden="true">rh.</span><span class="wordmark-name">Raghad Hanon<span>Backend engineer</span></span></a>
    <nav class="nav-links" id="navigation" aria-label="Main navigation"><a href="{base}#work">Work</a><a href="{base}#engineering">Approach</a><a href="{base}#about">About</a><a href="{base}#recognition">Recognition</a></nav>
    <a class="nav-resume" href="assets/Raghad-Hanon-Resume.pdf?v=2f77c40aebce" target="_blank" rel="noopener">Résumé {arrow('down')}</a>
    <button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="navigation" aria-expanded="false"><span></span><span></span></button>
    </div></header>'''

def footer():
    return f'''<section class="contact" id="contact" aria-labelledby="contact-title"><div class="wrap">
    <div class="contact-grid"><div><div class="eyebrow">The next good thing starts here</div><h2 id="contact-title">Let’s build<br>something that matters.</h2><p>I’m open to junior .NET backend and software engineering opportunities. Have a role or a problem in mind? I’d love to hear about it.</p></div>
    <div class="contact-actions"><a class="button" href="mailto:{EMAIL}">Start a conversation {arrow()}</a><button class="copy-email" type="button" data-copy-email="{EMAIL}" aria-label="Copy email address">{EMAIL}<svg class="arrow" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><rect x="7" y="6" width="9" height="11" rx="1"/><path d="M12 6V3H3v10h4"/></svg></button></div></div>
    <div class="contact-socials">{ext(GITHUB,'GitHub')}{ext(LINKEDIN,'LinkedIn')}{ext(CF,'Codeforces')}<span class="location">BASED IN PALESTINE · OPEN TO REMOTE WORK</span></div></div></section>
    <footer class="footer"><div class="wrap"><span>© 2026 Raghad Hanon. Thoughtfully built, from the inside out.</span><a href="#top">Back to top {arrow('up')}</a></div></footer>
    <div class="toast" role="status" aria-live="polite"></div>
    <dialog class="lightbox" aria-label="Expanded project screenshot"><button class="close-lightbox" type="button" aria-label="Close screenshot">×</button><img alt=""><p></p></dialog>'''

def document(title,description,content,filename='index.html',home=False):
    structured = {'@context':'https://schema.org','@type':'Person','name':'Raghad Hanon','jobTitle':'.NET Backend Developer / Software Engineer','url':ORIGIN,'email':EMAIL,'sameAs':[GITHUB,LINKEDIN,CF],'alumniOf':{'@type':'CollegeOrUniversity','name':'Palestine Technical University — Kadoorie'}} if home else {'@context':'https://schema.org','@type':'CreativeWork','name':title,'creator':{'@type':'Person','name':'Raghad Hanon'},'url':ORIGIN+'/'+filename,'description':description}
    return f'''<!doctype html><html lang="en" id="top"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(description,quote=True)}"><meta name="theme-color" content="#f8f7f3"><link rel="canonical" href="{ORIGIN}/{'' if home else filename}"><meta property="og:type" content="website"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{ORIGIN}/{'' if home else filename}"><meta property="og:image" content="{ORIGIN}/assets/social-preview.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Raghad Hanon — .NET Backend Engineer. Complex ideas. Clean solutions."><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="assets/manrope-regular.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script><script type="application/ld+json">{json.dumps(structured,ensure_ascii=False)}</script></head><body>{header(home)}{content}{footer()}</body></html>'''

HERO_ART = '''<svg viewBox="0 0 600 550" role="img" aria-labelledby="system-title system-desc"><title id="system-title">Connected, by design</title><desc id="system-desc">An architectural illustration of a .NET core connected to APIs, data, authentication, and real-time services.</desc><defs><pattern id="dot-grid" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#b7bcae" opacity=".52"/></pattern><linearGradient id="copper" x1="0" x2="1" y2="1"><stop stop-color="#e5ab84"/><stop offset="1" stop-color="#ca6c46"/></linearGradient><filter id="soft-shadow" x="-50%" y="-50%" width="200%" height="220%"><feGaussianBlur stdDeviation="13"/></filter></defs><rect x="25" y="15" width="550" height="505" fill="url(#dot-grid)" opacity=".8"/><g fill="none" stroke="#c6cebf"><ellipse cx="300" cy="303" rx="241" ry="135" transform="rotate(-26 300 303)"/><ellipse cx="300" cy="303" rx="244" ry="135" transform="rotate(27 300 303)"/><path d="M65 278h470M300 60v425" stroke-dasharray="3 9" opacity=".6"/></g><g fill="none" stroke="#a8b69b" stroke-width="1.4" class="packet"><ellipse cx="300" cy="303" rx="241" ry="135" transform="rotate(-26 300 303)"/></g><ellipse cx="303" cy="416" rx="125" ry="24" fill="#53624d" opacity=".14" filter="url(#soft-shadow)"/><g><path d="m300 287 145 82-145 82-145-82Z" fill="#e4e7db" stroke="#b5bfab"/><path d="m155 369 145 82v15l-145-82Zm145 82 145-82v15l-145 82Z" fill="#c4cdb9" stroke="#b5bfab"/><path d="m300 258 145 82-145 82-145-82Z" fill="#eef0e6" stroke="#b5bfab"/><path d="m155 340 145 82v15l-145-82Zm145 82 145-82v15l-145 82Z" fill="#d6ddcb" stroke="#b5bfab"/></g><g class="floating"><path d="m300 134 125 71-125 71-125-71Z" fill="url(#copper)" stroke="#ad5b3b"/><path d="m175 205 125 71v107l-125-71Z" fill="#b95735" stroke="#a84d2f"/><path d="m300 276 125-71v107l-125 71Z" fill="#cf764e" stroke="#ae5938"/><path d="m191 220 93 53v85l-93-53Z" fill="none" stroke="#e5a17c" opacity=".65"/><path d="m315 281 95-54v75l-95 54Z" fill="none" stroke="#f1bb96" opacity=".7"/><text transform="matrix(.88 .5 0 1 210 265)" font-family="Manrope,Arial" font-weight="600" font-size="43" fill="#fff1de">C#</text><text transform="matrix(.88 -.5 0 1 332 315)" font-family="Manrope,Arial" font-weight="500" font-size="24" fill="#fff0db">.NET</text><path d="m268 204 32-18 32 18-32 18Z" fill="none" stroke="#fff1de" stroke-width="1.6"/><path d="m285 194 31 18m-32 1 32-18" stroke="#fff1de" stroke-width="1.3"/></g><g font-family="Manrope,Arial"><g transform="translate(32 121)"><rect width="171" height="66" rx="8" fill="#f8f7f3" stroke="#c9cebf"/><rect x="12" y="14" width="35" height="35" rx="7" fill="#e5e9dc"/><path d="m23 25-4 6 4 6m12-12 4 6-4 6m-6-15-2 18" stroke="#68775d" stroke-width="1.2" fill="none"/><text x="58" y="29" font-size="13" font-weight="600" fill="#343d30">REST APIs</text><text x="58" y="46" font-size="9" fill="#75806b">Clear contracts.</text></g><g transform="translate(390 82)"><rect width="168" height="67" rx="8" fill="#f8f7f3" stroke="#c9cebf"/><path d="m28 18 13 6v12c0 9-13 14-13 14s-13-5-13-14V24Z" fill="#e5e9dc" stroke="#7c8b6d"/><path d="m22 33 4 4 8-9" stroke="#647554" stroke-width="1.6" fill="none"/><text x="56" y="30" font-size="13" font-weight="600" fill="#343d30">Identity</text><text x="56" y="47" font-size="9" fill="#75806b">The right access.</text></g><g transform="translate(412 369)"><rect width="157" height="66" rx="8" fill="#f8f7f3" stroke="#c9cebf"/><ellipse cx="28" cy="22" rx="13" ry="5" fill="#e5e9dc" stroke="#7c8b6d"/><path d="M15 22v21c0 7 26 7 26 0V22M15 32c0 7 26 7 26 0" fill="none" stroke="#7c8b6d"/><text x="55" y="29" font-size="13" font-weight="600" fill="#343d30">SQL Server</text><text x="55" y="46" font-size="9" fill="#75806b">Data, connected.</text></g><g transform="translate(31 389)"><rect width="165" height="66" rx="8" fill="#f8f7f3" stroke="#c9cebf"/><circle cx="30" cy="33" r="17" fill="#e5e9dc"/><path d="m33 20-10 15h9l-4 12 12-18h-9Z" stroke="#75866a" fill="none" stroke-linejoin="round"/><text x="58" y="29" font-size="13" font-weight="600" fill="#343d30">SignalR</text><text x="58" y="46" font-size="9" fill="#75806b">Conversations, live.</text></g></g><g fill="#f8f7f3" stroke="#879778"><circle cx="76" cy="277" r="5"/><circle cx="500" cy="235" r="5"/><circle cx="298" cy="75" r="4"/></g><text x="300" y="510" text-anchor="middle" font-family="monospace" font-size="9" letter-spacing="3" fill="#89927c">STRUCTURED. CONNECTED. PURPOSEFUL.</text></svg>'''

ACTIFY_ART = '''<svg viewBox="0 0 600 350" role="img" aria-label="Actify activity, attendance, and discussion model"><defs><pattern id="a-grid" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#c0a998" opacity=".6"/></pattern></defs><rect x="10" y="10" width="580" height="330" fill="url(#a-grid)"/><circle cx="300" cy="179" r="112" fill="none" stroke="#c3a793"/><circle cx="300" cy="179" r="139" fill="none" stroke="#cfbba9" stroke-dasharray="3 7"/><path d="m109 113 191 66 190-71M300 179v127" stroke="#ad8067" stroke-width="1.2" fill="none"/><g><rect x="233" y="112" width="134" height="134" rx="26" fill="#b15d3c"/><path d="m285 155-22 53h15l8-20h29l8 20h16l-22-53Zm6 21 10-24 10 24" fill="#faeddb"/><text x="300" y="231" text-anchor="middle" font-family="Manrope,Arial" font-size="15" font-weight="600" fill="#fff0dc">Actify</text></g><g font-family="Manrope,Arial"><g transform="translate(30 69)"><rect width="161" height="85" rx="12" fill="#f8f4ec" stroke="#cdb7a4"/><rect x="15" y="15" width="28" height="28" rx="6" fill="#e8d7c8"/><path d="M21 22h16v15H21Zm4-3v6m8-6v6M21 28h16" fill="none" stroke="#95684e"/><text x="55" y="32" font-size="13" fill="#4c4034">Activities</text><text x="17" y="65" font-size="10" fill="#8e7868">Discover · Create · Join</text></g><g transform="translate(409 65)"><rect width="161" height="85" rx="12" fill="#f8f4ec" stroke="#cdb7a4"/><circle cx="29" cy="25" r="7" fill="none" stroke="#95684e"/><path d="M17 44c0-14 24-14 24 0" fill="none" stroke="#95684e"/><text x="54" y="32" font-size="13" fill="#4c4034">People</text><text x="17" y="65" font-size="10" fill="#8e7868">Profiles · Follow · Attend</text></g><g transform="translate(222 271)"><rect width="156" height="58" rx="12" fill="#f8f4ec" stroke="#cdb7a4"/><path d="M17 18h22v14H25l-7 5v-5h-1Z" fill="none" stroke="#95684e"/><text x="50" y="33" font-size="12" fill="#4c4034">Live discussion</text></g></g></svg>'''

HOTEL_ART = '''<svg viewBox="0 0 600 350" role="img" aria-label="Hotel Booking API, from room search to booking and invoice"><defs><pattern id="h-grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0v24" fill="none" stroke="#bdc9cb" stroke-width=".6"/></pattern></defs><rect x="20" y="15" width="560" height="320" fill="url(#h-grid)"/><g stroke="#6c8385" fill="none" stroke-width="1.3"><path d="m87 110 101-56 102 56v143l-102 57-101-57Z" fill="#edf0e9"/><path d="m87 110 101 57 102-57M188 167v143"/><path d="m110 140 19 11v28l-19-11Zm36 20 19 11v28l-19-11Zm-36 40 19 11v28l-19-11Zm36 20 19 11v28l-19-11Zm64-50 18-10v28l-18 10Zm33-19 18-10v28l-18 10Zm-33 77 18-10v28l-18 10Zm33-19 18-10v28l-18 10Z" fill="#c9d6d1"/><path d="m167 133 21-12 21 12-21 12Z" fill="#567b73"/></g><path d="M307 179h36" stroke="#688d88" stroke-width="1.5" stroke-dasharray="3 5"/><path d="m337 173 6 6-6 6" stroke="#688d88" fill="none"/><g transform="translate(357 61)"><rect x="8" y="9" width="170" height="228" rx="10" fill="#b5c5c3" opacity=".45"/><rect width="170" height="228" rx="10" fill="#f8f8f0" stroke="#a3b7b4"/><rect x="18" y="19" width="32" height="32" rx="7" fill="#dce6db"/><path d="M28 28h12m-12 6h12m-12 6h8" stroke="#5a7767"/><text x="61" y="40" font-family="Manrope,Arial" font-size="17" fill="#354b45">Invoice</text><path d="M19 68h132M19 94h74m22 0h35M19 116h74m22 0h35M19 138h74m22 0h35M19 162h132" stroke="#cad6ca"/><text x="19" y="194" font-family="monospace" font-size="10" fill="#738878">GENERATED BY THE API</text><rect x="111" y="18" width="41" height="21" rx="4" fill="#567b68"/><text x="131" y="32" font-family="monospace" font-size="10" text-anchor="middle" fill="#edf4e8">PDF</text></g><g font-family="monospace" font-size="10" letter-spacing="1.5" fill="#67817d"><text x="97" y="334">SEARCH</text><text x="261" y="334">BOOK</text><text x="429" y="334">INVOICE</text><path d="M170 330h66m66 0h102" stroke="#91a7a1" stroke-dasharray="2 4"/></g></svg>'''

ARCHITECTURE = '''<svg viewBox="0 0 760 340" role="img" aria-label="Clean Architecture: API calls Application, Application uses Domain, and Infrastructure implements application interfaces"><defs><marker id="d-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="m0 0 10 5-10 5Z" fill="#77806b"/></marker></defs><g font-family="Manrope,Arial"><rect x="22" y="35" width="200" height="120" rx="10" fill="#f9f9f1" stroke="#c4cbb9"/><text x="45" y="68" font-size="11" fill="#8b927f">01 / PRESENTATION</text><text x="45" y="102" font-size="23" fill="#343e2d">API</text><text x="45" y="130" font-size="12" fill="#7a846d">HTTP contracts &amp; policies</text><rect x="280" y="35" width="200" height="120" rx="10" fill="#e0e5d6" stroke="#aab69b"/><text x="303" y="68" font-size="11" fill="#768567">02 / USE CASES</text><text x="303" y="102" font-size="23" fill="#343e2d">Application</text><text x="303" y="130" font-size="12" fill="#6d7e5f">Commands, queries &amp; ports</text><rect x="538" y="35" width="200" height="120" rx="10" fill="#b65d3e"/><text x="561" y="68" font-size="11" fill="#f2c9aa">03 / BUSINESS CORE</text><text x="561" y="102" font-size="23" fill="#fff2df">Domain</text><text x="561" y="130" font-size="12" fill="#f5d5ba">Rules, models &amp; invariants</text><path d="M228 96h43M487 96h43" stroke="#77806b" stroke-width="1.4" marker-end="url(#d-arrow)"/><rect x="191" y="233" width="377" height="80" rx="10" fill="#f9f9f1" stroke="#b8c3ad"/><text x="217" y="267" font-size="20" fill="#343e2d">Infrastructure</text><text x="217" y="292" font-size="12" fill="#7a846d">EF Core · SQL Server · Identity · External services</text><path d="M380 226v-63" fill="none" stroke="#77806b" stroke-width="1.4" stroke-dasharray="4 4" marker-end="url(#d-arrow)"/><text x="397" y="197" font-size="11" fill="#77806b">implements ports</text></g></svg>'''

def browser_image(file,alt):
    return f'<div class="browser-frame"><div class="browser-bar" aria-hidden="true"><i></i><i></i><i></i><span>Collabrium / workspace</span></div><img src="assets/{file}" alt="{escape(alt,quote=True)}" width="1866" height="912" loading="lazy" decoding="async"></div>'

def codeblock(code):
    import re
    pattern = r'(?P<comment>//[^\n]*)|(?P<string>\$?"(?:\\.|[^"\\])*")|(?P<keyword>\b(?:public|private|protected|static|sealed|class|if|else|return|throw|await|async|var|new|void|using|while|try|catch|is|not|null|true|false|in|out|where|switch)\b)|(?P<number>\b\d+\b)'
    parts=[]
    last=0
    for match in re.finditer(pattern,code):
        parts.append(escape(code[last:match.start()]))
        parts.append('<span class="'+match.lastgroup+'">'+escape(match.group())+'</span>')
        last=match.end()
    parts.append(escape(code[last:]))
    return '<pre><code>'+''.join(parts)+'</code></pre>' 

SECURITY_CODE = '''if (!string.Equals(user.TenantId, tenant.Id,
    StringComparison.Ordinal))
{
    throw new UnauthorizedAccessException(
        "The authenticated user does not belong to this tenant.");
}

tenantContext.TenantId = tenant.Id;
tenantContext.CurrentTenant = tenant;'''
DOMAIN_CODE = '''public void Block()
{
    Guard.Against(IsDone,
        "Cannot block a completed work item.");

    IsBlocked = true;
    Touch();
}'''
REALTIME_CODE = '''var comment = await mediator.Send(
    new AddComment.Command {
        CreateCommentDto = createCommentDto
    });

await Clients.Group(createCommentDto.ActivityId)
    .SendAsync("ReceiveComment", comment.Value);'''

def engine_panel(id,label,project,code,note,href):
    return f'<div class="code-window" id="{id}" role="tabpanel" aria-labelledby="tab-{id}" tabindex="0"><div class="code-header"><span>{label}</span><span>{project} / C#</span></div>{codeblock(code)}<div class="code-note"><span>{note}</span>{ext(href,"Read the source")}</div></div>'

def decision(number,title,text,source=None):
    link=ext(source,'Explore the implementation','source-link') if source else ''
    return f'<article class="decision"><span class="mono">{number:02}</span><div><h3>{title}</h3><p>{text}</p>{link}</div></article>'

def gallery(file,alt,caption):
    return f'<figure class="gallery-item"><button type="button" class="image-zoom" data-zoom="assets/{file}" data-caption="{escape(caption,quote=True)}" aria-label="Expand: {escape(alt,quote=True)}"><img src="assets/{file}" alt="{escape(alt,quote=True)}" loading="lazy" decoding="async" width="1866" height="912"></button><figcaption>{caption}</figcaption></figure>'

def case_page(slug,title,category,subtitle,lede,role,date,context,tech,cover,caption,sections,nextslug,nexttitle):
    nav=''.join(f'<a href="#{id}">{name}</a>' for id,name,_ in sections)
    parts=''.join(f'<section class="case-section" id="{id}"><h2>{name}</h2>{html}</section>' for id,name,html in sections)
    repo={'collabrium':'Collabrium','actify':'Actify','hotel-booking':'HotelBookingPlatform'}[slug]
    body=f'''<main id="main"><section class="case-hero wrap"><div class="breadcrumb"><a href="index.html#work">Selected work</a><span>/</span><span>{title}</span></div><div class="eyebrow">{category}</div><div class="case-title-row"><h1>{title}</h1>{ext(GITHUB+'/'+repo,'View repository','button outline')}</div><p class="case-subtitle">{subtitle}</p><p class="lede">{lede}</p><dl class="case-meta"><div><dt>My role</dt><dd>{role}</dd></div><div><dt>Timeline</dt><dd>{date}</dd></div><div><dt>Context</dt><dd>{context}</dd></div></dl></section><div class="wrap">{cover}<p class="image-caption"><span>{caption}</span><span>ENGINEERING CASE STUDY</span></p></div><div class="wrap case-content"><aside class="case-sidebar" aria-label="Case study contents"><div class="label">In this case study</div>{nav}<div class="stack-list"><div class="label">Technology</div>{tags(tech)}</div></aside><div class="case-body">{parts}</div></div><section class="next-project"><div class="wrap"><a href="{nextslug}.html"><div><span class="label">Next case study</span><h2>{nexttitle}</h2></div><span class="round-arrow">{arrow('right')}</span></a></div></section></main>'''
    return document(title+' — Raghad Hanon',lede,body,slug+'.html')


COLLABRIUM_ART = '''<svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 960 480" role="img" aria-labelledby="collabrium-art-title collabrium-art-desc"><title id="collabrium-art-title">Collabrium — one connected enterprise workspace</title><desc id="collabrium-art-desc">The Collabrium logo connects project delivery, people and teams, learning, community, reporting, and AI assistance.</desc><defs><pattern id="c-grid" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#a4ac8f" opacity=".35"/></pattern></defs><rect x="16" y="16" width="928" height="448" rx="20" fill="url(#c-grid)"/><g fill="none" stroke="#b4bda4" stroke-width="1.3"><ellipse cx="480" cy="240" rx="190" ry="173"/><ellipse cx="480" cy="240" rx="218" ry="198" stroke-dasharray="3 7"/><path d="M270 94 374 198M270 240h83M270 386l104-104M690 94 586 198M690 240h-83M690 386 586 282"/></g><g><rect x="339" y="171" width="282" height="143" rx="22" fill="#cbd2bc" opacity=".4"/><rect x="332" y="163" width="282" height="143" rx="22" fill="#fff" stroke="#d4d9ca"/><image href="assets/collabrium-logo.webp" xlink:href="assets/collabrium-logo.webp" x="347" y="185" width="252" height="85" preserveAspectRatio="xMidYMid meet"/><text x="473" y="285" text-anchor="middle" font-family="Plex Mono,monospace" font-size="9" letter-spacing="1.3" fill="#6b7759">ONE CONNECTED WORKSPACE</text></g><g font-family="Manrope,Arial,sans-serif">
<g transform="translate(30 52)"><rect width="240" height="84" rx="13" fill="#f9faf5" stroke="#c5ceb8"/><rect x="15" y="19" width="40" height="40" rx="9" fill="#e2e8d7"/><path d="M25 30h20v18H25Zm6-3v24m8-24v24" fill="none" stroke="#6f8158" stroke-width="1.4"/><text x="67" y="35" fill="#354629" font-size="14" font-weight="600">Project delivery</text><text x="67" y="57" fill="#6b775f" font-size="10">Projects · Sprints · Work items</text></g>
<g transform="translate(30 198)"><rect width="240" height="84" rx="13" fill="#f9faf5" stroke="#c5ceb8"/><rect x="15" y="19" width="40" height="40" rx="9" fill="#e2e8d7"/><circle cx="35" cy="32" r="6" fill="none" stroke="#6f8158" stroke-width="1.4"/><path d="M24 49c0-13 22-13 22 0" fill="none" stroke="#6f8158" stroke-width="1.4"/><text x="67" y="35" fill="#354629" font-size="14" font-weight="600">People &amp; teams</text><text x="67" y="57" fill="#6b775f" font-size="10">Tenants · Users · Roles</text></g>
<g transform="translate(30 344)"><rect width="240" height="84" rx="13" fill="#f9faf5" stroke="#c5ceb8"/><rect x="15" y="19" width="40" height="40" rx="9" fill="#e2e8d7"/><path d="M25 28h10v23H25Zm10 0h10v23H35Z" fill="none" stroke="#6f8158" stroke-width="1.4"/><text x="67" y="35" fill="#354629" font-size="14" font-weight="600">Learning Hub</text><text x="67" y="57" fill="#6b775f" font-size="10">Courses · Roadmaps · Articles</text></g>
<g transform="translate(690 52)"><rect width="240" height="84" rx="13" fill="#f9faf5" stroke="#c5ceb8"/><rect x="15" y="19" width="40" height="40" rx="9" fill="#e2e8d7"/><path d="M24 28h22v17H34l-7 7v-7h-3Z" fill="none" stroke="#6f8158" stroke-width="1.4"/><text x="67" y="35" fill="#354629" font-size="14" font-weight="600">Community Hub</text><text x="67" y="57" fill="#6b775f" font-size="10">Posts · Events · Announcements</text></g>
<g transform="translate(690 198)"><rect width="240" height="84" rx="13" fill="#f9faf5" stroke="#c5ceb8"/><rect x="15" y="19" width="40" height="40" rx="9" fill="#e2e8d7"/><path d="M24 50V35h5v15m6 0V27h5v23m6 0V31h5v19" fill="none" stroke="#6f8158" stroke-width="1.4"/><text x="67" y="35" fill="#354629" font-size="14" font-weight="600">Reports &amp; analytics</text><text x="67" y="57" fill="#6b775f" font-size="10">Charts · PDF · Insights</text></g>
<g transform="translate(690 344)"><rect width="240" height="84" rx="13" fill="#f9faf5" stroke="#c5ceb8"/><rect x="15" y="19" width="40" height="40" rx="9" fill="#e2e8d7"/><path d="m35 26 3 8 8 3-8 3-3 8-3-8-8-3 8-3Z" fill="none" stroke="#6f8158" stroke-width="1.4"/><text x="67" y="35" fill="#354629" font-size="14" font-weight="600">AI assistance</text><text x="67" y="57" fill="#6b775f" font-size="10">Suggestions · Drafts · Skill gaps</text></g></g></svg>'''
