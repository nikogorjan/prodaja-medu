# -*- coding: utf-8 -*-
"""Build a Shopify product-import CSV from the customer's xlsx export (products.json)."""
import json, csv, re, sys, io

SRC = 'client-data/izvoz-stara-stran-izdelki.json'
OUT = sys.argv[1]
VENDOR = 'Čebelarstvo Šemen'

rows = json.load(open(SRC, encoding='utf-8'))
by_model = {r['MODEL']: r for r in rows}

def imgs(r):
    return [u.strip() for u in str(r.get('IMAGES') or '').split(',') if u.strip()]

def pick(r, kind):
    for u in imgs(r):
        if kind in u.lower():
            return u
    return ''

def price(v):
    return '' if v in (None, '', 0, '0') else f'{float(v):.2f}'

# Short, neutral descriptions (taste/colour facts) for the client to review.
DESC = {
    'kostanjev-med': '<p>Kostanjev med je temen med izrazitega, rahlo grenkega okusa in močne arome. Je bogat z minerali in ostane dolgo tekoč. Odlično se poda k sirom in polnozrnatemu kruhu.</p>',
    'cvetlicni-med': '<p>Cvetlični med je mešanica nektarja travniških in gozdnih cvetov. Je blagega, sladkega okusa in zlate barve. Vsestranski med za vsak dan, za sladkanje čaja in namaze.</p>',
    'akacijev-med': '<p>Akacijev med je svetel, skoraj prozoren med nežnega, blagega okusa. Zelo dolgo ostane tekoč in ne kristalizira. Priljubljen pri otrocih in za sladkanje pijač.</p>',
    'hojev-med': '<p>Hojev med je temen gozdni med z značilnim smolnatim, karamelnim pridihom. Je bogat z minerali in dolgo ostane tekoč.</p>',
    'gozdni-med': '<p>Gozdni med je temen, manin med polnega okusa z blago karamelno noto. Nastane iz mane iglavcev in listavcev ter je bogat z minerali.</p>',
    'lipov-med': '<p>Lipov med je svetel do jantaren med osvežilnega okusa z rahlo mentolno noto. Tradicionalno ga uživamo v toplem čaju.</p>',
    'ajdov-med': '<p>Ajdov med je temen med močnega, polnega okusa in izrazite arome. Je značilen slovenski med in bogat z minerali.</p>',
    'soncnicni-med': '<p>Sončnični med je zlato rumen med blagega okusa, ki hitro kristalizira v kremasto strukturo. Odličen za namaze.</p>',
    'cvetni-prah': '<p>Cvetni prah je naravni čebelji izdelek, ki ga čebele naberejo na cvetovih. Posušen in shranjen v kozarcu je bogat vir beljakovin, vitaminov in mineralov. Priporočamo žličko dnevno, samostojno ali v jogurtu.</p>',
    'smrekov-med': '<p>Smrekov med je temen manin med z aromo smrekove smole in blagim karamelnim okusom.</p>',
    'kremni-med': '<p>Kremni med je mehko kristaliziran med kremaste strukture, ki se zlahka maže in ne kaplja.</p>',
    'medomix': '<p>Medomix je mešanica medu in čebeljih izdelkov. Opis dopolnimo.</p>',
    'med-v-satju': '<p>Med v satju je med v naravnem voščenem satju, tako kot ga pripravijo čebele. Uživamo ga skupaj s satjem.</p>',
    'propolis': '<p>Propolis je naravna čebelja smola. Opis dopolnimo.</p>',
    'propolis-nabran-z-mrezic': '<p>Propolis, nabran z mrežic. Opis dopolnimo.</p>',
    'propolis-rocno-bran': '<p>Ročno bran propolis. Opis dopolnimo.</p>',
}

# Product definitions: handle -> (title, type, tags, [(option value, model, grams)])
honey = [
    ('kostanjev-med', 'Kostanjev med', '0001', '0017'),
    ('cvetlicni-med', 'Cvetlični med', '0002', '0018'),
    ('akacijev-med', 'Akacijev med', '0003', '0019'),
    ('hojev-med', 'Hojev med', '0004', '0020'),
    ('gozdni-med', 'Gozdni med', '0005', '0021'),
    ('lipov-med', 'Lipov med', '0006', '0022'),
    ('ajdov-med', 'Ajdov med', '0007', '0023'),
    ('soncnicni-med', 'Sončnični med', '0008', '0024'),
]
products = []
for handle, title, big, small in honey:
    products.append(dict(handle=handle, title=title, type='Med', tags='med, domači med, 900 g, 450 g',
                         option='Pakiranje', variants=[('900 g', big, 1300, 'velik'), ('450 g', small, 700, 'mali')]))
