"""Skill map: the road a task travels, from requirement to production.

Each village is one stage of how Raghad works, in the order she works through it.
Every skill links to a project where it was actually used.
Testing runs alongside the build (a dashed loop back to Domain),
the frontend is a side road off the API, and problem solving is the river
that runs under the whole map.
"""
from html import escape
from components import CF, arrow

W, H = 1200, 600

C = 'collabrium.html'
CE = 'collabrium-engineering.html'
HB = 'hotel-booking.html'
POSTMAN = 'https://documenter.getpostman.com/view/27912762/2sBYHNX3rF/'

# key, name, (x, y), question, skills: [(skill, detail, [(project, href)])]
VILLAGES = [
    ('analysis', 'Analysis', (130, 150), 'What exactly is being asked, and what does “done” mean?', [
        ('Requirements → API contracts', 'Turning a requirement into the contract the team builds against.', [('Collabrium', C + '#contribution')]),
        ('Agile delivery', 'Two-week sprints with a four-person team I led.', [('Collabrium', C + '#contribution')]),
        ('Documented system design', 'Requirements and design recorded in a 272-page thesis.', [('Thesis', 'assets/docs/Collabrium-Thesis.pdf')]),
    ]),
    ('domain', 'Domain', (360, 150), 'Which rules must never break?', [
        ('Domain models with invariants', 'Business rules and state transitions live in the model, so no endpoint can bypass them.', [('Collabrium', CE + '#domain-rules')]),
        ('State transitions', 'Five work-item types; a user story ships only when its linked tasks, bugs and tests pass.', [('Collabrium', CE + '#domain-rules')]),
        ('Modelling by intent', 'Attendance behaves differently for a host and an attendee.', [('Actify', 'actify.html#decisions')]),
        ('OOP & SOLID', 'Structured training applied in the internship capstone.', [('Hotel Booking', HB)]),
    ]),
    ('data', 'Data', (600, 150), 'How is it stored, and how will it be read?', [
        ('EF Core & LINQ', 'Domain models kept separate from EF Core entities; migrations as a controlled step.', [('Collabrium', CE + '#data-api'), ('Hotel Booking', HB)]),
        ('SQL Server & relational design', 'Constraints, CTEs, window functions, procedures and triggers.', [('Library Database', 'library-database.html')]),
        ('Read models', 'Queries use purpose-built projections instead of domain models.', [('Collabrium', CE + '#data-api')]),
        ('Swappable persistence', 'SQL Server/EF Core and MongoDB adapters behind one contract.', [('Inventory Persistence', 'inventory-persistence.html')]),
    ]),
    ('architecture', 'Architecture', (840, 150), 'Where does this code belong?', [
        ('Clean Architecture', 'Four projects: API, Application, Domain, Infrastructure.', [('Collabrium', CE + '#system-map'), ('Hotel Booking', HB)]),
        ('CQRS / MediatR', 'Commands and queries take different paths.', [('Collabrium', C + '#architecture'), ('Actify', 'actify.html')]),
        ('Repository & Unit of Work', 'One transaction for one business operation.', [('Collabrium', CE + '#data-api'), ('Restaurant Reservation', 'restaurant-reservation.html')]),
        ('Design patterns & DI', 'Strategy, Observer and Factory behind interfaces.', [('Weather Service', 'weather-service.html')]),
    ]),
    ('api', 'API', (1060, 150), 'What is the contract with whoever calls it?', [
        ('ASP.NET Core Web API', '137 endpoints in Collabrium, 52 in Hotel Booking, 19 in Actify.', [('Collabrium', C), ('Hotel Booking', HB), ('Actify', 'actify.html')]),
        ('Validation & error contracts', 'FluentValidation and shared error responses; DTO validation.', [('Collabrium', C + '#decisions'), ('Restaurant Reservation', 'restaurant-reservation.html')]),
        ('DTOs & AutoMapper', 'Explicit request and response models.', [('Hotel Booking', HB)]),
        ('Swagger & Postman docs', 'Documented, explorable APIs.', [('Collabrium API docs', POSTMAN), ('Hotel Booking', HB)]),
    ]),
    ('frontend', 'Frontend', (965, 60), 'How does the interface use the API?', [
        ('React & TypeScript', 'MUI, MobX, API hooks, forms and protected routes.', [('Actify', 'actify.html')]),
        ('Connecting a React client', 'A React frontend talking to ASP.NET Core APIs.', [('MedicoPortal', 'medicoportal.html')]),
        ('JavaScript, HTML, CSS, Bootstrap', 'Responsive interfaces in a full-stack internship.', [('Experience', 'index.html#about')]),
    ]),
    ('security', 'Security', (1050, 440), 'Who is allowed, and within which scope?', [
        ('Multi-tenancy', 'Tenant-resolution middleware checks membership before any handler runs.', [('Collabrium', CE + '#security')]),
        ('Identity & JWT', 'Rotating refresh tokens and a forced first-login password change.', [('Collabrium', CE + '#security'), ('Restaurant Reservation', 'restaurant-reservation.html')]),
        ('RBAC & policies', '13 user roles and project-access policies.', [('Collabrium', CE + '#security')]),
        ('Resource ownership', 'A guest can read only their own bookings and invoices.', [('Hotel Booking', HB + '#decisions')]),
    ]),
    ('integrations', 'Integrations', (760, 440), 'What should happen after the change is saved?', [
        ('SignalR', 'Live comments, presence and notifications.', [('Collabrium', CE + '#integrations'), ('Actify', 'actify.html#code')]),
        ('Background workers & email', 'Persisted notifications and event-driven emails, so offline users still get every update.', [('Collabrium', CE + '#integrations'), ('Hotel Booking', HB)]),
        ('Reports & PDFs', '10 report types with ScottPlot and QuestPDF; PDF invoices.', [('Collabrium', CE + '#ai-reports'), ('Hotel Booking', HB)]),
        ('Local LLMs', 'Ollama (Gemma 3) with output validation, 3 repair attempts and fallbacks.', [('Collabrium', CE + '#ai-reports')]),
    ]),
    ('testing', 'Testing', (460, 440), 'How do I know it works, and keeps working?', [
        ('xUnit, Moq & AutoFixture', '100+ tests for booking rules, invoices, authorization and rollback.', [('Hotel Booking', HB + '#decisions')]),
        ('Parameterized tests', 'xUnit theories with FluentAssertions.', [('String Calculator Kata', 'string-calculator.html')]),
        ('Testing behaviour', 'Parser, validation and rule tests.', [('Weather Service', 'weather-service.html'), ('Airport Booking', 'airport-booking.html')]),
        ('API testing', 'Postman collections alongside the code.', [('Hotel Booking', HB)]),
    ]),
    ('delivery', 'Delivery', (160, 440), 'How does it reach people?', [
        ('GitHub Actions CI', 'Build and test on Ubuntu, Windows and macOS.', [('Hotel Booking', HB + '#decisions'), ('Weather Service', 'weather-service.html')]),
        ('Automated build & deploy', 'Pipelines from push to running app.', [('Actify', 'actify.html')]),
        ('Azure App Service & Azure SQL', 'Hands-on deployment in the backend internship.', [('Hotel Booking', HB)]),
        ('Git', 'Every project, every day.', [('GitHub', 'https://github.com/RaghadHanon')]),
    ]),
    ('river', 'Problem solving', (720, 302), 'The river under every task.', [
        ('Competitive programming', '918+ problems on Codeforces and 120+ on LeetCode, mostly in C++.', [('Codeforces', CF)]),
        ('ICPC', '25th in the Africa & Arab Collegiate Contest for Girls (2023); 20th in the Palestinian Collegiate Contest (2022).', [('Recognition', 'index.html#recognition')]),
        ('Algorithms & data structures', '110 Java files: AVL rotations, heaps, sorting and graph traversal.', [('Algorithms & Data Structures', 'algorithms-data-structures.html')]),
    ]),
]

