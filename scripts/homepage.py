"""A concise hiring journey, with optional routes into the project evidence."""
from components import *
from media import media_image


def home_page():
    board = media_image('screens/1Q7yzCP0K71hhNJGRyVwzTaeG7BxJmrDL.webp',
                        'Collabrium project board with work items grouped by delivery status')
    body = f'''<main id="main" class="pf-home">
    <section class="pf-hero" aria-labelledby="hero-title"><div class="wrap pf-hero-grid">
      <div class="pf-hero-content"><p class="eyebrow">Raghad Hanon · Computer Systems Engineering graduate</p>
      <h1 id="hero-title">Junior .NET<br>Backend <em>Engineer.</em></h1>
      <p class="pf-intro">I build APIs with <strong>C#, ASP.NET Core, EF Core and SQL Server.</strong> I led a four-person graduation team on Collabrium and contributed to its backend, connecting domain rules, access checks and application workflows.</p>
      <div class="pf-actions"><a class="button" href="#work">Explore selected projects {arrow('down')}</a><a class="text-link" href="assets/Raghad-Hanon-Resume.pdf?v=1d766086dcb8" target="_blank" rel="noopener">View résumé {arrow()}</a></div>
      <div class="pf-profile-links">{ext(GITHUB,'GitHub','text-link')}{ext(LINKEDIN,'LinkedIn','text-link')}<a class="text-link" href="mailto:{EMAIL}">Email me {arrow()}</a></div>
      <ul class="pf-quick-proofs" aria-label="Background at a glance"><li><strong>Team lead</strong><span>Four-person graduation project</span></li><li><strong>Backend internship</strong><span>Foothill Technology Solutions</span></li><li><strong>1st in college</strong><span>Engineering &amp; Technology · PTUK</span></li></ul></div>
      <figure class="pf-portrait"><img src="assets/raghad-hanon-portrait.webp" alt="Raghad Hanon" width="1122" height="1402" fetchpriority="high"><figcaption><strong>Raghad Hanon</strong><span>Based in Palestine</span><span class="pf-availability"><i class="status-dot" aria-hidden="true"></i>Open to junior roles · Remote welcome</span></figcaption></figure>
    </div></section>

    <section class="pf-section" id="work" aria-labelledby="work-title"><div class="wrap">
      <div class="pf-section-head"><div><p class="eyebrow">01 / Selected backend projects</p><h2 id="work-title">Selected backend projects.</h2></div><p>One connected platform, followed by two focused API projects.</p></div>
      <article class="pf-flagship"><div class="pf-flagship-copy"><span class="label">Graduation project · Oct 2025–Jun 2026</span><h3><a href="collabrium.html">Collabrium {arrow('right')}</a></h3>
      <p>A shared workspace for an organization’s projects, teams, learning and reporting.</p><p class="pf-role"><strong>Team Lead &amp; Backend Developer</strong><span>Four-person academic team</span></p>
      <p>I led requirements and two-week sprints, and contributed backend rules and use cases. Three examples to inspect:</p>
      <ul class="pf-decision-list"><li><strong>Organization-aware access</strong><span>Tenant and project checks establish the request’s scope.</span></li><li><strong>Meaningful work states</strong><span>Story completion checks linked tasks, bugs and test results.</span></li><li><strong>Connected changes</strong><span>Related writes and their history share a transaction.</span></li></ul>
      {tags(['C# / .NET 8','EF Core / SQL Server','CQRS / MediatR'])}
      <div class="pf-actions"><a class="button" href="collabrium.html">My contribution &amp; case study {arrow('right')}</a></div>
      <div class="pf-deep-links" id="collabrium-engineering"><a class="text-link" href="collabrium-engineering.html">Backend architecture &amp; code {arrow()}</a></div></div>
      <div class="pf-flagship-visual" id="showcase"><a href="collabrium.html#demo" aria-label="Explore Collabrium’s recorded work-item workflow">{board}</a><p>Actual project board · Recorded graduation-project workflow</p><a class="text-link" href="collabrium.html#demo">Watch the workflow {arrow('right')}</a></div></article>

      <div class="pf-supporting-projects" aria-label="Complementary backend projects">
      <article class="pf-project"><div class="pf-project-heading"><span class="label">Internship final project</span><h3><a href="hotel-booking.html">Hotel Booking API {arrow('right')}</a></h3></div><p>A booking-to-invoice API with guest ownership checks, price calculations and PDF invoices.</p><p><strong>Evidence to inspect:</strong> xUnit invoice tests and a GitHub Actions build/test definition across three operating systems.</p>{tags(['.NET 8','SQL Server','xUnit'])}<a class="text-link" href="hotel-booking.html">Explore booking &amp; testing {arrow('right')}</a></article>
      <article class="pf-project"><div class="pf-project-heading"><span class="label">ASP.NET Core API project</span><h3><a href="restaurant-reservation.html">Restaurant Reservation API {arrow('right')}</a></h3></div><p>Reservations and orders connected to customers, restaurant tables and employees.</p><p><strong>Evidence to inspect:</strong> related-record checks, explicit REST contracts, validation and SQL objects managed through EF Core migrations.</p>{tags(['ASP.NET Core','EF Core','SQL Server'])}<a class="text-link" href="restaurant-reservation.html">Explore the reservation API {arrow('right')}</a></article>
      </div>
      <div class="pf-collection-link" id="more-work"><p>More work in SQL, persistence, testing, full-stack integration and algorithms.</p><a class="text-link" href="projects.html">Browse all 11 projects {arrow('right')}</a></div>
    </div></section>

    <section class="pf-section pf-evidence" id="engineering" aria-labelledby="engineering-title"><div class="wrap">
      <div class="pf-section-head"><div><p class="eyebrow">02 / Skills with evidence</p><h2 id="engineering-title">What the code demonstrates.</h2></div><p>Each capability leads to a specific implementation.</p></div>
      <div class="pf-evidence-list">
      <article><h3>C# &amp; domain rules</h3><p>Work-item relationships and release gates expressed as model behavior.</p><a class="text-link" href="collabrium-engineering.html#domain-rules">Collabrium domain rules {arrow('right')}</a></article>
      <article><h3>APIs &amp; access checks</h3><p>Identity, organization membership and resource checks across request boundaries.</p><a class="text-link" href="collabrium-engineering.html#security">Tenant &amp; project access {arrow('right')}</a></article>
      <article><h3>Data &amp; persistence</h3><p>Relational models, EF Core mappings, SQL queries and database objects.</p><a class="text-link" href="restaurant-reservation.html#source">Restaurant API &amp; SQL {arrow('right')}</a></article>
      <article><h3>Testing &amp; CI</h3><p>Test code for invoice outcomes, with an explicit restore/build/test workflow.</p><a class="text-link" href="hotel-booking.html#decisions">Invoice tests &amp; CI {arrow('right')}</a></article>
      <article><h3>Backend integrations</h3><p>SignalR, email, scheduled workers and structured AI suggestions.</p><a class="text-link" href="collabrium-engineering.html#integrations">Connected workflows {arrow('right')}</a></article>
      </div>
    </div></section>

    <section class="pf-section" id="experience" aria-labelledby="experience-title"><span id="about" class="pf-anchor"></span><div class="wrap pf-experience-grid">
      <div><p class="eyebrow">03 / Experience &amp; technical training</p><h2 id="experience-title">Experience &amp;<br>technical training.</h2><p class="pf-section-intro">Backend training, full-stack integration and a graduation project delivered with a team.</p><a class="text-link" href="assets/Raghad-Hanon-Resume.pdf?v=1d766086dcb8" target="_blank" rel="noopener">View full résumé {arrow()}</a></div>
      <div class="pf-timeline"><article><div class="pf-timeline-top"><div><h3>Backend Intern</h3><p>Foothill Technology Solutions, LLC</p></div><time>Aug 2024–Jan 2025</time></div><p>Structured training in C#, ASP.NET Core, EF Core, architecture and automated testing. Built the Hotel Booking API as the final project, with test code, a CI workflow and hands-on Azure deployment.</p><a class="text-link" href="hotel-booking.html">See the internship project {arrow('right')}</a></article>
      <article><div class="pf-timeline-top"><div><h3>Full Stack Intern</h3><p>Knowledge Academy</p></div><time>Sep 2023–Dec 2024</time></div><p>Built and consumed REST APIs with C#, ASP.NET and relational databases, and connected responsive React interfaces to backend functionality.</p></article>
      <details class="pf-current-learning"><summary>Current career development <span>TAP · Oct 2026–Present</span></summary><p>Selected for a sponsored place in TAP’s Job Hunting Program, with interview preparation, professional networking and a structured search for software engineering opportunities.</p></details></div>
    </div></section>

    <section class="pf-section pf-education" id="recognition" aria-labelledby="recognition-title"><div class="wrap">
      <div class="pf-section-head"><div><p class="eyebrow">04 / Education &amp; selected recognition</p><h2 id="recognition-title">Education &amp;<br>selected recognition.</h2></div></div>
      <div class="pf-education-grid"><div class="pf-degree"><span class="label">September 2021–June 2026</span><h3>B.Sc. Computer Systems Engineering</h3><p>Palestine Technical University — Kadoorie</p><p><strong>First in the College of Engineering &amp; Technology</strong><br>Graduating average: 93.21/100.</p></div><div class="pf-recognition-list"><p><strong>GirlsACPC · 2023</strong><span>25th place in the ICPC Africa &amp; Arab Collegiate Contest for Girls.</span></p><p><strong>ICPC Palestine · 2022</strong><span>20th place in the Palestinian Collegiate Programming Contest.</span></p><a class="text-link" href="algorithms-data-structures.html">Explore my algorithm implementations {arrow('right')}</a></div></div>
      <details class="pf-milestones"><summary>More competitions, coding practice &amp; learning</summary><div class="pf-milestone-grid"><p><strong>Problem-solving practice</strong>918+ Codeforces and 120+ LeetCode problems solved. {ext(CF,'Codeforces profile','source-link')}</p><p><strong>Hebron Code-Jam · 2023</strong>9th nationwide with the 3Geeks team; 1st in the qualification contest. {ext(HEBRON_POST,'Event post','source-link')}</p><p><strong>Palestine Science &amp; Technology Fair · 2021</strong>5th place.</p><p><strong>Palestine Mobile Apps Fair · 2019</strong>5th nationwide.</p><p><strong>Further participation</strong>Meta Hacker Cup, Intel International Science &amp; Technology Fair, and Palestine FIRST LEGO League.</p><p><strong>Courses &amp; development</strong>.NET Core &amp; React; React at Knowledge Academy; Java Data Structures &amp; Algorithms; English Access Microscholarship Program.</p></div>{ext(LINKEDIN+'details/licenses/','Certificates &amp; learning record','text-link')}</details>
    </div></section></main>'''
    return document('Raghad Hanon — Junior .NET Backend Engineer',
                    'Junior .NET backend engineer working with C#, ASP.NET Core, EF Core and SQL Server. Explore Collabrium, backend project evidence, technical training and contact details.',
                    body, home=True)
