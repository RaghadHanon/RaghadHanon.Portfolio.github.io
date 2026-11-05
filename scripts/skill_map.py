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

# The full toolset at each stop, as agreed: shown in the bubble and in the details panel.
TOOLS = {
    'analysis': ['Requirements analysis', 'User stories', 'Acceptance criteria', 'Agile / Scrum', 'API contracts'],
    'domain': ['Domain models', 'Invariants', 'State transitions', 'OOP', 'SOLID'],
    'data': ['SQL Server', 'EF Core', 'LINQ', 'Relational design', 'Migrations', 'Read models', 'T-SQL', 'MongoDB'],
    'architecture': ['Clean Architecture', 'CQRS / MediatR', 'Dependency injection', 'Repository / Unit of Work', 'Design patterns'],
    'api': ['ASP.NET Core Web API', 'REST', 'DTOs', 'FluentValidation', 'AutoMapper', 'Swagger / OpenAPI'],
    'frontend': ['React', 'TypeScript', 'JavaScript', 'MUI', 'MobX', 'HTML', 'CSS', 'Bootstrap'],
    'security': ['ASP.NET Identity', 'JWT + refresh tokens', 'RBAC', 'Policy-based authorization', 'Multi-tenancy'],
    'integrations': ['SignalR', 'Background workers', 'Email notifications', 'QuestPDF', 'ScottPlot', 'Ollama / LLMs'],
    'testing': ['xUnit', 'Moq', 'AutoFixture', 'FluentAssertions', 'Postman'],
    'delivery': ['Git', 'GitHub Actions CI/CD', 'Azure App Service', 'Azure SQL'],
    'river': ['Algorithms', 'Data structures', 'C++', 'Java', 'Competitive programming'],
}
CARRIED = ['C#', '.NET 8']

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


INK, ROOF, ROOF_D, WALL, WALL_D, STONE, STONE_D, TEAL = '#2c312b', '#c0532f', '#8f3a22', '#fbf6ea', '#e6dcc4', '#cfc7b3', '#a99f8a', '#6f9aa3'


def shadow(rx=26, ry=6, y=0):
    return f'<ellipse cx="0" cy="{y}" rx="{rx}" ry="{ry}" fill="#2c3a26" opacity=".18"/>'


def roof(x1, x2, y, h, color=ROOF):
    m = (x1 + x2) / 2
    return f'<path d="M{x1 - 3} {y}L{m} {y - h}L{x2 + 3} {y}Z" fill="{color}"/><path d="M{m} {y - h}L{x2 + 3} {y}H{m}Z" fill="{ROOF_D}" opacity=".55"/>'


def box(x, y, w, h, lit=WALL, dark=WALL_D):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{lit}"/><rect x="{x + w * .62:.1f}" y="{y}" width="{w * .38:.1f}" height="{h}" fill="{dark}"/>'


