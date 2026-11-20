"""Client's document (prodaja-medu/assets/doc/Besedilo in foto za trgovino 11. 2026.docx) used on the pages too,
not only in the blog post (user, 2026-11-20: "use it on other pages where it makes sense; on apiturizem say they
have lectures and guided tours").

1) Apiturizem: new section "ogledi" (semen-split, wheat) right after "kaj_je": guided tours and lectures, with the
   expert visits from the document (Indian and Spanish beekeepers, European veterinarians) and the veterinarians'
   training photo. The duplicate offer sentence at the end of "kaj_je" is dropped, since the next section is about it.
2) Apiturizem: "okolica" ("Dan ob Muri") switched back on (ivory) with the document's surroundings paragraph
   (Mura 500 m, paths through the forest and oxbows, cycling, ferry and weekend food in Gornja Bistrica, spas).
   Its button pointed to the hidden booking form; it now points to the directions on the contact page. The garden
   photo was captioned "Reka Mura"; the caption now says what it shows.
   Bands after this: wheat hero, ivory kaj_je, wheat ogledi, ivory okolica, wheat kdaj, ivory clanki.
3) Everywhere (index, o-nas, apiturizem, kontakt, the footer's "O nas" text): "oglede in predavanja" -> "vodene oglede in predavanja".
4) Contact page FAQ: new question about groups and expert excursions, after "Kje se nahajate?".
Not used: the document's "~500 gospodarskih panjev" (the site says ~700 čebeljih družin; the client has to say
which is right) and its beds and rest wording (the client wants tours and lectures only, no stays).

usage: python tools/ogledi_predavanja.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/page.apiturizem.json, page.o-nas.json, index.json, page.kontakt.json and
sections/footer-group.json, never
on stale local JSON (see CLAUDE.md). On live, run it after tools/faq_to_contact.py and tools/simplify_content.py
(simplify_content writes the plain "Nudimo oglede in predavanja" sentence this script then extends).
Idempotent: running it again changes nothing.
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1]) / 'templates'
dry = '--dry' in sys.argv
log = []
CONTACT = '/pages/contact'
POST = '/blogs/news/cebelarji-iz-indije-in-spanije-na-obisku'

OGLEDI = {
    'type': 'semen-split',
    'blocks': {
        'o1': {'type': 'check', 'settings': {'text': '<strong>Vodeni ogled</strong> čebelarstva, poslikanega čebelnjaka in vrta'}},
        'o2': {'type': 'check', 'settings': {'text': '<strong>Predavanje</strong> o čebelarstvu, kranjski sivki in apiterapiji'}},
        'o3': {'type': 'check', 'settings': {'text': '<strong>Ogled prevozne enote</strong>, s katero čebele selimo na paše'}},
        'o4': {'type': 'check', 'settings': {'text': '<strong>Za skupine po dogovoru</strong>, tudi za strokovne ekskurzije'}},
    },
    'block_order': ['o1', 'o2', 'o3', 'o4'],
    'settings': {
        'scheme': 'cream',
        'accent': '#c99a5c',
        'setwidth': 'container',
        'anchor': 'ogledi',
        'image': 'shopify://shop_images/izobrazevanje-evropskih-veterinarjev.jpg',
        'image_side': 'right',
        'shape': 'rect',
        'ratio': 'original',
        'image_position': 'center center',
        'image_width': 50,
        'caption': 'Izobraževanje evropskih veterinarjev',
        'title_top': 'Ogledi in predavanja',
        'title': 'Vodeni ogledi in predavanja',
        'text': '<p>Na Melincih pripravljamo vodene oglede čebelarstva in čebelnjaka ter predavanja o čebelarstvu in '
                'apiterapiji. Pokažemo, kako živi čebelja družina, kako je urejen čebelnjak za apiterapijo in kako '
                'čebele prevažamo na različne paše po Sloveniji.</p>'
                '<p>Na strokovni ekskurziji so bili pri nas že čebelarji iz Indije in Španije, pri nas so se '
                'izobraževali tudi evropski veterinarji. Več o teh obiskih preberite '
                f'<a href="{POST}">v našem blogu</a>.</p>',
        'button': 'Dogovorite se za termin',
        'link': CONTACT,
        'style_btn': 'btn-theme',
        'button_2': '',
        'link_2': '',
        'style_btn_2': 'btn-underline',
        'padding_top': 104,
        'padding_bottom': 104,
    },
}
OKOLICA_TEXT = ('<p>Obisk čebelnjaka lahko povežete z izletom. Le 500 metrov stran teče reka Mura s svojevrstnim '
                'rastlinstvom in živalstvom, do nje pa skozi gozd in mimo mrtvic vodijo številne stezice. Ravnina je '
                'kot nalašč za kolesarjenje in sprehode.</p>'
                '<p>V bližnji Gornji Bistrici se lahko z brodom zapeljete po Muri, ob vikendih pa tam ponujajo domačo '
                'kulinariko, tudi murske ribe. V bližini so znane terme: Banovci, Moravske Toplice in Lendava.</p>')
FAQ_GROUPS = {
    'faq_title': 'Ali sprejemate skupine?',
    'faq_des': '<p>Da. Za skupine pripravimo vodene oglede in predavanja o čebelarstvu in apiterapiji, tudi strokovne '
               'ekskurzije. Pokličite nas, da se dogovorimo za termin in vsebino.</p>',
}
OLD_OFFER = 'oglede in predavanja'
NEW_OFFER = 'vodene oglede in predavanja'
KAJ_JE_DUP = ' Nudimo vodene oglede in predavanja o čebelarstvu ter apiterapiji.'


def edit(name, change):
    path = root / name
    if not path.exists():
        log.append(f'skip {name}: not in this pull')
        return
    raw = path.read_text(encoding='utf-8')
    m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
    header = m.group(0) if m else ''
    data = json.loads(raw[len(header):])
    if change(name, data) and not dry:
        path.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def guided(name, node, where=''):
    """'oglede in predavanja' -> 'vodene oglede in predavanja' in every string; returns the number of changes."""
    n = 0
    items = node.items() if isinstance(node, dict) else enumerate(node) if isinstance(node, list) else []
    for k, v in items:
        if isinstance(v, str) and OLD_OFFER in v and NEW_OFFER not in v:
            node[k] = re.sub(r'(?<!vodene )\b([Nn]udimo |pripravljamo )?oglede in predavanja',
                             lambda m: (m.group(1) or '') + NEW_OFFER, v)
            log.append(f'{name} {where}{k}: "vodene oglede"')
            n += 1
        elif isinstance(v, (dict, list)):
            n += guided(name, v, f'{where}{k}.')
    return n


def apiturizem(name, data):
    s, order = data['sections'], data['order']
    changed = guided(name, s) > 0
    kaj = s.get('kaj_je', {}).get('settings', {})
    if KAJ_JE_DUP in kaj.get('text', ''):
        kaj['text'] = kaj['text'].replace(KAJ_JE_DUP, '')
        log.append(f'{name} kaj_je: offer sentence dropped (the next section is about it)')
        changed = True
    if 'ogledi' not in s:
        s['ogledi'] = OGLEDI
        order.insert(order.index('kaj_je') + 1 if 'kaj_je' in order else 1, 'ogledi')
        log.append(f'{name} ogledi: new "Vodeni ogledi in predavanja" after kaj_je')
        changed = True
    else:
        log.append(f'ok   {name}: already has "ogledi"')
    ok = s.get('okolica')
    if ok:
        st = ok['settings']
        want = {'scheme': 'white', 'text': OKOLICA_TEXT, 'caption': 'Vrt ob čebelnjaku',
                'button': 'Pot do čebelnjaka', 'link': CONTACT + '#pot', 'style_btn': 'btn-theme'}
        diff = {k: v for k, v in want.items() if st.get(k) != v}
        if ok.get('disabled') or diff:
            ok.pop('disabled', None)
            st.update(want)
            if 'okolica' in order and 'ogledi' in order and order.index('okolica') != order.index('ogledi') + 1:
                order.remove('okolica')
                order.insert(order.index('ogledi') + 1, 'okolica')
            log.append(f'{name} okolica: on, document text, button to directions ({", ".join(diff) or "enabled"})')
            changed = True
    log.append(f'{name} visible: ' + ' > '.join(k for k in order if not s[k].get('disabled')))
    return changed


def plain(name, data):
    return guided(name, data['sections']) > 0


def kontakt(name, data):
    changed = guided(name, data['sections']) > 0
    v = data['sections'].get('vprasanja')
    if not v:
        log.append(f'skip {name}: no "vprasanja" section')
        return changed
    if any(b['settings'].get('faq_title') == FAQ_GROUPS['faq_title'] for b in v['blocks'].values()):
        log.append(f'ok   {name}: FAQ already has the groups question')
        return changed
    bid = 'skupine'
    v['blocks'][bid] = {'type': 'faq', 'settings': dict(FAQ_GROUPS)}
    after = next((k for k in v['block_order'] if v['blocks'][k]['settings'].get('faq_title') == 'Kje se nahajate?'), None)
    v['block_order'].insert(v['block_order'].index(after) + 1 if after else len(v['block_order']), bid)
    log.append(f'{name} vprasanja: new question "{FAQ_GROUPS["faq_title"]}"')
    return True


edit('page.apiturizem.json', apiturizem)
edit('page.o-nas.json', plain)
edit('index.json', plain)
edit('page.kontakt.json', kontakt)
edit('../sections/footer-group.json', plain)
print(('DRY RUN, ' if dry else '') + f'{sum(1 for l in log if not l.startswith(("skip", "ok", "page.apiturizem.json visible")))} changes')
for line in log:
    print(' ', line)
