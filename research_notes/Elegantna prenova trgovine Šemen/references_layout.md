# The client's two references and layout/component patterns for an elegant, light Šemen homepage

*Evidence gathered 2026-10-20. Method: colours were sampled as region medians from the client's two screenshots and from the full-resolution Behance artboards. Fonts and colour tokens of the old Rast site come from its archived CSS (Wayback Machine). Seven live sites were captured that day at 1440 px and 390 px with headless Edge (Playwright), and computed styles (font-family, size, weight, letter-spacing, background colours) were read from the live DOM. "Whitespace gap" means a full-width run of uniform background ≥40 px tall at 1440 px. It approximates the empty space between content blocks, not exact CSS padding. Capture files (temporary) are in the session scratchpad: `scratchpad/refshots/` (one PNG/JSON per site, plus `*_sheet.png`, `combo1.png`, `combo2.png`, `combo_mobile.png`) and `scratchpad/behance/` (`compare.png`, `detail.png`).*

---

## What exactly makes Reference B (Rast Kaffee) read as elegant, and which of its devices transfer to a honey shop?

### Takeaway
The client's Pinterest screenshot shows Rast's old site (footer "©2013", live until about 2019/2020), not today's rast.ch. Its elegance comes from restraint and repetition. The page uses two near-identical light tones (#f6f5f3, plus a barely deeper #f3f0eb map band). A single charcoal (#1e1e1c) is used only as a frame: the header bar and the footer. There is one typeface (Proxima Nova) in widely tracked capitals and one pin-point red accent. Five identical round "specimen" product images carry origin labels and no commerce clutter, followed by three equal photo tiles and one information band (an origin map). The devices that transfer to honey are the specimen row, the origin/season caption above the name, the three-tile story row, one storytelling band in a barely different tint, and dark used only as a frame. The live rast.ch (2026) is a different, much heavier editorial design: about one third of the page is solid black, with an orange accent.

### Cited Findings

