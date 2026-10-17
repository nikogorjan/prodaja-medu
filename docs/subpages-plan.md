# Subpages plan: O nas, Apiturizem, Kontakt

Status (2026-10-17): planned and built in code. Sections and templates are in the repo; they still have to be
synced to the development theme and the three pages created in the admin (see section 7).
Copy is Slovenian; this document is for whoever builds or reviews the pages.

## 1. Sitemap

```
Domov (/)
├── Trgovina (/collections/all)
│   └── izdelki (/products/…)
├── O nas (/pages/o-nas)                 template: page.o-nas
├── Apiturizem (/pages/apiturizem)       template: page.apiturizem
│   └── #ponudba, #obisk, #povprasevanje  (in-page anchors)
├── Kontakt (/pages/kontakt)             template: page.kontakt
├── Novice (/blogs/news)
└── footer: Pogoji poslovanja, Politika zasebnosti
```

Cross-links the pages must support (already used on the homepage and in blog posts):

| From | Link | To |
|---|---|---|
| Homepage "Naša zgodba", rich text | `/pages/o-nas` | O nas |
| Homepage apitherapy, grid banner | `/pages/apiturizem` | Apiturizem |
| Homepage "Rezervirajte obisk", parallax, blog post 3 | `/pages/kontakt` | Kontakt |
| Main menu "Kontakt" | `/pages/contact` (**wrong**) | must be changed to the Kontakt page |

Each page ends by pointing somewhere useful: O nas → shop + apitourism, Apiturizem → booking form on the
same page, Kontakt → shop and apitourism.

## 2. Design rules taken from the homepage

- Bands alternate: white `#ffffff`, cream `#f7f3ea`, dark brown `#2b2420`. Gold accent `#c99a5c`,
  muted text `#5c6978`, light text on dark `#cfc4b4`. Sharp corners everywhere.
- Eyebrow (`.subtop`): small letter-spaced uppercase above every heading; gold on dark and cream, dark on white.
- Left-aligned headings are sentence-case H2 (Zurich Extended). Centered section headings use the
  theme's uppercase section title (same as "POGOSTA VPRAŠANJA").
- Buttons: filled terracotta `btn-theme` for the main action, `btn-underline` for secondary links,
  `btn-outline-white` on dark.
- Thin gold line icons (stroke ~1.2), honeycomb pattern on cream, photo + text splits at 50/50.
- Page hero (new): split layout like the homepage map panel, dark panel left with breadcrumb, eyebrow,
  H1 and actions, photo right. Replaces the theme's plain white breadcrumb bar on these three pages.

## 3. New sections (code, editable in the theme editor)

| Section file | Editor name | Used for |
|---|---|---|
| `semen-page-hero` | Uvod strani (Šemen) | hero on all three pages; split or full-photo layout, optional fact row |
| `semen-split` | Slika in besedilo (Šemen) | story blocks; optional checklist, facts (label/value) and quote blocks |
| `semen-cards` | Kartice (Šemen) | values, offer, seasons, contact shortcuts; icon or photo per card |
| `semen-steps` | Koraki (Šemen) | "how a visit works", large solid gold numbers (no outline text anywhere) |
| `semen-year-wheel` | Čebelarjevo leto (Šemen) | O nas: interactive year wheel (months, forage rings, needle) |
| `semen-seasons` | Čebelji koledar (Šemen) | Apiturizem: buzz waveform, forage bands, season tabs |
| `semen-gallery` | Galerija (Šemen) | photo mosaic with captions |
| `semen-contact` | Kontaktni obrazec (Šemen) | contact data panel + Shopify contact form (topic, date, persons) |
| `semen-cta` | Poziv k dejanju (Šemen) | closing band with buttons and a phone number |
| `snippets/semen-icon` | – | shared line-icon set for the sections above |

Reused stock sections, styled like the homepage: `main-page` (shows the page body if the client ever adds one),
`service` (numbers row, same count-up as the homepage), `faq-accordion`, `map` (new optional anchor setting;
an embedded Google map can replace the photo).

Small changes to existing code: `snippets/breadcrumb.liquid` hides the theme's white breadcrumb bar on the
`o-nas`, `apiturizem` and `kontakt` templates (the hero has its own); `snippets/header-css.liquid` sizes an
embedded map iframe in the map section.

## 4. Wireframes