ROUTE = ['analysis', 'domain', 'data', 'architecture', 'api', 'security', 'integrations', 'testing', 'delivery']
TAGS = {'frontend': 'Side road', 'testing': 'Alongside the build', 'river': 'Underneath it all'}

# Road waypoints: villages plus wiggles between them, start sign and finish flag.
ROAD = [(30, 150), (130, 150), (245, 122), (360, 150), (480, 178), (600, 150), (720, 122), (840, 150), (950, 178),
        (1060, 150), (1140, 210), (1152, 300), (1135, 385), (1050, 440), (905, 468), (760, 440), (610, 412),
        (460, 440), (310, 468), (160, 440), (55, 440)]
RIVER = [(-20, 312), (180, 284), (420, 318), (640, 288), (860, 315), (1060, 290), (1220, 305)]


def smooth(points):
    """Catmull-Rom spline through the points, as an SVG cubic path."""
    d = f'M{points[0][0]} {points[0][1]}'
    for i in range(len(points) - 1):
        p0 = points[i - 1] if i else points[i]
        p1, p2 = points[i], points[i + 1]
        p3 = points[i + 2] if i + 2 < len(points) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]} {p2[1]}'
    return d


def house(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 10 10 2l10 8v12H0Z" fill="#fbfaf5" stroke="#8d9a80" stroke-width="1.2"/>'
            f'<path d="M-2 11 10 1l12 10" fill="none" stroke="#b84d2e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><rect x="8" y="15" width="4" height="7" fill="#c9d0bd"/></g>')