#### Reference B as seen in the client's screenshot (old design), component by component
Colours are sampled from the screenshot. Proportions are measured on a page about 517 px wide, so pixel values are relative.
- **Header**: a solid dark bar, sampled #272727; the era's CSS defines `.headerholder{background-color:#1e1e1c}`. Left: a boxed "R" monogram with the wordmark "RAST KAFFEE / GOURMET RÖSTEREI" in white tracked capitals. Right: nav DIE RÖSTEREI · KAFFEE · SHOP · AKADEMIE · MEIN KONTO plus a round cart icon, in small white tracked capitals. — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png); [archived app.css, July 2018](https://web.archive.org/web/20180727101537/https://www.rast.ch/static/css/app.css?r=25)
- **Hero**: a full-bleed photo of hands holding dried coffee beans in warm dark browns (median #484041), about 2.4:1. The headline "KAFFEE IST KULTUR, / IST LEBEN, IST LEIDENSCHAFT" is set in white bold capitals, left-aligned in the left third. Below it sits a ghost button "UNSER KAFFEE" (thin white outline, small tracked capitals), and four vertical slider dots run down the right edge (a slideshow hero). — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)
- **Product "specimen" row** on a light warm off-white #f6f5f3:
  - A centred two-line caps heading "REINER URSPRUNGS- UND PLANTAGENKAFFEE", with two small square prev/next buttons under it.
  - Five identical white discs (#fcfcfc), each about 13% of the page width with about 2% gaps, each holding a top-down pile of beans.
  - Under each disc: the origin in small light taupe tracked capitals (INDIEN, INDIEN, PANAMA, JAMAICA, TANSANIA) above the name in bold near-black capitals (#201e1b): BALAMAADI, BARISTA CRÈME, BARU GEISHA, BLUE MOUNTAIN, BUKOBA.
  - No prices, ratings, badges or cart buttons. One solid charcoal CTA "ZUM SHOP" sits centred below. The row spans about 74% of the page width, centred.
  - [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)
- **Three equal photo tiles** in portrait, about 4:5 (measured 120×155 px), each with a dark overlay (tile median #5b4f41). White bold caps titles sit near the top: "LEIDENSCHAFT AUS TRADITION", "NACHHALTIGER KAFFEE", "VOM LIEBHABER ZUM KENNER". At the bottom, one white line icon (cup, leaf, mortarboard) sits above a tracked caps label: "DIE RÖSTEREI", "UNSER KAFFEE", "ZUM KURSANGEBOT". The tiles share the product row's width, with narrow gutters (about 1.7% of the page width). — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png). The era's CSS sets the tile labels as `.home-abs-bottom .bottom-inner span{color:#fff;text-transform:uppercase;font-size:20px;letter-spacing:.22em}`. — [archived app.css](https://web.archive.org/web/20180727101537/https://www.rast.ch/static/css/app.css?r=25)
- **Map band**: it follows a long pause, about 3–4× the other vertical gaps on the page.
  - Full-width, in a barely deeper tint (#f3f0eb / #f2efe9 against #f6f5f3).
  - A small centred caps heading reads "UNSERE AUSLESEN AUS 12 VERSCHIEDENEN LÄNDERN".
  - The world map is drawn in pale taupe land (#ded6cc; the CSS has #ded6c4) with red origin dots: the most saturated pixel sampled is #f63f63, and the CSS red token is `.bg-red{background-color:#d33d3d}`.
  - A dark tooltip box (#2d2e2b–#3c3c3a) shows "BRASIL / MINAS GERAIS / [leaf icon] / ARABICA".
  - [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png); [archived app.css](https://web.archive.org/web/20180727101537/https://www.rast.ch/static/css/app.css?r=25)
- **Footer**: charcoal, sampled #272725; the CSS has `footer.bottom-adress{background:#1e1e1c;color:#bbb4a4}`.
  - Three columns: "ANFAHRT UND KONTAKT" (Rast Kaffee AG, Zugerstrasse 9, CH-6031 Ebikon, tel/fax/e-mail), "SITEMAP" (Die Rösterei, Kaffee, Shop, Akademie), and "NACHHALTIGKEIT" (five certification roundels rendered in grey).
  - Bottom line: "©2013 | Rast Kaffee AG | Impressum | AGB | Kontakt", plus Facebook and Twitter links.
  - Sampled text colours: headings about #cacaca, body about #8e8b89.
  - [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png); [archived app.css](https://web.archive.org/web/20180727101537/https://www.rast.ch/static/css/app.css?r=25)
- **Dark share**: the header bar and footer together take about 13% of the screenshot's height. Everything else is light, apart from the photos. — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)

| Role (Reference B, old) | Screenshot sample | Era CSS token |
|---|---|---|
| Header bar, CTA button, footer | #272727 / #272725 | #1e1e1c (97 uses) |
| Main light background | #f6f5f3 – #f7f5f4 | not present as hex in the 2018 CSS |
| Map band tint | #f3f0eb – #f2efe9 | not present |
| Product discs | #fcfcfc | #fff |
| Name text | ≈#201e1b | #1e1e1c |
| Origin label / footer text (taupe greys) | light taupe (text too small to sample exactly) | #bbb4a4 (44 uses), #aea08a (13) |
| Map land | #ded6cc | #ded6c4 (37 uses) |
| Map dots / accent | ≈#f63f63 | #d33d3d (7 uses) |
| Pale creams elsewhere | – | #f9f2de, #f1e9c6, #e6e0d1, #e0d6c2 |
Source: [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png); colour-frequency count of [archived app.css](https://web.archive.org/web/20180727101537/https://www.rast.ch/static/css/app.css?r=25)

- **Typography**: `body{font-family:proxima-nova,sans-serif}`, served from Typekit (the 2017 homepage loads `typekit.net/asm4ona.js`). The CSS has 46 `text-transform:uppercase` rules. Letter-spacing is .14em on headings (e.g. `.pimcore_area_title h1{letter-spacing:.14em}`) and .22em on tile labels. Weights are almost only 600 (12 rules) and 400 (7 rules). `.bg-dark{background-color:#1e1e1c;color:#ded6c4}` means dark areas carry beige rather than white text. — [archived app.css](https://web.archive.org/web/20180727101537/https://www.rast.ch/static/css/app.css?r=25); [archived homepage, April 2017](https://web.archive.org/web/20170406073214/http://rast.ch/)
- **Dating**: the screenshot footer reads ©2013. The archived April 2017 homepage reads "© 2016 Rast Kaffee AG" and uses the same Typekit/Proxima Nova setup (Pimcore CMS). The stylesheet `static/css/app.css` exists from Jan 2015, with revisions r=1 (May 2016) through r=38 (July 2018). Wayback CDX shows the root URL redirecting (301) from 2014 to 2019 and a different page (200, new digest) from June 2020. — [archived homepage 2017](https://web.archive.org/web/20170406073214/http://rast.ch/); [Wayback CDX for rast.ch](https://web.archive.org/cdx/search/cdx?url=rast.ch&output=txt&fl=timestamp,statuscode,digest&collapse=timestamp:4)

#### The live rast.ch today (captured 2026-10-20): it no longer matches the screenshot
- **Fonts** (computed): body `SpeziaMedium` 16 px. Nav `SpeziaMono` 16 px, uppercase, letter-spacing 0.8 px (0.05em). Headings in the serif `VictorSemibold`: h1 92 px desktop / 40 px mobile, h2 48 px, h3 40 px, all sentence case. All-caps is now used only for small mono labels. — [rast.ch/de](https://www.rast.ch/de)
- **Colours** (computed and sampled): base #ece5e0 (rgb 236,229,224) for body and the fixed header. Solid black #000000 sections. Orange accent #eb693c (rgb 235,105,60) for buttons, small square bullets before the eyebrow labels, the newsletter band and a line-art pattern strip under the footer. — [rast.ch/de](https://www.rast.ch/de)
- **Section order (desktop, 12,937 px tall)**:
  1. Fixed light header: R monogram; mono caps nav with dropdown chevrons (KAFFEE & RÖSTEREI, AKADEMIE, UNTERNEHMEN, KONTAKT); outlined buttons "Geschäftskunden" and "Shop".
  2. Full-bleed hero: hands holding green beans in a jute sack. The white serif headline "Wir leben Kaffee seit 1918" sits bottom-left, with a small orange filled button and a small white outlined button.
  3. Greige shop carousel with the eyebrow "■ SHOP". Bags are composited into photos of their origin farms, in portrait cards (about 5:6). Captions: serif name plus "Einzelsorte", mono price "CHF 9.30" and "250g". There are no buttons on the cards; prev/next arrows sit beside the heading.
  4. Centred line "Alle unsere 61 Kaffee-Sorten entdecken" (the 61 in orange) with an orange "Zum Shop" button.
  5. A mountain landscape fading into black.
  6. Black "Rohkaffee" section with an offset photo collage.
  7. Greige "Akademie".
  8. Black "Rösterei", then a full-bleed dark photo band, "Unser Versprechen: Garantiert röstfrisch".
  9. Greige "Familientradition" collage, including a black-and-white archive photo.
  10. Greige "Journal" carousel of white cards, with a hairline rule above it.
  11. Orange newsletter band: line-art illustration, underline-style e-mail field, black "Anmelden" button.
  12. Greige B2B section with hairline-separated benefit rows.
  13. Black "Kontaktpersonen".
  14. Black footer, then the orange pattern strip.
  - Sources: [rast.ch/de](https://www.rast.ch/de) (capture and fetched content)
- **Dark share**: three black zones (Rohkaffee; Rösterei plus the promise band; contacts plus footer) make up about one third of the desktop page height. On mobile, one black run is about 3,500 px of a 14,582 px page. — [rast.ch/de](https://www.rast.ch/de)
- **Rhythm**: the vertical whitespace gaps cluster at exactly 128 px (median 128 px), which points to a strict spacing token. — [rast.ch/de](https://www.rast.ch/de)
- **Content facts**: the shop links out to rastshop.ch. Six single-origin products appear on the homepage. There are no testimonials and no certification logos. The footer reads "© 2026 Rast Kaffee AG" with the address Industriestrasse 4, 6030 Ebikon. — [rast.ch/de](https://www.rast.ch/de)
- **Mobile**: the hamburger sits in a black square. The hero headline is 40 px with two stacked buttons. The product carousel shows one card plus a peek of the next. — [rast.ch/de](https://www.rast.ch/de)

### Inferences
- **What specifically makes old Rast elegant**:
  1. Palette discipline: one dark, two light neutrals and white. Colour comes from the photography, plus one tiny red used only for information (the map dots).
  2. One type family, two weights and tracked capitals, which give a single consistent voice.
  3. A narrow, centred content column (about 74% of the width) and exact repetition: five identical discs and three identical tiles.
  4. Products shown as specimens: same shape, same light, same top-down angle, so only the material (roast colour and texture) differs.
  5. Zero commerce noise on the homepage: no prices, stars, hearts, badges or per-item buttons, and only one CTA.
  6. Dark used as a frame (top bar, footer) and in photo overlays, never as a mid-page band.
  7. One information band, the map, which adds substance instead of decoration.
  8. A deliberate long pause before that band.
- **What dates it**: all-caps headings and labels everywhere, which would be hard to read for long Slovene words; ghost buttons; vertical slider dots; grey micro-text on charcoal; greyed-out certification logos. The 2026 rast.ch itself modernised by moving headlines to sentence-case serif and keeping tracked caps only for small labels. That is the right way to borrow the old site's voice.
- **Devices that transfer to Šemen**:
  1. **A specimen row of the eight honeys**: identical round or arched images showing each honey's colour. The colour range from pale (e.g. acacia) to very dark honeys plays the role Rast's roast shades played. Above each name goes a small tracked eyebrow with season or forage source; prices are hidden or very small; there is one "Vsi medovi" CTA.
  2. **Three equal portrait tiles** (story/family; apiturizem at the painted beehouse; quality), each with one thin line icon and a tracked label.
  3. **One storytelling band in a barely deeper tint**: Rast's origin map becomes a map of Šemen's hive and forage locations, or the honey-harvest calendar. The theme already has `semen-year-wheel` and `semen-seasons` sections that could fill this role.
  4. **Dark only as the closing frame** (footer), or not at all.
- **The live Rast is a cautionary example**: a respected brand moved to an editorial system with about one third black. That is exactly the heaviness the client dislikes in his own site. He is reacting to the old Rast's lightness, not to "Rast" in general. The current Rast is still useful for its 128 px rhythm, hairlines, sentence-case serif headlines, and products shown in an origin context.

### Gaps
- Who designed the old Rast site is unknown (a search of Pimcore partner agencies found no Rast case study).
- It is unverified whether the Pinterest image is the live site or an agency mockup: its light background values (#f6f5f3, #f3f0eb) do not appear as hex in the 2018 CSS. This could be a mockup, another CSS revision, or JPEG colour shift.
- The interaction of the map (hover vs click) and the exact launch date of the current design were not established.

---

## What in Reference A does the client probably like (warmth, light beige, softness), and what would look dated or generic if copied?

### Takeaway
Reference A is a Behance concept by Nirmal Kumar (Coimbatore, India; Figma and Photoshop), uploaded around August 2023. It is not a working shop.
- **What it does**: a warm beige canvas (#e2d9c8, about 62% of all pixels) holds near-white panels (#f1efee) with soft, low-contrast rounded cards and warm food photography. Dark brown (#30261c) is confined to small buttons and the footer.
- **What the client probably likes**: that lightness and warmth (beige and off-white instead of dark bands), and its softness. Its footer brown is practically identical to Šemen's #2b2420, so the issue is not the colour itself but how many mid-page blocks use it.
- **What would look like a stock theme if copied**: the boxed "board on a coloured canvas" layout, a Poppins-style geometric sans plus a script accent, floating cut-out coffee beans, a generic category-icon row, an "Order Now" button and heart on every card, avatar testimonial cards with stars, and the "15% off" newsletter.

### Cited Findings
- **Project metadata**: title "Coffee Shop Landing Page Design" by Nirmal Kumar, location "Coimbatore, India". Tags: UI/UX, Web Design, Interaction Design, Figma, Adobe Photoshop. There are four image modules: a 1400×873 cover, a 1400×690 module, the 1400×2820 desktop landing page (the client's screenshot), and a 3840×9213 "Mobile Version" board ending in "Thank You For Watching!". — [Behance project](https://www.behance.net/gallery/177842783/Coffee-Shop-Landing-Page-Design); [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png); [mobile module](https://mir-s3-cdn-cf.behance.net/project_modules/max_3840_webp/c65f79177842783.64ddbcf7d3485.png)
- **Grid**: the full-width beige canvas is #e2d9c8. Everything sits in a boxed content column of 1,188 px on the 1400 px artboard (x 106–1294; 7.6% side margins). Nothing is full-bleed except the canvas. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Hero**: boxed, about 1,188×490 (about 2.4:1). A dark, cool-toned photo (median about #19232b) shows a barista pouring latte art. The nav sits inside the photo: a small-caps "COFFEE" wordmark, caps links HOME / COFFEE / BAKERY / SHOP / ABOUT / LOGIN, and a search icon. The left-aligned white headline "Welcome! / We serve the richest coffee in the city!" is a sentence-case semibold geometric sans, followed by a white pill button "Order Now". — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Category row**: four filled dark-brown icons with labels (Hot Coffee, Cold Coffee, Cup Coffee, Dessert) sit on the canvas under the hero. A cut-out coffee bean floats, half-cropped, at the left page edge. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Product panel** (#f1efee–#f3efec):
  - Centred caps headings "OUR SPECIAL COFFEE" and "OUR SPECIAL DESSERT", with two rows of four cards. Cards are about 226 px wide with 11–17 px gutters (the row is about 947 px, centred), and small grey round arrows sit outside the row.
  - Each card: a rounded photo with a heart icon top-right, the name in medium weight, a one-line light-grey description, a bold price ("Rs. 199"), and a small dark-brown "Order Now" button (#30261b).
  - The card fill (#ece8e5–#efebe7) barely differs from the panel; cards are separated mainly by a soft shadow.
  - [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Promo band** (#e6e1d5–#e7e0d5): cut-out hands holding beans on the left and a scoop of beans on the right. The headline reads "Check out our best coffee betans" (typo in the original), with a dark pill button "Explore our products →". — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Testimonials** (#f0f0f0): a script eyebrow "Come and join" above the caps heading "OUR HAPPY CUSTOMERS". Three cards (#eee7e5–#eeece7) carry an avatar, name, role, orange stars (#fe8c06) and the quote; the centre card is larger and raised. Dots sit below. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Newsletter** (#e2d9c8): "Join in and get 15% Off!" with a subline, a pill e-mail field (#f1f0ee) and a dark pill "Subscribe" (#30261c). Bean piles bleed in from the corners. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Footer** (#302619–#30261c): the wordmark plus five caps column headings (PRIVACY, SERVICES, ABOUT US, INFORMATION, SOCIAL MEDIA), small grey links and social icons. It takes about 7% of the artboard height. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Whitespace**: the gaps between content blocks are compact, with a median of about 44 px at 1440 px equivalent. The current rast.ch uses 128 px. — measured on the [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Mobile board**: hero text enlarged, the icon row kept, two cards per row with a third peeking (horizontal scroll), the testimonial as one card with peeks either side, and stacked footer columns. Colour shares on this board: #e2d9c8 62.3%, #ffffff 6.8%, #efeae5 4.2%, #30261b 3.5%. — [mobile module](https://mir-s3-cdn-cf.behance.net/project_modules/max_3840_webp/c65f79177842783.64ddbcf7d3485.png)

| Role (Reference A) | Hex |
|---|---|
| Page canvas, newsletter band | #e2d9c8 |
| Product panel | #f1efee (to #f3efec) |
| Product card fill | #ece8e5 – #efebe7 |
| Promo band | #e6e1d5 – #e7e0d5 |
| Testimonial panel / cards | #f0f0f0 / #eee7e5 – #eeece7 |
| E-mail field | #f1f0ee |
| Buttons, heading text, footer | #30261b – #30261c (headings sample ≈#332920) |
| Star rating | #fe8c06 |
| Hero photo (median) | ≈#19232b (cool, dark) |
Source: pixel sampling of the [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)

### Inferences
- **What the client likely responds to**:
  - A light, warm page in which dark brown appears only at the very end (footer) and in small buttons.
  - Soft, rounded, low-contrast surfaces.
  - Warm close-up product photography.
  - A calm, regular four-across product rhythm.
  - The "light colour tint in one part of the page" he asked for corresponds to Reference A's beige/off-white bands.
  - Because Reference A's footer brown (#30261c) is effectively the same as Šemen's #2b2420, a single dark footer is probably acceptable to him; the heaviness he feels comes from the dark blocks in the middle of the current homepage.
- **What reads dated or generic if copied**:
  - The boxed artboard look (content floating on a coloured canvas).
  - Poppins-style geometric sans plus a script eyebrow, a combination typical of 2018–2022 UI kits.
  - Cut-out props bleeding off corners.
  - A generic icon row.
  - Per-card "Order Now" buttons and hearts.
  - Tiny light-grey description text, which is likely low contrast.
  - Avatar-and-stars testimonial cards with an enlarged centre card.
  - A discount-led newsletter.
  - Four almost-identical beige and grey tints (#e2d9c8, #e6e1d5, #f1efee, #f0f0f0), which together look muddy rather than intentional.
  - The cool, dark hero photo also works against the warm palette.
- **Typography (visual identification only)**: the geometric sans resembles Poppins (semibold headline, regular caps nav, medium card titles, bold "Thank You For Watching!"). The script eyebrow resembles Dancing Script.
- **Upload date**: the module asset IDs begin with hexadecimal Unix timestamps (`64dda517…`, `64ddbcf7…`), which decode to 17 Aug 2023. The design is therefore almost certainly from August 2023.
- **Translation for Šemen**: keep the warmth and softness but not the props.
  - Use one cream tint (the existing #f7f3ea) in one or two bands instead of a beige canvas everywhere.
  - Keep soft corners only if they are used consistently.
  - Drop per-card buttons and hearts.
  - Replace cut-outs with real photography: jars, comb, the painted beehouse, the family.

### Gaps
- Behance's server-rendered page did not expose the publication date, view or appreciation counts, or the fonts used. Font names are visual identifications, not confirmed.
- The contrast of the small grey card text was not measured at full resolution.

---

## Which product-image shapes and backgrounds make honey jars look premium?

### Takeaway
Across current elegant food shops, the premium signal is consistency plus a quiet "plate". Every product is shot the same way and centred with generous padding on a flat tint only about 2–5% darker than the page: La Cabra #eae2de on #f8f1ec, Sightglass #ece8e2 on #f2efe7, Brightland #f8f8f8 on white. Old Rast showed that identical circles work for top-down "specimen" shots. Shopify's own reference theme ships an arch mask, so arched windows are a native option and suit tall jars. The best captions put a small origin, season or tasting line above the name. For honey, the colour of the honey is the differentiator, so the photography (backlit jars or macro shots of the honey itself) has to show it.

### Cited Findings
- **Old Rast**: identical white discs (#fcfcfc) on #f6f5f3, holding top-down product piles. Origin label above the name; no price on the homepage row. — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)
- **Rast 2026**: each bag is composited into a photo of its origin farm (portrait card, about 5:6), with a serif name plus "Einzelsorte" and a monospaced price and weight ("CHF 9.30", "250g"). — [rast.ch/de](https://www.rast.ch/de)
- **La Cabra**: coffee boxes are centred on warm greige plates (#eae2de) on a #f8f1ec page, with a tiny caps tag inside the top of the plate ("HIGHLIGHT", "SEASONAL"). The caption gives the name, then origin and weights ("Kenya | 250g, 1kg"), then "From €18,95 EUR". Body text is rgba(52,53,42,0.75), a tinted text colour rather than grey. — [lacabra.com](https://lacabra.com)
- **Sightglass**: bags sit on #ece8e2 plates on a #f2efe7 page, with corner badges ("SEASONAL FAVORITE", "MADE BY WOMEN"). Tasting notes are printed *above* the name ("Cranberry, Raisin, Cocoa Nib"), then the price and a full-width dark "ADD TO CART". Category tabs (Customer Favorites, New Arrivals, Espresso, Blends, Single Origin) sit above the grid. — [sightglasscoffee.com](https://sightglasscoffee.com)
- **Brightland**: bottles sit on very light neutral plates (#f8f8f8) on a white page, with small outlined badges ("BEST SELLER", "NEW"). The caption has the name, a one-line descriptor ("Your salad's best friend"), and stars plus a review count. On mobile, an outlined "Add to Bag $58" pill sits under each card. — [brightland.co](https://brightland.co)
- **Pump Street**: chocolate bars sit on light grey plates, with names in tracked caps that include the cocoa percentage ("MADAGASCAR CRIOLLO 74%") and the price. — [pumpstreetchocolate.com](https://pumpstreetchocolate.com)
- **Scale**: Baymard found that 42% of users try to judge a product's size from its images, and that 28% of 60 large e-commerce sites offered no "in scale" image for best-sellers. In one study, 56% of participants began their visit to a product page by exploring the images. (Figures via search summary of the article.) — [Baymard, "All Products Need at Least One 'In Scale' Image"](https://baymard.com/blog/in-scale-product-images)
- **Shopify's Dawn** reference theme ships `assets/mask-arch.svg` and `assets/mask-blobs.css`, and its base.css applies blob shapes with `clip-path: polygon(var(--shape--blob-1))`. — [Dawn assets on GitHub](https://github.com/Shopify/dawn/tree/main/assets); [Dawn base.css](https://github.com/Shopify/dawn/blob/main/assets/base.css)

### Inferences
- **Shapes for honey jars, ranked**:
  1. **Rectangular 4:5 (or 1:1) plate in a soft warm tint.** This is the most versatile option and works in grids and product pages. The jar should fill about 60–70% of the plate height, centred, with its shadow coming from the photography rather than CSS.
  2. **Arch (round-topped window).** It echoes the jar's shoulders and the shape of beehouse panels. Use it in editorial places (a hero product, the story section, the three tiles) rather than on every card.
  3. **Circle.** Best for top-down or macro "specimen" shots (the honey surface, comb, a spoon drizzle), and ideal for an eight-variety colour row in the old Rast manner. Weaker for whole jars: lids get cropped and corners are wasted.
  4. **Hexagon.** Avoid it. It is a honey cliché, and the current quality section already uses a hexagon jar image.
- **Plate colour**: warm, not grey (cream, oat or greige), about 2–5% darker than the page; alternatively a white disc on a cream band. Avoid saturated yellow or amber plates, because the honey already carries that colour and the jar would disappear into it.
- **Photography rules**:
  - The same angle (straight-on, slightly above), the same soft key light plus backlight so the honey glows, and the same background on every jar.
  - The same jar scale in every card.
  - Each product page should have one in-scale or lifestyle image (in a hand, with a spoon, at breakfast), as Baymard's figures support.
- **Caption pattern**: a small tracked eyebrow with season and forage source → the name in the display face → weight and price in small figures. Use badges sparingly, as hairline-outlined tags rather than coloured stickers.
- **White space**: 24–32 px or more between cards. No borders or drop shadows on cards; the plate does the separating.

### Gaps
- No live example using arch masks was captured; the evidence is Dawn's built-in asset only.
- No usability or conversion study comparing circles, arches and rectangles for product images was found. Shape choice is an aesthetic judgement.
- Pump Street's exact plate colour is uncertain (sampled between #dadada and #eaeaec because of overlapping product shadows).

---

## How many tint bands and how much dark colour should a light, elegant homepage use, and where?

### Takeaway
The light, elegant examples use one base colour, one tint for at most two non-adjacent bands, and zero or one dark block, usually only the footer. That keeps dark at or below about 15% of page height. Sites with two or three dark blocks (Sightglass about 24%, Rast 2026 about 33% black) read bold and editorial, not light. For Šemen this means:
- a white or warm off-white base;
- the existing cream #f7f3ea as "the" tint, in one or two places;
- espresso #2b2420 at most once, ideally as the footer with the newsletter merged in, or not at all.

The current homepage has three espresso blocks: family/story, the numbers band, and the footer.

### Cited Findings
- **Old Rast**: two light tones (#f6f5f3 base, #f3f0eb map band). Dark appears only as the header bar and footer, about 13% of the height. — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)
- **Reference A**: a beige canvas plus three more light tints; dark only in the footer (about 7%), the buttons and the dark hero photo. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Mast**: #f6f5ef base and no dark block; only the footer is tinted (#e4e2dd). The whole homepage is just 3,362 px tall at 1440 px. — [mastmarket.com](https://mastmarket.com)
- **Brightland**: white base, with cream #f5f3ec used for exactly two bands (the testimonial, and a press-quote/logo band). Small accents are a pink "Build Your Own Set" card and a yellow claims marquee. The footer is white and there is no dark block. — [brightland.co](https://brightland.co)
- **Pump Street**: white base, a pale pink band (#fce4e5) for the press quote, a pale grey band, and a peach tinted footer (#f0d3c9). No dark block. — [pumpstreetchocolate.com](https://pumpstreetchocolate.com)
- **La Cabra**: #f8f1ec throughout. Dark appears only in the hero photo and in one merged newsletter-plus-footer block (#2e2c29), about 14% of page height. — [lacabra.com](https://lacabra.com)
- **Sightglass**: a #f2efe7 base alternating with #eae6dd tint bands, plus two #212121 blocks (a café band and the footer), about 24% of page height. — [sightglasscoffee.com](https://sightglasscoffee.com)
- **Rast 2026**: #ece5e0 base, three black zones (about 33% of height) and one orange band. — [rast.ch/de](https://www.rast.ch/de)
- **Diaspora Co.**: full-width bands in four saturated colours (yellow #ffd000, magenta #d5137b, green #326539 on cream #fffceb), plus a magenta footer. It is lively, but the opposite of quiet. — [diasporaco.com](https://www.diasporaco.com)
- **Šemen theme**: the espresso #2b2420 is hard-coded 22 times across 13 files. These are `semen-year-wheel` (7), `semen-quality` (4), `semen-hero`, `semen-split`, `semen-seasons`, `semen-steps`, `semen-gallery`, `semen-cta`, `semen-cards`, `semen-page-hero`, `semen-contact`, `snippets/header-css.liquid`, and `sections/footer-group.json`. — [local theme code](C:/Users/Uporabnik/Desktop/Work/Stranke/2026/prodaja-medu/website/sections)

### Inferences
- **Rule of thumb for a light, elegant homepage**:
  - Base colour for 70% or more of the height.
  - One tint for no more than 20% of the height, in at most two bands that are never adjacent and are separated by at least one base-colour section.
  - Dark for no more than 10–15% of the height, in at most one block, placed at the end.
  - A dark hero photo also counts visually as a dark zone. If the footer is espresso, choose a lighter, warm-toned hero image.
- **Where the tint goes on Šemen's page**, given the current order (hero → products → quality → family/story [dark] → numbers [dark] → production [cream] → testimonials → blog → newsletter → footer [dark]):
  - Put one cream band behind either the quality/seal section or the production section, not both.
  - Convert family/story into a light split section (large photo plus text) and fold the numbers into it as a hairline-separated row of three or four figures, instead of a separate dark band.
  - Merge the newsletter into the footer.
- **Two coherent options**:
  - **A, all-light**: the footer also becomes cream-tinted (the Mast / Pump Street model), so no espresso blocks remain; espresso is only the text colour.
  - **B, framed**: a single espresso footer that contains the newsletter (the La Cabra model), so espresso appears only at the close. This also matches the client's Reference A.
- **Make tint steps clearly visible** (e.g. white → #f7f3ea). Several almost-identical beiges, as in Reference A, look accidental.
- This matches the project's standing preference (few espresso sections, never several in a row; new sections white or cream).

### Gaps
- No quantitative research was found linking the number of dark sections to perceived elegance or conversion. These recommendations are based on the observed patterns.
- The height percentages are approximate: they come from pixel runs at a single 1440 px viewport and include photo-dark areas only where noted.

---

## Which footer and header treatments read as premium for a light site?

### Takeaway
Premium light sites pair a solid light header with one of two footer styles.
- **Header**: white or cream, with small tracked caps or a centred letterspaced wordmark, sticky, and sitting *above* the hero rather than overlaid on it.
- **Footer, option 1**: light or tinted (Mast #e4e2dd, Pump Street #f0d3c9, Brightland white).
- **Footer, option 2**: a single charcoal footer that also holds the newsletter (La Cabra #2e2c29).

Transparent headers over photos (Sightglass, Diaspora) depend on every hero image being dark at the top; NN/g's contrast guidance makes that hard to guarantee with a slideshow. For Šemen, a white or cream header with a hairline bottom border, plus either a cream footer or one espresso footer, is the elegant combination.

### Cited Findings
- **Headers**:
  - Old Rast: a solid charcoal bar with white tracked caps nav. — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)
  - Rast 2026: a fixed light header (#ece5e0) sitting above the full-bleed hero, with mono caps nav (letter-spacing 0.8 px) and two small outlined buttons. — [rast.ch/de](https://www.rast.ch/de)
  - Brightland: a sticky white header with a centred letterspaced wordmark, nav on the left and icons on the right, below a yellow announcement bar. — [brightland.co](https://brightland.co)
  - La Cabra: a light header with the tracked-caps wordmark on the left and the nav centred, plus a thin dark utility bar above. — [lacabra.com](https://lacabra.com)
  - Mast: a sticky light header with the nav in sofia-pro 11 px, weight 300, uppercase, letter-spacing 2.2 px (0.2em). — [mastmarket.com](https://mastmarket.com)
  - Pump Street: a fixed header with caps nav at 13 px, weight 500 and 1 px tracking, under a pale pink announcement bar. — [pumpstreetchocolate.com](https://pumpstreetchocolate.com)
  - Sightglass and Diaspora: an absolutely positioned, transparent header over the hero photo, with white nav. — [sightglasscoffee.com](https://sightglasscoffee.com); [diasporaco.com](https://www.diasporaco.com)
- **NN/g on text over images**: non-decorative text needs a contrast ratio of at least 4.5:1, or 3:1 for large text. Recommended techniques are darkening the image, a semi-transparent gradient, a "floor fade" over the lower part, blur, and semi-opaque text boxes. Solutions must work for "the worst-case background image and text placement". — [NN/g, "Ensure High Contrast for Text Over Images" (Harley, 2015, reviewed Jan 2026)](https://www.nngroup.com/articles/text-over-images/)
- **Footers**:
  - Brightland: white, with the wordmark, link columns, an inline e-mail field with an arrow, social links, and a half-width olive-grove photo. — [brightland.co](https://brightland.co)
  - Mast: light greige (#e4e2dd), with tiny caps column headings and a newsletter field with a dark "SUBSCRIBE" button. — [mastmarket.com](https://mastmarket.com)
  - Pump Street: peach (#f0d3c9), with About, Contact and Help columns, an "Awards" column with award roundels, and payment icons. — [pumpstreetchocolate.com](https://pumpstreetchocolate.com)
  - La Cabra: dark #2e2c29, with "Join our newsletter" at the top of the same block and text in rgba(248,241,236,0.75). — [lacabra.com](https://lacabra.com)
  - Sightglass: #212121, with an oversized wordmark. — [sightglasscoffee.com](https://sightglasscoffee.com)
  - Rast 2026: black, with an orange "Shop" box and an orange line-art strip below. — [rast.ch/de](https://www.rast.ch/de)
  - Old Rast: charcoal, with grey certification roundels. — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png)
  - Reference A: dark brown #30261c. — [desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)

### Inferences
- **Header for Šemen**:
  - Solid white or cream, with a 1 px hairline bottom border in espresso at 8–12% opacity.
  - Logo left or centred.
  - Nav either in small tracked caps (0.08–0.14em) or in 15–16 px sentence case.
  - Sticky, getting slightly shorter on scroll.
  - No coloured announcement bar; if one is needed, use cream or espresso text on cream.
  - A header overlaid on a slideshow risks failing NN/g's worst-case contrast test unless every slide has a top gradient.
- **Footer for Šemen**:
  - Either (A) a cream #f7f3ea footer with espresso text, or (B) one espresso footer that absorbs the newsletter.
  - In both cases, show quality seals or awards in the footer as small monochrome marks (the old Rast and Pump Street precedent), not as coloured stickers.
  - Use text opacity (La Cabra's 75% on a tinted colour) for secondary text instead of mid-greys, so the footer stays warm.

### Gaps
- Sticky and scroll behaviour was not tested (static captures only).
- Aesop, often cited as the benchmark for light, editorial e-commerce, returned a bot-protection page to the headless browser, so it is not included.

---

## Which other layout, component and motion patterns suit a premium honey shop, and what should be avoided?

### Takeaway
**Patterns to use**:
- A single static full-bleed hero, with a short sentence-case headline bottom-left over a gentle floor fade. The floating benefits card can stay; Sightglass floats a product card on its hero in the same way.
- A static product grid instead of a carousel: eight honeys fit in a 4×2 grid.
- One row of equal editorial tiles.
- Hairline rules instead of boxes and shadows.
- A strict spacing rhythm, about 96–128 px between sections on desktop.
- One large quote or press line instead of avatar cards.
- Awards and quality marks as quiet monochrome marks.
- The newsletter folded into the footer.
- Motion limited to short ease-out fades, underline hovers and slow image zooms, with reduced-motion support.

**Patterns to avoid**:
- Auto-rotating slideshows, especially on mobile.
- Honeycomb motifs everywhere.
- Consecutive dark blocks.
- Decorative props and icon rows.
- Bouncy or overshooting easing.

### Cited Findings

#### Hero treatments
- **Rast 2026**: full-bleed photo with a serif headline (92 px) bottom-left and two small buttons. **Old Rast** and **Reference A** heroes are both about 2.4:1. — [rast.ch/de](https://www.rast.ch/de); [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png); [Reference A desktop module](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)
- **Sightglass**: full-bleed roaster photo with the headline "Fall Forward" bottom-left and a product card (image, name, notes, price) floating over the hero's bottom-right corner. This is the same idea as Šemen's floating benefits card. — [sightglasscoffee.com](https://sightglasscoffee.com)
- **La Cabra**: a dark full-width photo with a serif headline on the left and a small rectangular "LEARN MORE" button. **Pump Street**: a full-bleed macro photo with a centred, tracked caps headline and an outlined button. — [lacabra.com](https://lacabra.com); [pumpstreetchocolate.com](https://pumpstreetchocolate.com)
- **NN/g on carousels**:
  - A static hero image "may be a better choice": it is less distracting and keeps the global navigation more visible.
  - Use five or fewer frames.
  - Don't auto-forward on mobile, and avoid auto-forwarding when reading time can't be guaranteed.
  - Show how many frames there are and which is current; "Dots are a particularly poor cue on mobile devices."
  - Put controls inside the carousel and make them large and high-contrast.
  - Signal that more content exists by "bleeding" (showing part of) the next image.
  - Source: [NN/g, "Carousel Usability" (Pernice, 2013, reviewed Aug 2026)](https://www.nngroup.com/articles/designing-effective-carousels/)
- **Baymard on carousels**:
  - 46% of desktop and mobile sites with a homepage carousel have usability problems.
  - On desktop, rotate every 5–7 s (up to about 10 s for text-heavy slides), pause on hover, and stop permanently after any manual interaction.
  - "Carousel autorotation should be avoided on mobile sites."
  - Support swipe in addition to buttons, and keep slide text as real HTML rather than baked into images.
  - Static content sections perform as well as a good carousel and are simpler to get right.
  - Source: [Baymard, "10 UX Requirements…Homepage Carousel" (Scott, 2019, updated Apr 2025)](https://baymard.com/blog/homepage-carousel)

#### Product presentation and carousels
- **Rast 2026**: arrows beside the section heading, four cards visible, and a centred count-based link ("Alle unsere 61 Kaffee-Sorten entdecken"). **Brightland**: an arrow over the last card plus a peek of the next card, with pill tabs to filter the collection. **Sightglass**: text tabs above a static grid with a "VIEW ALL" button. — [rast.ch/de](https://www.rast.ch/de); [brightland.co](https://brightland.co); [sightglasscoffee.com](https://sightglasscoffee.com)

#### Editorial image tiles
- **Old Rast**: three equal tiles with overlaid caps titles, one line icon and a label. **La Cabra**: four category tiles (Favourites, K.H. Würtz, Coffee, Brewing Equipment) with a serif title bottom-left and an underlined "Shop now". **Sightglass**: two large tiles with overlaid titles and a button ("Never Run Out Of Fresh Coffee", "Become an Expert with In-Person Classes"). **Mast**: three lifestyle tiles with small white label buttons ("SHOP PANTRY", "SHOP COFFEE", "SHOP CHOCOLATE"). — [Client screenshot B](C:/Users/UPORAB~1/AppData/Local/Temp/claude/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/7c41fca9-10a2-48ee-a221-6b9cb5504eca/images/26.png); [lacabra.com](https://lacabra.com); [sightglasscoffee.com](https://sightglasscoffee.com); [mastmarket.com](https://mastmarket.com)
- **Split editorial sections**: La Cabra alternates text-left/image-right and image-left/text-right blocks (a store, a ceramics collaboration, an interview, a seasonal product). Rast 2026 uses asymmetric, offset photo collages in its story sections, including a black-and-white archive photo. — [lacabra.com](https://lacabra.com); [rast.ch/de](https://www.rast.ch/de)

#### Hairlines, labels and spacing rhythm
- **Rast 2026**: a hairline rule above the Journal section, hairlines between the B2B benefit rows, and mono caps eyebrows marked with a small orange square. — [rast.ch/de](https://www.rast.ch/de)
- **Measured whitespace gaps** (median, at 1440 px):

  | Site | Median gap |
  |---|---|
  | Rast 2026 | 128 px (strict) |
  | La Cabra | 79 px (range 41–161) |
  | Mast | 64 px (consistent) |
  | Pump Street | 54 px |
  | Brightland | 53 px |
  | Sightglass | 48 px |
  | Reference A | about 44 px |

  Sources: [rast.ch/de](https://www.rast.ch/de); [lacabra.com](https://lacabra.com); [mastmarket.com](https://mastmarket.com); [pumpstreetchocolate.com](https://pumpstreetchocolate.com); [brightland.co](https://brightland.co); [sightglasscoffee.com](https://sightglasscoffee.com); [Reference A](https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ce6495177842783.64dda5174a2c9.png)

#### Testimonials, press and quality marks
- **Brightland**:
  - A single centred customer quote with five stars and arrow-plus-dot controls, on a cream band.
  - A strip of press logos directly under the hero (Food & Wine, The New York Times, Bon Appétit, Oprah Daily, Women's Health).
  - A second press quote with a logo.
  - A founder quote with a signature and portrait.
  - A marquee of claims ("Ships Within 24 Hours", "California Grown", "Beautifully Packaged").
  - Source: [brightland.co](https://brightland.co)
- **Pump Street**: an "IN THE PRESS" band with a single quote on pale pink, and an awards column in the footer. — [pumpstreetchocolate.com](https://pumpstreetchocolate.com)
- **Sightglass**: three quote cards marked "VERIFIED BUYER", an aggregate line ("★★★★★ 4.9/5 — Join 100,000+ customers…"), and an "Our Mission" row of three pillars with thin line icons (Responsible Sourcing, Small Batch Roasting, Sustainability & Community). — [sightglasscoffee.com](https://sightglasscoffee.com)
- **Diaspora Co.**: four icon claims (Single Origin, Fair Wages, Freshest Harvest, Highest Quality) on a yellow band, a "What Sets Us Apart" comparison table, a Vogue quote on magenta, and a band reading "Sourced from 150+ farms across India & Sri Lanka". — [diasporaco.com](https://www.diasporaco.com)

#### Newsletter
- **Rast 2026**: a full orange band with an underline field. **La Cabra**: the top of the dark footer. **Brightland** and **Mast**: an inline field inside the footer. **Pump Street**: a small centred "SUBSCRIBE" block above the footer. **Reference A**: a separate band offering "15% Off". — [rast.ch/de](https://www.rast.ch/de); [lacabra.com](https://lacabra.com); [brightland.co](https://brightland.co); [mastmarket.com](https://mastmarket.com); [pumpstreetchocolate.com](https://pumpstreetchocolate.com)

#### Motion and micro-interactions
- **NN/g timing**:
  - Most UI animations should take 100–500 ms: about 100 ms for simple feedback and 200–300 ms for larger changes. At 500 ms, animations "start to feel like a real drag".
  - Animations are far more often too long than too short.
  - Entering motion can be slightly longer than exiting motion.
  - Use ease-out by default and avoid linear motion.
  - Source: [NN/g, "Executing UX Animations: Duration and Motion Characteristics" (Laubheimer, 2020)](https://www.nngroup.com/articles/animation-duration/)
- **Shopify's Dawn theme**:
  - Motion tokens: `--duration-short: 100ms`, `--duration-default: 200ms`, `--duration-medium: 300ms`, `--duration-long: 500ms` and `--duration-extended: 3s`, with `--ease-out-slow: cubic-bezier(0, 0, 0.3, 1)`.
  - Animations are wrapped in `prefers-reduced-motion` media queries.
  - The Image-with-text section offers an `image_behavior` setting: none / "ambient" movement / "zoom-in" on scroll.
  - Sources: [Dawn base.css](https://github.com/Shopify/dawn/blob/main/assets/base.css); [Dawn image-with-text.liquid](https://github.com/Shopify/dawn/blob/main/sections/image-with-text.liquid)
- **Shopify performance guidance**: animate `transform` and `opacity` rather than layout properties, and remove CSS transitions from LCP images, because they can delay the LCP event. — [Shopify, Performance best practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance)
- **WCAG 2.2.2 (Pause, Stop, Hide)**: moving content that starts automatically, lasts more than five seconds and is shown alongside other content needs a way to pause, stop or hide it. — [W3C Understanding SC 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html). The `prefers-reduced-motion` media feature detects a user setting to minimise non-essential motion. — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

### Inferences
- **Pattern catalogue for Šemen**:
  - **Hero**: one static image, or at most three manually controlled slides with no autoplay on mobile. Use 16:9 to 2.4:1 on desktop and a 4:5 crop on mobile. The headline is one short sentence-case line at 48–72 px, bottom-left, over a floor-fade gradient (about 0→45% black over the lower 40%). Keep the white benefits card overlapping the hero's bottom edge, but give it three items separated by vertical hairlines and no colour icons.
  - **Products**: a static 4×2 grid for the eight honeys on desktop and two-up on mobile, using the plates and caption format above, with one "Vsi medovi" link. This avoids the carousel problems NN/g and Baymard describe.
  - **Tiles**: three equal 4:5 tiles (Zgodba / Apiturizem / Kakovost), with text bottom-left on a floor fade, one thin line icon at most, and a slow hover zoom.
  - **Story**: a light split section with a large photo. The numbers become a row of three or four figures with large numerals and small tracked captions, separated by vertical hairlines, replacing the dark numbers band.
  - **Quality**: the seal plus four pillars as a quiet row of thin line icons with hairline separators, on the single cream band (the Sightglass "Our Mission" pattern). Drop the hexagon frame.
  - **Testimonials**: one large quote at a time (24–32 px display face), with a small tracked-caps attribution, at most five quotes and manual arrows only. No avatars or stars unless they are real, verifiable reviews.
  - **Blog**: three cards with 3:2 images, a category eyebrow and a title, and a hairline above the section heading (the Rast Journal pattern).
  - **Newsletter**: inside the footer.
- **Hairlines and spacing**:
  - Hairlines are 1 px espresso at 10–15% opacity.
  - Use one spacing scale: 96–128 px between sections on desktop, 64–80 px on mobile, and 32–48 px from heading to content.
  - Content max-width about 1200–1280 px. Old Rast's centred column was about 74% of the viewport.
  - The contrast between Reference A's about 44 px gaps and Rast 2026's 128 px is a large part of why one looks like a template and the other like an editorial site.
- **Motion that reads premium**:
  - Reveal on scroll: fade-up of 8–16 px over 300–500 ms with ease-out, once per element, with a 60–80 ms stagger in grids.
  - Link and nav hover: an underline drawing in from the left over 200–300 ms.
  - Buttons: a colour or fill change over 150–200 ms.
  - Image hover: a slow scale to 1.03–1.05. This decorative zoom can run longer than UI feedback (Dawn's 3 s "extended" token exists for ambient motion).
  - Never animate the hero LCP image. Honour `prefers-reduced-motion`. No parallax-heavy scenes, scroll-jacking, spring or overshoot ("bouncy") easing, or autoplaying slides.
- **Avoid list**:
  1. **Honeycomb overload**: hexagon masks, hex patterns, bee clip-art and dripping-honey graphics. At most one subtle reference.
  2. **Two or more dark blocks mid-page** (currently family plus numbers).
  3. **Stock-theme tells**: generic icon rows, a geometric sans plus a script eyebrow, cut-out props, per-card buttons and hearts, tiny arrows outside carousels, dot pagination as the only control, and many near-identical tints.
  4. **Auto-rotating slideshows.**
  5. **Text baked into images.**
  6. **Saturated brand-colour blocking** (Diaspora's approach), which suits a playful brand, not a quiet premium one.

### Gaps
- Hover, scroll and reveal behaviour of the example sites was not observed (static captures only), so the motion recommendations rest on NN/g, Shopify/Dawn tokens and convention.
- No dated 2024–2026 Awwwards or Siteinspire food e-commerce collection was retrieved; searches returned only undated element pages, e.g. [Awwwards – Ceremony Coffee Roasters](https://www.awwwards.com/inspiration/ceremony-coffee-roasters-thesis). Examples are therefore live sites captured on 2026-10-20, with no award status verified.
- Diaspora's hero did not render in the headless capture (probably a video), so its hero treatment is not described.

---

## How should these patterns be implemented in a Shopify theme (section structure, image sizes, performance, mobile)?

### Takeaway
Build the patterns as code-level section settings so the client can choose white, cream or espresso per section in the theme editor, without anyone hand-editing content JSON. The settings are colour scheme, spacing, an optional hairline divider and image shape. Centralise the 22 hard-coded #2b2420 values into one CSS variable. Follow Shopify's performance rules:
- eager loading plus `fetchpriority="high"` on the hero;
- lazy loading only below the fold;
- `image_tag` with srcset and sizes;
- `<picture>` for a separate mobile hero crop;
- animation of transform and opacity only;
- self-hosted fonts.

On mobile, replace carousels with swipeable scroll-snap rows that show a peek of the next card, and never auto-rotate.

### Cited Findings
- **Shopify performance guidance**:
  - Apply `loading="lazy"` only to images outside the initial viewport, and never to the LCP image. Mark the LCP image with `fetchpriority="high"`.
  - Use an `<img>`, not a CSS background-image, for hero content, and a `<picture>` element when mobile and desktop heroes differ.
  - Use `srcset` and `sizes` through `image_tag`, which also adds width and height attributes to prevent layout shift.
  - Defer non-critical JS. Animate `transform` and `opacity`. Self-host fonts on Shopify's CDN. Preload only one or two critical resources.
  - Theme Store themes must average a Lighthouse performance score of at least 60 across the home, product and collection pages.
  - Source: [Shopify, Performance best practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance)
- **Dawn's native options**: arch and blob masks (`mask-arch.svg`, `mask-blobs.css`) and an "image behaviour" setting (none / ambient / zoom-in) are part of Shopify's reference theme. — [Dawn assets](https://github.com/Shopify/dawn/tree/main/assets); [Dawn image-with-text.liquid](https://github.com/Shopify/dawn/blob/main/sections/image-with-text.liquid)
- **Product image size**: third-party guides say 2048×2048 px (1:1) is the recommended size, that themes generally show product images at 1:1 (non-square images get letterboxed or cropped), and that about 800×800 px is the minimum for zoom. They disagree on the maximum (5000×5000 px / 25 MP versus 20 MB). — [Cloudinary guide](https://cloudinary.com/guides/ecosystems/shopify-image-sizes); [GemPages guide](https://help.gempages.net/articles/shopify-product-image-size)
- **Project rules**: content JSON (`templates/*.json`, the section-group JSON, `config/settings_data.json`) is owned by the theme editor and ignored by the default CLI environment. Code work happens in `sections/*.liquid`, `snippets/` and `assets/`, and content changes should preferably be made in the editor. — [Project CLAUDE.md](C:/Users/Uporabnik/Desktop/Work/Stranke/2026/prodaja-medu/website/CLAUDE.md)
- **Hard-coded colour**: #2b2420 is hard-coded in 13 files (22 occurrences), including the footer-group JSON. — [local theme code](C:/Users/Uporabnik/Desktop/Work/Stranke/2026/prodaja-medu/website/sections)

### Inferences
- **Section schema pattern**:
  - Add a `color_scheme` select (base / tint / espresso) to every homepage section. It maps to CSS custom properties: `--section-bg`, `--section-fg`, `--section-muted` (text colour at 70–75% opacity) and `--section-rule` (espresso at 12%).
  - Add `padding_top` and `padding_bottom` selects: none / S / M / L = 0 / 64 / 96 / 128 px on desktop, scaled to roughly 0 / 40 / 56 / 72 px on mobile.
  - Add a `show_divider` checkbox (a hairline at the top of the section) and an `image_shape` select (rectangle / arch / circle) implemented with `border-radius` or `mask-image`/`clip-path`.
  - This lets the client test "one tint band" or "no dark blocks" in the editor himself, with schema-only code changes and no edits to content JSON.
- **Centralise the colour**: replace the hard-coded `#2b2420` with `var(--color-espresso)` (and a `--color-cream` for #f7f3ea), defined once in `snippets/header-css.liquid`. Then reducing espresso usage, or retuning it, is a single edit.
- **Product card snippet**:
  - An `aspect-ratio: 4/5` (or 1/1) plate with `background: var(--plate)`, where the plate is one step darker than the page.
  - The jar image uses `object-fit: contain` with about 10–14% padding.
  - Jars shot on white can sit on a tinted plate using `mix-blend-mode: multiply`, which works well for opaque packshots but can dull glass highlights, so test it on real jar photos. The cleanest alternative is shooting every jar on a seamless backdrop in the plate colour, or using transparent WebP/PNG.
  - Store the eyebrow line (season or forage) in a product metafield, e.g. `custom.season` and `custom.source`, so it is editable per product.
- **Image sizes and aspect ratios**:

  | Use | Source size | Aspect | `sizes` / notes |
  |---|---|---|---|
  | Desktop hero | 2880 px wide or more | 16:9–2.4:1 | `100vw`, widths about 750–3000 |
  | Mobile hero | about 1080×1350 | 4:5 | separate crop via `<picture>` |
  | Editorial tiles | about 1200×1500 | 4:5 | |
  | Product packshots | 2048×2048 or 1600×2000 | 1:1 or 4:5, kept identical across all eight honeys | e.g. `(min-width: 990px) 25vw, 50vw` |
  | Blog cards | about 1200×800 | 3:2 | |

- **Performance**:
  - Only the first hero image is eager and high priority; every other slide and image below the fold is lazy.
  - No fade-in on the first hero image.
  - Reveal animations use a small IntersectionObserver script, deferred, with the CSS wrapped in `@media (prefers-reduced-motion: no-preference)` as Dawn does.
  - Avoid heavy slider libraries. A static grid for the eight honeys needs no JS at all.
- **Mobile behaviour**:
  - Carousels become `scroll-snap-type: x mandatory` rows with about 1.2–1.5 cards visible (a peek), swipe enabled and no autoplay; a "2 / 8" count or progress line replaces the dots.
  - The eight honeys show two-up.
  - Tiles stack one-up, or 1.2-up in a swipe row.
  - The floating benefits card becomes a static row directly under the hero, so it doesn't cover the photo on small screens.
  - Header about 56–64 px tall; footer columns collapse into accordions; tap targets at least 44 px.

### Gaps
- Molding 2.0's own settings architecture (whether it already has per-section colour schemes or spacing settings) was not inspected.
- Shopify's official help-centre page on product image dimensions was not retrieved; the size guidance above comes from third-party guides.
- No Lighthouse or Core Web Vitals measurement of the current Šemen homepage was taken, so the performance impact of the current slideshow is unknown.
