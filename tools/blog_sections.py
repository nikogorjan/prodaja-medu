"""Blog sections in the content templates (user, 2026-11-20). Each step runs only when its file is in the pull and
only adds what is missing, so running the script again changes nothing.

1) The newest post is shown big ("Najnovejša objava velika", setting feature_first) on the homepage news
   (index.json "novice_semen") and on the blog page (blog.json "main"). The user wanted the visit of the Indian and
   Spanish beekeepers, written from the client's document, to be the most prominent post on both; it was published
   last, so it is the newest.
2) Apiterapija posts on the Apiturizem page ("if you write 2 posts about apiterapija render them on apiterapija
   subpage"): page.apiturizem.json gets the section "clanki" (featured-articles) right after the seasons calendar
   ("kdaj"). It lists only posts tagged "Apiterapija" (setting filter_tag, case-insensitive), so new posts with that
   tag appear there automatically, and the section stays hidden for visitors if no post carries the tag.
   Ivory band after the wheat calendar, so the bands keep alternating before the black footer; 104px top and bottom
   like the other sections of that page, 56px on mobile. Cards as in the homepage news (4:3 photo, date, excerpt,
   "Več" button, no tags or comments); with fewer posts than columns they fill the row.
3) "Več" under each post card is a small dark filled button, not an underlined text link (user, 2026-11-20:
   "ti mali gumbi naj bodo temni mali gumbi"): setting enable_btn_line ("Gumb s podčrtajem") off in the homepage
   news and the Apiturizem posts, like on the blog page and under articles.
Needs the theme code with feature_first and filter_tag (sections/featured-articles.liquid, blog-template-1.liquid).

usage: python tools/blog_sections.py CONTENT_DIR [--dry]
Run it on a fresh pull of templates/index.json, templates/blog.json and templates/page.apiturizem.json, never on
stale local JSON (see CLAUDE.md). On live, run it after tools/homepage_layout.py, which sets up the homepage news.
"""
import json, re, sys, pathlib

root = pathlib.Path(sys.argv[1]) / 'templates'
dry = '--dry' in sys.argv
log = []
IVORY = '#faf7f0'
APITERAPIJA = {
    'type': 'featured-articles',
    'settings': {
        'animation': 'fade-up',
        'setwidth': 'container',
        'bgsection': IVORY,
        'title_top': 'Iz bloga',
        'title': 'Več o apiterapiji',
        'des': 'Preberite, kaj je apiterapija in kako je urejen naš čebelnjak na Melincih.',
        'align-heading': 'center',
        'blog': 'news',
        'filter_tag': 'Apiterapija',
        'item_style': 'blog-1',
        'enable_btn_blog': True,
        'enable_btn_line': False,
        'enable_date': True,
        'enable_tag': False,
        'enable_comment': False,
        'enable_short': True,
        'image_size': 'landscape',
        'gutter_padding': 30,
        'arrows': True,
        'draggable': True,
        'dots': False,
        'infinite': False,
        'rows': '1',
        'limit': 6,
        'feature_first': False,
        'show': 3,
        'paddingsection': '104px 0px 104px 0px',
        'paddingmobile': '56px 0px 56px 0px',
        'marginsection': '0px 0px 0px 0px',
        'marginmobile': '0px 0px 0px 0px',
    },
}


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


def feature_first(section_id, section_type):
    def change(name, data):
        s = data['sections'].get(section_id)
        if not s or s.get('type') != section_type:
            log.append(f'skip {name} {section_id}: no {section_type} section')
            return False
        if s.setdefault('settings', {}).get('feature_first') is True:
            log.append(f'ok   {name} {section_id}: newest post already big')
            return False
        s['settings']['feature_first'] = True
        log.append(f'{name} {section_id}: newest post big (feature_first)')
        return True
    return change


def dark_button(section_id):
    def change(name, data):
        s = data['sections'].get(section_id)
        if not s or s.get('type') != 'featured-articles':
            log.append(f'skip {name} {section_id}: no featured-articles section')
            return False
        if s.setdefault('settings', {}).get('enable_btn_line') is False:
            log.append(f'ok   {name} {section_id}: "Več" already a dark button')
            return False
        s['settings']['enable_btn_line'] = False
        log.append(f'{name} {section_id}: "Več" as a small dark button')
        return True
    return change


def apiterapija(name, data):
    sections, order = data['sections'], data['order']
    if 'clanki' in sections:
        log.append(f'ok   {name}: already has "clanki"')
        return False
    sections['clanki'] = APITERAPIJA
    order.insert(order.index('kdaj') + 1 if 'kdaj' in order else len(order), 'clanki')
    log.append(f'{name} clanki: new "Več o apiterapiji" (posts tagged Apiterapija) after '
               + ('"kdaj"' if 'kdaj' in order else 'the last section') + '; visible: '
               + ' > '.join(k for k in order if not sections[k].get('disabled')))
    return True


edit('index.json', feature_first('novice_semen', 'featured-articles'))
edit('blog.json', feature_first('main', 'blog-template-1'))
edit('page.apiturizem.json', apiterapija)
edit('index.json', dark_button('novice_semen'))
edit('page.apiturizem.json', dark_button('clanki'))
print(('DRY RUN, ' if dry else '') + f'{sum(1 for l in log if not l.startswith(("skip", "ok")))} changes')
for line in log:
    print(' ', line)
