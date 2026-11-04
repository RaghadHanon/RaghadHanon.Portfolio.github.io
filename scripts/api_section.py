"""'Hire me as an API': a playful, interactive summary in the language of HTTP.
Every value is real and matches the evidence elsewhere in the portfolio."""
from html import escape
from components import EMAIL, LINKEDIN, GITHUB, RESUME, arrow, bridge

ENDPOINTS = [
    ('profile', 'GET', '/raghad', 200, 'OK', {
        'name': 'Raghad Hanon',
        'role': 'Backend Software Engineer · C# / ASP.NET Core',
        'based_in': 'Palestine',
        'work_mode': ['Remote', 'On-site in Palestine'],
        'status': 'open_to_work',
        'looking_for': ['Junior .NET backend roles', 'Software engineering roles'],
        'languages': {'arabic': 'native', 'english': 'B2–C1'},
        'links': {'github': GITHUB, 'linkedin': LINKEDIN},
    }),
    ('stack', 'GET', '/raghad/stack', 200, 'OK', {
        'backend': ['C#', '.NET 8', 'ASP.NET Core Web API', 'EF Core', 'LINQ', 'SQL Server', 'REST APIs'],
        'architecture': ['Clean Architecture', 'CQRS / MediatR', 'SOLID', 'Dependency injection', 'Repository / Unit of Work', 'Multi-tenancy'],
        'security': ['ASP.NET Identity', 'JWT + refresh tokens', 'RBAC', 'Policy-based authorization'],
        'testing_delivery': ['xUnit', 'Moq', 'AutoFixture', 'FluentValidation', 'Swagger / OpenAPI', 'Postman', 'Git', 'GitHub Actions CI/CD', 'Azure App Service', 'Azure SQL'],
        'also': ['SignalR', 'Background workers', 'AutoMapper', 'Ollama / LLMs', 'React', 'TypeScript', 'JavaScript', 'C++', 'Algorithms'],
    }),
    ('soft-skills', 'GET', '/raghad/soft-skills', 200, 'OK', {
        'leadership': 'Led a four-person team through two-week Agile sprints (Collabrium)',
        'communication': 'Turned requirements into API contracts; wrote a six-part LinkedIn series on the build',
        'problem_solving': 'Years of competitive programming: Codeforces, LeetCode, ICPC',
        'teamwork': 'Team contests: ICPC Africa & Arab Girls 2023, Palestinian Collegiate 2022',
        'ownership': 'Took projects from requirements to delivery, then documented them',
    }),
    ('proof', 'GET', '/raghad/proof', 200, 'OK', {
        'college_rank': '1st, College of Engineering & Technology (PTUK)',
        'graduating_average': '93.21 / 100',
        'problems_solved': {'codeforces': '918+', 'leetcode': '120+'},
        'icpc': ['25th, Africa & Arab Collegiate Contest for Girls (2023)', '20th, Palestinian Collegiate Contest (2022)'],
        'api_endpoints_built': {'total': '200+', 'collabrium': '137 of the platform’s 292', 'hotel_booking': 52, 'actify': 19},
        'xunit_tests_written': {'count': '100+', 'project': 'Hotel Booking API'},
    }),
    ('projects', 'GET', '/raghad/projects?featured=true', 200, 'OK', [
        {'name': 'Collabrium', 'role': 'Team Lead & Backend Developer', 'url': 'collabrium.html'},
        {'name': 'Actify', 'role': 'Full-Stack Developer', 'url': 'actify.html'},
        {'name': 'Hotel Booking API', 'role': 'Backend Developer (internship)', 'url': 'hotel-booking.html'},
        {'more': '8 additional projects', 'url': 'projects.html'},
    ]),
    ('coffee', 'GET', '/raghad/coffee', 418, "I'm a teapot", {
        'error': 'This engineer runs on tea.',
        'hint': 'Ask about it in the interview.',
    }),
    ('bugs', 'DELETE', '/raghad/bugs', 202, 'Accepted', {
        'message': 'Working on it. Always.',
    }),
    ('interview', 'POST', '/interview', 201, 'Created', {
        'status': 'Looking forward to it',
        'next_step': 'mailto:' + EMAIL,
        'resume': RESUME,
    }),
]


def _value(v):
    if isinstance(v, str):
        text = escape(v)
        if v.startswith(('http', 'mailto:')) or v.endswith('.html') or v.startswith('assets/'):
            ext = v.startswith('http')
            attrs = ' target="_blank" rel="noopener noreferrer"' if ext else (' target="_blank" rel="noopener"' if v.startswith('assets/') else '')
            return f'<a class="j-str j-link" href="{escape(v, quote=True)}"{attrs}>"{text}"</a>'
        return f'<span class="j-str">"{text}"</span>'
    if isinstance(v, bool):
        return f'<span class="j-num">{str(v).lower()}</span>'
    if isinstance(v, (int, float)):
        return f'<span class="j-num">{v}</span>'
    return None


def to_html(obj, level=0):
    """Pretty-print JSON as highlighted HTML; links stay clickable."""
    pad, inner = '  ' * level, '  ' * (level + 1)
    simple = _value(obj)
    if simple is not None:
        return simple
    if isinstance(obj, dict):
        rows = [f'{inner}<span class="j-key">"{escape(k)}"</span>: {to_html(v, level + 1)}' for k, v in obj.items()]
        return '{\n' + ',\n'.join(rows) + '\n' + pad + '}'
    if all(isinstance(x, str) for x in obj) and sum(len(x) for x in obj) < 46:
        return '[' + ', '.join(to_html(x) for x in obj) + ']'
    return '[\n' + ',\n'.join(inner + to_html(x, level + 1) for x in obj) + '\n' + pad + ']'


def api_section():
    buttons, panels = [], []
    for i, (key, method, path, code, reason, body) in enumerate(ENDPOINTS):
        pid, tid = f'api-{key}', f'api-tab-{key}'
        kind = 'ok' if code < 300 else 'warn'
        buttons.append(f'<button type="button" class="api-endpoint" role="tab" id="{tid}" aria-controls="{pid}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}"><span class="api-method m-{method.lower()}">{method}</span><span class="api-path">{escape(path)}</span></button>')
        panels.append(f'''<div class="api-response" id="{pid}" role="tabpanel" aria-labelledby="{tid}" tabindex="0"><div class="api-request"><span class="api-method m-{method.lower()}">{method}</span> <span>{escape(path)}</span></div><div class="api-status s-{kind}"><span class="api-dot" aria-hidden="true"></span>HTTP/1.1 {code} {escape(reason)}<span class="api-type">application/json</span></div><pre class="api-json"><code>{to_html(body)}</code></pre></div>''')
    return f'''<section class="section api-section" id="api" aria-labelledby="api-title"><div class="wrap">
    <div class="section-head reveal"><div><div class="eyebrow">Bonus / Try it</div><h2 id="api-title">Hire me as an API</h2><p class="section-tagline">Send a request. Every response is real.</p></div><p>A backend engineer’s summary, in the language I work in. Pick an endpoint to see the response, then try the last one.</p></div>
    <div class="api-console reveal" data-api-console><div class="api-bar" aria-hidden="true"><i></i><i></i><i></i><span>raghad · portfolio api · v1</span></div><div class="api-body"><div class="api-endpoints" role="tablist" aria-label="Endpoints" aria-orientation="vertical">{''.join(buttons)}</div><div class="api-output" aria-live="polite">{''.join(panels)}</div></div></div>
    {bridge('#contact', 'Or skip the API and just say hello')}</div></section>'''
