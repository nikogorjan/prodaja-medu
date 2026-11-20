"""Article page, related posts (user, 2026-11-20: "the related posts have that thick line, remove it; also remove the
divider that separates this section from the blog post").

templates/article.json:
- the "line" section between the post and "Beri dalje" is hidden (disabled, not deleted);
- "Beri dalje" (featured-articles): no comment count (enable_comment off) and 80px top padding instead of 0, since
  the hidden line section gave the space before (64px above and below the line).
The thick light bar behind the date on the photo cards is CSS (semen-design.liquid, .blog__item--3 .blog__meta),
the Slovenian date is in snippets/blog-grid-3.liquid. Idempotent.

usage: python tools/article_related.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/article.json, never on stale local JSON (see CLAUDE.md).
"""
import json, re, sys, pathlib

path = pathlib.Path(sys.argv[1]) / 'templates' / 'article.json'
dry = '--dry' in sys.argv
raw = path.read_text(encoding='utf-8')
m = re.match(r'\s*/\*.*?\*/\s*', raw, flags=re.S)
header = m.group(0) if m else ''
data = json.loads(raw[len(header):])
log = []
for sid in data['order']:
    s = data['sections'][sid]
    st = s.setdefault('settings', {})
    if s.get('type') == 'line' and not s.get('disabled'):
        s['disabled'] = True
        log.append(f'{sid} (line): hidden')
    if s.get('type') == 'featured-articles':
        if st.get('enable_comment') is not False:
            st['enable_comment'] = False
            log.append(f'{sid} ({st.get("title")}): no comment count')
        if st.get('paddingsection') == '0px 0px 64px 0px':
            st['paddingsection'] = '80px 0px 80px 0px'
            log.append(f'{sid} ({st.get("title")}): padding 80px top and bottom')
if log and not dry:
    path.write_text(header + json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(('DRY RUN, ' if dry else '') + f'{len(log)} changes')
for line in log:
    print(' ', line)
