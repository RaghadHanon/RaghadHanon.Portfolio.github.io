"""Curated project archive, with source-linked case studies."""
from html import escape
import json
from components import ROOT, GITHUB, arrow, tags, ext, document, codeblock


def projects():
    return json.loads((ROOT / 'scripts/additional_projects.json').read_text())['projects']


def featured():
    return [
        {'slug': 'collabrium', 'title': 'Collabrium', 'number': '01',
         'context': 'Graduation project · Team Lead & Backend Developer',
         'categories': ['backend', 'full-stack'],
         'tags': ['.NET 8', 'Clean Architecture', 'CQRS', 'SignalR'],
         'metric': '13 connected modules', 'metric_label': 'One tenant-aware enterprise workspace.',
         'short': 'Project delivery, people, learning, community, reporting, and AI assistance in one connected platform.',
         'repo': 'Collabrium'},
        {'slug': 'actify', 'title': 'Actify', 'number': '02',
         'context': 'Course-based full-stack project',
         'categories': ['backend', 'full-stack'],
         'tags': ['ASP.NET Core', 'React', 'TypeScript', 'SignalR'],
         'metric': 'Activities + people', 'metric_label': 'Discovery, attendance, and live discussion.',
         'short': 'An activity-based social application connecting event discovery, attendance, profiles, and real-time comments.',
         'repo': 'Actify'},
        {'slug': 'hotel-booking', 'title': 'Hotel Booking API', 'number': '03',
         'context': 'Foothill internship project',
         'categories': ['backend', 'data'],
         'tags': ['.NET 8', 'EF Core', 'SQL Server', 'xUnit'],
         'metric': 'Search → stay', 'metric_label': 'A connected booking and invoice workflow.',
         'short': 'Hotel discovery, room management, bookings, discounts, and PDF invoices, with automated test code and a CI workflow.',
         'repo': 'HotelBookingPlatform'},
    ]


def repo_url(p):
    return GITHUB + '/' + p.get('repo', p.get('sources', [{}])[0].get('repo', ''))


def card(p, compact=False):
    searchable = ' '.join([p['title'], p['short'], *p['tags'], p['context']])
    category = escape(' '.join(p['categories']), quote=True)
    search = escape(searchable.lower(), quote=True)
    return f'''<article class="rx-card rx-{p['slug']}" data-rx-category="{category}" data-rx-search="{search}">
    <a class="rx-card-main" href="{p['slug']}.html">
      <div class="rx-card-visual"><span class="rx-card-index mono">{p['number']} / ENGINEERING</span><strong>{escape(p['metric'])}</strong><span>{escape(p['metric_label'])}</span><span class="rx-visual-lines" aria-hidden="true"></span></div>
      <div class="rx-card-heading"><h3>{escape(p['title'])}</h3>{arrow('right')}</div><p>{escape(p['short'])}</p>
    </a>
    <div class="rx-card-tags">{tags(p['tags'][:3] if compact else p['tags'])}</div>
    <div class="rx-card-foot"><span>{escape(p['context'])}</span>{ext(repo_url(p),'Repository','rx-repo-link')}</div>
    </article>'''


def additional_work():
    cards = ''.join(card(p, True) for p in projects())
    return f'''<section class="section rx-home" id="more-work" aria-labelledby="more-work-title"><div class="wrap">
    <div class="section-head"><div><div class="eyebrow">More engineering work</div><h2 id="more-work-title">Different problems.<br>More ways to build.</h2></div><div class="rx-section-intro"><p>Focused projects in testable C# design, SQL analysis, database adapters, and full-stack integration.</p><a href="projects.html" class="text-link">Explore all {len(featured()) + len(projects())} projects {arrow('right')}</a></div></div>
    <div class="rx-grid rx-compact-grid">{cards}</div></div></section>'''