def tree(x, y, r=9):
    return f'<g><rect x="{x - 1.2}" y="{y + r - 2}" width="2.4" height="7" fill="#9a8a6c"/><circle cx="{x}" cy="{y}" r="{r}" fill="#b9c7a6"/><circle cx="{x - 3}" cy="{y - 3}" r="{r * .45:.1f}" fill="#c9d5b8"/></g>'


def map_svg():
    road = smooth(ROAD)
    river = smooth(RIVER)
    villages = [v for v in VILLAGES if v[0] != 'river']
    grounds = ''.join(f'<circle cx="{x}" cy="{y}" r="{40 if k == "frontend" else 54}" fill="#e2e7d6"/>' for k, _, (x, y), _, _ in villages)
    houses = ''.join(house(x - 46, y - 40, .9) + house(x + 26, y - 46) + house(x + 40, y - 18, .8)
                     if k != 'frontend' else house(x - 38, y - 26, .75) + house(x + 22, y - 30, .75)
                     for k, _, (x, y), _, _ in villages)
    trees = ''.join(tree(x, y, r) for x, y, r in [(250, 60, 10), (272, 74, 8), (520, 66, 9), (540, 80, 7), (700, 60, 10),
                                                   (420, 240, 8), (880, 238, 9), (905, 250, 7), (60, 250, 10), (82, 262, 7),
                                                   (300, 540, 10), (330, 552, 8), (620, 545, 9), (940, 540, 10), (962, 553, 7),
                                                   (1130, 540, 9), (1180, 60, 9), (480, 555, 7), (180, 560, 8), (780, 560, 8)])
    return f'''<svg class="sm-map" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid meet">
<defs><pattern id="sm-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#c3cbb4" opacity=".55"/></pattern></defs>
<rect width="{W}" height="{H}" fill="url(#sm-dots)"/>
<g class="sm-water"><path d="{river}" fill="none" stroke="#bcd3d8" stroke-width="34" stroke-linecap="round"/><path d="{river}" fill="none" stroke="#d3e4e7" stroke-width="24" stroke-linecap="round"/><path class="sm-flow" d="{river}" fill="none" stroke="#f2f8f8" stroke-width="2" stroke-dasharray="14 26" stroke-linecap="round"/></g>
{trees}{grounds}
<path d="M1060 150C1050 104 1012 74 965 60" fill="none" stroke="#cdbf9f" stroke-width="7" stroke-dasharray="2 9" stroke-linecap="round"/>
<path class="sm-loop" d="M460 440C478 352 318 262 360 150" fill="none" stroke="#b84d2e" stroke-width="2.2" stroke-dasharray="7 8" stroke-linecap="round" opacity=".75"/>
<path d="M454 434l6 6 7-5" fill="none" stroke="#b84d2e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" opacity=".75"/>
<text x="168" y="252" font-family="Manrope,Arial,sans-serif" font-size="13" font-weight="600" fill="#a24529">↺ tests travel alongside the build</text>
<path d="{road}" fill="none" stroke="#cbbd9c" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
<path id="sm-road" d="{road}" fill="none" stroke="#e9dfc8" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{road}" fill="none" stroke="#fbf7ee" stroke-width="2" stroke-dasharray="9 11" stroke-linecap="round"/>
<g stroke="#8b6c4b" stroke-width="3" stroke-linecap="round"><path d="M1137 280v40M1167 282v40"/></g><g stroke="#8b6c4b" stroke-width="1.5"><path d="M1137 290h30M1137 300h30M1137 310h30"/></g>
{houses}
<g transform="translate(30 150)"><path d="M0 0V-44" stroke="#7d6a4f" stroke-width="3" stroke-linecap="round"/><rect x="-6" y="-64" width="74" height="24" rx="4" fill="#242622"/><text x="31" y="-47.5" text-anchor="middle" font-family="Plex Mono,monospace" font-size="11" letter-spacing="1" fill="#f8f7f3">NEW TASK</text></g>
<g transform="translate(55 440)"><path d="M0 0V-48" stroke="#7d6a4f" stroke-width="3" stroke-linecap="round"/><path d="M1 -48h30l-7 9 7 9H1Z" fill="#b84d2e"/><text x="0" y="30" text-anchor="middle" font-family="Plex Mono,monospace" font-size="11" letter-spacing="1" fill="#5f6a55">IN PRODUCTION</text></g>
</svg>'''


