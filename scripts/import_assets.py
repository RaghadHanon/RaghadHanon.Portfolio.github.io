#!/usr/bin/env python3
"""Import the public portfolio's media once, checking every byte against its manifest."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'asset-manifest.json'
MARKER = ROOT / '.assets-materialized'


def file_matches(path, entry):
    if not path.is_file() or path.stat().st_size != entry['bytes']:
        return False
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest() == entry['sha256']


def main():
    if MARKER.exists():
        print('Portfolio media is already stored in this repository.')
        return
    manifest = json.loads(MANIFEST.read_text())
    base_url = manifest['source_url'].rstrip('/') + '/'

    def import_one(entry):
        relative = Path(entry['path'])
        if relative.is_absolute() or '..' in relative.parts or relative.parts[:2] != ('dist', 'assets'):
            raise ValueError(f'Invalid asset path: {relative}')
        destination = ROOT / relative
        if file_matches(destination, entry):
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(destination.name + '.importing')
        url = base_url + quote(relative.relative_to('dist').as_posix(), safe='/')
        for attempt in range(3):
            try:
                request = Request(url, headers={'User-Agent': 'RaghadHanon-Portfolio-Import/1.0'})
                with urlopen(request, timeout=60) as response, temporary.open('wb') as output:
                    while block := response.read(1024 * 1024):
                        output.write(block)
                if not file_matches(temporary, entry):
                    raise ValueError(f'Integrity check failed for {relative}')
                temporary.replace(destination)
                return
            except Exception:
                temporary.unlink(missing_ok=True)
                if attempt == 2:
                    raise
                time.sleep(attempt + 1)

    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(import_one, manifest['files']))
    MARKER.write_text(json.dumps({
        'files': len(manifest['files']),
        'bytes': sum(entry['bytes'] for entry in manifest['files']),
        'manifest_sha256': hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
    }, indent=2) + '\n')
    print(f"Verified and imported {len(manifest['files'])} media files.")


if __name__ == '__main__':
    main()