def archive_page():
    all_work = featured() + projects()
    filters = [('all','All work'),('backend','Backend & APIs'),('data','Data & SQL'),('design','Design & testing'),('full-stack','Full stack'),('algorithms','Algorithms')]
    buttons = ''.join(f'<button type="button" class="rx-filter" data-rx-filter="{key}" aria-pressed="{str(key == "all").lower()}">{label}</button>' for key,label in filters)
    body = f'''<main id="main"><section class="wrap rx-archive-hero"><div class="breadcrumb"><a href="index.html">Home</a><span>/</span><span>Selected projects</span></div>
    <div class="eyebrow">The project collection</div><h1>A closer look<br>at the <em>work.</em></h1><p class="rx-archive-lede">{len(all_work)} selected projects across backend APIs, data persistence, algorithms, testable design, and full-stack integration.</p>
    <div class="rx-archive-meta"><span>{len(featured()):02} featured case studies</span><span>{len(projects()):02} additional projects</span><a href="collabrium-engineering.html">Explore Collabrium’s backend {arrow('right')}</a></div></section>
    <section class="wrap rx-collection" aria-labelledby="collection-title"><h2 class="rx-sr-only" id="collection-title">Browse the projects</h2>
    <div class="rx-controls" hidden><div class="rx-filters" role="group" aria-label="Filter projects by focus">{buttons}</div><div class="rx-search-row"><label for="project-search">Find a project or technology</label><input id="project-search" type="search" placeholder="Try MongoDB, xUnit, React…" autocomplete="off"><p class="rx-count mono" aria-live="polite">{len(all_work)} projects</p></div></div>
    <div class="rx-grid rx-archive-grid">{''.join(card(p) for p in all_work)}</div><p class="rx-empty" hidden>No projects match this search. Try another technology or choose All work.</p>
    </section><section class="wrap rx-archive-note"><span class="label">A thread through the work</span><p>Clear responsibilities, explicit data models, and workflows that connect features into a useful whole.</p><a class="text-link" href="index.html#engineering">See my engineering approach {arrow('right')}</a></section></main><script src="project-archive.js" defer></script>'''
    return document('Selected projects — Raghad Hanon', f'Explore {len(all_work)} projects in C# and .NET backend engineering, SQL, MongoDB, Java algorithms, automated testing, and React integration.', body, 'projects.html')