def window(x, y, w=5, h=7, c='#f2c879'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1" fill="{c}" stroke="{INK}" stroke-width=".8"/>'


def _analysis():  # observatory: look closely at the problem
    return (shadow(24) + box(-18, -24, 36, 24) + '<path d="M-20 -24a20 20 0 0 1 40 0Z" fill="#dfe8ea"/><path d="M0 -44a20 20 0 0 1 20 20H0Z" fill="#c3d3d7"/>'
            + f'<path d="M-3 -42h6v18h-6z" fill="{INK}" opacity=".75"/><path d="M4 -34 26 -50" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><circle cx="26" cy="-50" r="2.6" fill="{ROOF}"/>'
            + window(-12, -16) + f'<rect x="-4" y="-12" width="8" height="12" fill="{INK}" opacity=".8"/>')


def _domain():  # keep: the rules that hold
    merlons = ''.join(f'<rect x="{x}" y="-55" width="5" height="6" fill="#ddd5c2"/>' for x in (-13, -4, 5))
    low = ''.join(f'<rect x="{x}" y="-27" width="5" height="5" fill="{STONE}"/>' for x in (-28, -19, 15, 23))
    return (shadow(30) + box(-28, -22, 56, 22, STONE, STONE_D) + box(-13, -50, 26, 50, '#ddd5c2', STONE_D) + merlons + low
            + f'<path d="M0 -55V-72" stroke="{INK}" stroke-width="1.6"/><path class="sm-flag" d="M0 -72h15l-4 4 4 4H0Z" fill="{ROOF}"/>'
            + f'<path d="M-5 0v-9a5 5 0 0 1 10 0V0Z" fill="{INK}" opacity=".85"/>' + window(-4, -40, 8, 9))


def _data():  # silos
    silos = ''
    for x, h in ((-26, 46), (-6, 56)):
        rings = ''.join(f'<path d="M{x} {-h + k}a9 3.6 0 0 0 18 0" fill="none" stroke="{STONE_D}" stroke-width=".8"/>' for k in range(12, h, 12))
        silos += (f'<rect x="{x}" y="{-h}" width="18" height="{h}" fill="#e7e1d1"/><rect x="{x + 11}" y="{-h}" width="7" height="{h}" fill="#cfc6b0"/>'
                  f'<ellipse cx="{x + 9}" cy="{-h}" rx="9" ry="3.6" fill="#f6f1e4" stroke="{STONE_D}" stroke-width=".8"/>' + rings)
    return shadow(30) + silos + box(14, -22, 18, 22) + roof(14, 32, -22, 12)


def _architecture():  # workshop and crane
    lattice = 'M18 0V-62M24 0V-62M18 -8 24 -16M24 -16 18 -24M18 -24 24 -32M24 -32 18 -40M18 -40 24 -48M24 -48 18 -56'
    return (shadow(30) + box(-26, -24, 34, 24) + roof(-26, 8, -24, 16) + window(-19, -15) + window(-6, -15)
            + f'<path d="{lattice}" stroke="{ROOF}" stroke-width="1.6" fill="none"/>'
            + f'<path d="M12 -62H44" stroke="{ROOF}" stroke-width="3" stroke-linecap="round"/><path d="M40 -62V-44" stroke="{INK}" stroke-width="1"/><rect x="36" y="-44" width="8" height="6" fill="{INK}"/>')


def _api():  # gatehouse: the contract at the edge
    bars = ''.join(f'<path d="M{x} -20V0" stroke="#f2c879" stroke-width="1.2" opacity=".8"/>' for x in (-8, 0, 8))
    return (shadow(32) + box(-30, -40, 14, 40, STONE, STONE_D) + box(16, -40, 14, 40, STONE, STONE_D) + roof(-30, -16, -40, 12) + roof(16, 30, -40, 12)
            + '<path d="M-16 -30H16V-8a16 16 0 0 0 -32 0Z" fill="#ddd5c2"/>' + f'<path d="M-16 0V-8a16 16 0 0 1 32 0V0Z" fill="{INK}" opacity=".85"/>' + bars
            + f'<path d="M-23 -26v10l4-3 4 3v-10Z" fill="{ROOF}"/><path d="M23 -26v10l-4-3-4 3v-10Z" fill="{ROOF}"/>')


def _frontend():  # market stall: the storefront
    awning = ''.join(f'<path d="M{x} -18l3 -9h6l-3 9Z" fill="{c}"/>' for x, c in ((-21, ROOF), (-15, WALL), (-9, ROOF), (-3, WALL), (3, ROOF), (9, WALL), (15, ROOF)))
    return (shadow(22) + box(-18, -18, 36, 18) + awning
            + f'<rect x="-13" y="-12" width="26" height="7" rx="1.5" fill="#dfe8ea" stroke="{INK}" stroke-width=".8"/><path d="M-10 -8.5h8M2 -8.5h8" stroke="{TEAL}" stroke-width="1.6"/>')


def _security():  # watchtower with a shield
    return (shadow(22) + box(-11, -64, 22, 64, '#ddd5c2', STONE_D) + f'<path d="M-15 -64 0 -88 15 -64Z" fill="{ROOF}"/><path d="M0 -88 15 -64H0Z" fill="{ROOF_D}" opacity=".55"/>'
            + f'<path d="M0 -50 9 -46v7c0 7-9 11-9 11s-9-4-9-11v-7Z" fill="{TEAL}" stroke="{INK}" stroke-width="1"/><path d="M-4 -40 -1 -37 4 -43" stroke="#fff" stroke-width="1.6" fill="none"/>'
            + window(-3, -22, 6, 9) + f'<path d="M-4 0v-8a4 4 0 0 1 8 0V0Z" fill="{INK}" opacity=".85"/>')


def _integrations():  # signal tower: messages going out
    waves = ''.join(f'<path class="sm-wave" style="animation-delay:{d}s" d="M{-r} {-68 - r * .55:.1f}a{r} {r} 0 0 1 {2 * r} 0" fill="none" stroke="{ROOF}" stroke-width="1.8" stroke-linecap="round"/>' for r, d in ((8, 0), (14, .4), (20, .8)))
    return (shadow(24) + box(-16, -14, 32, 14)
            + f'<path d="M-9 -14 0 -66 9 -14M-6 -30H6M-4 -44H4M-7.5 -22 4 -38M7.5 -22 -4 -38" stroke="{INK}" stroke-width="1.6" fill="none" stroke-linejoin="round"/>'
            + f'<circle cx="0" cy="-68" r="3.4" fill="{ROOF}"/>' + waves)


def _testing():  # lighthouse: keeps watch
    stripes = ''.join(f'<path d="M{-10.4 + k * .06:.1f} {-k}h{20.8 - k * .12:.1f}l-.5 -8h-{19.8 - k * .12:.1f}Z" fill="{ROOF}"/>' for k in (8, 26, 44))
    return (shadow(22) + f'<path d="M-11 0 -7 -58H7L11 0Z" fill="{WALL}"/>' + stripes
            + '<circle class="sm-glow" cx="0" cy="-64" r="14" fill="#f2c879" opacity=".35"/>'
            + f'<rect x="-9" y="-70" width="18" height="12" rx="2" fill="#f7e2a8" stroke="{INK}" stroke-width="1"/><path d="M-11 -70h22l-11 -9Z" fill="{INK}"/>')


def _delivery():  # rocket on the launch pad
    return (shadow(22) + f'<rect x="-20" y="-6" width="40" height="6" fill="{STONE_D}"/><rect x="-20" y="-8" width="40" height="3" fill="{STONE}"/>'
            + f'<path class="sm-flame" d="M-5 -26c0 7 2.5 11 5 14 2.5-3 5-7 5-14Z" fill="#f2a64a"/>'
            + f'<path d="M0 -70c9 8 11 22 9 44H-9c-2-22 0-36 9-44Z" fill="{WALL}" stroke="{INK}" stroke-width="1"/><circle cx="0" cy="-46" r="4.5" fill="#dfe8ea" stroke="{INK}" stroke-width="1"/>'
            + f'<path d="M-9 -34-17 -18-9 -22ZM9 -34 17 -18 9 -22Z" fill="{ROOF}"/><path d="M0 -70c4 3.5 6.5 7 7.5 11h-15c1-4 3.5-7.5 7.5-11Z" fill="{ROOF}"/>')


LANDMARKS = {'analysis': _analysis, 'domain': _domain, 'data': _data, 'architecture': _architecture, 'api': _api,
             'frontend': _frontend, 'security': _security, 'integrations': _integrations, 'testing': _testing, 'delivery': _delivery}
# Where each landmark stands: above the road on the top row, beside the badge on the bottom row.
SPOTS = {'analysis': (130, 104), 'domain': (360, 106), 'data': (604, 106), 'architecture': (842, 104), 'api': (1124, 118),
         'frontend': (1022, 66), 'security': (1124, 432), 'integrations': (830, 428), 'testing': (530, 430), 'delivery': (228, 430)}


def plateau(x, y, rx=60, ry=22):
    return (f'<ellipse cx="{x}" cy="{y + 7}" rx="{rx}" ry="{ry}" fill="#b5c29e"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="url(#sm-plaza)"/>')


def pine(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="3" cy="2" rx="10" ry="3" fill="#2c3a26" opacity=".16"/><rect x="-1.6" y="-6" width="3.2" height="8" fill="#8a7454"/>'
            '<path d="M0 -34 11 -14H-11Z" fill="#7f9c72"/><path d="M0 -26 13 -4H-13Z" fill="#6d8b62"/><path d="M0 -34 11 -14H0ZM0 -26 13 -4H0Z" fill="#5b7752" opacity=".55"/></g>')


def bush(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="2" cy="3" rx="12" ry="3" fill="#2c3a26" opacity=".14"/>'
            '<circle cx="-5" cy="-3" r="7" fill="#9db58c"/><circle cx="4" cy="-5" r="8" fill="#a9c095"/><circle cx="2" cy="-7" r="4" fill="#bfd2ab"/></g>')


def map_svg():
    road, river = smooth(ROAD), smooth(RIVER)
    villages = [v for v in VILLAGES if v[0] != 'river']
    plazas = ''.join(plateau(x, y, 44, 16) if k == 'frontend' else plateau(x, y) for k, _, (x, y), _, _ in villages)
    marks = ''.join(f'<g class="sm-mark" transform="translate({SPOTS[k][0]} {SPOTS[k][1]})">{LANDMARKS[k]()}</g>' for k, *_ in villages)
    forest = ''.join(pine(x, y, s) for x, y, s in [
        (232, 64, .9), (252, 78, 1.05), (272, 62, .8), (478, 74, .85), (500, 86, 1), (716, 60, .9), (736, 76, 1.1), (1182, 70, .9), (1170, 96, .75),
        (40, 270, 1), (62, 284, .8), (434, 236, .75), (888, 238, .9), (910, 252, .7), (1080, 250, .8),
        (300, 560, 1), (322, 574, .8), (960, 556, 1), (982, 570, .85), (1150, 560, .95), (1172, 576, .75), (110, 580, .8)])
    bushes = ''.join(bush(x, y, s) for x, y, s in [(186, 210, .9), (566, 228, .8), (676, 236, .7), (980, 212, .8), (154, 380, .8), (690, 382, .8),
                                                    (360, 378, .7), (1002, 382, .7), (620, 574, .8), (796, 580, .9), (226, 540, .7)])
    clouds = ''.join(f'<g class="sm-cloud" style="animation-delay:{d}s"><ellipse cx="{x}" cy="{y}" rx="46" ry="14" fill="#fff" opacity=".75"/>'
                     f'<ellipse cx="{x - 18}" cy="{y - 8}" rx="22" ry="13" fill="#fff" opacity=".8"/><ellipse cx="{x + 14}" cy="{y - 11}" rx="26" ry="15" fill="#fff" opacity=".8"/></g>'
                     for x, y, d in [(330, 30, 0), (900, 22, -14), (640, 590, -7)])
    planks = ''.join(f'<rect x="-22" y="{y}" width="44" height="4" fill="#c29d6f"/>' for y in range(-28, 28, 8))
    posts = ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#6f5238"/>' for x in (-22, 22) for y in (-32, 0, 32))
    side = 'M1060 150C1050 104 1012 74 965 60'
    return f'''<svg class="sm-map" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice">
<defs>
<radialGradient id="sm-ground" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#eef2e3"/><stop offset=".7" stop-color="#dfe6cf"/><stop offset="1" stop-color="#c9d4b5"/></radialGradient>
<radialGradient id="sm-plaza" cx="45%" cy="35%" r="70%"><stop offset="0" stop-color="#f1f3e6"/><stop offset="1" stop-color="#d7dfc4"/></radialGradient>
<linearGradient id="sm-hill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d3ddbf"/><stop offset="1" stop-color="#c3d0aa"/></linearGradient>
<pattern id="sm-grain" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#7d8f66" opacity=".12"/><circle cx="4" cy="4" r=".5" fill="#fff" opacity=".25"/></pattern>
<radialGradient id="sm-vignette" cx="50%" cy="50%" r="72%"><stop offset=".62" stop-color="#1f2a1c" stop-opacity="0"/><stop offset="1" stop-color="#1f2a1c" stop-opacity=".22"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sm-ground)"/>
<ellipse cx="160" cy="-10" rx="260" ry="70" fill="url(#sm-hill)"/><ellipse cx="1040" cy="-20" rx="300" ry="80" fill="url(#sm-hill)"/><ellipse cx="600" cy="640" rx="420" ry="90" fill="url(#sm-hill)"/>
<ellipse cx="300" cy="350" rx="170" ry="40" fill="#e9eedb" opacity=".7"/><ellipse cx="900" cy="250" rx="140" ry="32" fill="#e9eedb" opacity=".7"/>
<g class="sm-water"><path d="{river}" fill="none" stroke="#d9cfae" stroke-width="54" stroke-linecap="round"/><path d="{river}" fill="none" stroke="#8fb5bf" stroke-width="40" stroke-linecap="round"/><path d="{river}" fill="none" stroke="#a9cbd2" stroke-width="28" stroke-linecap="round"/>
<path class="sm-flow" d="{river}" fill="none" stroke="#e8f4f5" stroke-width="2.4" stroke-dasharray="16 30" stroke-linecap="round"/><path class="sm-flow sm-flow-2" d="{river}" fill="none" stroke="#d5eaee" stroke-width="1.4" stroke-dasharray="6 40" stroke-linecap="round" transform="translate(0 7)"/></g>
<g class="sm-boat"><path d="M300 314h34l-6 8h-22Z" fill="#8b6c4b"/><path d="M316 312V286l14 22Z" fill="#fbf6ea" stroke="#2c312b" stroke-width=".8"/><path d="M314 312V292l-10 18Z" fill="#c0532f"/></g>
<rect width="{W}" height="{H}" fill="url(#sm-grain)"/>
{plazas}
<path d="{side}" fill="none" stroke="#b39c73" stroke-width="10" stroke-linecap="round"/><path d="{side}" fill="none" stroke="#e9dec4" stroke-width="6" stroke-linecap="round" stroke-dasharray="4 6"/>
<path d="{road}" fill="none" stroke="#2c3a26" stroke-opacity=".14" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 5)"/>
<path d="{road}" fill="none" stroke="#b39c73" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>
<path id="sm-road" d="{road}" fill="none" stroke="#e9dec4" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{road}" fill="none" stroke="#d8caa8" stroke-width="7" stroke-dasharray="2 13" stroke-linecap="round"/>
<g transform="translate(1152 300)"><rect x="-22" y="-30" width="44" height="60" rx="3" fill="#a8835a"/>{planks}<path d="M-22 -32V32M22 -32V32" stroke="#6f5238" stroke-width="4" stroke-linecap="round"/>{posts}</g>
<path class="sm-loop" d="M460 440C478 352 318 262 360 150" fill="none" stroke="#c0532f" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
<path d="M452 432l8 8 8-7" fill="none" stroke="#c0532f" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
<g transform="translate(168 236)"><rect x="-8" y="-4" width="214" height="26" rx="13" fill="#fbf6ea" stroke="#d9cfae"/><text x="99" y="13.5" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-size="12.5" font-weight="700" fill="#a24529">&#8634; tests travel alongside the build</text></g>
{bushes}{forest}{marks}
<g transform="translate(30 150)"><ellipse cx="2" cy="2" rx="10" ry="3" fill="#2c3a26" opacity=".2"/><path d="M0 0V-46" stroke="#6f5238" stroke-width="3.4" stroke-linecap="round"/><path d="M-8 -68h80l8 12-8 12h-80Z" fill="{INK}"/><text x="32" y="-51.5" text-anchor="middle" font-family="Plex Mono,monospace" font-size="11" font-weight="600" letter-spacing="1.2" fill="#f8f2e6">NEW TASK</text></g>
<g transform="translate(55 440)"><ellipse cx="2" cy="2" rx="12" ry="3.5" fill="#2c3a26" opacity=".2"/><path d="M0 0V-58" stroke="#6f5238" stroke-width="3.4" stroke-linecap="round"/><path class="sm-flag" d="M1 -58c12 -5 22 5 34 0v20c-12 5-22-5-34 0Z" fill="{ROOF}"/><circle cx="0" cy="-60" r="3" fill="#f2c879"/><g transform="translate(8 24)"><rect x="-48" y="-11" width="96" height="20" rx="10" fill="#fbf6ea" stroke="#d9cfae"/><text x="0" y="3" text-anchor="middle" font-family="Plex Mono,monospace" font-size="9.5" font-weight="600" letter-spacing="1" fill="#56664a">IN PRODUCTION</text></g></g>
{clouds}
<rect width="{W}" height="{H}" fill="url(#sm-vignette)" pointer-events="none"/>
</svg>'''


def links(items):
    out = []
    for name, href in items:
        external = href.startswith('http')
        new_tab = external or href.endswith('.pdf')
        attrs = (' target="_blank" rel="noopener noreferrer"' if external else ' target="_blank" rel="noopener"') if new_tab else ''
        out.append(f'<a href="{escape(href, quote=True)}"{attrs}>{escape(name)}{arrow() if external else ""}</a>')
    return ' · '.join(out)


CHECK = '<svg viewBox="0 0 12 12"><path d="M2.5 6.2 5 8.6l4.5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CUP = ('<span class="sm-cup" aria-hidden="true"><svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#fffefa" stroke="#2c312b" stroke-width="1.6"/>'
       '<circle cx="20" cy="20" r="15.5" fill="none" stroke="#e6dcc4" stroke-width="1.2"/><path class="sm-steam" d="M16 13c-1.5-2 1.5-3.5 0-6M21 13c-1.5-2 1.5-3.5 0-6" fill="none" stroke="#9aa18e" stroke-width="1.6" stroke-linecap="round"/>'
       '<path d="M10 16h17v5a8 8 0 0 1-8 8h-1a8 8 0 0 1-8-8z" fill="#c0532f"/><path d="M27 18h2a3.2 3.2 0 0 1 0 6.4h-2.4" fill="none" stroke="#c0532f" stroke-width="2.2"/>'
       '<path d="M8 31.5h22" stroke="#2c312b" stroke-width="2" stroke-linecap="round"/></svg></span>')


