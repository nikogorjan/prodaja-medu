"""FAQ only on the contact page, plus two removals from the same feedback (user, 2026-11-20).

- page.kontakt.json: adds the section "vprasanja" (Pogosta vprašanja, faq-accordion) right after the map ("pot").
  It is built from the visible questions of the homepage FAQ (index.json faq_semen: delivery, honey, gifts,
  location) followed by the visible questions of the Apiturizem FAQ (safety, allergy, "not a medical treatment"),
  so no answer disappears from the site. The location answer points to the map above instead of linking to the
  contact page itself. Same wheat background as the other contact sections (the user's wish), 96px top and
  bottom, 56px on mobile.
  Hides "bliznjice" (Hitre povezave / Kako vam lahko pomagamo).
- page.apiturizem.json: hides the FAQ "vprasanja".
- page.o-nas.json: hides the hero fact "Čebelnjak / Melinci ob Muri" (uvod/dejstvo_3), which wrapped onto a second row.
- index.json is only read; tools/homepage_layout.py hides the homepage FAQ.
Everything is hidden (the eye icon in the theme editor), never deleted. The contact FAQ is only created when it
is missing, so running the script again changes nothing.

usage: python tools/faq_to_contact.py CONTENT_DIR [--dry]
Run it on a fresh pull of the four templates, never on stale local JSON (see CLAUDE.md). On live, run it after
tools/simplify_content.py, so the copied homepage questions already have their simplified wording.
"""
import copy, json, re, sys, pathlib

root = pathlib.Path(sys.argv[1]) / 'templates'
dry = '--dry' in sys.argv
log, docs = [], {}
WHEAT = '#f3ebda'   # like the hero panel, the contact section and the map panel on this page
OLD_LOCATION_LINK = 'Naslov in pot do nas najdete na strani <a href="/pages/contact">Kontakt</a>.'
NEW_LOCATION_LINK = 'Naslov in pot do nas najdete zgoraj, ob <a href="#pot">zemljevidu</a>.'


def load(name):
    if name not in docs:
        p = root / name
        raw = p.read_text(encoding='utf-8')
        m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
        header = m.group(0) if m else ''
        docs[name] = [p, header, json.loads(raw[len(header):]), False]
    return docs[name]


def hide(name, section, block=None, label=''):
    doc = load(name)
    s = doc[2]['sections'].get(section)
    node = s and (s.get('blocks', {}).get(block) if block else s)
    if not node:
        log.append(f'skip {name} {section}{"/" + block if block else ""}: not found')
    elif not node.get('disabled'):
        node['disabled'] = True
        doc[3] = True
        log.append(f'{name} {section}{"/" + block if block else ""}: hidden {label}')


def visible_questions(name, section):
    s = load(name)[2]['sections'].get(section)
    if not s:
        return []
    return [copy.deepcopy(s['blocks'][b]) for b in s['block_order'] if not s['blocks'][b].get('disabled')]


# 1) the contact page gets the FAQ (once)
contact = load('page.kontakt.json')
cs = contact[2]['sections']
if 'vprasanja' not in cs:
    home = load('index.json')[2]['sections'].get('faq_semen')
    if not home:
        sys.exit('index.json has no faq_semen to copy, nothing written')
    blocks = visible_questions('index.json', 'faq_semen') + visible_questions('page.apiturizem.json', 'vprasanja')
    for b in blocks:
        des = b.get('settings', {}).get('faq_des', '')
        if OLD_LOCATION_LINK in des:
            b['settings']['faq_des'] = des.replace(OLD_LOCATION_LINK, NEW_LOCATION_LINK)
    ids = [f'q{i}' for i in range(1, len(blocks) + 1)]
    section = {'type': 'faq-accordion', 'blocks': dict(zip(ids, blocks)), 'block_order': ids,
               'settings': copy.deepcopy(home.get('settings', {}))}
    section['settings'].update({'bgsection': WHEAT, 'paddingsection': '96px 0px 96px 0px', 'paddingmobile': '56px 0px 56px 0px'})
    cs['vprasanja'] = section
    order = contact[2]['order']
    order.insert(order.index('pot') + 1 if 'pot' in order else len(order), 'vprasanja')
    contact[3] = True
    log.append(f'page.kontakt.json vprasanja: new FAQ after the map with {len(blocks)} questions: '
               + ' | '.join(b['settings'].get('faq_title', '') for b in blocks))
hide('page.kontakt.json', 'bliznjice', label='(Hitre povezave)')

# 2) no FAQ elsewhere, 3) O nas hero without the wrapping fact
hide('page.apiturizem.json', 'vprasanja', label='(FAQ, now on the contact page)')
hide('page.o-nas.json', 'uvod', 'dejstvo_3', label='(Čebelnjak / Melinci ob Muri)')

print(('DRY RUN, ' if dry else '') + f'{sum(1 for l in log if not l.startswith("skip"))} changes')
for line in log:
    print(' ', line)
if not dry:
    for p, header, data, changed in docs.values():
        if changed:
            p.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
