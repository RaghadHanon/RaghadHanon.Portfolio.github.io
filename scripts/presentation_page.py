"""A lightweight project brief before the optional original presentation."""
from components import *


def build_presentation_page():
    body = f'''<main class="wrap pf-brief" id="main"><a class="text-link" href="collabrium.html">Back to the Collabrium case study {arrow('left')}</a>
    <p class="eyebrow">Collabrium / Project summary</p><h1>The project,<br>at a glance.</h1>
    <p class="pf-brief-intro">A four-person graduation project at PTUK, completed in June 2026. Collabrium connects an organization’s projects, teams, learning, community and reporting.</p>
    <div class="pf-brief-grid"><article><h2>Purpose</h2><p>Bring related organizational workflows into one application, sharing the same people, teams, organization and project context.</p></article>
    <article><h2>My role</h2><p>Team Lead &amp; Backend Developer: requirements and sprint coordination, backend rules and use cases, and React/API integration alongside the team.</p><a class="text-link" href="collabrium.html#contribution">Contribution examples {arrow('right')}</a></article>
    <article><h2>Backend approach</h2><p>ASP.NET Core and C#, with EF Core/SQL Server. Four projects separate API contracts, application use cases, domain behavior and infrastructure.</p><a class="text-link" href="collabrium-engineering.html#system-map">Architecture reference {arrow('right')}</a></article>
    <article><h2>What to inspect</h2><p>Organization-aware access, work-item release rules, transactional changes, recorded delivery workflows, and the linked C# source.</p><a class="text-link" href="collabrium.html#demo">Recorded workflow {arrow('right')}</a></article></div>
    <div class="pf-status-note"><strong>Academic implementation</strong><p>The linked source snapshot documents the shared platform. Automated backend tests and a deployment pipeline are planned next steps.</p></div>
    <section class="pf-download-panel" aria-labelledby="presentation-title"><span class="label">Optional full reference</span><h2 id="presentation-title">Graduation presentation</h2><p>The original 53-slide PowerPoint includes embedded demonstrations. The complete download is <strong>196.3 MB</strong>.</p><button type="button" class="button" id="download-presentation">Download full presentation {arrow('down')}</button><p role="status" aria-live="polite" id="download-status">The full file downloads only when you request it.</p><noscript><p>Enable JavaScript to download the PowerPoint. The project summary above remains available.</p></noscript></section>
    </main><script src="{asset_href('presentation-download.js')}" defer></script>'''
    (DIST/'presentation.html').write_text(document('Collabrium summary & presentation — Raghad Hanon','A lightweight Collabrium project summary, with the optional original graduation presentation.',body,'presentation.html'),encoding='utf-8')