def diagram(p):
    """Small source-grounded system maps; deliberately not product screenshots."""
    kind = p['diagram']
    boxes, paths = [], []

    def box(x,y,w,h,title,subtitle='',dark=False):
        fill, stroke, ink, muted = ('#26332a','#26332a','#fff3e8','#d0dbc8') if dark else ('#fafaf5','#bac3b0','#28372a','#626c5c')
        boxes.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}"/><text x="{x+18}" y="{y+32}" font-size="16" font-weight="600" fill="{ink}">{escape(title)}</text><text x="{x+18}" y="{y+54}" font-size="11" fill="{muted}">{escape(subtitle)}</text></g>')

    def right(x1,y,x2):
        paths.append(f'<path d="M{x1} {y}H{x2}m-7 -5 7 5-7 5"/>')

    def down(x,y1,y2):
        paths.append(f'<path d="M{x} {y1}V{y2}m-5 -7 5 7 5-7"/>')

    caption = ''
    if kind == 'weather':
        box(24,116,185,80,'JSON or XML','Input weather reading')
        box(270,116,220,80,'Parse & notify','Strategy + weather notifier',True)
        for y,title,sub in [(26,'Rain bot','Humidity threshold'),(126,'Snow bot','Temperature threshold'),(226,'Sun bot','Temperature threshold')]:box(552,y,184,70,title,sub)
        right(214,156,260)
        paths.append('<path d="M495 156h27V61h20m-7 -5 7 5-7 5M522 156h20m-7 -5 7 5-7 5M522 156v105h20m-7 -5 7 5-7 5"/>')
        caption = 'Configured services respond independently to the shared weather model.'
    elif kind == 'inventory':
        box(24,116,190,80,'Inventory service','Product operations')
        box(275,116,225,80,'IProductRepository','Shared persistence contract',True)
        box(554,54,182,80,'SQL Server','EF Core adapter')
        box(554,196,182,80,'MongoDB','Native driver adapter')
        right(220,156,264)
        paths.append('<path d="M505 156h22V94h17m-7 -5 7 5-7 5M527 156v80h17m-7 -5 7 5-7 5"/>')
        caption = 'The factory selects one storage adapter when the service is constructed.'
    elif kind == 'airport':
        box(24,72,190,80,'Console interface','Passenger / manager')
        box(275,72,220,80,'Services & queries','Booking rules + LINQ',True)
        box(552,72,184,80,'Repositories','In-memory collections')
        box(275,218,220,76,'Flight CSV import','Model validation')
        right(220,112,264);right(500,112,542)
        paths.append('<path d="M500 256h144V162m-5 7 5-7 5 7"/>')
        caption = 'Search and booking workflows sit above repositories; CSV imports populate flights.'
    elif kind == 'library':
        box(24,55,190,80,'Books','ISBN · status · genre')
        box(280,55,200,80,'Loans','Book + borrower keys',True)
        box(546,55,190,80,'Borrowers','Unique email · membership')
        right(220,95,270)
        paths.append('<path d="M536 95H490m7 -5-7 5 7 5"/>')
        box(280,218,200,76,'Reporting SQL','CTEs + window functions')
        down(380,145,208)
        caption = 'Loans connect books to borrowers and provide the data for borrowing analysis.'
    elif kind == 'medico':
        box(24,64,190,80,'React frontend','Forms + Axios requests')
        box(278,64,210,80,'ASP.NET Core API','DTOs + JWT claims',True)
        box(550,64,186,80,'SQL Server','EF Core relationships')
        right(220,104,268);right(494,104,540)
        box(278,218,210,76,'Request → response','Medical-record entries')
        down(383,154,208)
        caption = 'Two repositories connect the user interface, request workflow, and related records.'
    elif kind == 'restaurant':
        box(24,64,190,80,'REST controllers','DTOs + AutoMapper')
        box(278,64,210,80,'Repository contracts','Async persistence',True)
        box(550,64,186,80,'SQL Server','EF Core + SQL objects')
        right(220,104,268);right(494,104,540)
        box(24,218,190,76,'Identity + validation','JWT roles + request rules')
        paths.append('<path d="M119 208V154m-5 7 5-7 5 7"/>')
        caption = 'Controllers coordinate requests and related-record checks; repositories use EF Core for persistence.'
    elif kind == 'algorithms':
        box(24,64,190,80,'Data structures','Trees + heaps + linked nodes')
        box(278,64,210,80,'Algorithms','Sorting + graph traversal',True)
        box(550,64,186,80,'Practice problems','Apply the patterns')
        right(220,104,268);right(494,104,540)
        box(278,218,210,76,'Representation & state','Links + order + discovery')
        paths.append('<path d="M383 208V154m-5 7 5-7 5 7"/>')
        caption = 'A collection of Java implementations and practice solutions exploring structures, invariants, and algorithms.'
    else:
        box(24,64,190,80,'Text input','Separators + numbers')
        box(278,64,210,80,'String calculator','Parse · check · sum',True)
        box(550,64,186,80,'Result or exception','Explicit behavior')
        right(220,104,268);right(494,104,540)
        box(278,218,210,76,'xUnit theories','9 parameterized inputs')
        paths.append('<path d="M383 208V154m-5 7 5-7 5 7"/>')
        caption = 'Parameterized examples check valid results, malformed input, and negative values.'
    svg = '<svg viewBox="0 0 760 320" role="img" aria-label="'+escape(caption,quote=True)+'" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="#849377" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'+''.join(paths)+'</g><g font-family="Manrope, Arial, sans-serif">'+''.join(boxes)+'</g></svg>'
    return f'<figure class="rx-system"><div class="rx-system-scroll">{svg}</div><figcaption>{escape(caption)}</figcaption></figure>'


