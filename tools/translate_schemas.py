"""Slovenian labels for the theme editor: translates the section schemas in sections/*.liquid.

usage: python tools/translate_schemas.py [--write]
Without --write it only reports. Translations live in tools/schema_sl.json:
  "strings"        English label -> Slovenian (labels, info texts, headers, options, block names)
  "section_names"  file -> section name in the editor and the "Add section" picker (max 25 characters)

Only the text of "name", "label", "info", "content" and "placeholder" changes, in place: ids, types,
values, defaults and the file's formatting stay as they are. After rewriting, each schema is checked
to differ from the original in those strings only. Run it again after a theme update (new English
sections or settings) and add the missing strings it lists to schema_sl.json.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((pathlib.Path(__file__).parent / 'schema_sl.json').read_text(encoding='utf-8'))
TR, NAMES = DATA['strings'], DATA['section_names']
KEYS = ('name', 'label', 'info', 'content', 'placeholder')
SCHEMA_RE = re.compile(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', re.S)
PAIR_RE = re.compile(r'"(name|label|info|content|placeholder)"(\s*:\s*)("(?:[^"\\]|\\.)*")')
SLOVENIAN = re.compile(r'[čšžČŠŽ]')
ENGLISH = re.compile(r'\b(the|and|with|your|enable|show|color|image|button|title|style|width|height|size|background|link|item|product|collection|heading|padding|margin|banner|border|icon|font|mobile|desktop|section|grid|column|header|footer|popup|opacity|overlay|align|layout|position|description|content|page|logo|search|cart|newsletter)\b', re.I)


def strip(node):
    """The schema without the translatable strings, to prove nothing else changed."""
    if isinstance(node, dict):
        return {k: ('' if k in KEYS and isinstance(v, str) else strip(v)) for k, v in node.items()}
    if isinstance(node, list):
        return [strip(v) for v in node]
    return node


def translate(body, fname):
    top = json.loads(body).get('name')
    presets_at = body.find('"presets"')
    state = {'top': False, 'preset': -1}

    def repl(m):
        key, sep, literal = m.group(1), m.group(2), m.group(3)
        value = json.loads(literal)
        if key == 'name' and not state['top'] and value == top:
            state['top'] = True
            new = NAMES.get(fname) or TR.get(value, value)
        elif key == 'name' and presets_at != -1 and m.start() > presets_at:
            state['preset'] += 1
            new = NAMES[fname] if state['preset'] == 0 and fname in NAMES else TR.get(value, value)
        else:
            new = TR.get(value, value)
        return m.group(0) if new == value else f'"{key}"{sep}{json.dumps(new, ensure_ascii=False)}'

    out = PAIR_RE.sub(repl, body)
    if fname == 'footer.liquid':   # the footer's font choice: heading font or body font
        i = out.find('"footer_font_family"')
        j = out.find(']', i)
        if i != -1:
            seg = re.sub(r'("label"\s*:\s*)"Naslov"', lambda mm: mm.group(1) + '"Pisava naslovov"', out[i:j], count=1)
            out = out[:i] + seg + out[j:]
    return out


changed, left, problems = 0, {}, []
for f in sorted((ROOT / 'sections').glob('*.liquid')):
    text = f.read_bytes().decode('utf-8')
    m = SCHEMA_RE.search(text)
    if not m:
        continue
    body = m.group(1)
    new_body = translate(body, f.name)
    before, after = json.loads(body), json.loads(new_body)
    if strip(before) != strip(after):
        problems.append(f'{f.name}: structure changed, not written')
        continue
    if len(after.get('name', '')) > 25:
        problems.append(f'{f.name}: section name longer than 25 characters')

    def collect(node, path=''):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in KEYS and isinstance(v, str) and not SLOVENIAN.search(v) and ENGLISH.search(v):
                    left.setdefault(v, f'{f.name}{path}.{k}')
                else:
                    collect(v, f'{path}.{k}')
        elif isinstance(node, list):
            for i, v in enumerate(node):
                collect(v, f'{path}[{i}]')
    collect(after)
    if new_body != body:
        changed += 1
        if '--write' in sys.argv:
            f.write_bytes((text[:m.start(1)] + new_body + text[m.end(1):]).encode('utf-8'))

print(f'sections with new translations: {changed}' + ('' if '--write' in sys.argv else ' (not written, use --write)'))
for p in problems:
    print('PROBLEM', p)
print(f'strings that still look English: {len(left)}')
for v, where in sorted(left.items()):
    print(f'  {json.dumps(v, ensure_ascii=False)}  <- {where}')
