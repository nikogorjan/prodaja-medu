# Premium honey and artisan food producer websites: design patterns that read as elegant

## 1. Which premium honey brand sites are widely regarded as beautiful or award-winning, and what do they do visually?

### Takeaway
Very few honey producers have formal web-design awards. The ones found are Rowse (The Drum Awards 2022, by Evensix), Local Hive (an ADDY Gold for website design, per its own blog) and Wild Taygetos (Awwwards nominee 2022, since replaced). Design press (Dieline and similar) covers honey packaging, not websites. The best live references are therefore well-made sites rather than prize winners:
- **Honey:** Manukora, Mieli Thun, Comvita, Beechworth Honey, Savannah Bee Company and Miels d'Anicet.
- **Artisan food:** Flamingo Estate, Brightland, Mariage Frères, Tiptree, Pump Street and Daylesford.

What they share:
- A warm off-white or white base.
- One display typeface (usually a serif) at regular weight.
- Products on quiet or tinted plates.
- At most one or two dark areas, often green, olive or black rather than brown.

### Cited Findings

#### How the data was collected
- On 2026-10-20 every site below was loaded in headless Microsoft Edge at 1440×900. Values come from the browser's computed CSS (`getComputedStyle`), `document.fonts`, the Shopify theme object, and colour samples taken from full-page screenshots, so hex values are the colours actually rendered. Section sequences come from Shopify section IDs and the heading order. Each bullet cites the page it was measured on.

