"""Homepage layout (user feedback of 2026-11-20): few sections, consistent spacing, no FAQ.

Order and visibility:
  hero (naslovna) -> honeys (izdelki_semen) -> "O nas" and "Apiterapija" as two equal blocks side by side, each
  with a photo, heading, text and a filled button (o_nas_apiterapija, a "Kartice (Šemen)" section in a wheat band)
  -> news (novice_semen) -> footer.
  Every other homepage section is hidden (the eye icon in the theme editor), never deleted. The former zig-zag
  blocks druzina_semen and apiterapija_semen stay hidden for later use; their texts seed the new cards. The FAQ
  (faq_semen) is hidden too: the FAQ lives only on the contact page (tools/faq_to_contact.py copies its questions).
Spacing: every section has the same padding, 96px top and bottom on desktop, 56px on mobile.
Backgrounds alternate: ivory honeys, wheat cards, ivory news, then the dark footer.

usage: python tools/homepage_layout.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/index.json, never on stale local JSON (see CLAUDE.md); on live after
tools/simplify_content.py. The cards section is only created when it is missing; an existing one keeps its texts.
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1])
dry = '--dry' in sys.argv
p = root / 'templates' / 'index.json'
raw = p.read_text(encoding='utf-8')
m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
header = m.group(0) if m else ''
d = json.loads(raw[len(header):])
S = d['sections']
log = []

IVORY = '#faf7f0'
CARDS = 'o_nas_apiterapija'
VISIBLE = ['naslovna', 'izdelki_semen', CARDS, 'novice_semen']
LAYOUT = {   # theme sections: (background, desktop padding, mobile padding)
    'izdelki_semen': (IVORY, '96px 0px 96px 0px', '56px 0px 56px 0px'),
    'novice_semen': (IVORY, '96px 0px 96px 0px', '56px 0px 56px 0px'),
}
CARDS_SETTINGS = {'scheme': 'cream', 'columns': '2', 'card_style': 'line', 'card_title': 'lg', 'card_btn': 'btn-theme',
                  'heading_layout': 'center', 'padding_top': 96, 'padding_bottom': 96,
                  # no section heading above the two blocks (unset settings would fall back to the schema's placeholders)
                  'title_top': '', 'title': '', 'des': '', 'button': ''}
O_NAS_IMAGE = 'shopify://shop_images/semen-med-polica.png'   # the client's own honey shelf (no stock photos, 2026-11-20)


def setv(node, key, value, label):
    old = node.get(key, '<unset>')
    if old != value:
        node[key] = value
        log.append(f'{label}.{key}: {old!r} -> {value!r}')


def text_block(section_key):
    s = S[section_key]
    return next(s['blocks'][b]['settings'] for b in s['block_order'] if s['blocks'][b]['type'] != 'image_block')


def image_of(section_key):
    s = S[section_key]
    return next((s['blocks'][b]['settings'].get('image') for b in s['block_order'] if s['blocks'][b]['type'] == 'image_block'), None)


if CARDS not in S:
    fam, api = text_block('druzina_semen'), text_block('apiterapija_semen')
    first_paragraph = (re.findall(r'<p>.*?</p>', fam.get('answer_content', ''), flags=re.S) or [''])[0]
    S[CARDS] = {
        'type': 'semen-cards',
        'blocks': {
            'o_nas': {'type': 'card', 'settings': {'icon': 'none', 'image': O_NAS_IMAGE, 'title': fam.get('title', 'Čebelarimo od leta 1982'),
                                                   'text': first_paragraph, 'link_label': 'O nas', 'link': '/pages/o-nas'}},
            'apiterapija': {'type': 'card', 'settings': {'icon': 'none', 'image': image_of('apiterapija_semen'), 'title': api.get('title', 'Apiterapija'),
                                                         'text': api.get('answer_content', ''), 'link_label': api.get('button') or 'Več o apiterapiji',
                                                         'link': api.get('link') or '/pages/apiturizem'}},
        },
        'block_order': ['o_nas', 'apiterapija'],
        'settings': {},
    }
    log.append(f'{CARDS}: new "Kartice (Šemen)" section with the cards O nas and Apiterapija')

missing = [k for k in VISIBLE if k not in S]
if missing:
    sys.exit(f'missing sections, nothing written: {missing}')

# order: the visible sections first, in this order; all others after them, in their current relative order
new_order = VISIBLE + [k for k in d['order'] if k not in VISIBLE] + [k for k in S if k not in d['order'] and k not in VISIBLE]
if d['order'] != new_order:
    log.append(f'order -> {VISIBLE} + {len(new_order) - len(VISIBLE)} hidden')
    d['order'] = new_order

for k in d['order']:
    s = S[k]
    if k in VISIBLE:
        if s.get('disabled'):
            del s['disabled']
            log.append(f'{k}.disabled: True -> <unset>')
    else:
        setv(s, 'disabled', True, k)

for k, (bg, pad, padm) in LAYOUT.items():
    st = S[k].setdefault('settings', {})
    setv(st, 'bgsection', bg, k)
    setv(st, 'paddingsection', pad, k)
    setv(st, 'paddingmobile', padm, k)
for key, value in CARDS_SETTINGS.items():
    setv(S[CARDS].setdefault('settings', {}), key, value, CARDS)

print(('DRY RUN, ' if dry else '') + f'{len(log)} changes')
for line in log:
    print(' ', line)
if not dry and log:
    p.write_text(header + json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
