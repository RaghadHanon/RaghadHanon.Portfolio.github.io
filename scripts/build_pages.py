#!/usr/bin/env python3
"""Render the buildless portfolio from its editable content components."""
from components import *
from case_studies import collabrium_page, actify_page, hotel_page
from collabrium_engineering import engineering_page
from project_archive import archive_pages

from homepage import home_page

if __name__ == '__main__':
    DIST.mkdir(exist_ok=True)
    from presentation_page import build_presentation_page
    build_presentation_page()
    extra_pages = archive_pages()
    for filename, markup in extra_pages.items():
        (DIST/filename).write_text(markup,encoding='utf-8')
    for filename,fn in [('index.html',home_page),('collabrium.html',collabrium_page),('collabrium-engineering.html',engineering_page),('actify.html',actify_page),('hotel-booking.html',hotel_page)]:
        (DIST/filename).write_text(fn(),encoding='utf-8')
        print(filename)
    (DIST/'404.html').write_text(document('Page not found — Raghad Hanon','This page could not be found.',f'<main class="wrap not-found" id="main"><div class="eyebrow">404 / A small detour</div><h1>Let’s get you<br>back on track.</h1><p>The page you’re looking for has moved or doesn’t exist.</p><a class="button" href="index.html">Back to the portfolio {arrow("right")}</a></main>','404.html'),encoding='utf-8')
    (DIST/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="17" fill="#b84d2e"/><text x="10" y="43" fill="#fff3e2" font-family="Arial,sans-serif" font-size="32" font-weight="bold" letter-spacing="-3">rh.</text></svg>')
    (DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
    urls=['','collabrium.html','collabrium-engineering.html','actify.html','hotel-booking.html','presentation.html']
    urls.extend(extra_pages)
    (DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+ORIGIN+'/'+u+'</loc></url>' for u in urls)+'</urlset>')
    (DIST/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n/assets/*\n  Cache-Control: public, max-age=604800\n')