def skill_map():
    by_key = {v[0]: v for v in VILLAGES}
    order = ROUTE[:5] + ['frontend'] + ROUTE[5:] + ['river']
    pins, panels, bubbles = [], [], []
    for key in order:
        _, name, (x, y), question, skills = by_key[key]
        stop = ROUTE.index(key) + 1 if key in ROUTE else None
        badge = f'{stop:02}' if stop else ('≈' if key == 'river' else '+')
        kind = 'stop' if stop else key
        tag = f'<span class="sm-tag">{TAGS[key]}</span>' if key in TAGS else ''
        data_stop = f' data-sm-stop="{stop}"' if stop else ''
        label = f'Stop {stop}: {name}' if stop else f'{name} ({TAGS[key].lower()})'
        pins.append(f'<li class="sm-village sm-{kind}" style="--x:{x};--y:{y}"><button type="button" class="sm-pin" data-sm-key="{key}" data-x="{x}" data-y="{y}"{data_stop} '
                    f'aria-controls="sm-{key}" aria-pressed="false" aria-label="{escape(label, quote=True)}"><span class="sm-badge" aria-hidden="true"><span class="sm-badge-num">{badge}</span>'
                    f'<span class="sm-check">{CHECK}</span></span><span class="sm-name" aria-hidden="true">{escape(name)}{tag}</span></button></li>')
        if stop and stop < len(ROUTE):
            nxt_btn = f'<button type="button" class="sm-next" data-sm-go="{ROUTE[stop]}" hidden>Next stop: {escape(by_key[ROUTE[stop]][1])} {arrow("right")}</button>'
        elif stop:
            nxt_btn = f'<button type="button" class="sm-next" data-sm-go="river" hidden>And underneath it all {arrow("right")}</button>'
        else:
            nxt_btn = ''
        where = f'Stop {stop:02} of {len(ROUTE):02}' if stop else TAGS[key]
        rows = ''.join(f'<li><strong>{escape(s)}</strong><span class="sm-detail">{escape(d)}</span><span class="sm-used">Used in {links(l)}</span></li>' for s, d, l in skills)
        panels.append(f'<article class="sm-panel" id="sm-{key}" aria-labelledby="sm-title-{key}"><div class="sm-panel-head"><span class="sm-num" aria-hidden="true">{badge}</span>'
                      f'<div><span class="label">{where}</span><h4 id="sm-title-{key}">{escape(name)}</h4><p class="sm-q">{escape(question)}</p></div>{nxt_btn}</div><ul class="sm-tools" aria-label="Tools at this stop">{''.join(f'<li>{escape(t)}</li>' for t in TOOLS[key])}</ul><h5 class="sm-evidence">Where I’ve used them</h5><ul class="sm-skills">{rows}</ul></article>')
        chips = ''.join(f'<li>{escape(t)}</li>' for t in TOOLS[key])
        bubbles.append(f'<div class="sm-bubble sm-bubble-{kind}" data-sm-bubble="{key}" aria-hidden="true" hidden><div class="sm-bubble-top"><span class="sm-bubble-num">{badge}</span>'
                       f'<span class="sm-bubble-stage">{escape(where)}</span></div><strong class="sm-bubble-title">{escape(name)}</strong><span class="sm-bubble-q">{escape(question)}</span>'
                       f'<ul class="sm-bubble-skills">{chips}</ul><span class="sm-bubble-more">Where I’ve used them, below ↓</span></div>')
    segments = ''.join(f'<i data-seg="{i}"></i>' for i in range(1, len(ROUTE) + 1))
    hud = ('<div class="sm-hud" data-sm-js hidden><button type="button" class="sm-play" aria-pressed="false"><svg class="sm-play-icon" viewBox="0 0 20 20" aria-hidden="true">'
           '<path class="i-play" d="M6.5 4.5v11l9-5.5z" fill="currentColor"/><path class="i-stop" d="M5.5 5.5h9v9h-9z" fill="currentColor"/></svg><span class="sm-play-label">Start a task</span></button>'
           f'<div class="sm-hud-info"><span class="sm-hud-quest">Quest · Ship a new feature</span><span class="sm-progress" aria-hidden="true">{segments}</span>'
           '<span class="sm-status" aria-live="polite">Follow a task, or open any village.</span></div></div>')
    return f'''<div class="wrap skillmap reveal" id="skill-map" data-skillmap>
    <div class="sm-head"><div><span class="label">Skill map / How I work</span><h3>From a new task to production.</h3></div><p>Every task travels the same road. Each village is one stage of how I work, with the skills I use there and where I’ve used them. Tests travel alongside the build, and problem solving runs underneath it all.</p></div>
    <p class="sm-carry"><span class="label">Carried to every stop</span>{''.join(f'<span class="sm-carry-chip">{escape(t)}</span>' for t in CARRIED)}</p>
    <div class="sm-stage">{map_svg()}<ol class="sm-villages" aria-label="Stages of a task, in order">{''.join(pins)}</ol>{CUP}{''.join(bubbles)}<span class="sm-confetti" aria-hidden="true"></span>{hud}</div>
    <div class="sm-panels">{''.join(panels)}</div>
    </div>'''