### 4.1 O nas (/pages/o-nas)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ HEADER (existing)                                                        │
├────────────────────────────────┬─────────────────────────────────────────┤
│ Domov / O nas                  │                                         │
│ DRUŽINA ŠEMEN                  │   photo: beekeeper with frame           │
│ ČEBELARIMO OD LETA 1982  (H1)  │   (New_Project.webp)                    │
│ lead: family apiary in         │                                         │
│ Prekmurje, ~700 colonies …     │                                         │
│ [V TRGOVINO]  Obiščite nas ──  │                                         │
│ 1982 | 700 družin | Melinci    │                                         │
├────────────────────────────────┴─────────────────────────────────────────┤ dark
│ NAŠA ZGODBA                                                              │ white
│ ┌──────────────┐  Od nekaj panjev do 700 čebeljih družin (H2)           │
│ │ photo: truck │  3 short paragraphs: 1982 start, migratory beekeeping,  │
│ │ with hives   │  AŽ hives, products. Quote block.                       │
│ └──────────────┘                                                         │
├──────────────────────────────────────────────────────────────────────────┤
│  ⬡ 40+ let   ⬡ 700 družin   ⬡ 8 vrst medu   ⬡ 40 panjev za apiterapijo  │ dark (count-up)
├──────────────────────────────────────────────────────────────────────────┤
│ KAJ NAS VODI                     intro right                             │ cream + honeycomb
│ [icon] Čebele na prvem mestu  [icon] Hladno točenje                      │
│ [icon] Majhne serije, doma    [icon] Odprta vrata čebelnjaka             │
├──────────────────────────────────────────────────────────────────────────┤
│ ČEBELARJEVO LETO: year wheel (12 month segments, honey rings, needle  │ white
│ on today's month) │ panel: month, bees, our work, active forage     │
├──────────────────────────────────────────────────────────────────────────┤
│ Poslikan čebelnjak (H2)                       ┌──────────────┐           │ cream
│ painted hive fronts tradition, our apiary     │ painted wall │           │
│ checklist; [Več o apiturizmu]                 └──────────────┘           │
├──────────────────────────────────────────────────────────────────────────┤
│ IZ NAŠEGA ČEBELNJAKA  gallery mosaic (6 photos, captions)                │ white
├──────────────────────────────────────────────────────────────────────────┤
│ CTA: Poskusite naš med ali nas obiščite  [V TRGOVINO] Rezervirajte obisk │ cream
│      ali pokličite 031 787 235                                           │
├──────────────────────────────────────────────────────────────────────────┤
│ FOOTER (existing)                                                        │
└──────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Apiturizem (/pages/apiturizem)

```
┌────────────────────────────────┬─────────────────────────────────────────┐
│ Domov / Apiturizem             │                                         │
│ APITURIZEM IN APITERAPIJA      │   photo: rest room in the apiary        │
│ DIHAJTE Z ČEBELAMI (H1)        │   (semen-apiturizem-soba.webp)          │
│ lead                           │                                         │
│ [REZERVIRAJTE OBISK] Kaj vas…  │                                         │
│ 1–2 uri | po dogovoru | Melinci│                                         │
├────────────────────────────────┴─────────────────────────────────────────┤ dark
│ ┌──────────────┐  KAJ JE APITURIZEM                                      │ white
│ │painted apiary│  Turizem, ki vas pripelje k čebelam (H2) + text + quote │
│ └──────────────┘                                                         │
├──────────────────────────────────────────────────────────────────────────┤
│ #ponudba  KAJ VAS ČAKA (left)                       intro (right)        │ cream + honeycomb
│ [apiterapija] [počitek] [degustacija]                                    │
│ [cvetni prah] [spoznavanje čebel] [izdelki za domov]                     │
├──────────────────────────────────────────────────────────────────────────┤
│ #obisk  KAKO POTEKA OBISK                                                │ dark
│  01 ─────── 02 ─────── 03 ─────── 04                                     │
│  Dogovor    Sprejem    Apiterapija Degustacija                           │
├──────────────────────────────────────────────────────────────────────────┤
│ ZA KOGA (H2) + checklist (posamezniki, pari, družine, skupine, starejši) │ white
│ safety note (wall between you and the bees), allergy note  ┌─────────┐   │
│                                                            │ couple  │   │
├──────────────────────────────────────────────────────────────────────────┤
│ ČEBELJI KOLEDAR: buzz waveform + forage bands by half-month, "today"   │ dark
│ line, season tabs with hear / smell / taste / best-for               │
├──────────────────────────────────────────────────────────────────────────┤
│ ┌──────────────┐  DAN OB MURI (H2) + distances list:                     │ white
│ │ Mura photo   │  Mura 500 m · brod 2 km · Banovci 4 km · M. Toplice 15 km│
│ └──────────────┘                                                         │
├──────────────────────────────────────────────────────────────────────────┤
│ POGOSTA VPRAŠANJA (accordion, visit questions)                           │ cream
├──────────────────────────────────────────────────────────────────────────┤
│ #povprasevanje  dark panel: phone, e-mail, location │ form: name, e-mail,│ white
│                                                     │ phone, date, persons│
│                                                     │ message [POŠLJI]   │
└──────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Kontakt (/pages/kontakt)

```
┌────────────────────────────────┬─────────────────────────────────────────┐
│ Domov / Kontakt                │   photo: jars of honey and pollen       │
│ KONTAKT                        │   (gasilska.webp)                       │
│ PIŠITE ALI POKLIČITE (H1)      │                                         │
│ [POŠLJITE SPOROČILO] Kako do…  │                                         │
│ 031 787 235 | 02 541 13 38 | po dogovoru                                 │
├────────────────────────────────┴─────────────────────────────────────────┤ dark
│ #sporocilo                                                               │ cream
│ dark panel "Kontaktni podatki":  │ form: Zadeva (naročilo / obisk /      │
│ ☎ mobitel, ☎ telefon, ✉ e-pošta, │ darila / drugo), ime*, e-pošta*,      │
│ ⌂ sedež Lipa 145 A,              │ telefon, sporočilo                    │
│ ⬡ čebelnjak Melinci (map links)  │ [POŠLJI SPOROČILO]                    │
├──────────────────────────────────────────────────────────────────────────┤
│ #pot  KAKO DO NAS  dark panel + directions │ embedded Google map         │ map section
├──────────────────────────────────────────────────────────────────────────┤
│ KAKO VAM LAHKO POMAGAMO: [Naročila in dostava] [Obisk] [Darilni paketi]  │ white
└──────────────────────────────────────────────────────────────────────────┘
```

## 5. Content sources and facts used

Only facts that already appear on the new homepage or in the business's own earlier listings are used.

- New homepage and blog posts: since 1982, ~700 colonies, migratory pastures across Slovenia, cold
  extraction, 8 honey varieties, 40-hive apitherapy room, two beds and two seats downstairs, bed for two
  upstairs with a view of the park and pond, visits of 1–2 hours by appointment, Melinci 12 km from
  Murska Sobota, Mura 500 m, Banovci / Moravske Toplice / Lendava 4–15 km.
- Archived prodaja-medu.si (2024) and apiturizem.si listing (2019) "Šemen Štefan s.p. prodaja medu":
  Lipa 145 A, 9231 Beltinci; tel. 02 541 13 38; GSM 031 787 235; semen.stefan@gmail.com; AŽ hives;
  aerosol through round openings, intensity adjustable; fresh pollen from the hive; guided visits;
  ferry at Gornja Bistrica (2 km).
- melinci.si: the apiary is on the road between Melinci and Gornja Bistrica, signposted "APITERAPIJA",
  about 300 m off the road.

## 6. Open questions for the client (marked in copy where relevant)

1. Prices for visits and apitherapy (pages say "po dogovoru").
2. Is the 2019 offer still current: overnight stays, sauna, fishing, picnics? Not mentioned on the pages.
3. Maximum group size (2019 listing: up to 50 people). Pages say "skupine po dogovoru".
4. Business hours / best time to call. Not shown.
5. Real photos still missing: family portrait, guided visit, tasting room
   (`semen-apiturizem-degustacija.jpg` exists locally but is not uploaded to Shopify Files).
6. Social media links in theme settings still point to Shopify demo accounts.

## 7. Launch checklist (admin, ~5 minutes)

1. Online Store › Pages › Add page, three times:
   - "O nas", handle `o-nas`, template `o-nas`
   - "Apiturizem", handle `apiturizem`, template `apiturizem`
   - "Kontakt", handle `kontakt`, template `kontakt`
   Leave the body empty (all content is in the template), fill SEO title/description (section 8).
2. Navigation › Main menu: point "Kontakt" to the Kontakt page (currently `/pages/contact`).
   Optional: URL redirect `/pages/contact` → `/pages/kontakt`.
3. Publishing the theme: the three `templates/page.*.json` files are content JSON and are ignored by
   `npm run push`; push them with the content environment and `--only` (see CLAUDE.md).

## 8. SEO

| Page | SEO title (<60) | Meta description (<155) |
|---|---|---|
| O nas | O nas: družinsko čebelarstvo Šemen od leta 1982 | Družina Šemen čebelari od leta 1982. 700 čebeljih družin, hladno točen med iz lastne pridelave in poslikan čebelnjak na Melincih ob Muri. |
| Apiturizem | Apiturizem in apiterapija na Melincih \| Šemen | Dihajte zrak iz 40 panjev, poskusite naš med in spoznajte čebele. Apiterapija in obisk poslikanega čebelnjaka ob Muri, po predhodnem dogovoru. |
| Kontakt | Kontakt: Čebelarstvo Šemen, Melinci ob Muri | Pokličite 031 787 235 ali pišite na semen.stefan@gmail.com. Naročila medu, darilni paketi in rezervacije obiska čebelnjaka na Melincih. |
