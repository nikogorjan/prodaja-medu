"""Replaces the stock photos in the theme content with the client's real photos (request of 2026-11-20:
"remove the stock images ... only use their real ones").

Stock photos: New_Project.webp (beekeeper with a child and smoker), New_Project_1.webp (honey extractor),
New_Project_2.webp (colourful hive truck), 1.webp (river Mura with mills).
Real photos used instead: the client's own (semen-*.webp/png, gasilska.webp) and the photos from their document
of 11/2026 (cebelarji-iz-indije-*, izobrazevanje-evropskih-veterinarjev, spanski-*), uploaded to Content › Files.

Each replacement is targeted (template, section, block, setting) and only happens while the setting still holds
the stock photo, so a photo the client has since chosen in the theme editor is never overwritten. Captions are
only changed while they still describe the stock photo. Hidden sections are handled too, so switching one back on
never brings a stock photo back. At the end every remaining stock reference is listed.

usage: python tools/replace_stock_images.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/index.json, page.o-nas.json and page.apiturizem.json, never on stale local
JSON (see CLAUDE.md). On live, run it after simplify_content.py and homepage_layout.py.
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1])
dry = '--dry' in sys.argv
STOCK = ('New_Project.webp', 'New_Project_1.webp', 'New_Project_2.webp', '1.webp')
IMG = 'shopify://shop_images/'

# (template, section, block or None, setting, stock file, real file, extra settings {key: (old value or None, new value)})
REPLACE = [
    # homepage: card "Čebelarimo od leta 1982" (O nas), and the hidden sections it replaced
    ('index.json', 'o_nas_apiterapija', 'o_nas', 'image', 'New_Project_2.webp', 'semen-med-polica.png', {}),
    ('index.json', 'druzina_semen', 'druzina_image', 'image', 'New_Project.webp', 'semen-med-polica.png', {}),
    ('index.json', 'pridelava_semen', 'korak_1', 'image', 'New_Project_2.webp', 'spanski-cebelarji-prevozna-enota.jpg', {}),
    ('index.json', 'pridelava_semen', 'korak_3', 'image', 'New_Project_1.webp', 'semen-med-polica.png', {}),
    ('index.json', '0a081843-18cc-4628-a950-350c7308b356', None, 'image', '1.webp', 'semen-cebelnjak-vrt.webp', {}),
    # O nas page
    ('page.o-nas.json', 'uvod', None, 'image', 'New_Project.webp', 'semen-poslikan-cebelnjak.png',
     {'image_position': (None, 'center center')}),
    ('page.o-nas.json', 'zgodba', None, 'image', 'New_Project_2.webp', 'spanski-cebelarji-prevozna-enota.jpg',
     {'image_position': (None, 'left center')}),          # the truck's hive doors, no visitors in the frame
    ('page.o-nas.json', 'galerija', 'g2', 'image', 'New_Project_1.webp', 'cebelarji-iz-indije-pri-panjih.jpg',
     {'caption': ('Hladno točenje', 'Obisk čebelarjev iz Indije'), 'position': (None, 'center center')}),
    ('page.o-nas.json', 'galerija', 'g6', 'image', '1.webp', 'izobrazevanje-evropskih-veterinarjev.jpg',
     {'caption': ('Reka Mura, 500 m od čebelnjaka', 'Izobraževanje evropskih veterinarjev'), 'position': (None, 'center center')}),
    # Apiturizem page (hidden section "Dan ob Muri")
    ('page.apiturizem.json', 'okolica', None, 'image', '1.webp', 'semen-cebelnjak-vrt.webp', {}),
]

log, files = [], {}


def load(name):
    if name not in files:
        p = root / 'templates' / name
        if not p.exists():
            files[name] = None
        else:
            raw = p.read_text(encoding='utf-8')
            m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
            header = m.group(0) if m else ''
            files[name] = (p, header, json.loads(raw[len(header):]), [False])
    return files[name]


for tpl, sec, blk, key, stock, real, extra in REPLACE:
    f = load(tpl)
    if not f:
        log.append(f'skip {tpl}: not in {root}')
        continue
    s = f[2]['sections'].get(sec)
    node = s and (s.get('blocks', {}).get(blk) if blk else s)
    if not node:
        log.append(f'skip {tpl} {sec}{"/" + blk if blk else ""}: not found')
        continue
    st = node.setdefault('settings', {})
    label = f'{tpl} {sec}{"/" + blk if blk else ""}'
    if st.get(key) != IMG + stock:
        continue                                   # already real, or changed by the client: leave it
    st[key] = IMG + real
    log.append(f'{label}.{key}: {stock} -> {real}')
    for k, (old, new) in extra.items():
        if (old is None or st.get(k) == old) and st.get(k) != new:
            log.append(f'{label}.{k}: {st.get(k, "<unset>")!r} -> {new!r}')
            st[k] = new
    f[3][0] = True

print(('DRY RUN, ' if dry else '') + f'{sum(1 for l in log if not l.startswith("skip"))} changes')
for line in log:
    print(' ', line)

# anything still pointing to a stock photo, in any template of the pull
left = []
for p in sorted((root / 'templates').rglob('*.json')):
    name = p.relative_to(root / 'templates').as_posix()
    f = files.get(name)
    text = json.dumps(f[2]) if f else p.read_text(encoding='utf-8')
    for st in STOCK:
        if (IMG + st) in text:
            left.append(f'{name}: {st}')
print('stock photos left:', left or 'none')

if not dry:
    for name, f in files.items():
        if f and f[3][0]:
            f[0].write_text(f[1] + json.dumps(f[2], ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