#### Recognition evidence (awards, galleries, design press)
- **Awwwards "House of Honey"** (houseofhoney.com): Site of the Day on 14 July 2026, score 7.33/10, by Edoardo Lunardi and Eva Landaluce. Palette #331917 dark brown with #EDCCBE pale peach; tagged Architecture / Portfolio / Luxury. **Not a honey producer.** It is still an example of dark brown paired with a pale peach in an "editorial" register — [Awwwards](https://www.awwwards.com/sites/house-of-honey-1)
- **Awwwards "Wild Taygetos' Honey"** (melitaygetos.gr): Nominee, 31 March 2022, by Anveto Marketers; WordPress + GSAP; described as "Clean, cozy and minimal!" — [Awwwards](https://www.awwwards.com/sites/wild-taygetos-honey). On 2026-10-20 the domain led to honeytaygetos.com, a dark store (#080706 base, gold #dbb459, Roboto). The awarded design has been replaced — [honeytaygetos.com](https://honeytaygetos.com/)
- **Local Hive Honey:** its blog said the brand won nine awards, including Best of Show at the Dallas ADDYs and "Gold – Website Design" — [search result for Local Hive blog](https://localhivehoney.com/blogs/blog/our-award-winning-new-look). The URL returned HTTP 404 on 2026-10-20. The live theme is named "2025 - Destini" (Envy) — [localhivehoney.com](https://localhivehoney.com/)
- **Rowse Honey:** a case study on The Drum covers Evensix's Rowse site at The Drum Awards for Digital Industries 2022. The search summary called the category "Best Website Design" but the URL slug says "best tech platform", so the exact category is unverified. The site centred the "Hives for Lives" mission — [The Drum](https://www.thedrum.com/awards-case-study/heres-how-evensix-won-best-tech-platform-the-drum-awards-digital-industries)
- **Beechworth Honey:** an efront.digital case study says efront built beechworthhoney.com.au (designed by Wolf) around heritage, sustainability, rich video and imagery. No dates or awards are given — [efront](https://efront.digital/case-study/beechworth-honey/)
- **Brightland** (olive oil): The Dieline (2018) credits SDCO Partners with the bright white bottle and art-led identity — [Dieline](https://www.thedieline.com/blog/2018/8/17/sdco-changes-the-olive-oil-game-with-brightland). Fast Company credits Stitch Design for the powder-coated bottles — [Fast Company](https://www.fastcompany.com/90247127/olive-oil-gets-a-modernist-makeover). The credits conflict.
- **Hilltop Honey** (UK): rebrand of positioning, identity and packaging by Big Fish, including a mass line and a premium single-origin line — [FMCG CEO](https://www.fmcgceo.co.uk/honey-brand-hilltop-unveils-major-refresh). Campaign "For Honey Heads" by St Luke's (2024) — [Creative Salon](https://creative.salon/articles/work/st-luke-s-hilltop-honey-honey-heads). Neither covers the website.
- **Manukora:** SynapseIndia says it revamped Manukora's Shopify store (design customisation, reviews, geo-redirects). No design award found — [SynapseIndia](https://www.synapseindia.com/case-study/manukora.html)
- **Flamingo Estate:** designer David Diliberto says he has led the website's design and development for four years. No award named — [Contra](https://contra.com/p/cNoElOmg-flamingo-estate)
- **Shopify showcases:** a search for honey-brand Shopify Plus case studies returned only Honey Birdette, a lingerie brand — [Shopify](https://www.shopify.com/case-studies/honey-birdette)
- **Dieline-type coverage of honey** is about packaging: Bee Roots (gold foil, torn-paper motif), Pure Mother Bee (crown + B logo, no bee), Wiener Honig (packaging that shows the honeys' colours) — [Dieline: Wiener Honig](https://thedieline.com/wiener-honig-html-2/); Hive Index concept (macro photography and batch data instead of cartoon bees) — [Contra](https://contra.com/p/mggbOqUE-hive-index-raw-honey-brand-identity)

#### Inventory A: honey producers (all live and measured on 2026-10-20)

**1. Manukora** (New Zealand; direct-to-consumer raw mānuka honey). Shopify theme "Horizon" 2.1.5.
- **Palette:**
  - Base #f4f0e6 (warm oat), used for almost every section; header #faf9f6.
  - Ink #2e2e24 (olive-black).
  - Calls to action: yellow #f6be00 pills (radius 200px); secondary pill #faf9f6 with #72645a text.
  - Announcement marquee #2e2e24 with cream text — the only dark band.
  - The About page opens with a saturated yellow band (~#febd03).
  — [manukora.com](https://manukora.com/), [About](https://manukora.com/pages/aboutmanukora)
- **Type:**
  - Metro Sans for headlines (H1 70px w400; H2 26px w500) and body (18px/28.8px).
  - Moret Book, a soft serif, for product names and quotes (26–40px, w300–400).
  - No uppercase headings; uppercase only in buttons and the marquee.
  — [manukora.com](https://manukora.com/)
- **Homepage sequence:**
  1. Marquee and sticky header (SHOP MĀNUKA HONEY · SHOP BIOACTIVE BLENDS · OUR ORIGINS · LEARN · TAKE QUIZ).
  2. Full-bleed macro photo of amber honey with "Honey With Superpowers." and a "25,000+ Verified 5-Star Reviews" line.
  3. "Start Your Mānuka Ritual." starter kits.
  4. "Meet Manukora": a centred sentence with small round image chips set between the words.
  5. Grade slider (MGO 600+ / 850+ / 1000+).
  6. "Why Manukora is Different" comparison table.
  7. Amber "Mānuka Taste" band listing tasting notes.
  8. Bioactive blends, benefits diagram, video testimonials, ethical beekeeping statement.
  9. "Meet Jim" founder section, then "Shop Starter Kits" / "Take the Honey Quiz", blog, "Not sure where to start?".
  10. Footer with a giant "Manukora" wordmark over a yellow-flower photo.
  — [manukora.com](https://manukora.com/)
- **Product presentation:** dark jars on tinted plates with 20px corners, one plate colour per grade (sampled from the screenshot): #b5c3cc dusty blue (MGO 600+), #cfcfcf grey (850+), #bdae8d sand (1000+) — [manukora.com](https://manukora.com/)
- **Photography:** macro honey texture and drips in warm amber light; founder outdoors with hive boxes; video testimonials — [manukora.com](https://manukora.com/)

**2. Mieli Thun** (Ton, Val di Non, Trentino, Italy; nomadic monofloral honeys; "Mieli Thun – Andrea Paternoster s.s.a."). WordPress + WPML.
- **Palette:**
  - Base #ffffff; ink #3f3f3d.
  - Hero slideshow dark #262624.
  - Cream band #f6efe5 for "Scopri la selezione di stagione" (the seasonal selection).
  - Bottle-green bands #2e564d (home) and #265c4f (story page); beige band #eae4ce (story page).
  - Orange call-to-action pills #e95a0c (radius 40px).
  - Product cards white with a 1px #e9deca border and 8px radius.
  - Footer cream #f5ecdd.
  — [mielithun.it](https://www.mielithun.it/), [Chi](https://www.mielithun.it/chi/)
- **Type:**
  - Instrument Serif for headings: 60–76px, weight 400, normal tracking, sentence case.
  - Manrope for body (16px/27.2px, w500).
  - Both loaded from Google Fonts in the page HTML.
  — [mielithun.it](https://www.mielithun.it/)
- **Header:** centred logo with split navigation. The menu exposes honey and its derivatives (Mieli, Quintessenza, Pollini, Aceti di miele, Idromiele, Acquavite di miele, Confezioni Regalo, Hotel e Ristorazione) and learning pages (Chi, Perché, Come si produce/degusta/conserva, Ricette, Mielicromia, Dizionario) — [mielithun.it](https://www.mielithun.it/)
- **Homepage sequence:**
  1. Dark hero: "Il meglio della natura italiana" / "Mieli e prodotti dell'alveare", with copy "Sessanta territori straordinari. Mieli monofloreali raccolti nel momento della massima fioritura."
  2. "Mieli Monofloreali Italiani Puri e Nomadi": large serif, macro bee photo, short text.
  3. Seasonal selection cards on cream ("Mieli abete", "Mieli bosco", "Mieli sulla", "Mieli tiglio", Idromiele…).
  4. "Manifesto dei mieli futuristi": green panel over a honey photo.
  5. Gift sets "mielimania" and "trasparenza 5" on dark product photos.
  6. "Come si produce / Come si degusta / Come si conserva" with orange hand-drawn line illustrations.
  7. Green band with "Mielicromia" and "Ricette" cards.
  8. Cream footer.
  — [mielithun.it](https://www.mielithun.it/)
- **Range devices:**
  - "Dizionario": an A–Z lexicon of honeys, each entry with an add-to-cart button — [Dizionario](https://www.mielithun.it/dizionario/)
  - "Mielicromia": a section about honey colour, linked from the homepage — [mielithun.it](https://www.mielithun.it/)
  - All 18 large homepage images have square corners — [mielithun.it](https://www.mielithun.it/)
- **Story page ("Chi"):**
  - Full-bleed beekeeper portrait.
  - "Andrea Paternoster: un sogno nato tra gli alveari" with a black-and-white portrait.
  - "Mieli nomadi di origine sconosciuta" on green.
  - A word ticker: Monoflora · Crudo · Nomade · Artigianale.
  - "L'apicoltura di montagna: un viaggio eroico e condiviso" on beige; "La Val di Non, la terra che ci accoglie".
  - "Il negozio Mieli Thun, tempio della degustazione": the shop presented as a tasting temple.
  — [Chi](https://www.mielithun.it/chi/)
- Retailers describe the hives being moved around Italy to follow the blooms — [olio2go](https://www.olio2go.com/products/mieli-thun-artisan-castagno-chestnut-honey-mth-002)

**3. Comvita** (New Zealand mānuka; "Beekeeping Since 1974"). Custom Shopify theme labelled "Production | 9-29-2026 | ehouse".
- **Palette:**
  - Base #ffffff; ink #48382b (warm brown), also used for the pill buttons (radius 42px, cream text #faf2da).
  - Cream band #faf2db ("Benefits of Manuka Honey").
  - Category tile plates tan #dcba9f and sand #d3c4b1 (sampled).
  - Forest-green bands #466351 and green pills #45634f.
  - Footer #48382b with #faf2da text — the only large dark brown area.
  — [comvita.com](https://comvita.com/)
- **Type:**
  - Libre Baskerville for headings (H1 57px w400; H2 26–44px), with single bold words ("Pure **Mānuka** Honey, Trusted Worldwide.").
  - Mark Pro for body (17.6px/30.4px).
  - Uppercase only for a 13px eyebrow with 1.76px tracking.
  — [comvita.com](https://comvita.com/)
- **Homepage sequence:**
  1. Hero: a hand holds a jar while honey drips from a wooden dipper against a tan wall.
  2. Trust row of three icons: "Certified UMF Quality", "Backed by Nature & Science", "Certified B Corp"; plus "Rated Excellent · 19,235 Verified Reviews" and "Join 50,000+ Comvita Enjoyers".
  3. "Shop By Category" (three tan tiles).
  4. "Benefits of Manuka Honey" (four icons on cream).
  5. "The Gold Standard in Mānuka Honey".
  6. "Shop Bestsellers" (UMF 5+ to UMF 20+).
  7. Bee video; sustainability band (green).
  8. "Beekeeping Since 1974" with an archival storefront photo and "Learn About Our Roots".
  9. Footer.
  — [comvita.com](https://comvita.com/)
- About 9px rounded corners on 18 of 23 images — [comvita.com](https://comvita.com/)
- **Story page:**
  - "Connecting people to nature and good health." and "Drawn by the Hum".
  - "Local to New Zealand" with three blocks: Hive To Shelf / Environmental Practices / Comvita Heritage.
  - Video "Pioneers of Mānuka Honey".
  — [Our Story](https://comvita.com/pages/our-story)
- Comvita runs a guided visitor centre, Experience Comvita, in Paengaroa — [SunLive](https://www.sunlive.co.nz/news/58691-world-class-visitor-centre-opens.html), [GrabOne](https://new.grabone.co.nz/activities-events-outdoors/other-adventure-outdoors/p/experience-comvita-7). It was not visible on the captured homepage or story page — [comvita.com](https://comvita.com/)

**4. Savannah Bee Company** (Georgia, USA; founded by beekeeper Ted Dennard). Custom Shopify theme "Savannah Bee" (version 26.1.29).
- **Palette:**
  - White header; cream content #fcfaf2–#fdfaf3.
  - Ink and square buttons in navy #002855 (add-to-cart #0c2d7c).
  - Honey-yellow #ffdb8e bands, used twice: "Our Mission" and the closing "We love bees. And honey. In that order."
  - Footer #f2ecdc; a brown token #532b1e is defined in the CSS.
  — [savannahbee.com](https://savannahbee.com/)
- **Type:** Merriweather (H1 40px w400; H2 30–48px w700); a display face "Typeka" for "Our Mission" at 60px; Open Sans body (16px/28.8px) — [savannahbee.com](https://savannahbee.com/)
- **Homepage sequence:**
  1. Mega-menu header (Shop, Honey, Gifts, Learn, Mission, Rewards).
  2. Seasonal hero ("Winter White Honey is BACK", product still life in snow).
  3. "Best Sellers" with tabs: Top Four / Squeeze / Whipped.
  4. Yellow "Our Mission" band with a beekeeper portrait ("Exceptional Honey. Packed with Purpose.").
  5. "Our Favorites" collection tiles; reviews carousel; recipe tabs.
  6. "Join the Hive & Sweeten Every Order" loyalty block; user-photo strip "From the Hive"; blog "The Latest Buzz".
  7. Yellow closing band, then footer.
  — [savannahbee.com](https://savannahbee.com/)
- **Range page:**
  - "Premium Raw Honey Products Worth Savoring": varietals such as Tupelo, Orange Blossom, Lavender and "Port Bourbon Barrel Aged Orange Blossom Honey", plus whipped flavours.
  - White square-cornered tiles on cream, with an editorial tile ("Exceptional Honey. Packed with Purpose.") inside the grid.
  - FAQ at the bottom, e.g. "What makes tupelo honey different?"
  — [Honey collection](https://savannahbee.com/collections/honey)
- **Stores:** 16 US stores; the Nashville store offers guided tastings from single-source honeys to mead flights. The founder says a store "should feel like entering a hive" — [Newswire 2026](https://www.newswire.com/news/savannah-bee-company-opens-new-store-in-nashville-22646207)

**5. Beechworth Honey** (Victoria, Australia; family beekeepers). Product URLs look like WooCommerce (inferred).
- **Palette:**
  - Base #ffffff; ink #403e39.
  - Warm-grey plates #f9f8f7 and #f1f0ec behind products.
  - Sage statement bands #98a29a and #95a299 with off-white text #f9f8f7.
  - One deep forest-green block #13241e ("Visit Us" / "Hello Healesville!"); pale mint band #e9f2ef.
  - White footer.
  — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- **Type:**
  - Tiempos Headline for headings (32px, w300–400, +0.64px tracking; 60px H1 on collection pages).
  - Freight Sans Pro for body (15px, +0.3px tracking).
  - Uppercase only in 14px square outline buttons.
  — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- **Homepage sequence:**
  1. Header: Shop · About Us · Visit Us · Learn · Bee Cause · Recipes · Honey Journals.
  2. Hero video (did not render in the headless capture).
  3. Call-to-action tiles.
  4. Heritage statement: "For 140 years, Beechworth Honey family beekeepers have been keeping bees in and around our hometown of Beechworth…"
  5. "Shop Australian Honey" category tiles, under a row of small round badges (likely award medals; too small to read).
  6. Sage band "Beechworth Honey starts and ends with bees and nature".
  7. "Not all honey is created equal!" (education).
  8. Second sage band; "Shop other Beechworth Honey products".
  9. Dark-green "Visit Us" with a photo of the historic shop, and "Hello Healesville!" (new retail site).
  10. "Our best sellers"; footer with an AWARDS link.
  — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- **Range page:** "Single Varietal Honey" with sidebar groups (The Art of Pollination Honey, Traditional Honey, Bee Cause Honey); a "Take the Honey Quiz" tile inside the product grid; jars on #f1f0ec — [Single varietal](https://www.beechworthhoney.com.au/shop-beechworth-honey/australian-honey/single-varietal-honey/)
- **Experiences page:**
  - Photo hero "Beechworth Honey Experiences"; peach intro band #fff6ed.
  - Three cards: "Bees, Flowers, & Food: Tasting Experience", "Private Groups Experiences", "Honey Tasting Counter".
  - Calls to action "DETAILS & BOOKINGS" / "ENQUIRE" / "VISIT HONEY SHOP".
  — [Experiences](https://www.beechworthhoney.com.au/visit-us/experiences/)
- **Third-party listings:** a free self-guided shop tour (family history across four generations, live bees) — [WeekendNotes](https://www.weekendnotes.com/free-honey-tour-at-beechworth-honey/). A paid "All Things Beechworth Honey" tasting at A$150 per ticket for up to six people — [Rezdy](https://beechworthhoney.rezdy.com/541718/all-things-beechworth-honey). The listings disagree on the number of varieties and the tour length.

**6. Miels d'Anicet** (Québec; organic honey farm with shop, restaurant and on-site activities). WordPress + WPML.
- **Palette:**
  - Pure white base, black text.
  - One black band (#020202–#0d0d0d) for "Our story / Our commitment" with black-and-white imagery; black footer with a black-and-white botanical photo.
  - No colour accent: buttons are white, square, black text.
  — [mielsdanicet.com](https://mielsdanicet.com/en-ca/)
- **Type:** "Austin", a high-contrast serif display (64–112px, w400), with Inter Light (300) body at 16–18px; a few headings in uppercase serif ("OUR STORY", "SEASONAL PRODUCTS") — [mielsdanicet.com](https://mielsdanicet.com/en-ca/)
- **Homepage sequence:**
  1. Header nav: About Us, Our history and commitment, Team, Queen bees, Blog, Restaurant, Retailers, Corporate gifts, Boutique at the farm, Pollens & Nectars Canteen.
  2. Hero slider.
  3. "Featured products" with a large "Seasonal products" image tile.
  4. "Pollinated by the bee, created by Miels d'Anicet." with category tiles titled in serif (Honeys, Gourmet, Care and wellbeing, Health through the bee, For the home).
  5. Black story/commitment band; "Our news"; "Corporate gifts"; product index as a serif text list.
  6. Footer with Contact Us / Visit Us.
  — [mielsdanicet.com](https://mielsdanicet.com/en-ca/)
- **Activities page:**
  - Landscape hero "Activités sur le site" (112px), then "Quoi faire sur le site des Miels d'Anicet ?"
  - Accordion (read from the capture): boutique, honey tasting, Pollens & Nectars canteen, honey-wine tasting and meadery visit, honey-plant gardens, events.
  - Alternating photo/text blocks: "Buvette au champ", "NOUVEAUTÉ 2026", "Visite immersive", "L'Essaim"; then an FAQ.
  — [Activités](https://mielsdanicet.com/fr-ca/contact/activites-sur-le-site/)

**7. Hédène** (Paris; "L'Excellence du miel Français depuis 2013"; French single-flower and terroir honeys). Shop software not identified; URL patterns resemble PrestaShop (inferred).
- **Palette:**
  - White base; black text and square black "AJOUTER AU PANIER" buttons.
  - Mustard promo band #d19012.
  - Charcoal newsletter strip #464646–#4a4a4a; footer #f8f8f8; red #c0392b on the CONTACT nav item.
  — [hedene.fr](https://hedene.fr/fr/)
- **Type:** Jost bold uppercase for headings (H1 48px w700; H2 21–28px); Nunito Sans body — [hedene.fr](https://hedene.fr/fr/)
- **Homepage sequence:**
  1. Reassurance top bar; nav MIELS · BIEN-ÊTRE · COFFRETS · GOURMANDISES · MARQUE · CONTACT.
  2. H1 "HÉDÈNE, MIEL 100% FRANÇAIS".
  3. Mustard promo band with a jars-in-flowers photo ("[LES JOURS DORÉS]", −20%).
  4. "NOS COUPS DE COEUR" products on white; "NOS COLLECTIONS" photo tiles; reassurance icons.
  5. "TRÉSOR NATUREL AUX SAVEURS INFINIES"; Instagram grid; brand text; newsletter (−15%).
  — [hedene.fr](https://hedene.fr/fr/)
- **Range page:**
  - Filters RÉGION / TEXTURE / GOÛT.
  - Two tiers: "Miels incontournables" (essentials) and "Miels rares" (rare).
  - Product names pair flower and terroir (Miel Sapin de Lorraine, Miel Rhododendron des Pyrénées, Miel Houx du Cantal, Miel Lavande du Luberon, Miel de Paris).
  - Jars with a tricolour ribbon on white.
  — [Miels](https://hedene.fr/fr/3-miels)
- **Story page:** uppercase chapters, including "LA GÉNÈSE", "UN VOYAGE DES SENS ET DES TERROIRS FRANÇAIS" and "LE MIEL DES MAÎTRES FROMAGERS AFFINEURS" (the cheese-maturers' honey) — [Histoire](https://hedene.fr/fr/content/6-histoire)

**8. Famille Mary** (France; "Maison familiale Française depuis 1921"; three generations of beekeepers). Included as a **counter-example**.
- **Palette:** white base; ink #312f27; yellow accent #ffcd00; plum #8b2231 for prices and promotions; purple promo panels; category tiles with 10px corners; service band #f4f6f4 — [famillemary.fr](https://www.famillemary.fr/)
- **Type:** Hanken Grotesk throughout (H1 54px w500; H2 24–36px) — [famillemary.fr](https://www.famillemary.fr/)
- **Homepage sequence:**
  1. Promo carousel (e.g., "Gamme articulation à -20%").
  2. "Acheter par catégories"; "Nos sélections de la semaine" with Nouveautés / Meilleures ventes / Promotions tabs.
  3. Banner "Maison familiale Française depuis 1921".
  4. Recipes; ingredients; about text ("savoir-faire familial issu de 3 générations d'apiculteurs"); FAQ; newsletter; customer service.
  — [famillemary.fr](https://www.famillemary.fr/)

**9. Local Hive** (USA; raw honey sold by region; ADDY award per its blog). A playful reference.
- **Palette:** cream #fff7e4 (about 65% of page pixels); navy #194051 / #013e52; gold headings #e6bc51; tomato-red pill buttons #e74f3d with a 3px navy outline — [localhivehoney.com](https://localhivehoney.com/)
- **Type:** Harman display, Harman Script and Barley Aged (vintage-poster style); Barlow body — [localhivehoney.com](https://localhivehoney.com/)
- **Range by origin:** cards named "COLORADO Honey Blend", "FLORIDA Honey Blend", "ORGANIC HIVE Honey"; a retailer-logo strip; an "As featured in:" press slider — [localhivehoney.com](https://localhivehoney.com/)

#### Inventory B: artisan and family food producers

**10. Flamingo Estate** (Los Angeles; pantry, candles, farm produce). Shopify Prestige 8.3.0.
- **Palette:**
  - Off-white base #fcfbf6; olive ink #45523e for text and outline buttons.
  - Product plates #f1f1ec.
  - Footer olive #45523e with #eff2e9 text and #9eb091 secondary text.
  - No dark bands mid-page.
  — [flamingoestate.com](https://flamingoestate.com/)
- **Type:** Exposure, a serif display (H1 44px w400); Maison Neue body (14px); uppercase micro-labels and buttons at 11px with +0.5px tracking ("MOST LOVED", "ADD TO BASKET $80") — [flamingoestate.com](https://flamingoestate.com/)
- **Homepage sequence:**
  1. Membership announcement; slim sticky header.
  2. Two-up hero ("From Morocco, With Love", "OPEN YOUR LOVE LETTER").
  3. "Most Loved" carousel.
  4. Editorial 2-up blocks with poetic titles ("Paradise, Uncivilized" / "Marrakesh Express", "Hot & Bothered" / "Love at First Light", "Object of Desire" / "Forbidden Fig"), alternating with product carousels.
  5. Press quote ("Best Luxury Candles for Your Home, According to Vogue Editors").
  6. Estate banner; recipes; olive footer.
  — [flamingoestate.com](https://flamingoestate.com/)
- **Products:** 41 of 49 images are 1:1, mostly square-cornered, on #f1f1ec; still lifes with props on saturated pink and mustard backdrops — [flamingoestate.com](https://flamingoestate.com/)

**11. Brightland** (California olive oil; also sells honey). Shopify Impact 6.6.0.
- **Palette:**
  - White base; ink #1b1b1b.
  - Off-white bands #f4f4e8 (testimonial) and #f3f3eb (press); a blush block #f2d4d6 ("Build Your Own Set").
  - Yellow announcement bar; white footer with an olive-grove photo.
  — [brightland.co](https://brightland.co/)
- **Type:** CircularXX, a geometric sans, for interface and headings; custom display faces (Advercase, Alia family) are loaded for campaign headlines — [brightland.co](https://brightland.co/)
- **Homepage sequence:**
  1. Still-life hero ("Hello, Cozy Season"); press-logo strip (e.g., The New York Times, Bon Appétit, Food & Wine).
  2. "All Favorites" carousel; chef testimonial.
  3. Featured set; collection tabs; "Meet the Brightland Pantry".
  4. Origin statement ("Clean, cold-pressed, 100% single origin…"); press quotes.
  5. Build-your-own set (blush).
  6. Founder story with signature; scrolling text; footer.
  — [brightland.co](https://brightland.co/)
- **Products:** cards with 18px corners (39 of 46 images); white art-label bottles on white plates; 9px uppercase badges (BESTSELLER, "OPRAH'S FAVORITE THINGS", "ALMOST GONE") — [brightland.co](https://brightland.co/)

**12. Mariage Frères** (Paris tea house, "French tea since 1854").
- **Palette:** white base; black text; saturated photographic product tiles; 2px white outline buttons over images; footer #f2f2f2 — [mariagefreres.com](https://www.mariagefreres.com/en/)
- **Type:** Copperplate Gothic caps (engraved feel) for navigation and headings (24–70px); **Poppins** for body (15px) — [mariagefreres.com](https://www.mariagefreres.com/en/)
- **Homepage sequence:**
  1. Seal-logo header with uppercase nav over the hero; editorial hero slideshow.
  2. "THE IRREPLACEABLE — Discover the legendary collections", with an ornamental flourish divider and three tins on colour photos.
  3. "THE MARIAGE FRÈRES RESTAURANTS" / "TEA CLUB ATELIERS".
  4. "EARL GREY TEAS" full-bleed; "TYPES OF TEAS" (cup icons coloured by tea); "PU-ERH".
  5. "HISTORY & SAVOIR-FAIRE" black-and-white archival band; "THE FAVOURITES"; footer.
  — [mariagefreres.com](https://www.mariagefreres.com/en/)
- **History page:** a timeline of chapters with archival black-and-white photos ("THE GREAT ADVENTURE", "THE FIRST MAISON DE THÉ MARIAGE FRÈRES", "ARRIVAL IN JAPAN", "COVENT GARDEN", "3 CENTURIES OF PASSION", "TEA MUSEUM") — [History](https://www.mariagefreres.com/en/history)
- **Experiences page:** workshops and books sold as product cards — [Experiences](https://www.mariagefreres.com/en/gifts/experiences.html)

**13. Tiptree / Wilkin & Sons** (Essex; "Wilkin & Sons Since 1885"). Shopify Symmetry 7.1.2.
- **Palette:** off-white #fcfbf9; ink #434242; raspberry #a41b3d (announcement bar, buttons, heritage captions); plates #f4f4f4; footer #edece6; divider #dfddd7 — [tiptree.com](https://www.tiptree.com/)
- **Type:** custom "TipTreeSP" uppercase for headings (14–34px, w500); Antique Olive body (14px) — [tiptree.com](https://www.tiptree.com/)
- **Header:** royal-warrant crest at top left, oval logo centred, four nav items (Shop, Our Story, Recipes, Contact) — [tiptree.com](https://www.tiptree.com/)
- **Homepage sequence:**
  1. Background video.
  2. Two small heritage captions in raspberry: "TIPTREE, AS IT SHOULD BE. — Making quality preserves since 1885." and "FRUITS FROM THE FARM. — Farming in Essex since 1757."
  3. Products on #f4f4f4.
  4. "TIPTREE TEA ROOMS": a map tile plus seven tea-room cards.
  5. Recipes; news; reviews; newsletter; footer.
  — [tiptree.com](https://www.tiptree.com/)
- **History page:** long-form with archival photos — [Our History](https://www.tiptree.com/blogs/about-us/our-history)

**14. Pump Street Chocolate** (Suffolk bakery and bean-to-bar maker). Shopify Turbo 9.0.0.
- **Palette:** white base; ink #373736; blush band #fde3e2 (press/testimonials); lilac-grey strip #edecf1; **pink footer #f0d3c9** — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- **Type:** Work Sans; uppercase headings at 22–36px w600 with 1–2px tracking; 13px body with 1px tracking — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- **Homepage sequence:**
  1. Header nav: OUR SHOPS · WHOLESALE · JOURNAL · WORKSHOP.
  2. Hero with boxed uppercase calls to action ("SHOP OUR ARTISAN CHOCOLATE", "DISCOVER THE COCOA FARMS", "FIND US IN SUFFOLK").
  3. "DISCOVER OUR AWARD WINNING BARS"; "SHOP OUR COLLECTIONS".
  4. Press section; "Visit us" with a photo of the bakery.
  5. Pink footer with an "ABOUT" paragraph ("made by hand from bean to bar…").
  — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)

**15. Daylesford** (Cotswolds organic farm: shop, food, stays, events).
- **Palette:** white / #fafaf8 base; ink #35292b; flat #f5f5f4 buttons and announcement bar; white footer — [daylesford.com](https://www.daylesford.com/)
- **Type:** Trade Gothic Light in uppercase with wide tracking (hero 48px +5px; H2 24px +3px) — [daylesford.com](https://www.daylesford.com/)
- **Navigation:** VISIT · EAT · STAY · RESTORE · SHOP — [daylesford.com](https://www.daylesford.com/)
- **Homepage sequence:**
  1. "THE HEART OF THE COTSWOLDS" landscape hero; "DISCOVER DAYLESFORD".
  2. "LIVE CONSCIOUSLY, LIVE WELL"; "STAY WITH US"; "UPCOMING EVENTS".
  3. "HERITAGE HOUSE CHRISTMAS MARKET"; "ESCAPE TO THE FARM"; "WORKING WITH NATURE".
  4. Credentials trio: SOIL ASSOCIATION · GREEN MICHELIN STAR · B CORP ("Since 2001 we have partnered with the Soil Association"; "awarded a Michelin Green Star in 2021").
  5. Newsletter; footer.
  — [daylesford.com](https://www.daylesford.com/)

#### Also checked (brief)
- **Fortnum & Mason:** FM Serif / FM Sans; white base; light turquoise #64c5b7 pill buttons; dark-teal newsletter band #0b6f6d; round category images (radius 9999px); royal warrants beside a centred "FORTNUM & MASON EST 1707" — [eu.fortnumandmason.com](https://eu.fortnumandmason.com/)
- **Rowse Honey:** a full-screen, fixed-layout scrolling experience; Adelle slab serif plus Barlow Condensed (a 401px "UP NEXT"); butter base #fef2cc; teal ink #03383f; yellow pills #f5bc00; small labels #937100 with 4px tracking — [rowsehoney.co.uk](https://rowsehoney.co.uk/)
- **The Bee Charmer** (formerly Asheville Bee Charmer; the announcement bar confirms the rename):
  - Shopify Flow theme; Instrument Sans + Figtree; white base; sage footer #6c756c.
  - Honeys grouped into flavour families ("Floral Varietals", "Sweet & Fruity", "Spicy Hot", "Earthy Varietals").
  - "Honey of the Week: Sourwood Honey" with a cocktail pairing; store map with "GET DIRECTIONS".
  — [shopbeecharmer.com](https://shopbeecharmer.com/)
- **Mielizia** (Conapi cooperative, Italy): Oswald uppercase + Inter; white base; yellow footer #fdc52c; sections "DAL FIORE A TE", "GLI APICOLTORI", "TRACCIABILITÀ" — [mielizia.com](https://mielizia.com/)
- **Apicoltura Casentinese** (Tuscany): Spartan font; sage #708573 header bar and headings; white/#f6f6f6 base — [apicolturacasentinese.com](https://www.apicolturacasentinese.com/)
- **Bermondsey Street Bees** (London):
  - White base with black-and-white botanical line illustrations and ochre #d6992b accents.
  - Footer credit: "Website by Martin Lewis Design – Design concept by Lydia Thornley".
  - Separate page for corporate events, workshops and talks; nav includes honey-sommelier services.
  — [Experiences page](https://bermondseystreetbees.co.uk/corporate-events-experiences-workshops-talks/)
- **Black Mountain Honey** (UK family business: queens, nucs, honey, courses): Aldgate Sans; near-black #120805 bands; orange #f2800f buttons — [blackmountainhoney.co.uk](https://www.blackmountainhoney.co.uk/)
- **Honey Mama's** (hot-pink #e31c79 footer, Recoleta) and **Beekeeper's Naturals** (moss #1a4338 footer, Begum serif): wellness and confectionery brands, off-target for this brief — [honeymamas.com](https://honeymamas.com/), [beekeepersnaturals.com](https://www.beekeepersnaturals.com/)

#### Could not verify / excluded
- **Hilltop Honey** (hilltophoney.co.uk): TLS errors from headless Edge, curl and WebFetch on 2026-10-20. The website could not be inspected — [hilltophoney.co.uk](https://hilltophoney.co.uk/)
- **Bee Raw** (beeraw.com): a Wayback snapshot of 15 January 2026 shows "Coming Soon — Future home of something quite cool."; the live HTTPS request failed with a certificate error — [Wayback](https://web.archive.org/web/20260115211717/http://beeraw.com/)
- **The London Honey Company** (londonhoney.co.uk): a Wayback snapshot of 20 November 2024 shows a Sedo-parked domain; the live request timed out — [Wayback](https://web.archive.org/web/20241120203711/http://www.londonhoney.co.uk/)

### Inferences
Why each main site reads as elegant:
- **Manukora:** one warm base colour throughout, one bright accent kept to the buttons, a soft serif for product names, plates tinted per grade, and a big confident wordmark instead of a dark footer.
- **Mieli Thun:** a regular-weight editorial serif at large sizes, generous white space, square photography, dark used only in the hero and one bottle-green band, and real editorial content (manifesto, dictionary, honey-colour chart, illustrations) rather than promotions.
- **Comvita:** a classic serif with selective bold words, a warm-brown ink instead of black, and dark brown limited to the footer and buttons. Mid-page contrast comes from green, not brown.
- **Beechworth:** muted sage bands and warm greys make a calm, gallery-like page; one deep-green block marks "Visit Us" as the emotional peak.
- **Miels d'Anicet:** a monochrome, magazine-like design with huge serif headings, black-and-white photography and no accent colour. Its black is graphic, not heavy, because it sits on pure white with photography.
- **Flamingo, Tiptree, Mariage Frères:** a custom or distinctive display face, editorial naming, and heritage marks (crest, warrants, ornament) carry the premium feel with very few colours.
- **Counter-examples:** Famille Mary and Hédène have premium products and long histories, but their sites read as standard e-commerce. Causes: promo carousels, discount bands, bold uppercase sans headings everywhere, reassurance icon rows and template product grids.

Relevance to Šemen:
- The current mix (cream #f7f3ea, several espresso #2b2420 bands, gold, terracotta, wide uppercase grotesque) is closest to Comvita's palette and Hédène's typography.
- The elegant references suggest keeping the cream, moving dark to a single place, and moving headlines to a regular-weight serif or a light tracked style.

### Gaps
- No honey producer was found with a current (2025–2026) Awwwards, CSS Design Awards or Webby win. Rowse's award category is unverified. Local Hive's award post is gone (404).
- Dieline, Behance and BP&O results were packaging-focused; no write-up of a honey website's design was found.
- Hilltop Honey's site could not be reached; its web design is unknown (only the packaging rebrand is documented).
- Beechworth's homepage hero video did not render in the headless capture.
- Some small text (badge contents, a few tasting-note labels) was read from reduced screenshots and is noted as approximate where it appears.
- Not checked: Miel Martine, Le Comptoir du Miel, Bee & Flower (unclear identities); Fortnum & Mason's honey category page (homepage only).

## 2. How do these sites use colour: light neutral bases, tint bands, dark sections, accent colours?

### Takeaway
The elegant sites use a warm off-white or white base, one family of light tint bands (honey-yellow, cream, sage or blush), and one bright accent reserved for buttons. Full-width dark sections are rare: usually one per page, often a deep green, olive or black, and often only the footer. Several premium sites use a light or tinted footer instead of a dark one.

### Cited Findings
Measured palettes (2026-10-20):

| Site | Base | Ink / text | Accent (buttons) | Tint bands | Dark areas | Footer |
|---|---|---|---|---|---|---|
| [Manukora](https://manukora.com/) | #f4f0e6 | #2e2e24 | #f6be00 yellow pills | per-grade plates #b5c3cc / #cfcfcf / #bdae8d; About page yellow ~#febd03 | marquee bar #2e2e24 only | #f4f0e6 + photo with giant wordmark |
| [Mieli Thun](https://www.mielithun.it/) | #ffffff | #3f3f3d | #e95a0c orange pills | cream #f6efe5; beige #eae4ce (story page) | hero #262624; bottle green #2e564d / #265c4f | cream #f5ecdd |
| [Comvita](https://comvita.com/) | #ffffff | #48382b | #48382b brown pills; green #45634f | cream #faf2db; tan plates #dcba9f / #d3c4b1 | green #466351 bands | brown #48382b, cream text #faf2da |
| [Savannah Bee](https://savannahbee.com/) | #fcfaf2–#fdfaf3 | navy #002855 | navy #002855 square buttons | honey yellow #ffdb8e (2 bands) | none | #f2ecdc |
| [Beechworth](https://www.beechworthhoney.com.au/) | #ffffff | #403e39 | outline buttons; sage #94a596 | sage #98a29a / #95a299; mint #e9f2ef; peach #fff6ed (experiences page) | forest green #13241e (Visit Us) | #ffffff |
| [Miels d'Anicet](https://mielsdanicet.com/en-ca/) | #ffffff | #000000 | none (white/black) | none | black story band | black + black-and-white photo |
| [Hédène](https://hedene.fr/fr/) | #ffffff | #000000 / #2e2323 | black square buttons | mustard #d19012 promo band | charcoal #464646 newsletter | #f8f8f8 |
| [Flamingo Estate](https://flamingoestate.com/) | #fcfbf6 | olive #45523e | olive outline pills | plates #f1f1ec | none mid-page | olive #45523e |
| [Brightland](https://brightland.co/) | #ffffff | #1b1b1b | white pills with dark outline | #f4f4e8, #f3f3eb, blush #f2d4d6 | none | white + photo |
| [Tiptree](https://www.tiptree.com/) | #fcfbf9 | #434242 | raspberry #a41b3d | plates #f4f4f4 | none | #edece6 |
| [Pump Street](https://pumpstreetchocolate.com/en-eu) | #ffffff | #373736 | white boxed buttons | blush #fde3e2; lilac-grey #edecf1 | none | pink #f0d3c9 |
| [Daylesford](https://www.daylesford.com/) | #ffffff / #fafaf8 | #35292b | flat #f5f5f4 | none | none | white |
| [Fortnum & Mason](https://eu.fortnumandmason.com/) | #ffffff | #000000 | turquoise #64c5b7 pills | none | dark teal #0b6f6d newsletter band | white |

How dark is used or avoided:
- Mieli Thun confines dark to the hero slideshow (#262624) and a bottle-green band; its footer is light cream — [mielithun.it](https://www.mielithun.it/)
- Comvita's only large dark-brown area is the footer (#48382b); its mid-page contrast bands are green (#466351) — [comvita.com](https://comvita.com/)
- Beechworth uses one deep-green block (#13241e) to frame "Visit Us"; the other bands are light sage — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Manukora's darkest elements are the marquee bar and the dark jars themselves — [manukora.com](https://manukora.com/)
- Miels d'Anicet uses pure black twice (story band and footer), always with black-and-white photography, on a white page — [mielsdanicet.com](https://mielsdanicet.com/en-ca/)
- Flamingo replaces black with olive (#45523e) for text and the footer — [flamingoestate.com](https://flamingoestate.com/)
- Light footers appear at Mieli Thun (#f5ecdd), Savannah Bee (#f2ecdc), Tiptree (#edece6), Pump Street (#f0d3c9), Manukora (#f4f0e6 + photo), Daylesford and Brightland (white) — [mielithun.it](https://www.mielithun.it/), [savannahbee.com](https://savannahbee.com/), [tiptree.com](https://www.tiptree.com/), [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- The all-dark honey shop found (Taygetos, #080706 with gold #dbb459) is the replacement of a 2022 Awwwards nominee and reads as a generic dark store template — [honeytaygetos.com](https://honeytaygetos.com/)

Tint bands as a single "colour moment":
- Savannah Bee: honey-yellow #ffdb8e for the mission and closing statements — [savannahbee.com](https://savannahbee.com/)
- Beechworth: sage #98a29a for brand statements — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Brightland: one blush block #f2d4d6 — [brightland.co](https://brightland.co/)
- Pump Street: blush #fde3e2 — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- Mieli Thun: cream #f6efe5 for the seasonal selection — [mielithun.it](https://www.mielithun.it/)
- Comvita: cream #faf2db for benefits — [comvita.com](https://comvita.com/)

### Inferences
- **The pattern to copy:** one base (warm white or cream), one tint used for one or two bands, one accent kept to calls to action, and at most one dark band. Šemen currently has several dark espresso bands; every premium reference above has zero to one.
- **Brown ink as a softer black:** Comvita's #48382b on white and Flamingo's #45523e olive show that a dark warm colour reads elegant when used for text, buttons and the footer, not as repeated full-width sections. Šemen's #2b2420 could become the ink and footer colour only.
- **Candidate light tints for Šemen's one tinted part:**
  - A pale honey or straw tint, lighter than Savannah Bee's #ffdb8e, to echo the gold crest.
  - A muted sage (Beechworth #98a29a family) to signal meadows and nature.
  - A blush or peach (Pump Street #fde3e2, Beechworth's #fff6ed), which suits the terracotta accent.
- **Terracotta:** Mieli Thun's orange #e95a0c pills on white and cream are the closest live analog to Šemen's #bb5237 buttons, supporting terracotta as the single call-to-action colour.
- **Footer options:** Mieli Thun and Tiptree show that a cream or tinted footer (#f5ecdd, #edece6, #f0d3c9) feels finished without a dark block.

### Gaps
- Hover, focus and secondary-page colour states were not systematically measured.
- Screenshot-sampled colours for photographic areas (e.g., Flamingo's hero backdrops ~#d9a49e and ~#b4a237, Manukora's amber band ~#b1703c–#ca7328) come from photos, not CSS tokens.

## 3. What typography do they use (serif vs sans, letterspacing, uppercase labels), and how is hierarchy built?

### Takeaway
The most elegant honey and artisan sites pair a display serif at regular weight (400) and large size (40–112px) with a quiet sans body (14–18px, line-height about 1.6–1.8). Uppercase is mostly kept for small labels, navigation and buttons with added tracking. Bold uppercase grotesque headlines appear mainly on the more commercial, template-like sites.

### Cited Findings
Serif display with sans body:
- Mieli Thun: Instrument Serif 60–76px w400 with Manrope 16px/27.2px — [mielithun.it](https://www.mielithun.it/)
- Comvita: Libre Baskerville 26–57px w400 (single bold words) with Mark Pro 17.6px/30.4px — [comvita.com](https://comvita.com/)
- Beechworth: Tiempos Headline 32–60px w300–400 with +0.64 to +1.2px tracking; Freight Sans Pro 15px with +0.3px — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Manukora: Metro Sans for headlines (70px w400), with the Moret serif for product names, quotes and section titles (26–70px) — [manukora.com](https://manukora.com/), [About](https://manukora.com/pages/aboutmanukora)
- Flamingo Estate: Exposure serif 44px w400 with Maison Neue 14px — [flamingoestate.com](https://flamingoestate.com/)
- Miels d'Anicet: Austin serif 64–112px w400 with Inter 300 — [mielsdanicet.com](https://mielsdanicet.com/en-ca/)
- Savannah Bee: Merriweather (H1 40px w400; H2 up to 48px w700), the Typeka display face and Open Sans 16px/28.8px — [savannahbee.com](https://savannahbee.com/)

Uppercase headline systems:
- Hédène: Jost w700 uppercase 21–48px — [hedene.fr](https://hedene.fr/fr/)
- Mielizia: Oswald w600–700 uppercase 30–57px — [mielizia.com](https://mielizia.com/)
- Tiptree: custom uppercase w500 14–34px — [tiptree.com](https://www.tiptree.com/)
- Pump Street: Work Sans w600 uppercase with +2px tracking — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- Daylesford: Trade Gothic **Light (w300–400)** uppercase with +3 to +5px tracking — [daylesford.com](https://www.daylesford.com/)
- Mariage Frères: Copperplate Gothic caps for headings and navigation, with **Poppins** as body — [mariagefreres.com](https://www.mariagefreres.com/en/)

Labels and buttons:
- Flamingo: 11px uppercase with +0.5px tracking — [flamingoestate.com](https://flamingoestate.com/)
- Comvita: 13.2px eyebrow with +1.76px — [comvita.com](https://comvita.com/)
- Rowse: 10–12px labels with about +4px — [rowsehoney.co.uk](https://rowsehoney.co.uk/)
- Beechworth: 14px uppercase outline buttons — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Manukora: uppercase pill buttons, 14–18px w600 — [manukora.com](https://manukora.com/)

Hierarchy devices:
- Comvita bolds one keyword inside a light serif headline ("Pure **Mānuka** Honey…") — [comvita.com](https://comvita.com/)
- Manukora uses two typefaces for two roles: sans for statements, serif for product and grade names — [manukora.com](https://manukora.com/)
- Mieli Thun runs a word ticker ("Monoflora · Crudo · Nomade · Artigianale") as a typographic band — [Chi](https://www.mielithun.it/chi/)
- Rowse uses an oversized display line ("UP NEXT" at 401px) — [rowsehoney.co.uk](https://rowsehoney.co.uk/)
- Manukora closes with a giant wordmark footer — [manukora.com](https://manukora.com/)

### Inferences
- Šemen's wide uppercase grotesque headings put it in the same group as Hédène, Mielizia and Famille Mary, which read as commercial. To read as elegant, the strongest move is a serif (or high-contrast display) at regular weight for H1/H2, in sentence case, with the grotesque kept for eyebrows, navigation and buttons at 11–14px with +0.5 to +3px tracking.
- If the grotesque is kept for headlines, Daylesford shows the alternative: light weight, uppercase and very wide tracking. Bold or medium weight with tight tracking is what looks commercial.
- Poppins as body is compatible with an elegant system: Mariage Frères uses Poppins under Copperplate caps.
- Serif display faces observed on these sites include Instrument Serif, Libre Baskerville and Merriweather (delivered from Google Fonts on the sites that load them), plus Tiempos, Moret, Exposure and Austin. Licensing is out of scope for this note.

### Gaps
- Proprietary faces (Typeka, TipTreeSP, FM Serif, Austin) were identified only by their CSS family names; foundries were not researched.
- Mobile type scales were not measured; all values are at 1440px desktop width.

## 4. How are products shown (round, arched or rectangular images, tinted plates, white backgrounds, lifestyle shots), and how is a range of varieties presented attractively?

### Takeaway
Product images are mostly rectangular or square with square corners, or with soft 8–20px rounding. No arched frames were seen on these sites, and only Fortnum & Mason uses circles (for categories). The premium signal is the plate behind the product: warm grey, cream or tinted per variety (Manukora). Lifestyle and macro shots are kept for heroes and story sections. Strong range presentations treat varieties like wine or tea: seasonal selections, a lexicon, colour charts, flavour families, region/texture/taste filters and quizzes.

### Cited Findings
Image shapes:
- Square corners on every large homepage image at Mieli Thun (18/18), Beechworth (23/23), Mariage Frères (53/53), Daylesford (44/44) and Hédène (17/17) — [mielithun.it](https://www.mielithun.it/), [beechworthhoney.com.au](https://www.beechworthhoney.com.au/), [mariagefreres.com](https://www.mariagefreres.com/en/), [daylesford.com](https://www.daylesford.com/), [hedene.fr](https://hedene.fr/fr/)
- Soft rounding: Manukora 20px, Brightland 18px, Famille Mary 10px, Comvita about 9px; Mieli Thun's product cards 8px with a hairline #e9deca border — [manukora.com](https://manukora.com/), [brightland.co](https://brightland.co/), [famillemary.fr](https://www.famillemary.fr/), [comvita.com](https://comvita.com/), [mielithun.it](https://www.mielithun.it/)
- Circles: Fortnum & Mason category bubbles — [eu.fortnumandmason.com](https://eu.fortnumandmason.com/)
- Aspect ratios: Flamingo square (41/49 images); Bee Charmer square (76/87); Beechworth landscape tiles (~0.7 height/width); Daylesford and Brightland portrait (~1.2–1.3) — [flamingoestate.com](https://flamingoestate.com/), [shopbeecharmer.com](https://shopbeecharmer.com/), [beechworthhoney.com.au](https://www.beechworthhoney.com.au/), [daylesford.com](https://www.daylesford.com/), [brightland.co](https://brightland.co/)

Plates behind products:
- Manukora tinted per grade: #b5c3cc / #cfcfcf / #bdae8d — [manukora.com](https://manukora.com/)
- Comvita tan #dcba9f and sand #d3c4b1 — [comvita.com](https://comvita.com/)
- Flamingo #f1f1ec — [flamingoestate.com](https://flamingoestate.com/)
- Beechworth #f1f0ec / #f9f8f7 — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Tiptree #f4f4f4 — [tiptree.com](https://www.tiptree.com/)
- Savannah Bee: white tiles on cream #fcfaf2 — [savannahbee.com](https://savannahbee.com/collections/honey)
- Hédène and Mieli Thun: products on white — [hedene.fr](https://hedene.fr/fr/3-miels), [mielithun.it](https://www.mielithun.it/)

Lifestyle and macro photography:
- Manukora: macro honey texture in the hero — [manukora.com](https://manukora.com/)
- Comvita: a hand with a jar and honey dripping from a wooden dipper — [comvita.com](https://comvita.com/)
- Brightland: a sunlit kitchen still life with bread, lemons and wooden utensils — [brightland.co](https://brightland.co/)
- Flamingo: saturated still lifes on coloured backdrops — [flamingoestate.com](https://flamingoestate.com/)
- Mieli Thun: dark, moody product scenes for gift boxes and macro bee photography — [mielithun.it](https://www.mielithun.it/)

Range and variety devices:
- **Seasonal selection:** "Scopri la selezione di stagione" on a cream band — [Mieli Thun](https://www.mielithun.it/)
- **Lexicon:** an A–Z "Dizionario" of honeys with add-to-cart per entry — [Mieli Thun](https://www.mielithun.it/dizionario/)
- **Honey colour:** a "Mielicromia" section — [Mieli Thun](https://www.mielithun.it/)
- **Grades as tinted cards** with a comparison table and a tasting-notes band — [Manukora](https://manukora.com/)
- **Filters and tiers:** RÉGION / TEXTURE / GOÛT filters; "incontournables" vs "rares"; flower-plus-terroir product names — [Hédène](https://hedene.fr/fr/3-miels)
- **Flavour families and a weekly feature:** Floral / Sweet & Fruity / Spicy Hot / Earthy, plus "Honey of the Week" with a pairing — [The Bee Charmer](https://shopbeecharmer.com/)
- **Origin as the product name:** COLORADO, FLORIDA — [Local Hive](https://localhivehoney.com/)
- **Single-varietal collection** with a quiz tile inside the grid — [Beechworth](https://www.beechworthhoney.com.au/shop-beechworth-honey/australian-honey/single-varietal-honey/)
- **Monofloral FAQ** under the grid — [Savannah Bee](https://savannahbee.com/collections/honey)
- **"Types of teas"** with cup icons coloured by tea — [Mariage Frères](https://www.mariagefreres.com/en/)

### Inferences
- **Tinted plates per variety:** for Šemen's eight varieties, a plate behind each 250g jar, tinted to that honey's colour, would make the range read like a curated flight. This combines Manukora's per-grade plates with Mieli Thun's honey-colour idea. Order from light to dark: acacia, sunflower, linden and wildflower first; chestnut, forest, fir and buckwheat after.
- **Two photo registers:** keep the 900g-on-dark-wood photos for hero and story sections (like Mieli Thun's dark gift-box scenes), and use plain plates in the shop grid. That avoids several dark sections while keeping the warmth.
- **Square corners or one radius:** square corners or a single modest radius (8–20px) read more premium than mixed shapes. Arched frames were not found in this sample, so arches would be a Šemen-specific choice rather than a category convention.
- **A variety guide page:** a "dictionary" or tasting page with colour, aroma, crystallisation, season and pairings per honey, plus a seasonal "this month's harvest" strip, mirrors Mieli Thun and Bee Charmer. It also gives the client content for the light tint band.

### Gaps
- Product detail pages were not systematically captured, so gallery layouts and tasting-note modules are inferred only from collection pages and homepages.
- No site in the sample used arched or pill-shaped product frames; a wider search would be needed to confirm this is not a category trend.

## 5. How do they present producer heritage, awards/quality marks, and experiences (tours, visits)?

### Takeaway
- **Heritage** appears as short dated captions ("since 1885", "Beekeeping Since 1974", "depuis 1921"), founder portraits, and archival black-and-white photo timelines, not long walls of text.
- **Quality marks** are a slim row of three icons or credentials, a press-logo strip, or review counts, not big badges.
- **Visits and tastings** get top-level navigation and a dedicated page of bookable experience cards (photo, short description, booking or enquiry button), often with a map and an FAQ.

### Cited Findings
Heritage:
- Dated captions: Tiptree ("Making quality preserves since 1885" / "Farming in Essex since 1757"); Comvita ("Beekeeping Since 1974" with an archival storefront photo); Hédène's top bar ("L'Excellence du miel Français depuis 2013"); Famille Mary ("Maison familiale Française depuis 1921"); Fortnum ("EST 1707"); Beechworth ("For 140 years, Beechworth Honey family beekeepers…") — [tiptree.com](https://www.tiptree.com/), [comvita.com](https://comvita.com/), [hedene.fr](https://hedene.fr/fr/), [famillemary.fr](https://www.famillemary.fr/), [eu.fortnumandmason.com](https://eu.fortnumandmason.com/), [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Founder and family portraits: Manukora "Meet Jim" and "Where it all began" — [manukora.com](https://manukora.com/), [About](https://manukora.com/pages/aboutmanukora); Mieli Thun's black-and-white portrait of Andrea Paternoster and a full-bleed beekeeper photo — [Chi](https://www.mielithun.it/chi/); Brightland's founder story with signature — [brightland.co](https://brightland.co/)
- Archival timelines: Mariage Frères (dated chapters with archival photos, ending with the tea museum) — [History](https://www.mariagefreres.com/en/history); Tiptree's long-form history with archival images — [Our History](https://www.tiptree.com/blogs/about-us/our-history)
- Crests in the header: Tiptree's royal-warrant crest; Fortnum's warrants; Mariage Frères' seal logo — [tiptree.com](https://www.tiptree.com/), [eu.fortnumandmason.com](https://eu.fortnumandmason.com/), [mariagefreres.com](https://www.mariagefreres.com/en/)

Quality marks, awards, press:
- Comvita: three-icon trust row under the hero (Certified UMF Quality, Backed by Nature & Science, Certified B Corp) and a review count — [comvita.com](https://comvita.com/)
- Daylesford: a quiet credentials trio near the footer (Soil Association, Green Michelin Star, B Corp) — [daylesford.com](https://www.daylesford.com/)
- Beechworth: a row of small round badges above the shop grid and an "AWARDS" footer link — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/)
- Pump Street: "DISCOVER OUR AWARD WINNING BARS" as a section title — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- Brightland: press-logo strip and an "OPRAH'S FAVORITE THINGS" badge — [brightland.co](https://brightland.co/)
- Flamingo: an editor quote — [flamingoestate.com](https://flamingoestate.com/)
- Local Hive: "As featured in:" press slider — [localhivehoney.com](https://localhivehoney.com/)
- Manukora: "25,000+ Verified 5-Star Reviews" in the hero — [manukora.com](https://manukora.com/)

Visits and experiences:
- Beechworth: "Visit Us" in the main nav; a homepage block in deep green; an experiences page with three cards and booking/enquiry buttons; separate shop pages — [beechworthhoney.com.au](https://www.beechworthhoney.com.au/), [Experiences](https://www.beechworthhoney.com.au/visit-us/experiences/)
- Miels d'Anicet: nav items "Boutique at the farm", "Pollens & Nectars Canteen" and "Restaurant"; an activities page with an accordion of on-site activities, photo/text blocks ("Visite immersive", "L'Essaim", "Buvette au champ") and an FAQ — [mielsdanicet.com](https://mielsdanicet.com/en-ca/), [Activités](https://mielsdanicet.com/fr-ca/contact/activites-sur-le-site/)
- Daylesford: VISIT / EAT / STAY as top-level nav, plus an "UPCOMING EVENTS" section — [daylesford.com](https://www.daylesford.com/)
- Tiptree: "TIPTREE TEA ROOMS" with a map tile and seven location cards — [tiptree.com](https://www.tiptree.com/)
- Mariage Frères: restaurants and "Tea Club Ateliers" on the homepage; a tea-museum chapter; workshops sold as products — [mariagefreres.com](https://www.mariagefreres.com/en/), [Experiences](https://www.mariagefreres.com/en/gifts/experiences.html)
- Mieli Thun: the shop as "tempio della degustazione" on the story page — [Chi](https://www.mielithun.it/chi/)
- Pump Street: "FIND US IN SUFFOLK" in the hero and a bakery "Visit us" block — [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu)
- The Bee Charmer: a store map with "GET DIRECTIONS" — [shopbeecharmer.com](https://shopbeecharmer.com/)
- Bermondsey Street Bees: corporate events, workshops, talks and honey-sommelier services — [Experiences page](https://bermondseystreetbees.co.uk/corporate-events-experiences-workshops-talks/)
- Savannah Bee: stores with honey and mead tasting bars (16 stores in 2026) — [Newswire](https://www.newswire.com/news/savannah-bee-company-opens-new-store-in-nashville-22646207)

### Inferences
- **Heritage, in the references' format:**
  - A small "od 1982" / "since 1982" caption near the crest or in the hero, as Tiptree and Comvita do.
  - A family portrait section in the manner of "Meet Jim".
  - A dated photo timeline (1982 to today, 700 colonies) like Mariage Frères or Tiptree.
- **Apitourism and apitherapy, Beechworth / Miels d'Anicet style:**
  - A top-level "Obisk" / "Visit" nav item.
  - An experiences page with cards per offer (painted beehouse visit, apitherapy session, tasting): photo, duration, price or "on request", booking or enquiry button.
  - A map and an FAQ.
  - On the homepage, the visit block is the natural candidate for the one dark or tinted band, as Beechworth's deep-green "Visit Us" shows.
- **Awards:** a single slim credentials row, as Comvita and Daylesford do, rather than scattered medals.

### Gaps
- Booking mechanics (third-party tools, calendars) behind the experience cards were not examined.
- Comvita's visitor centre exists but was not visible on the pages captured; its web presentation is unknown.
- Hilltop's web presentation of awards could not be checked (site unreachable).

## 6. What makes a small producer's site feel premium rather than generic theme-like?

### Takeaway
A standard theme is not the problem: Manukora (Horizon), Flamingo (Prestige), Brightland (Impact), Tiptree (Symmetry) and Pump Street (Turbo) all run stock Shopify themes. What separates them from template-looking honey shops:
- Restraint: few colours, one dark area, few promotions.
- One distinctive display typeface.
- A consistent plate and photo system.
- Editorial copy and naming.
- One or two bespoke details, such as a big wordmark footer, inline image chips, illustrations, a word ticker or an ornament divider.

### Cited Findings
- Shopify themes observed: Manukora (Horizon 2.1.5), Flamingo (Prestige 8.3.0), Brightland (Impact 6.6.0), Tiptree (Symmetry 7.1.2), Pump Street (Turbo 9.0.0), Local Hive (Envy), The Bee Charmer (Flow), Beekeeper's Naturals (Focal), Honey Mama's (Dawn). Savannah Bee and Comvita run custom themes — [manukora.com](https://manukora.com/), [flamingoestate.com](https://flamingoestate.com/), [brightland.co](https://brightland.co/), [tiptree.com](https://www.tiptree.com/), [pumpstreetchocolate.com](https://pumpstreetchocolate.com/en-eu), [localhivehoney.com](https://localhivehoney.com/), [shopbeecharmer.com](https://shopbeecharmer.com/), [savannahbee.com](https://savannahbee.com/), [comvita.com](https://comvita.com/)
- Bespoke details:
  - Manukora: giant wordmark footer; round image chips inside a sentence — [manukora.com](https://manukora.com/)
  - Mieli Thun: hand-drawn line illustrations; word ticker; dictionary — [mielithun.it](https://www.mielithun.it/), [Chi](https://www.mielithun.it/chi/)
  - Mariage Frères: ornamental flourish dividers; engraved caps — [mariagefreres.com](https://www.mariagefreres.com/en/)
  - Flamingo: poetic section titles — [flamingoestate.com](https://flamingoestate.com/)
  - Bermondsey Street Bees: black-and-white botanical line art — [Experiences page](https://bermondseystreetbees.co.uk/corporate-events-experiences-workshops-talks/)
  - Tiptree: crest and dated captions in the header area — [tiptree.com](https://www.tiptree.com/)
- Generic signals on otherwise premium producers:
  - Famille Mary: promo carousel and discount tabs (Promotions, "-20%") — [famillemary.fr](https://www.famillemary.fr/)
  - Hédène: −20% promo band, −15% newsletter offer, reassurance icon row, uppercase bold headings throughout, and long SEO text blocks on the range page — [hedene.fr](https://hedene.fr/fr/), [Miels](https://hedene.fr/fr/3-miels)
- Retailer and press credibility is shown compactly: Brightland's press-logo strip, Local Hive's retailer and press logos — [brightland.co](https://brightland.co/), [localhivehoney.com](https://localhivehoney.com/)

### Inferences
Practical moves for the Šemen theme, derived from the patterns above:
1. **Colour budget:** cream base; one tint band (pale honey, sage or blush); terracotta only on calls to action; espresso only for text and/or the footer. The current several full-width #2b2420 sections are the clearest "heavy" signal.
2. **Type:** a serif (or high-contrast display) at regular weight for H1/H2; the grotesque reduced to small tracked labels and buttons; Poppins kept for body.
3. **Product system:** one plate style (warm grey, cream or per-variety tint) and one corner radius across all cards; the 250g white-label jars on plates; dark-wood 900g shots kept for hero and story imagery.
4. **Editorial devices:**
   - a variety guide (dictionary or tasting notes);
   - a seasonal selection;
   - a dated heritage caption ("since 1982") near the gold crest, a family portrait and a photo timeline;
   - a "Visit" experiences page with cards for the painted beehouse in Melinci and apitherapy.
5. **One or two signature details** instead of many sections: the crest's honeycomb band as a thin divider (as Mariage Frères uses ornaments), or a large "Šemen" wordmark in a light footer (as Manukora does).
6. **Fewer promotional elements:** avoid discount carousels and icon rows that make heritage producers look generic (Famille Mary, Hédène).

### Gaps
- Performance, accessibility and mobile behaviour were not compared; the assessment is visual and at desktop width only.
- Whether these patterns convert better (sales impact) was not researched; no source in this pass measured it.