def links(items):
    out = []
    for name, href in items:
        external = href.startswith('http')
        new_tab = external or href.endswith('.pdf')
        attrs = (' target="_blank" rel="noopener noreferrer"' if external else ' target="_blank" rel="noopener"') if new_tab else ''
        out.append(f'<a href="{escape(href, quote=True)}"{attrs}>{escape(name)}{arrow() if external else ""}</a>')
    return ' · '.join(out)


def skill_map():
    by_key = {v[0]: v for v in VILLAGES}
    order = ROUTE[:5] + ['frontend'] + ROUTE[5:] + ['river']
    pins, panels = [], []
    for key in order:
        _, name, (x, y), question, skills = by_key[key]
        stop = ROUTE.index(key) + 1 if key in ROUTE else None
        badge = f'{stop:02}' if stop else ('≈' if key == 'river' else '+')
        kind = 'stop' if stop else key
        tag = f'<span class="sm-tag">{TAGS[key]}</span>' if key in TAGS else ''
        data_stop = f' data-sm-stop="{stop}"' if stop else ''
        label = f'Stop {stop}: {name}' if stop else f'{name} ({TAGS[key].lower()})'
        pins.append(f'''<li class="sm-village sm-{kind}" style="--x:{x};--y:{y}"><button type="button" class="sm-pin" data-sm-key="{key}" data-x="{x}" data-y="{y}"{data_stop} aria-controls="sm-{key}" aria-pressed="false" aria-label="{escape(label, quote=True)}"><span class="sm-badge" aria-hidden="true">{badge}</span><span class="sm-name" aria-hidden="true">{escape(name)}{tag}</span></button></li>''')
        if stop and stop < len(ROUTE):
            nxt = by_key[ROUTE[stop]][1]
            nxt_btn = f'<button type="button" class="sm-next" data-sm-go="{ROUTE[stop]}" hidden>Next stop: {escape(nxt)} {arrow("right")}</button>'
        elif stop:
            nxt_btn = '<button type="button" class="sm-next" data-sm-go="river" hidden>And underneath it all {arrow("right")}</button>'
        else:
            nxt_btn = ''
        where = f'Stop {stop:02} of {len(ROUTE):02}' if stop else TAGS[key]
        rows = ''.join(f'<li><strong>{escape(s)}</strong><span class="sm-detail">{escape(d)}</span><span class="sm-used">Used in {links(l)}</span></li>' for s, d, l in skills)
        panels.append(f'''<article class="sm-panel" id="sm-{key}" aria-labelledby="sm-title-{key}"><div class="sm-panel-head"><span class="sm-num" aria-hidden="true">{badge}</span><div><span class="label">{where}</span><h4 id="sm-title-{key}">{escape(name)}</h4><p class="sm-q">{escape(question)}</p></div>{nxt_btn}</div><ul class="sm-skills">{rows}</ul></article>''')
    cup = '<span class="sm-cup" aria-hidden="true"><svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#fffefa" stroke="#e2d7c4"/><path class="sm-steam" d="M16 13c-1.5-2 1.5-3.5 0-6M21 13c-1.5-2 1.5-3.5 0-6" fill="none" stroke="#9aa18e" stroke-width="1.6" stroke-linecap="round"/><path d="M10 16h17v5a8 8 0 0 1-8 8h-1a8 8 0 0 1-8-8z" fill="#b84d2e"/><path d="M27 18h2a3.2 3.2 0 0 1 0 6.4h-2.4" fill="none" stroke="#b84d2e" stroke-width="2.2"/><path d="M8 31.5h22" stroke="#242622" stroke-width="2" stroke-linecap="round"/></svg></span>'
    return f'''<div class="wrap skillmap reveal" id="skill-map" data-skillmap>
    <div class="sm-head"><div><span class="label">Skill map / How I work</span><h3>From a new task to production.</h3></div><p>Every task travels the same road. Each village is one stage of how I work, with the skills I use there and where I’ve used them. Tests travel alongside the build, and problem solving runs underneath it all.</p></div>
    <div class="sm-controls" data-sm-js hidden><button type="button" class="button sm-play" aria-pressed="false"><span class="sm-play-label">Start a task</span><svg class="arrow" viewBox="0 0 20 20" aria-hidden="true"><path d="M6 4l10 6-10 6z" fill="currentColor"/></svg></button><span class="sm-status" aria-live="polite">Follow a task from start to finish, or open any village.</span></div>
    <div class="sm-stage">{map_svg()}<ol class="sm-villages" aria-label="Stages of a task, in order">{''.join(pins)}</ol>{cup}</div>
    <div class="sm-panels">{''.join(panels)}</div>
    </div>'''