products.append(dict(handle='cvetni-prah', title='Cvetni prah', type='Cvetni prah', tags='cvetni prah, čebelji izdelki',
                     option='Pakiranje', variants=[('720 ml', '0013', 700, 'velik'), ('370 ml', '0025', 400, 'mali')]))
# Inactive items from the export: imported as drafts without price, for the client to complete.
for handle, title, model, typ in [
    ('smrekov-med', 'Smrekov med', '0009', 'Med'),
    ('kremni-med', 'Kremni med', '0010', 'Med'),
    ('medomix', 'Medomix', '0011', 'Med'),
    ('med-v-satju', 'Med v satju', '0012', 'Med'),
    ('propolis', 'Propolis', '0014', 'Propolis'),
    ('propolis-nabran-z-mrezic', 'Propolis, nabran z mrežic', '0015', 'Propolis'),
    ('propolis-rocno-bran', 'Propolis, ročno bran', '0016', 'Propolis'),
]:
    products.append(dict(handle=handle, title=title, type=typ, tags=typ.lower() + ', osnutek', option='Title',
                         variants=[('Default Title', model, 0, '')], draft=True))

COLS = ['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published',
        'Option1 Name', 'Option1 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker',
        'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fulfillment Service',
        'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable',
        'Image Src', 'Image Position', 'Image Alt Text', 'Variant Image', 'Variant Weight Unit', 'Status']

out = []
notes = []
for p in products:
    draft = p.get('draft', False)
    first_model = p['variants'][0][1]
    # product image gallery: velik, mali, skupaj (skip the generic 'Vsi_izdelki' shot)
    gallery = []
    for kind in ('velik', 'mali', 'skupaj'):
        u = pick(by_model[first_model], kind)
        if u and u not in gallery:
            gallery.append(u)
    if not gallery:  # fall back to whatever the export has (e.g. propolis photo)
        gallery = [u for u in imgs(by_model[first_model]) if 'vsi_izdelki' not in u.lower()] or imgs(by_model[first_model])[:1]
    for i, (val, model, grams, img_kind) in enumerate(p['variants']):
        r = by_model[model]
        if r.get('DISCOUNT_PRICE'):
            notes.append(f"{p['title']} {val}: v izvozu je DISCOUNT_PRICE={r['DISCOUNT_PRICE']} pri redni ceni {r['REGULAR_PRICE']} – NI preneseno, preverite s stranko.")
        row = {c: '' for c in COLS}
        row['Handle'] = p['handle']
        if i == 0:
            row.update({'Title': p['title'], 'Body (HTML)': DESC.get(p['handle'], ''), 'Vendor': VENDOR, 'Type': p['type'],
                        'Tags': p['tags'], 'Published': 'FALSE' if draft else 'TRUE', 'Status': 'draft' if draft else 'active'})
            if gallery:
                row['Image Src'] = gallery[0]; row['Image Position'] = '1'; row['Image Alt Text'] = p['title']
        row.update({'Option1 Name': p['option'], 'Option1 Value': val, 'Variant SKU': model,
                    'Variant Grams': str(grams) if grams else '', 'Variant Inventory Tracker': '',
                    'Variant Inventory Qty': '', 'Variant Inventory Policy': 'deny', 'Variant Fulfillment Service': 'manual',
                    'Variant Price': price(r['REGULAR_PRICE']) or '0.00', 'Variant Compare At Price': '',
                    'Variant Requires Shipping': 'TRUE', 'Variant Taxable': 'TRUE',
                    'Variant Image': pick(r, img_kind) if img_kind else '', 'Variant Weight Unit': 'g'})
        out.append(row)
    for pos, u in enumerate(gallery[1:], start=2):
        row = {c: '' for c in COLS}
        row.update({'Handle': p['handle'], 'Image Src': u, 'Image Position': str(pos), 'Image Alt Text': p['title']})
        out.append(row)

with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader(); w.writerows(out)

print(f'{len(products)} izdelkov, {sum(len(p["variants"]) for p in products)} variant, {len(out)} vrstic CSV -> {OUT}')
for n in notes: print('OPOMBA:', n)
