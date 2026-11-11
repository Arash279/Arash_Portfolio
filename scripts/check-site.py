"""Check generated static output, including project Pages base paths. No network needed."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'dist'
base = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else ''
site = sys.argv[2].rstrip('/') if len(sys.argv) > 2 else 'http://localhost:4321'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.refs, self.h1, self.canonical = set(), [], 0, None
        self.imgs, self.robots, self.redirect = [], None, False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh': self.redirect = True
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'img': self.imgs.append(a)
        if tag == 'meta' and a.get('name') == 'robots': self.robots = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a['href']
        for key in ('href', 'src'):
            if key in a and not (tag == 'link' and a.get('rel') == 'canonical'):
                self.refs.append(a[key])

pages = {p: Page(p.read_text(encoding='utf-8')) for p in root.rglob('*.html')}
errors, external = [], set()
for path, page in pages.items():
    route = '/' + path.relative_to(root).as_posix()
    route = route[:-10] if route.endswith('index.html') else route
    expected = site + base + route
    if not page.redirect and page.h1 != 1: errors.append(f'{route}: {page.h1} H1 elements')
    if not page.redirect and page.canonical != expected: errors.append(f'{route}: canonical {page.canonical} != {expected}')
    if site != 'http://localhost:4321' and route != '/404.html' and not page.redirect and page.robots:
        errors.append(f'{route}: production unexpectedly noindexed')
    for image in page.imgs:
        if not image.get('alt'): errors.append(f'{route}: image missing descriptive alt')
        if not image.get('width') or not image.get('height'): errors.append(f'{route}: image missing dimensions')
    for ref in page.refs:
        u = urlsplit(ref)
        if u.scheme or u.netloc:
            if u.scheme in ('http','https'): external.add(ref)
            continue
        if not u.path:
            target = path
        else:
            if not u.path.startswith(base + '/'):
                errors.append(f'{route}: base not preserved: {ref}')
                continue
            relative = unquote(u.path[len(base):]).lstrip('/')
            target = root / relative
            if target.is_dir(): target /= 'index.html'
        if not target.is_file(): errors.append(f'{route}: missing {ref}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{route}: missing anchor {ref}')
    text = path.read_text(encoding='utf-8')
    for obsolete in ('umami', 'googletagmanager', 'Nietzsche', 'John Doe', 'cdn.jsdelivr.net/npm/katex'):
        if obsolete in text: errors.append(f'{route}: obsolete template reference {obsolete}')

for css in root.rglob('*.css'):
    for ref in re.findall(r'url\([\"\']?([^\"\')]+)', css.read_text(encoding='utf-8')):
        if ref.startswith('data:'): continue
        u = urlsplit(ref)
        if u.scheme: continue
        target = root / u.path[len(base):].lstrip('/') if u.path.startswith('/') else css.parent / u.path
        if not target.is_file(): errors.append(f'{css.name}: missing CSS resource {ref}')

if len(pages) != 9: errors.append(f'Expected 8 content pages and 1 legacy redirect, found {len(pages)}')
print(f'Checked {len(pages)} pages, images, CSS resources, canonical URLs, local links and fragments; base={base or "/"}')
print('External links: ' + ', '.join(sorted(external)))
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS')
