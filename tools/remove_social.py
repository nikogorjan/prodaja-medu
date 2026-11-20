"""Remove the social networks from the shop (user, 2026-11-20: "remove the social networks from the footer and
anywhere else they still are").

The links in the theme settings were the theme's demo links (facebook.com/shopify, instagram.com/shopify, ...,
TikTok "#"), so they are cleared rather than kept hidden. Also switched off:
- footer newsletter column icons (block setting enablesocial) and any other footer social block,
- announcement bar icons (enable_social_topbar),
- "share" buttons: article page (social_sharing_blog), the product page "share" block (disabled, not deleted),
  show_share_buttons, and the global share_facebook / share_twitter / share_pinterest.
Only these keys change; nothing is deleted. Idempotent.

usage: python tools/remove_social.py CONTENT_DIR [--dry]
Run it on a fresh pull of config/settings_data.json, sections/footer-group.json, sections/header-group.json,
templates/product.json and templates/article.json, never on stale local JSON (see CLAUDE.md).
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1])
dry = '--dry' in sys.argv
log = []
FILES = ['config/settings_data.json', 'sections/footer-group.json', 'sections/header-group.json',
         'templates/product.json', 'templates/article.json']
OFF = {'enablesocial', 'enable_social_topbar', 'social_sharing_blog', 'show_share_buttons',
       'share_facebook', 'share_twitter', 'share_pinterest'}
LINK = re.compile(r'^social_[a-z]+_(link|tiktok)$')


def walk(name, node, path=''):
    n = 0
    if isinstance(node, dict):
        if node.get('type') in ('share', 'social') and 'settings' in node and not node.get('disabled'):
            node['disabled'] = True
            log.append(f'{name} {path.rstrip(".")}: "{node["type"]}" block hidden')
            n += 1
        for k, v in list(node.items()):
            if k in OFF and v is True:
                node[k] = False
                log.append(f'{name} {path}{k}: off')
                n += 1
            elif LINK.match(k) and isinstance(v, str) and v:
                node[k] = ''
                log.append(f'{name} {path}{k}: cleared ({v})')
                n += 1
            elif isinstance(v, (dict, list)) and k != 'presets':
                n += walk(name, v, f'{path}{k}.')
    elif isinstance(node, list):
        for i, v in enumerate(node):
            n += walk(name, v, f'{path}{i}.')
    return n


for rel in FILES:
    p = root / rel
    if not p.exists():
        log.append(f'skip {rel}: not in this pull')
        continue
    raw = p.read_text(encoding='utf-8')
    m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
    header = m.group(0) if m else ''
    data = json.loads(raw[len(header):])
    if walk(rel, data) and not dry:
        p.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(('DRY RUN, ' if dry else '') + f'{sum(1 for l in log if not l.startswith("skip"))} changes')
for line in log:
    print(' ', line)
