# Raghad Hanon — engineering portfolio

A buildless portfolio for junior .NET backend opportunities, with 16 pages and 11 project case studies.

## Reader journey

The homepage introduces the role and three short background proofs, then features Collabrium, Hotel Booking API and Restaurant Reservation API. Capability-to-source links lead to deeper evidence. Technical experience, education and contact follow without a full project or media inventory in between.

The project collection retains all 11 projects, labeled by context, with category/search controls and a combined reset action. Restaurant Reservation and Algorithms & Data Structures remain first in the complete collection; a separate compact route highlights the three featured backend cases.

Collabrium has a concise contribution-led case study and a separate backend reference. The reference retains 13 functional areas, six workflows, 14 exact C# excerpts and the extended engineering decision notes. Recordings, 202 application screenshots, project visuals, documents and development posts remain accessible as optional case-study resources. The presentation page provides a lightweight browser summary before its optional 196.3 MB PowerPoint download.

## Edit and build

- Homepage: `scripts/homepage.py`.
- Shared document/navigation/contact components: `scripts/components.py`.
- Collabrium narrative: `scripts/collabrium_case.py`; other original cases: `scripts/case_studies.py`.
- Backend reference: `scripts/collabrium_engineering.py` and `scripts/collabrium_evidence.json`.
- Collection/additional cases: `scripts/project_archive.py` and `scripts/additional_projects.json`.
- Shared refreshed styling: `dist/portfolio-refresh.css`, loaded after the existing stylesheets.
- Media and presentation: `scripts/media.py` and `scripts/presentation_page.py`.
- Interactions: `dist/app.js`, `dist/project-archive.js`, `dist/collabrium-engineering.js`, and `dist/presentation-download.js`.

Run `python scripts/build_pages.py`, `python scripts/validate_site.py`, and JavaScript syntax checks after changes. `PORTFOLIO_URL` supplies the hosting origin. The build driver generates HTML, the sitemap, headers and robots file. Serve `dist/` with a static host.

The static site has no form backend, analytics, account integration or API keys.

## Evidence and scope

| Project | Reviewed source commit |
| --- | --- |
| Collabrium | `01aa3dd11fe0b888f54de64314ec3ca2aeb4ca1a` |
| Actify | `2d2204fc04000f73354a956c1841d26846cacb70` |
| HotelBookingPlatform | `f469dcc3dafa81ccd2478bebfd161a4150f62b7d` |

The eight additional case studies carry their own pinned source references in `scripts/additional_projects.json`. Exact excerpts are validated against that data. Collabrium source fingerprints and excerpts are recorded in `scripts/collabrium_evidence.json`.

`contribution_evidence.json` records the path-history evidence reviewed on 3 November 2026 for the first-person Collabrium contribution summary. Those histories include Raghad Hanon / RaghadHanon contributions; the site does not claim sole authorship of the shared team platform.

Collabrium is a four-person graduation project. Actify is course-based. Hotel Booking is an internship final project. The Hotel Booking workflow defines restore/build/test across three operating systems; historical hands-on Azure deployment is described separately. The linked Collabrium snapshot has no automated unit/integration test project or deployment pipeline.

The résumé remains the unchanged latest user-supplied PDF, SHA-256 `1d766086dcb86cd87782a638489245d422759d1e27a63edc3ea77c5ac35f43a7`. Download links carry the content version. Drive originals and sharing were not changed.

## Validation

The static validator checks document structure, local resources, links/fragments, IDs, labels, image dimensions, structured data, exact source excerpts and fonts. Its browser field describes only that static check. Browser QA is performed separately through the managed preview: desktop and narrow layouts, navigation, filtering/reset, disclosures, screenshot viewing and clipboard feedback.

## Published copies

- [GitHub Pages](https://raghadhanon.github.io/RaghadHanon.Portfolio.github.io/)
- [ChatGPT Sites](https://raghad-hanon-engineering.dreamy-83654.chatgpt.site)
