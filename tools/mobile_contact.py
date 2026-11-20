"""Mobile menu contact details (user, 2026-11-20: "mobile menu has false mail and phone number there still").

The mobile menu (snippets/menu-mobile.liquid, slide-menu.liquid) shows theme settings mobile_phone and
mobile_email. They were the theme's demo values ("+012 345 678"; the email was unset, so the schema default
"mailsupport@gmail.com" showed). Set to the shop's real contacts, the same as on the contact page.
Also: free shipping line stays off until it is set up in the admin (free_shipping_enable false, threshold 0), see
snippets/free-shipping.liquid. Idempotent.

usage: python tools/mobile_contact.py CONTENT_DIR [--dry]
Run it on a fresh pull of config/settings_data.json, never on stale local JSON (see CLAUDE.md).
"""
import json, re, sys, pathlib

path = pathlib.Path(sys.argv[1]) / 'config' / 'settings_data.json'
dry = '--dry' in sys.argv
WANT = {'mobile_phone': '031 787 235', 'mobile_email': 'semen.stefan@gmail.com'}
OFF_UNLESS_SET = {'free_shipping_enable': False, 'free_shipping_value': 0}

raw = path.read_text(encoding='utf-8')
m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
header = m.group(0) if m else ''
data = json.loads(raw[len(header):])
cur = data['current']
log = []
for k, v in WANT.items():
    if cur.get(k) != v:
        log.append(f'{k}: {cur.get(k)!r} -> {v!r}')
        cur[k] = v
# the old range setting held 1000 while switched off; a number threshold of 0 means "not set up"
if cur.get('free_shipping_enable') is not True:
    for k, v in OFF_UNLESS_SET.items():
        if cur.get(k) != v:
            log.append(f'{k}: {cur.get(k)!r} -> {v!r} (free shipping not set up)')
            cur[k] = v
if log and not dry:
    path.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(('DRY RUN, ' if dry else '') + f'{len(log)} changes')
for line in log:
    print(' ', line)