def proof_html(proof):
    code = codeblock(proof['code']) if proof['language'] in ('C#', 'Java') else '<pre><code>'+escape(proof['code'])+'</code></pre>'
    return f'''<figure class="rx-proof"><figcaption><span class="label">{proof['language']} / Source example</span><h3>{escape(proof['label'])}</h3><p>{escape(proof['explanation'])}</p></figcaption><div class="rx-source-code">{code}</div><div class="rx-proof-link">{ext(proof['url'],'Read the exact source lines','source-link')}<span>{escape(proof['path'].rsplit('/',1)[-1])}</span></div></figure>'''


def project_page(p):
    features = ''.join(f'<article class="rx-feature"><span class="mono">{i:02}</span><div><h3>{escape(title)}</h3><p>{escape(text)}</p></div></article>' for i,(title,text) in enumerate(p['features'],1))
    steps = ''.join(f'<li><span class="rx-step-index mono">{i:02}</span><div><h3>{escape(title)}</h3><p>{escape(text)}</p></div></li>' for i,(title,text) in enumerate(p['workflow'],1))
    sources = ''.join(ext(s['url'],s['label'],'rx-source-tile') for s in p['sources'])
    additional_repo = ext(GITHUB+'/MedicoPortal','Frontend repository','button outline') if p['slug'] == 'medicoportal' else ''
    body = f'''<main id="main"><section class="wrap rx-case-hero"><div class="breadcrumb"><a href="index.html">Home</a><span>/</span><a href="projects.html">Projects</a><span>/</span><span>{escape(p['title'])}</span></div>
    <div class="eyebrow">{escape(p['context'])}</div><div class="rx-case-title"><h1>{escape(p['title'])}</h1><span class="rx-case-number mono">{p['number']} / {len(featured()) + len(projects()):02}</span></div><p class="rx-case-lede">{escape(p['description'])}</p>
    <div class="rx-case-actions">{ext(repo_url(p),'Backend repository' if p['slug']=='medicoportal' else 'View repository','button outline')}{additional_repo}<a href="#source" class="text-link">Read the code {arrow('down')}</a></div>
    <dl class="rx-case-meta"><div><dt>Engineering focus</dt><dd>{escape(p['focus'])}</dd></div><div><dt>Project context</dt><dd>{escape(p['context'])}</dd></div></dl>{tags(p['tags'])}</section>
    <div class="wrap">{diagram(p)}</div>
    <div class="wrap rx-case-layout"><aside class="rx-case-nav" aria-label="Project contents"><span class="label">Inside the project</span><a href="#overview">The idea</a><a href="#features">What stands out</a><a href="#workflow">How it works</a><a href="#source">Code & sources</a><a href="projects.html" class="rx-back">All projects {arrow('left')}</a></aside>
    <div class="rx-case-body"><section id="overview" class="rx-case-section"><div class="eyebrow">01 / The idea</div><h2>{escape(p['metric_label'])}</h2><p>{escape(p['overview'])}</p><div class="rx-skill-note"><span class="label">Skills demonstrated</span><p>{escape(p['skills'])}</p></div></section>
    <section id="features" class="rx-case-section"><div class="eyebrow">02 / What stands out</div><h2>The engineering details.</h2><div class="rx-features">{features}</div></section>
    <section id="workflow" class="rx-case-section"><div class="eyebrow">03 / How it works</div><h2>Follow the workflow.</h2><ol class="rx-workflow">{steps}</ol></section>
    <section id="source" class="rx-case-section"><div class="eyebrow">04 / Code & sources</div><h2>From the implementation.</h2>{''.join(proof_html(x) for x in p['proofs'])}<div class="rx-source-grid">{sources}</div></section></div></div>
    <section class="wrap rx-case-end"><div><span class="label">Keep exploring</span><h2>Another problem.<br>Another perspective.</h2></div><a class="button outline" href="projects.html">Browse all projects {arrow('right')}</a></section></main>'''
    return document(p['title']+' — Raghad Hanon',p['description'],body,p['slug']+'.html')


def archive_pages():
    pages = {'projects.html': archive_page()}
    pages.update({p['slug']+'.html': project_page(p) for p in projects()})
    return pages
