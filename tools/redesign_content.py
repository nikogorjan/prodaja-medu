"""Apply the light cream redesign ("Šemen · Nova podoba") to a freshly pulled copy of the theme's content JSON.

usage: python redesign_content.py CONTENT_DIR [--dry]
CONTENT_DIR holds templates/, sections/ (groups) and config/settings_data.json as pulled from a
theme. Every change is targeted and idempotent, so the same script can later be run on a fresh
pull of the live theme (content the client edited in the meantime is kept).
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1])
dry = '--dry' in sys.argv
log = []

IVORY, TINT, WHEAT = '#faf7f0', '#f6edd3', '#f3ebda'
DARK_OLD = ('#2b2420', '#2e3a29', '#262626')
BRONZE = '#88612d'
INK, MUTED = '#252320', '#67625a'

def load(p):
    raw = p.read_text(encoding='utf-8')
    m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
    header = m.group(0) if m else ''
    return header, json.loads(raw[len(header):])

def save(p, header, data):
    if not dry:
        p.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

def setv(where, key, value, label):
    old = where.get(key, '<unset>')
    if old != value:
        where[key] = value
        log.append(f'{label}.{key}: {old} -> {value}')

def section(d, key):
    return d['sections'].get(key)

# ------------------------------------------------------------------ homepage
p = root / 'templates' / 'index.json'
hdr, d = load(p)
S = d['sections']

hero = section(d, 'naslovna')
if hero:
    # pisava in velikost naslova ostaneta kot prej (velike črke); svetlejši je le preliv čez fotografijo
    if hero['settings'].get('title_size') == 76:
        setv(hero['settings'], 'title_size', 56, 'naslovna')
    if hero['settings'].get('uppercase') is False:
        setv(hero['settings'], 'uppercase', True, 'naslovna')
    for bid in hero.get('block_order', []):
        b = hero['blocks'][bid]
        if b['type'] == 'slide':
            setv(b['settings'], 'shade', 60, f'naslovna.{bid}')
            t = b['settings'].get('title', '')
            if '*' in t:
                setv(b['settings'], 'title', t.replace('*', ''), f'naslovna.{bid}')

prod = section(d, 'izdelki_semen')
if prod:
    st = prod['settings']
    setv(st, 'bgsection', IVORY, 'izdelki_semen')
    if st.get('title') == 'Izbrani izdelki':
        setv(st, 'title', 'Od svetle akacije do temne ajde', 'izdelki_semen')
    # nad medovi je samo naslov, brez nadnaslova
    setv(st, 'title_top', '', 'izdelki_semen')
    setv(st, 'paddingsection', '96px 0px 96px 0px', 'izdelki_semen')

q = section(d, 'kakovost')
if q:
    st = q['settings']
    setv(st, 'edge', False, 'kakovost')
    setv(st, 'pattern', False, 'kakovost')
    setv(st, 'frame', 'arch', 'kakovost')
    setv(st, 'scheme', 'cream', 'kakovost')
    if '*' in st.get('title', ''):
        setv(st, 'title', st['title'].replace('*', ''), 'kakovost')

for key in ('druzina_semen',):
    s = section(d, key)
    if s:
        setv(s['settings'], 'bgsection', IVORY, key)
        setv(s['settings'], 'paddingsection', '110px 0px 40px 0px', key)

num = section(d, 'stevilke_semen')
if num:
    st = num['settings']
    setv(st, 'bgsection', IVORY, 'stevilke_semen')
    setv(st, 'titlecolor', INK, 'stevilke_semen')
    setv(st, 'subcolor', MUTED, 'stevilke_semen')
    setv(st, 'paddingsection', '40px 0px 96px 0px', 'stevilke_semen')

pr = section(d, 'pridelava_semen')
if pr:
    # pridelava na pšeničnem pasu (med kremno družino in medeno apiterapijo)
    setv(pr['settings'], 'bgsection', WHEAT, 'pridelava_semen')
    setv(pr['settings'], 'pattern_opacity', 0, 'pridelava_semen')

for key in ('apiterapija_semen', 'prostori_semen'):
    s = section(d, key)
    if s:
        setv(s['settings'], 'bgsection', TINT, key)
        setv(s['settings'], 'animation', 'fade-up', key)
if section(d, 'apiterapija_semen'):
    setv(S['apiterapija_semen']['settings'], 'paddingsection', '110px 0px 20px 0px', 'apiterapija_semen')
if section(d, 'prostori_semen'):
    setv(S['prostori_semen']['settings'], 'paddingsection', '70px 0px 110px 0px', 'prostori_semen')

# the ticker band and the separate newsletter band go (the footer keeps the newsletter)
for key, s in S.items():
    if s['type'] == 'scrolling-text':
        setv(s, 'disabled', True, key)
    if s['type'] == 'newsletter':
        setv(s, 'disabled', True, key)
for key in ('line_FJRLJP', 'line_3i3f9f'):
    if key in S:
        setv(S[key], 'disabled', True, key)

for key, s in S.items():
    st = s.get('settings', {})
    if s['type'] in ('grid-banner', 'faq-accordion', 'featured-articles', 'line') and st.get('bgsection', '').lower() in ('#ffffff', '#f7f3ea'):
        setv(st, 'bgsection', IVORY, key)
    if s['type'] == 'line':
        setv(st, 'bgborder', '#e3dccd', key)
    if s['type'] == 'parallax-banner':
        setv(st, 'opacity_bg_overlay', 0.4, key)
    if s['type'] == 'grid-banner':
        setv(st, 'opacity_overlay', 0.6, key)

# numbers directly after the family story: one light chapter instead of two dark bands
order = d['order']
if 'stevilke_semen' in order and 'druzina_semen' in order:
    order.remove('stevilke_semen')
    order.insert(order.index('druzina_semen') + 1, 'stevilke_semen')
    log.append('index.order: stevilke_semen moved after druzina_semen')
save(p, hdr, d)

# ------------------------------------------------------------------ subpages
PAGE_SCHEMES = {
    'page.o-nas.json': {'poslikava': 'tint'},
    # Apiturizem: kremni in barvni pasovi se izmenjujejo (pšenični, medeni)
    'page.apiturizem.json': {'kaj_je': 'white', 'kdaj': 'cream', 'ponudba': 'white', 'obisk': 'tint',
                             'za_koga': 'white', 'okolica': 'cream', 'povprasevanje': 'tint'},
    # Kontakt: obrazec in hitre povezave na medenem pasu (vmes pšenični zemljevid)
    'page.kontakt.json': {'kontakt': 'tint', 'bliznjice': 'tint'},
}
# Apiturizem: čebelji koledar takoj za uvodom "Kaj je apiturizem"
PAGE_MOVES = {'page.apiturizem.json': [('kdaj', 'kaj_je')]}
for fname, schemes in PAGE_SCHEMES.items():
    p = root / 'templates' / fname
    if not p.exists():
        continue
    hdr, d = load(p)
    for key, after in PAGE_MOVES.get(fname, []):
        order = d['order']
        if key in order and after in order and order.index(key) != order.index(after) + 1:
            order.remove(key)
            order.insert(order.index(after) + 1, key)
            log.append(f'{fname}.order: {key} moved after {after}')
    for key, s in d['sections'].items():
        st = s.get('settings', {})
        if s['type'] == 'semen-page-hero' and st.get('bgsection', '').lower() in DARK_OLD:
            setv(st, 'bgsection', WHEAT, f'{fname}:{key}')
        if s['type'] == 'service' and st.get('bgsection', '').lower() == '#2b2420':
            setv(st, 'bgsection', IVORY, f'{fname}:{key}')
            setv(st, 'titlecolor', INK, f'{fname}:{key}')
            setv(st, 'subcolor', MUTED, f'{fname}:{key}')
        if s['type'] == 'faq-accordion' and st.get('bgsection', '').lower() in ('#f7f3ea', '#ffffff'):
            setv(st, 'bgsection', IVORY, f'{fname}:{key}')
        if key in schemes and 'scheme' in st:
            setv(st, 'scheme', schemes[key], f'{fname}:{key}')
    save(p, hdr, d)

# ------------------------------------------------------------------ other templates: white bands -> ivory
for p in sorted((root / 'templates').glob('*.json')):
    if p.name in ('index.json',) or p.name in PAGE_SCHEMES:
        continue
    hdr, d = load(p)
    changed = False
    for key, s in d.get('sections', {}).items():
        st = s.get('settings', {})
        for k in ('bgsection', 'cart_bg'):
            if str(st.get(k, '')).lower() == '#ffffff':
                setv(st, k, IVORY, f'{p.name}:{key}')
                changed = True
    if changed:
        save(p, hdr, d)

# ------------------------------------------------------------------ product page: sticky "add to cart" bar, cream like the page
p = root / 'templates' / 'product.json'
if p.exists():
    hdr, d = load(p)
    m = d['sections'].get('main')
    if m:
        ms = m['settings']
        setv(ms, 'mix_1', IVORY, 'product.main')
        setv(ms, 'text_cl', INK, 'product.main')
        setv(ms, 'cart_bg', INK, 'product.main')
        setv(ms, 'cart_cl', IVORY, 'product.main')
        setv(ms, 'cart_cl_hover', INK, 'product.main')
        save(p, hdr, d)

# ------------------------------------------------------------------ header and footer groups
p = root / 'sections' / 'header-group.json'
if p.exists():
    hdr, d = load(p)
    h = d['sections'].get('header')
    if h:
        st = h['settings']
        for k in ('textcolor', 'linkcolor', 'menutext', 'menudroptexttitle'):
            setv(st, k, INK, 'header')
        for k in ('linkhover', 'menutexthover'):
            setv(st, k, BRONZE, 'header')
        setv(st, 'color_indicator', '#c99a5c', 'header')
        setv(st, 'type_menu', 'uppercase', 'header')
        setv(st, 'font_sizemenu', '12px', 'header')
    save(p, hdr, d)

p = root / 'sections' / 'footer-group.json'
if p.exists():
    hdr, d = load(p)
    f = d['sections'].get('footer')
    if f:
        st = f['settings']
        setv(st, 'background', WHEAT, 'footer')
        setv(st, 'border_headfooter', '#e3dccd', 'footer')
        setv(st, 'border-copryright', '#e3dccd', 'footer')
        setv(st, 'text', '#3f3b35', 'footer')
        setv(st, 'text_hover', BRONZE, 'footer')
        setv(st, 'title', BRONZE, 'footer')
        setv(st, 'footer_font_family', '--g-font-2', 'footer')
        setv(st, 'footer_font_weight', '500', 'footer')
        setv(st, 'padding_top', 88, 'footer')
        for bid in f.get('block_order', []):
            b = f['blocks'][bid]
            bs = b['settings']
            # zlati grb nad stolpcem "O nas": edini podpis v temni nogi
            if b['type'] == 'text' and str(bs.get('title', '')).strip().lower() == 'o nas' and not bs.get('logofooter'):
                setv(bs, 'logofooter', 'shopify://shop_images/semen-logo.png', f'footer.{bid}')
                setv(bs, 'widthlogofooter', 80, f'footer.{bid}')
            if b['type'] == 'newsletter':
                setv(bs, 'btn_bg_new', INK, f'footer.{bid}')
                setv(bs, 'btn_cl_new', IVORY, f'footer.{bid}')
                setv(bs, 'btn_cl_new_hover', INK, f'footer.{bid}')
                setv(bs, 'border_new', '#8f8879', f'footer.{bid}')
    save(p, hdr, d)

# ------------------------------------------------------------------ theme settings: fonts
p = root / 'config' / 'settings_data.json'
if p.exists():
    hdr, d = load(p)
    cur = d['current'] if isinstance(d['current'], dict) else d['presets'][d['current']]
    if cur.get('font_family') in ('ebgaramond_n4', 'cormorant_n5'):
        setv(cur, 'font_family', 'zurich_extended_n4', 'settings')
    if cur.get('font_family2') == 'jost_n4':
        setv(cur, 'font_family2', 'poppins_n4', 'settings')
    if str(cur.get('bg_breadcrumb', '')).lower() == '#ffffff':
        setv(cur, 'bg_breadcrumb', IVORY, 'settings')
    save(p, hdr, d)

print(('DRY RUN, ' if dry else '') + f'{len(log)} changes')
for line in log:
    print('  ' + line)
