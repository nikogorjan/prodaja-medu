"""Shop page without filters (user, 2026-11-20: "my client doesn't like the filters in the shop, remove them and make
the items span the width").

templates/collection.json, section "product-grid" (main-collection-template): enable_filtering off. Without filters
the theme drops the col-md-3 sidebar and the product grid takes the full container width; the toolbar with the
column switch and "Razvrsti po" (sorting, first option "Po nagradah") stays. Idempotent.

usage: python tools/shop_layout.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/collection.json, never on stale local JSON (see CLAUDE.md).
"""
import json, re, sys, pathlib

path = pathlib.Path(sys.argv[1]) / 'templates' / 'collection.json'
dry = '--dry' in sys.argv
raw = path.read_text(encoding='utf-8')
m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
header = m.group(0) if m else ''
data = json.loads(raw[len(header):])
s = next((v for v in data['sections'].values() if v.get('type') == 'main-collection-template'), None)
if not s:
    print('0 changes\n  skip: no main-collection-template section')
elif s.setdefault('settings', {}).get('enable_filtering') is False:
    print('0 changes\n  ok   filters already off')
else:
    s['settings']['enable_filtering'] = False
    if not dry:
        path.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(('DRY RUN, ' if dry else '') + '1 changes\n  collection.json product-grid: filters off (grid full width)')
