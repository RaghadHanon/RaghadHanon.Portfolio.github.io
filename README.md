# Raghad Hanon — Backend Engineering Portfolio

Responsive static portfolio featuring .NET backend engineering, three project case studies, 12 source-linked code examples, 22 Collabrium engineering decisions, the complete 202-screen product gallery, three recordings, and project documentation.

[Visit the portfolio](https://raghadhanon.github.io/)

## Publishing

The repository includes a GitHub Actions workflow that builds, checks, and deploys `dist/` to GitHub Pages on pushes to `main`. Enable **Settings → Pages → Build and deployment → Source: GitHub Actions** in the selected repository, then run **Publish portfolio to GitHub Pages** from Actions if needed.

The workflow reads the actual Pages URL and uses it for canonical links, social metadata, structured data, and the sitemap. It works with either a user-site repository or a project-site repository.

The first run imports the existing public media, verifies every file's SHA-256 and size against `asset-manifest.json`, and commits the files into this repository. Later runs use those checked-in assets directly; the published portfolio then has no dependency on the previous host. The `.assets-materialized` marker records the completed import.

## Local preview

Requires Python 3.12+ and Node.js for JavaScript syntax checks.

```sh
python -m pip install -r requirements.txt
python scripts/build_pages.py
python scripts/validate_site.py
python -m http.server 8000 --directory dist
```

Set `PORTFOLIO_URL` when building for a different public host. The environment variable contains a public URL, not a credential.

## Editing

- Page content: `scripts/build_pages.py`, `scripts/case_studies.py`, and `scripts/components.py`.
- Engineering stories: `scripts/engineering.py` and `scripts/engineering_stories.json`.
- Gallery: `scripts/all_screens.json` and `dist/assets/screens/`.
- Presentation page: `scripts/presentation_page.py`.
- Styles and interactions: `dist/styles.css`, `dist/app.js`.
- Generated pages and static assets: `dist/`.

Keep the presentation parts in `dist/assets/docs/presentation/` together. The dedicated download page combines them into the original 53-slide PPTX, including embedded media. The main pages do not fetch these parts until the visitor starts a download.

## Project evidence

Project descriptions link to pinned source revisions reviewed for this portfolio:

| Project | Commit |
| --- | --- |
| Collabrium | `01aa3dd11fe0b888f54de64314ec3ca2aeb4ca1a` |
| Actify | `2d2204fc04000f73354a956c1841d26846cacb70` |
| Hotel Booking | `f469dcc3dafa81ccd2478bebfd161a4150f62b7d` |

Collabrium is a four-person graduation project. Actify is a course-based implementation. Hotel Booking is an internship final project. GitHub Actions CI experience and hands-on Azure deployment are described separately.

The publishing workflow checks generated pages, local asset references, and JavaScript syntax before deploying. Source and DOM interaction checks also cover gallery navigation, image viewing, and media controls.
