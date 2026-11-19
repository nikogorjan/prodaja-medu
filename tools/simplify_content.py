"""Gregor's feedback of 2026-11-05 applied to a freshly pulled copy of the theme's content JSON.

- Homepage: fewer sections, only what helps a buyer decide (hero with two honey slides and the
  benefits, honeys, quality promise, family, a short apitherapy presentation, FAQ, news).
- Apitherapy is presented, not offered: no stays or overnight wording, no booking calls to action;
  the offer is a single sentence (OFFER below).
- Links to /pages/kontakt (that page does not exist) point to /pages/contact.

2026-11-19: the offer sentence is now about tours and lectures (no booking, no stays), and the
homepage also hides "Naša obljuba" (kakovost) and "Družina Šemen" (druzina_semen) and the four
benefits under the hero slider (prednost_1-4). Older wording already applied to a theme is
rewritten too (OLD_PHRASE -> NEW_PHRASE).

usage: python simplify_content.py CONTENT_DIR [--dry]
Every change is targeted and idempotent. Sections and blocks are only disabled (the eye icon in the
theme editor), never deleted, so each one can be switched back on. Run it on a fresh pull, never on
stale local JSON (see CLAUDE.md).
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1])
dry = '--dry' in sys.argv
log = []

OFFER = 'Nudimo oglede in predavanja o čebelarstvu ter apiterapiji.'
OLD_PHRASE = 'ogled in predstavitev čebelarstva ter apiterapije'
NEW_PHRASE = 'oglede in predavanja o čebelarstvu ter apiterapiji'


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
        log.append(f'{label}.{key}: {str(old)[:70]!r} -> {str(value)[:70]!r}')


def swap(where, key, old, new, label):
    """Replace a phrase inside a text setting, if it is still there."""
    text = where.get(key)
    if isinstance(text, str) and old in text:
        setv(where, key, text.replace(old, new), label)


def hide(node, label):
    setv(node, 'disabled', True, label)


def fix_links(node, label):
    """/pages/kontakt does not exist; the contact page is /pages/contact."""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and '/pages/kontakt' in v:
                setv(node, k, v.replace('/pages/kontakt', '/pages/contact'), label)
            else:
                fix_links(v, label)
    elif isinstance(node, list):
        for v in node:
            fix_links(v, label)


def rephrase(node, label):
    """Older offer wording (2026-11-05) -> tours and lectures (2026-11-19)."""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and OLD_PHRASE in v:
                setv(node, k, v.replace(OLD_PHRASE, NEW_PHRASE), label)
            else:
                rephrase(v, label)
    elif isinstance(node, list):
        for v in node:
            rephrase(v, label)


def page(name):
    p = root / 'templates' / name
    if not p.exists():
        return None, None, None
    hdr, d = load(p)
    return p, hdr, d


# ------------------------------------------------------------------ homepage
p, hdr, d = page('index.json')
if d:
    S = d['sections']
    hero = S.get('naslovna')
    if hero and 'slide_apiturizem' in hero.get('blocks', {}):
        hide(hero['blocks']['slide_apiturizem'], 'index.naslovna.slide_apiturizem')
    # 2026-11-19: the four "prednosti" under the slider (Dostava po Sloveniji, Lastna pridelava,
    # Skrbno pakirano, Tradicija od leta 1982) are no longer shown
    for bid in ('prednost_1', 'prednost_2', 'prednost_3', 'prednost_4'):
        if hero and bid in hero.get('blocks', {}):
            hide(hero['blocks'][bid], f'index.naslovna.{bid}')

    # fewer sections: numbers, production steps, rooms, "Dan ob Muri", "Med, izdelki in doživetja", map
    # 2026-11-19: also "Naša obljuba" (kakovost) and "Družina Šemen" (druzina_semen), kept for later use
    for key in ('stevilke_semen', 'pridelava_semen', 'prostori_semen', 'lokacija_semen', 'kakovost', 'druzina_semen'):
        if key in S:
            hide(S[key], f'index.{key}')
    for key, s in S.items():
        if s['type'] in ('parallax-banner', 'grid-banner'):
            hide(s, f'index.{key}')

    fam = S.get('druzina_semen')
    if fam:
        # the numbers no longer follow the family story, so it gets its full bottom padding back
        setv(fam['settings'], 'paddingsection', '110px 0px 110px 0px', 'index.druzina_semen')
        txt = fam.get('blocks', {}).get('druzina_text', {}).get('settings', {})
        swap(txt, 'answer_content', 'naš poslikani čebelnjak na Melincih ob Muri pa smo odprli tudi za obiskovalce.',
             'naš poslikani čebelnjak na Melincih ob Muri pa je namenjen tudi apiterapiji.', 'index.druzina_text')

    api = S.get('apiterapija_semen')
    if api:
        txt = api.get('blocks', {}).get('prostori_text', {}).get('settings', {})
        setv(txt, 'subtitle', 'Apiterapija', 'index.apiterapija')
        setv(txt, 'title', 'Poslikani čebelnjak na Melincih', 'index.apiterapija')
        setv(txt, 'answer_content',
             '<p>V našem čebelnjaku je 40 panjev, prirejenih za apiterapijo. Zrak iz panjev je topel in diši po medu, '
             'vosku in propolisu, čebele pa ostanejo za steno: slišite in vonjate jih, srečate pa ne.</p>'
             f'<p>{OFFER}</p>', 'index.apiterapija')

    faq = S.get('faq_semen')
    if faq:
        B = faq.get('blocks', {})
        if 'q4' in B and 'obisk' in B['q4']['settings'].get('faq_title', '').lower():
            hide(B['q4'], 'index.faq.q4')
        if 'q3' in B:
            swap(B['q3']['settings'], 'faq_des', ' Ob obisku čebelnjaka lahko vse vrste tudi poskusite.', '', 'index.faq.q3')
        if 'q6' in B and B['q6']['settings'].get('faq_title', '').startswith('Kje se nahajate'):
            setv(B['q6']['settings'], 'faq_des',
                 '<p>Na Melincih pri Beltincih, 12 km od Murske Sobote. Naslov in pot do nas najdete na strani '
                 '<a href="/pages/contact">Kontakt</a>.</p>', 'index.faq.q6')

    fix_links(d, 'index')
    rephrase(d, 'index')
    save(p, hdr, d)

# ------------------------------------------------------------------ Apiturizem page: presentation, not offer
p, hdr, d = page('page.apiturizem.json')
if d:
    S = d['sections']
    u = S.get('uvod')
    if u:
        st = u['settings']
        setv(st, 'title_top', 'Apiterapija', 'apiturizem.uvod')
        setv(st, 'text', f'<p>V poslikanem čebelnjaku na Melincih ob Muri je 40 panjev, prirejenih za apiterapijo. {OFFER}</p>',
             'apiturizem.uvod')
        setv(st, 'button', '', 'apiturizem.uvod')
        setv(st, 'link', '', 'apiturizem.uvod')
        setv(st, 'button_2', 'Kontakt', 'apiturizem.uvod')
        setv(st, 'link_2', '/pages/contact', 'apiturizem.uvod')
        F = u.get('blocks', {})
        if 'dejstvo_1' in F:
            setv(F['dejstvo_1']['settings'], 'label', 'Panjev', 'apiturizem.uvod.dejstvo_1')
            setv(F['dejstvo_1']['settings'], 'value', '40', 'apiturizem.uvod.dejstvo_1')
        if 'dejstvo_2' in F:
            setv(F['dejstvo_2']['settings'], 'label', 'Čebelarimo', 'apiturizem.uvod.dejstvo_2')
            setv(F['dejstvo_2']['settings'], 'value', 'od leta 1982', 'apiturizem.uvod.dejstvo_2')

    k = S.get('kaj_je')
    if k:
        st = k['settings']
        setv(st, 'title_top', 'Kaj je apiterapija', 'apiturizem.kaj_je')
        setv(st, 'title', 'Zrak iz čebeljih panjev', 'apiturizem.kaj_je')
        setv(st, 'text',
             '<p>Apiterapija (iz latinske besede <em>apis</em>, čebela) je uporaba čebeljih pridelkov, med njimi tudi zraka '
             'iz panjev. V našem čebelnjaku je 40 panjev, prirejenih tako, da topel zrak z vonjem medu, voska in propolisa '
             'skozi odprtine prehaja v prostor, čebele pa ostanejo za steno.</p>'
             '<p>Čebelarstvo je del slovenske dediščine, od kranjske sivke, avtohtone slovenske čebele, do poslikanih '
             f'panjskih končnic. To tradicijo nadaljuje tudi naš čebelnjak, ki ga krasijo velike poslikave. {OFFER}</p>',
             'apiturizem.kaj_je')
        q = k.get('blocks', {}).get('citat', {}).get('settings')
        if q is not None:
            setv(q, 'quote', 'Zrak v čebelnjaku je topel in diši po medu, vosku in propolisu.', 'apiturizem.kaj_je.citat')

    c = S.get('kdaj')
    if c:
        st = c['settings']
        setv(st, 'title', 'Leto v čebelnjaku', 'apiturizem.kdaj')
        setv(st, 'des', 'Čebelnjak se spreminja z vsakim mesecem. Izberite letni čas in poglejte, kaj takrat cveti in kateri med točimo.',
             'apiturizem.kdaj')
        setv(st, 'button', '', 'apiturizem.kdaj')
        for bk, b in c.get('blocks', {}).items():
            if b['type'] == 'season':
                setv(b['settings'], 'best', '', f'apiturizem.kdaj.{bk}')
        z = c.get('blocks', {}).get('zima', {}).get('settings', {})
        swap(z, 'text', 'Panjev ne odpiramo, zato obisk prilagodimo: več pogovora, ogled poslikav in degustacija.',
             'Panjev ne odpiramo, čebelnjak počiva do prvih toplih dni.', 'apiturizem.kdaj.zima')

    # the offer, the visit steps, target groups, surroundings and the booking form go
    for key in ('ponudba', 'obisk', 'za_koga', 'okolica', 'povprasevanje'):
        if key in S:
            hide(S[key], f'apiturizem.{key}')

    v = S.get('vprasanja')
    if v:
        setv(v['settings'], 'title', 'Pogosta vprašanja o apiterapiji', 'apiturizem.vprasanja')
        B = v.get('blocks', {})
        for bk in ('q3', 'q4', 'q5', 'q6'):   # duration, children, groups, price: questions about booking a visit
            if bk in B:
                hide(B[bk], f'apiturizem.vprasanja.{bk}')
        if 'q2' in B:
            setv(B['q2']['settings'], 'faq_des',
                 '<p>Od čebel vas v čebelnjaku loči stena, kljub temu nam alergijo prosimo sporočite vnaprej. '
                 'Če imate predpisano zdravilo za nujne primere, ga imejte pri sebi.</p>', 'apiturizem.vprasanja.q2')

    fix_links(d, 'apiturizem')
    rephrase(d, 'apiturizem')
    save(p, hdr, d)

# ------------------------------------------------------------------ O nas
p, hdr, d = page('page.o-nas.json')
if d:
    S = d['sections']
    if 'uvod' in S:
        st = S['uvod']['settings']
        swap(st, 'text', 'v poslikanem čebelnjaku na Melincih ob Muri pa sprejemamo obiskovalce.',
             'v poslikanem čebelnjaku na Melincih ob Muri pa nudimo oglede in predavanja o čebelarstvu ter apiterapiji.', 'o-nas.uvod')
        if st.get('button_2') == 'Obiščite čebelnjak':
            setv(st, 'button_2', 'O apiterapiji', 'o-nas.uvod')
    v4 = S.get('vrednote', {}).get('blocks', {}).get('v4', {}).get('settings')
    if v4 is not None:
        setv(v4, 'title', 'Čebelnjak za apiterapijo', 'o-nas.vrednote.v4')
        setv(v4, 'text', '<p>V poslikanem čebelnjaku na Melincih nudimo oglede in predavanja o čebelarstvu ter apiterapiji.</p>',
             'o-nas.vrednote.v4')
        setv(v4, 'link_label', 'Več o apiterapiji', 'o-nas.vrednote.v4')
    if S.get('poslikava', {}).get('settings', {}).get('button') == 'Več o apiturizmu':
        setv(S['poslikava']['settings'], 'button', 'Več o apiterapiji', 'o-nas.poslikava')
    g3 = S.get('galerija', {}).get('blocks', {}).get('g3', {}).get('settings')
    if g3 is not None and g3.get('caption') == 'Prostor za počitek pod streho':
        setv(g3, 'caption', 'Prostor za apiterapijo', 'o-nas.galerija.g3')
    if 'poziv' in S:
        st = S['poziv']['settings']
        if st.get('title') == 'Poskusite naš med ali nas obiščite':
            setv(st, 'title', 'Poskusite naš med', 'o-nas.poziv')
        setv(st, 'text', '<p>Med in čebelje izdelke pošljemo po vsej Sloveniji, po dogovoru pa jih lahko prevzamete tudi v čebelnjaku na Melincih.</p>',
             'o-nas.poziv')
        setv(st, 'button_2', '', 'o-nas.poziv')
        setv(st, 'link_2', '', 'o-nas.poziv')
    fix_links(d, 'o-nas')
    rephrase(d, 'o-nas')
    save(p, hdr, d)

# ------------------------------------------------------------------ Kontakt
p, hdr, d = page('page.kontakt.json')
if d:
    S = d['sections']
    b2 = S.get('bliznjice', {}).get('blocks', {}).get('b2', {}).get('settings')
    if b2 is not None:
        setv(b2, 'title', 'Apiterapija', 'kontakt.bliznjice.b2')
        setv(b2, 'text', '<p>Nudimo oglede in predavanja o čebelarstvu ter apiterapiji v čebelnjaku na Melincih ob Muri.</p>',
             'kontakt.bliznjice.b2')
        setv(b2, 'link_label', 'Več o apiterapiji', 'kontakt.bliznjice.b2')
    i5 = S.get('kontakt', {}).get('blocks', {}).get('i5', {}).get('settings')
    if i5 is not None and i5.get('label') == 'Čebelnjak in apiturizem':
        setv(i5, 'label', 'Čebelnjak', 'kontakt.kontakt.i5')
    if 'pot' in S:
        swap(S['pot']['settings'], 'address', 'Čebelnjak in apiturizem Šemen', 'Čebelarstvo Šemen', 'kontakt.pot')
    fix_links(d, 'kontakt')
    rephrase(d, 'kontakt')
    save(p, hdr, d)

# ------------------------------------------------------------------ every other template: only the broken links
for p in sorted((root / 'templates').rglob('*.json')):
    if p.name in ('index.json', 'page.apiturizem.json', 'page.o-nas.json', 'page.kontakt.json'):
        continue
    hdr, d = load(p)
    before = len(log)
    fix_links(d, p.name)
    if len(log) > before:
        save(p, hdr, d)

# ------------------------------------------------------------------ footer: the one-sentence offer
p = root / 'sections' / 'footer-group.json'
if p.exists():
    hdr, d = load(p)
    f = d['sections'].get('footer')
    if f:
        for bk, b in f.get('blocks', {}).items():
            st = b.get('settings', {})
            swap(st, 'text', 'Čebelarstvo in apiturizem Šemen je', 'Čebelarstvo Šemen je', f'footer.{bk}')
            swap(st, 'text', ' ter doživetja v našem poslikanem čebelnjaku.',
                 ', v poslikanem čebelnjaku na Melincih pa nudimo oglede in predavanja o čebelarstvu ter apiterapiji.', f'footer.{bk}')
    fix_links(d, 'footer-group')
    rephrase(d, 'footer-group')
    save(p, hdr, d)

print(('DRY RUN, ' if dry else '') + f'{len(log)} changes')
for line in log:
    print('  ' + line)
