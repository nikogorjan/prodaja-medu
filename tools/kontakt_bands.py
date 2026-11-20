"""Contact page bands (user, 2026-11-20: "on the contact page I don't like that all sections are cream").

Before: hero, contact, map and FAQ were all wheat (#f3ebda). After, alternating down to the black footer:
  uvod (hero) wheat > kontakt ivory > pot (full-width map) > vprasanja (FAQ) wheat
- kontakt: scheme "white" (Slonokoščeno). With the semen-contact.liquid code the details and the form sit directly
  on the ivory band, no card (user: "I don't like the form on cream bg").
- pot: layout "full" (map across the full width, 640px tall, address card floating on it; user: "the map could be
  taller, maybe full width"). Needs the map.liquid code with the layout and map_height settings.
- vprasanja: stays wheat (#f3ebda), so it differs from the ivory contact band above the map.
Idempotent.

usage: python tools/kontakt_bands.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/page.kontakt.json, never on stale local JSON (see CLAUDE.md). On live, run it
after tools/faq_to_contact.py, which creates "vprasanja".
"""
import json, re, sys, pathlib

path = pathlib.Path(sys.argv[1]) / 'templates' / 'page.kontakt.json'
dry = '--dry' in sys.argv
WANT = [('kontakt', 'scheme', 'white'), ('pot', 'layout', 'full'), ('pot', 'map_height', 640),
        ('vprasanja', 'bgsection', '#f3ebda')]

raw = path.read_text(encoding='utf-8')
m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
header = m.group(0) if m else ''
data = json.loads(raw[len(header):])
log = []
for sid, key, value in WANT:
    s = data['sections'].get(sid)
    if not s:
        log.append(f'skip {sid}: not on the page')
    elif s.setdefault('settings', {}).get(key) == value:
        log.append(f'ok   {sid}: {key} already {value}')
    else:
        log.append(f'{sid}: {key} {s["settings"].get(key)} -> {value}')
        s['settings'][key] = value
changed = [l for l in log if not l.startswith(('skip', 'ok'))]
if changed and not dry:
    path.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(('DRY RUN, ' if dry else '') + f'{len(changed)} changes')
for line in log:
    print(' ', line)
