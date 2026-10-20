# Elegant, light colour and typography system for Čebelarstvo Šemen (palette and type tokens)

## 1. What light, elegant palettes suit honey and premium food in 2025–2026, and should any dark colour stay?

### Takeaway
The 2026 forecasts lead with a soft white (Pantone Cloud Dancer, 11-4201) and warm naturals: khaki, brown, rich gold, amber and deep teal. A heritage honey brand that wants lightness is better served by an ivory/white base, one pale tint band, gold kept for ornament, and at most one deep anchor colour (best kept to the footer) than by repeated espresso-brown bands. The anchor should preferably be deep linden green or ink blue rather than brown, or there can be no dark band at all.

### Cited Findings
- Pantone's Colour of the Year 2026 is Cloud Dancer, PANTONE 11-4201, a white described as "billowy, balanced". The article is by Bill McCool, dated 4 Dec 2025. The rest of the article (any packaging commentary) is paywalled — [The Dieline](https://thedieline.com/pantones-2026-color-of-the-year-is-cloud-dancer-its-white)
- Cloud Dancer was announced on 4 Dec 2025 as "a billowy, balanced white imbued with a feeling of serenity", replacing 2025's Mocha Mousse (a brown) — [NBC News](https://www.nbcnews.com/pop-culture/pop-culture-news/pantone-names-2026-color-year-rcna247366) (search-result summary; page not opened)
- Wallpaper*, "7 colours that will define 2026" (Kelly Allen, 26 Dec 2025), names seven colours. No hex codes are given — [Wallpaper*](https://www.wallpaper.com/design-interiors/colour-trends-2026)
  - Chocolate brown: a 1stDibs survey found brown is "the top colour designers anticipate embracing in 2026", and Benjamin Moore's 2026 colour Silhouette is "a charcoal-infused espresso".
  - Burgundy.
  - Deep teal: WGSN's Colour of 2026 is "Transformative Teal".
  - Glacier blue.
  - Rich "curried" gold.
  - Classic khaki: Sherwin-Williams' 2026 colour is "Universal Khaki".
  - Pillowy white: Cloud Dancer.
- The WGSN × Coloro Spring/Summer 2026 key colours are Transformative Teal (Colour of the Year 2026), Electric Fuchsia, Blue Aura, Amber Haze (an "amber yellow") and Jelly Mint — [FashionUnited](https://fashionunited.uk/news/fashion/these-are-the-colors-for-ss26-according-to-wgsn/2024062076206) (search-result summary of a 2024 article; page not opened; Coloro codes not verified)
- Butter yellow, 2025: WGSN data cited by Glossy says global searches for "butter yellow" grew 324% year on year between Feb and May 2025, and soft yellows "spread to all kinds of foodstuffs by the summer" — [Glossy](https://www.glossy.co/beauty/from-butter-to-banana-how-yellow-took-over-2025/) (search-result summary)
- Butter yellow, 2026: butter yellow now "feel[s] distinctly mainstream", and luxury brands are moving to a bolder primary yellow for SS26 — [CORQ](https://corq.studio/insights/trend-board-luxury-brands-and-tastemakers-are-moving-from-butter-to-primary-yellow-for-spring-summer-2026/) (search-result summary)
- I computed contrast for the current Šemen palette with the WCAG 2.2 relative-luminance formula ([Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)):
  - Gold #C3935B: 2.74:1 on white, 2.48:1 on cream #F7F3EA.
  - Gold #C99A5C: 2.54:1 on white, 2.29:1 on cream.
  - Both golds pass only on espresso #2B2420 (5.55:1 and 6.00:1).
  - White on the terracotta #BB5237 button: 4.79:1 (AA).
  - Terracotta as text: 4.33:1 on cream (fails AA normal) and 4.48:1 on an ivory #FAF7F0 (fails AA normal).
  - Body #222222 on cream: 14.36:1.
- The project's standing preferences say: "few dark #2b2420 sections, never several in a row; new sections white/cream" and "never use stroke-only/unfilled text; always solid fill" — [project memory](C:/Users/Uporabnik/.claude/projects/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/memory/MEMORY.md)

### Inferences
- **Base direction.** With Cloud Dancer and a general move to restraint, a warm ivory or white base reads as current and premium, not plain.
  - The jar labels (cream/white with gold) already speak this language. The site should look like the label: an ivory field, gold used only as engraving-like ornament (crest, hairline rules, icons, dividers), and dark ink for text.
  - Good base and tint names and values:
    - ivory #FAF7F0
    - parchment #F8F4EB (almost the current cream #F7F3EA, so it carries continuity)
    - paper white #FFFDF8
    - oat #EEE5D4
    - wheat #F3EBDA
    - acacia/butter wash #F6EDD3
    - linden mist #EDF0E3 (a pale, slightly green tint)
- **Tint band.** Use exactly one tint band per page, for example on the honey-varieties or apitourism section.
  - A slightly cool linden-green tint makes amber honey photography stand out by complementary contrast.
  - A honey-yellow tint (acacia/butter) ties in with the 2025 butter-yellow and SS26 Amber Haze trends. The risk is monotony: amber jars on a yellow band. It also makes a gold button almost invisible (1.80:1 against #F6EDD3, see section 6, system C).
  - Butter yellow is already "mainstream", so keep it pale and use it once.
- **Dark colour.** Keep at most one dark band, the footer, where it closes the page without interrupting it.
  - Charcoal, deep linden green or ink blue all read lighter in mood than espresso brown, because they do not merge with the honey colours and do not suggest coffee or chocolate.
  - Brown stays fashionable (Mocha Mousse, Silhouette, chocolate). It can survive as a warm near-black ink for text (#252320 or #2A2019) instead of as full-bleed bands.
  - No full-width dark section mid-page. Dark appears as type, buttons and small cards only.
- **Accent hues next to honey gold** (my assessment):
  - Deep linden/olive green (#3E5234): botanical (meadow, linden, forest), heraldically classic with gold ("or on vert"), not dated. It is the best primary CTA colour.
  - Sage (#9AA58A family): good only as a pale tint. As a mid tone it reads 2020–2022, and as text it needs darkening to olive anyway.
  - Ink blue (#2A3F5E): heraldic azure with gold, formal and timeless, slightly cooler and less "food".
  - Deep teal (#1E4245): matches WGSN's Transformative Teal 2026. On-trend, but more likely to date quickly. It passes 10.93:1 with white text and 9.96:1 on parchment.
  - Plum or burgundy: luxurious, but drifts toward wine and cosmetics. Use only as a tiny accent, if at all.
  - Terracotta (current): its hue sits close to amber honey, so it competes with the product. Combined with espresso and gold it reads rustic rather than elegant. Retire it as the CTA colour.

### Gaps
- I did not retrieve The Dieline's own 2026 packaging trend report: the only Dieline page reached was the paywalled Pantone article. No WGSN primary page was retrieved either.
- I found no reliable public brand guidelines for premium food brands that give hex palettes.
- Trend sources for Amber Haze and butter yellow are search-result summaries of secondary articles, not opened pages.

## 2. Which honey-gold shades work as text or button colours on light backgrounds while passing contrast, and which only as decoration?

### Takeaway
On white, ivory or cream, every gold lighter than about #9A6824 fails 4.5:1. The current golds #C3935B and #C99A5C manage only 2.2–2.7:1, so they are decoration only. They do work as a button fill under dark ink text (5.70–6.16:1).
- For gold-looking small text, use "old gold" #8A6428 (4.61–5.33:1 on every proposed light base) or darker.
- For white text on a honey-coloured fill, the fill must be #9A6824 (4.79:1) or darker.

### Cited Findings
- **WCAG thresholds.** AA requires 4.5:1 for normal text and 3:1 for large text. AAA requires 7:1 and 4.5:1. "18 point text or 14 point bold text is judged to be large enough to require a lower contrast ratio", and 14pt and 18pt "are equivalent to approximately 18.5px and 24px" — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- **No rounding.** "the computed values should not be rounded (e.g., 4.499:1 would not meet the 4.5:1 threshold)" — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- **Thin fonts.** "particularly thin or unusual fonts may be rendered by user agents with a much fainter color" — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- **Logos exempt.** "Text that is part of a logo or brand name has no contrast requirement", so the gold crest itself can stay gold — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- **Luminance threshold.** The relative-luminance threshold is 0.04045. "Before May 2021 the value of 0.04045 in the definition was different (0.03928)", which "has no practical effect" — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [WCAG 2.2 definition](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)
- **Non-text contrast (1.4.11).** "a border or other indication of the overall boundary of the hit area is not required", so a labelled button needs no 3:1 fill-to-page contrast. However, "the visual focus indicator for a component must have sufficient contrast against the adjacent background", and inactive (disabled) components "are not required to meet contrast requirements" — [W3C Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- **Honey-gold ladder.** These are illustrative shades I chose, not measured honey colours. Ratios were computed with the WCAG 2.2 formula ([WCAG 2.2](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)) and floored to two decimals.

| Shade | Hex | vs #FFFFFF | vs ivory #FAF7F0 | vs cream #F7F3EA | vs linden tint #EDF0E3 | White text on it | Ink #252320 text on it | Verdict on light backgrounds |
|---|---|---|---|---|---|---|---|---|
| Acacia pale | #F3E7BF | 1.23 | 1.15 | 1.11 | 1.06 | 1.23 | 12.68 | Decoration / tint only; fine as fill under dark text |
| Butter | #EBD798 | 1.42 | 1.33 | 1.28 | 1.23 | 1.42 | 10.97 | Decoration; fill under dark text |
| Light honey | #E2C06F | 1.74 | 1.63 | 1.57 | 1.51 | 1.74 | 8.95 | Decoration; fill under dark text (AAA) |
| Wildflower gold | #D4A44C | 2.27 | 2.13 | 2.05 | 1.97 | 2.27 | 6.87 | Decoration; fill under dark text |
| Current gold 2 | #C99A5C | 2.54 | 2.37 | 2.29 | 2.20 | 2.54 | 6.16 | Decoration; fill under dark text |
| Current gold 1 | #C3935B | 2.74 | 2.56 | 2.48 | 2.37 | 2.74 | 5.70 | Decoration; fill under dark text |
| Amber | #B07A2E | 3.70 | 3.46 | 3.34 | 3.20 | 3.70 | 4.23 | Large text (24px+ / 18.5px+ bold), icons, focus rings only |
| Deep amber | #9A6824 | 4.79 | 4.48 | 4.32 | 4.14 | 4.79 | 3.26 | AA text on pure white only; large/UI on ivory/cream. Fill under white text passes AA |
| Old gold / bronze | #8A6428 | 5.33 | 4.98 | 4.82 | 4.61 | 5.33 | 2.93 | AA body text on all light bases |
| Bronze dark | #845D26 | 5.87 | 5.49 | 5.30 | 5.08 | 5.87 | 2.66 | AA body text |
| Chestnut | #8A5A1C | 5.89 | 5.51 | 5.32 | 5.10 | 5.89 | 2.65 | AA body text (redder) |
| Dark chestnut | #6F4518 | 8.26 | 7.72 | 7.46 | 7.15 | 8.26 | 1.89 | AAA text |
| Forest-honey brown | #4F3318 | 11.54 | 10.78 | 10.42 | 9.99 | 11.54 | 1.35 | AAA text |
| Buckwheat | #33231A | 15.04 | 14.05 | 13.58 | 13.01 | 15.04 | 1.04 | AAA text / ink |

### Inferences
- Use three gold roles:
  1. Ornament gold #C99A5C. Keep the brand gold for the crest, hairlines, icons, stars and dividers. #C3935B and #C99A5C are near-duplicates, so consolidate on one.
  2. Text gold #8A6428 or #845D26, for eyebrows and labels in "gold".
  3. Honey fill, #C99A5C or #D4A44C under ink text, for a secondary button or badges.
- Never set white text on the current golds (2.54–2.74:1).
- Never set gold headings on light backgrounds, even large ones: #C99A5C fails even the 3:1 large-text bar.
  - Amber #B07A2E passes 3:1 for headings of 24px and up (3.46:1 on ivory).
  - Combined with a hairline serif such as Cormorant Light, the W3C warning about faint thin strokes applies, so avoid it.
- A gold-filled button on a light page fails 3:1 fill-to-page (2.2–2.5:1). That is permitted, because the label identifies the button. Still, use it as a secondary action and keep the dark or green primary button for the main CTA. Optionally add a 1px bronze #8A6428 border for definition.

### Gaps
- I did not compute APCA (the WCAG 3 draft method). Light-on-dark footers can feel different under APCA than the WCAG 2.2 ratios suggest.
- I found no source mapping real honey colours (for example the Pfund scale) to sRGB hex values, so the ladder is illustrative.

## 3. Which OFL fonts are best: Latin Extended coverage (č š ž), variable versions, weights, woff2 size, and availability in Shopify's font library?

### Takeaway
Every candidate except Italiana covers Slovenian. Italiana lacks Č č Š š Ž ž Ć ć Đ đ and €, so it is excluded.
- **Display.** Cormorant (Christian Thalmann) is the strongest elegant display face. It is in Shopify's library with weights 300–700 and italics, variable for self-hosting, and has true small caps in the full font. Fraunces (soft and warm), Playfair 2.0 (refined Didone-leaning) and EB Garamond (bookish, small caps) are the alternatives.
- **Text.** Jost and Figtree are the lightest and cleanest. Work Sans is the most feature-rich.
- **Not in Shopify's library:** Cormorant Garamond, Cormorant SC, Marcellus SC, Libre Caslon Display, Italiana, Bellefair, Mulish and Hanken Grotesk.
- **Theme warning.** The current heading font, Zurich Extended, is on Shopify's deprecated list (replacement: Epilogue), so the heading font has to change anyway.

### Cited Findings
- **Method.** For each family:
  - Glyphs and OpenType features were checked with fontTools 4.65 on the regular TTF from the google/fonts repo. Characters tested: Č č Š š Ž ž Ć ć Đ đ „ " " ‚ ' ' – — … €.
  - Subsets, axes and licence come from each family's METADATA.pb.
  - woff2 sizes are the files the Google Fonts css2 API served to a Chrome user agent on 2026-10-20, for the "latin" and "latin-ext" subsets.
  - Weights and variable flags come from the Fontsource API.
  - Shopify handles come from the [Shopify fonts doc (markdown)](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts.md).
  - All families are licensed OFL (METADATA `license: "OFL"`; Fontsource `OFL-1.1`).

**Display / serif candidates**

| Family (METADATA source) | Fontsource | Slovenian glyphs (cmap) | Variable axes | Weights / italic | woff2 KB per static weight (latin + latin-ext) | woff2 KB variable roman (latin + latin-ext) | Shopify library | OT features in full repo TTF | x-height / UPM |
|---|---|---|---|---|---|---|---|---|---|
| [Cormorant](https://github.com/google/fonts/blob/main/ofl/cormorant/METADATA.pb) | [link](https://fontsource.org/fonts/cormorant) | yes | wght 300–700 | 300–700 + italics | 21.9 + 19.1 = 41.0 | 34.5 + 29.6 = 64.1 | **yes**: cormorant_n3–n7, i3–i7 | smcp, c2sc, onum, lnum, tnum, dlig, ss01, ss02, frac, case | 0.386 |
| [Cormorant Garamond](https://github.com/google/fonts/blob/main/ofl/cormorantgaramond/METADATA.pb) | [link](https://fontsource.org/fonts/cormorant-garamond) | yes | wght 300–700 | 300–700 + italics | 22.3 + 19.4 = 41.7 | 36.8 + 32.9 = 69.7 | no | smcp, c2sc, onum, lnum, tnum, dlig, ss01 | 0.386 |
| [Cormorant SC](https://github.com/google/fonts/blob/main/ofl/cormorantsc/METADATA.pb) | [link](https://fontsource.org/fonts/cormorant-sc) | yes | static | 300–700, no italic | 20.4 + 18.8 = 39.2 | – | no | smcp, lnum, tnum | 0.386 |
| [Fraunces](https://github.com/google/fonts/blob/main/ofl/fraunces/METADATA.pb) (Undercase Type) | [link](https://fontsource.org/fonts/fraunces) | yes | SOFT 0–100, WONK 0–1, opsz 9–144, wght 100–900 | 100–900 + italics | 17.5 + 16.9 = 34.4 | 35.8 + 32.8 = 68.6 (wght axis only) | **yes**: fraunces_n1–n9, i1–i9 | liga, case, ss01 (no smcp, no onum) | 0.482 |
| [Playfair Display](https://github.com/google/fonts/blob/main/ofl/playfairdisplay/METADATA.pb) | [link](https://fontsource.org/fonts/playfair-display) | yes | wght 400–900 | 400–900 + italics | 21.3 + 12.0 = 33.3 | 37.5 + 20.6 = 58.1 | **yes**: playfair_display_n4–n9, i4–i9 | smcp, c2sc, onum, lnum, dlig | 0.514 |
| [Playfair (2.0, added 2023)](https://github.com/google/fonts/blob/main/ofl/playfair/METADATA.pb) | [link](https://fontsource.org/fonts/playfair) | yes | opsz 5–1200, wdth 87–112, wght 300–900 | 300–900 + italics | 30.8 + 33.3 = 64.1 | 54.6 + 57.3 = 111.9 | **yes**: playfair_n3–n9, i3–i9 | smcp, c2sc, onum, lnum, pnum, tnum, dlig | 0.413 |
| [Bodoni Moda](https://github.com/google/fonts/blob/main/ofl/bodonimoda/METADATA.pb) | [link](https://fontsource.org/fonts/bodoni-moda) | yes | opsz 6–96, wght 400–900 | 400–900 + italics | 14.2 + 8.2 = 22.4 | 25.3 + 13.8 = 39.1 | **yes**: bodoni_moda_n4–n9, i4–i9 | smcp, c2sc, onum, lnum, pnum, tnum, dlig, ss01, ss02 | 0.460 |
| [Gilda Display](https://github.com/google/fonts/blob/main/ofl/gildadisplay/METADATA.pb) | [link](https://fontsource.org/fonts/gilda-display) | yes | static | 400 only, no italic | 19.7 + 13.2 = 32.9 | – | **yes**: gilda_display_n4 | dlig, case | 0.473 |
| [Marcellus](https://github.com/google/fonts/blob/main/ofl/marcellus/METADATA.pb) | [link](https://fontsource.org/fonts/marcellus) | yes | static | 400 only | 14.2 + 8.7 = 22.9 | – | **yes**: marcellus_n4 | liga, frac | 0.500 |
| [Marcellus SC](https://github.com/google/fonts/blob/main/ofl/marcellussc/METADATA.pb) | [link](https://fontsource.org/fonts/marcellus-sc) | yes | static | 400 only | 14.2 + 8.7 = 22.9 | – | no | liga, frac | 0.525 |
| [EB Garamond](https://github.com/google/fonts/blob/main/ofl/ebgaramond/METADATA.pb) | [link](https://fontsource.org/fonts/eb-garamond) | yes | wght 400–800 | 400–800 + italics | 23.3 + 55.6 = 78.9 | 43.3 + 111.3 = 154.6 | **yes**: ebgaramond_n4–n8, i4–i8 | smcp, c2sc, onum, lnum, pnum, tnum, dlig, swsh, ss01, ss02 | 0.400 |
| [Libre Caslon Display](https://github.com/google/fonts/blob/main/ofl/librecaslondisplay/METADATA.pb) | [link](https://fontsource.org/fonts/libre-caslon-display) | yes | static | 400 only | 23.7 + 15.9 = 39.6 | – | no | dlig, onum, ss01 | 0.424 |
| [Libre Caslon Text](https://github.com/google/fonts/blob/main/ofl/librecaslontext/METADATA.pb) | [link](https://fontsource.org/fonts/libre-caslon-text) | yes | repo shows wght 400–700 (v2.000); Fontsource and css2 served static only | 400/700 + italics | 24.4 + 14.0 = 38.4 | not served as variable on test date | **yes**: libre_caslon_text_n4–n7, i4–i7 | dlig, onum, tnum | 0.524 |
| [DM Serif Display](https://github.com/google/fonts/blob/main/ofl/dmserifdisplay/METADATA.pb) | [link](https://fontsource.org/fonts/dm-serif-display) | yes | static | 400 + italic | 24.2 + 10.6 = 34.8 | – | **yes**: dm_serif_display_n4, i4 | dlig | 0.481 |
| [Gloock](https://github.com/google/fonts/blob/main/ofl/gloock/METADATA.pb) | [link](https://fontsource.org/fonts/gloock) | yes | static | 400 only | 25.7 + 14.2 = 39.9 | – | **yes**: gloock_n4 | case, pnum, tnum | 0.508 |
| [Italiana](https://github.com/google/fonts/blob/main/ofl/italiana/METADATA.pb) | [link](https://fontsource.org/fonts/italiana) | **NO**: missing Č č Š š Ž ž Ć ć Đ đ and € (subset: latin only) | static | 400 only | 9.9 (latin only) | – | no | none | 0.500 |
| [Bellefair](https://github.com/google/fonts/blob/main/ofl/bellefair/METADATA.pb) | [link](https://fontsource.org/fonts/bellefair) | yes | static | 400 only | 16.1 + 11.1 = 27.2 | – | no | case | 0.364 |

**Text / sans candidates**

| Family (METADATA source) | Fontsource | Slovenian glyphs | Variable axes | Weights / italic | woff2 KB per static weight (latin + latin-ext) | woff2 KB variable roman | Shopify library | OT features (repo TTF) | x-height / UPM |
|---|---|---|---|---|---|---|---|---|---|
| [Jost](https://github.com/google/fonts/blob/main/ofl/jost/METADATA.pb) | [link](https://fontsource.org/fonts/jost) | yes | wght 100–900 | 100–900 + italics | 9.2 + 6.2 = 15.4 | 26.0 + 16.7 = 42.7 | **yes**: jost_n1–n9, i1–i9 | ss01, tnum | 0.460 |
| [Figtree](https://github.com/google/fonts/blob/main/ofl/figtree/METADATA.pb) | [link](https://fontsource.org/fonts/figtree) | yes | wght 300–900 | 300–900 + italics | 11.1 + 6.0 = 17.1 | 19.7 + 10.0 = 29.7 | **yes**: figtree_n3–n9, i3–i9 | tnum, pnum, ss01, ss02, case | 0.500 |
| [Work Sans](https://github.com/google/fonts/blob/main/ofl/worksans/METADATA.pb) | [link](https://fontsource.org/fonts/work-sans) | yes | wght 100–900 | 100–900 + italics | 19.4 + 14.9 = 34.3 | 49.1 + 34.9 = 84.0 | **yes**: work_sans_n1–n9, i1–i9 | smcp, c2sc, onum, lnum, tnum, ss01, ss02, salt, swsh | 0.500 |
| [Karla](https://github.com/google/fonts/blob/main/ofl/karla/METADATA.pb) | [link](https://fontsource.org/fonts/karla) | yes | wght 200–800 | 200–800 + italics | 12.8 + 6.7 = 19.5 | 31.4 + 14.9 = 46.3 | **yes**: karla_n2–n8, i2–i8 | onum, lnum, pnum, tnum | 0.478 |
| [Manrope](https://github.com/google/fonts/blob/main/ofl/manrope/METADATA.pb) | [link](https://fontsource.org/fonts/manrope) | yes | wght 200–800 | 200–800, **no italic** | 13.8 + 8.1 = 21.9 | 24.3 + 14.8 = 39.1 | **yes**: manrope_n2–n8 | pnum, tnum | 0.540 |
| [Outfit](https://github.com/google/fonts/blob/main/ofl/outfit/METADATA.pb) | [link](https://fontsource.org/fonts/outfit) | yes | wght 100–900 | 100–900, **no italic** | 13.7 + 6.2 = 19.9 | 31.5 + 14.5 = 46.0 | **yes**: outfit_n1–n9 | pnum, tnum, ss01, salt, dlig | 0.460 |
| [Mulish](https://github.com/google/fonts/blob/main/ofl/mulish/METADATA.pb) | [link](https://fontsource.org/fonts/mulish) | yes | wght 200–1000 | 200–900 + italics (Fontsource) | 13.1 + 12.8 = 25.9 | 29.3 + 26.2 = 55.5 | no | onum | 0.500 |
| [Hanken Grotesk](https://github.com/google/fonts/blob/main/ofl/hankengrotesk/METADATA.pb) | [link](https://fontsource.org/fonts/hanken-grotesk) | yes | wght 100–900 | 100–900 + italics | 13.1 + 8.8 = 21.9 | 33.9 + 19.1 = 53.0 | no | ss01, ss02, dlig | 0.493 |
| [Montserrat](https://github.com/google/fonts/blob/main/ofl/montserrat/METADATA.pb) | [link](https://fontsource.org/fonts/montserrat) | yes | wght 100–900 | 100–900 + italics | 18.3 + 31.5 = 49.8 | 37.1 + 69.0 = 106.1 | **yes**: montserrat_n1–n9 + italics | smcp, c2sc, onum, lnum, pnum, tnum | 0.517 |
| [Lato](https://github.com/google/fonts/blob/main/ofl/lato/METADATA.pb) | [link](https://fontsource.org/fonts/lato) | yes | static | Fontsource: 100/300/400/700/900 + italics (repo METADATA already lists v2.015 with 100–900) | 23.0 + 5.5 = 28.5 | – | **yes**: lato_n1–n9, i1–i9 | onum, lnum, tnum, ss01, ss02 | 0.506 |
| [Poppins](https://github.com/google/fonts/blob/main/ofl/poppins/METADATA.pb) (current body) | [link](https://fontsource.org/fonts/poppins) | yes | static | 100–900 + italics | 7.7 + 5.5 = 13.2 | – | **yes** (not deprecated) | ss01, ss02 | 0.548 |

- **Shopify library scope.** "Shopify's font library is a collection of fonts that includes system fonts and a selection of Google fonts. These fonts are free to use on all Shopify online stores, and are provided in both WOFF and WOFF2 formats."
  - "The files for each font include the following Unicode ranges, if the ranges are available for the font: Basic Latin, Latin-1 Supplement, Latin Extended-A, Currency Symbols."
  - Latin Extended-A (U+0100–017F) is the block that contains Č Š Ž Ć Đ.
  - "Personal access to the font files isn't currently available."
  - Source: [Shopify fonts doc](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts)
- **Loading Shopify fonts.** A `font_picker` setting returns a `font` object. `font_face` inserts the `@font-face`, `font_url` returns "a CDN URL", and `font_modify` reaches bold and italic variants of the same family — [Shopify fonts doc](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts.md)
- **Deprecated fonts.** Shopify's "Deprecated fonts" table lists `zurich_extended_n4 n7 n8 n9` with replacement **Epilogue**. Zurich maps to Instrument Sans, and Cooper BT to Petrona. The stated reason is "a broader move towards open-source fonts" — [Shopify fonts doc (markdown)](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts.md)
- **Automatic replacement.** Changelog of 18 Aug 2025: deprecated fonts "will be automatically replaced with fonts of a similar style", "gradually throughout August 2025", and "Merchants using deprecated fonts will see their stores updated with replacement fonts" — [Shopify changelog](https://shopify.dev/changelog/font-library-updates-automatic-replacement-for-deprecated-fonts)
- **Theme Store deadline.** The deprecation was announced in Nov 2024, with a 3 Jan 2025 deadline for Theme Store presets — [Shopify changelog](https://shopify.dev/changelog/changes-to-our-font-library) (search-result summary)
- **Local theme settings.** The local, possibly stale [config/settings_data.json](config/settings_data.json) (lines 37–40, 243) sets:
  - `font_family: "zurich_extended_n4"` (headings)
  - `font_family2: "poppins_n4"` (body)
  - `font_family3: "cooper_bt_n5"`
  - Both Google-font text fields blank.
- **Feature stripping, measured.** Served subsets lose OpenType features that the full repo font has:
  - **Google css2 API.** Cormorant 500 as served (TTF, 1,387 glyphs) has GSUB features calt, ccmp, dnom, frac, liga, lnum, locl, numr, tnum: no smcp, c2sc, onum, dlig or ss01. The full repo TTF has all of them.
  - **Fontsource woff, Cormorant.** latin-500 has the same set as the Google file; latin-ext-500 has only calt, ccmp, liga, lnum, locl.
  - **Fontsource woff, others.** EB Garamond latin-ext-500 has no GSUB at all, Fraunces latin-ext-400 only rvrn, and Jost latin-ext-500 none.
  - **Slovenian glyphs.** All of these subsets do contain Č č Š š Ž ž.
  - **Fontsource woff2 sizes:** Cormorant latin-500 22.7 KB and latin-ext-500 19.6 KB; Jost latin-ext-500 6.9 KB; EB Garamond latin-ext-500 64.1 KB; Fraunces latin-ext-400 17.3 KB.
  - Sources: measured from [Google Fonts css2](https://fonts.googleapis.com/css2?family=Cormorant:wght@500) and the [Fontsource CDN](https://cdn.jsdelivr.net/fontsource/fonts/cormorant@latest/latin-500-normal.woff) on 2026-10-20.
- **Cormorant README.** Cormorant is "a free display type family developed by Christian Thalmann", with nine styles in five weights (Roman, Italic, Infant, Garamond, Upright Cursive, Small Caps, Unicase), and the fonts are "free software under the SIL Open Font License" — [Cormorant on GitHub](https://github.com/CatharsisFonts/Cormorant)
- **Designers per METADATA.**
  - Fraunces: Undercase Type, Phaedra Charles, Flavia Zimbardi.
  - Playfair and Playfair Display: Claus Eggers Sørensen.
  - Bodoni Moda and Jost: Owen Earl.
  - EB Garamond: Georg Duffner and Octavio Pardo.
  - Figtree: Erik Kennedy.
  - Work Sans: Wei Huang.
  - Source: [google/fonts](https://github.com/google/fonts/tree/main/ofl)

### Inferences
- **Shortlist for this brand:**
  1. Cormorant (display) with Jost (text). Elegant, airy and Garamond-derived, with calligraphic italics. Both are in Shopify's library, both variable for self-hosting, and the pair is light (about 41 + 15 KB per weight).
  2. EB Garamond (display, small caps) with Work Sans (text). Bookish and printed-heritage. Heavy latin-ext (55.6 KB per weight).
  3. Fraunces (display, soft serif) with Figtree (text). The warmest and most "honey-viscous". Very widely used by food brands since 2020, so it risks looking generic. No small caps.
- **Avoid or limit:**
  - Italiana: fails Slovenian.
  - Playfair Display and Montserrat: overexposed, and Montserrat's latin-ext is heavy (31.5 KB per weight).
  - Bodoni Moda: reads fashion and cosmetics rather than food heritage.
  - DM Serif Display, Gloock and Gilda Display: a single weight with no or a limited italic; fine for headlines only.
  - Bellefair: x-height 0.364, not in Shopify.
- **Marcellus** (Shopify ✓, 22.9 KB) is a good optional third face for crest-like uppercase lockups ("OD LETA 1982", the name in the header). Its flared, engraved capitals echo the heraldic crest. Use it sparingly.
- **Cormorant sizing.** Cormorant's x-height (0.386 of the em) is about 16% smaller than Jost's (0.46). Set it at 22px or more and never for body text. This also follows from its own README calling it a display family.
- **Shopify vs self-hosting.** Via the Shopify font picker the theme gets static weight/italic instances (handles like cormorant_n5) with Latin Extended-A included. Variable axes are not controllable that way (Fraunces SOFT/WONK/opsz), and true small caps are not guaranteed. For variable fonts or smcp, self-host the full repo fonts subset with features kept (for example pyftsubset with all layout features). Do not use Google API or Fontsource subsets for this, since they strip smcp and onum.
- **Implication of the Zurich Extended deprecation.** The store may already show Epilogue instead of Zurich Extended, because of the August 2025 automatic replacement. The redesign is the moment to pick a deliberate heading face rather than inherit the auto-replacement.

### Gaps
- I could not measure Shopify CDN file sizes, or whether Shopify-served files keep smcp/onum. The storefront is password-protected (the /password page loads only ShopifySans), and Shopify font URLs are hashed and signed.
- I could not confirm whether the live store's `font_family` setting now reads `zurich_extended_n4` or `epilogue_*`. Check this in the theme editor; the local JSON may be stale.
- The difference between Cormorant and Cormorant Garamond is not described in the README text I retrieved. Measured OS/2 x-heights are identical (0.386).
- Lato and Libre Caslon Text: the google/fonts repo (main branch) is ahead of what Fontsource and the API serve. Lato v2.015 has 9 weights in the repo but 5 in Fontsource; Libre Caslon Text has a variable version in the repo but is static as served.

## 4. What is the current EU legal guidance on hotlinking Google Fonts (LG München I, 20 Jan 2022), and why prefer self-hosting or Shopify's font CDN?

### Takeaway
LG München I (20 Jan 2022, 3 O 17493/20) held that loading Google Fonts from Google's servers without consent unlawfully transmits the visitor's IP address. The legitimate-interest defence failed because self-hosting is an equally effective, milder alternative. The court awarded €100 non-material damages and an injunction.
- Later German and Austrian rulings rejected mass, crawler-generated warning-letter claims as abusive. They did not declare hotlinking lawful.
- The EU–US Data Privacy Framework (2023, upheld by the General Court in Sept 2025) weakens the "unsafe third country" argument, but not the necessity argument.
- Practical guidance: do not hotlink. Use Shopify's font library (served by Shopify) or self-hosted files, and keep the theme's "Google font" fields empty.

### Cited Findings
- **LG München I, 20.01.2022, Az. 3 O 17493/20.**
  - Dynamically embedding Google Fonts without consent is unlawful.
  - Transferring the IP address to Google without consent violated the visitor's right to informational self-determination.
  - The plaintiff received €100 non-material damages, the injunction was granted, and a fine of up to €250,000 was threatened for repeat violations.
  - Source: [IHK Bergisch](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176) (search-result summary)
- **The reasoning, per a commentary dated 7 Feb 2022:**
  - The dynamic IP is personal data (Art. 4(1) GDPR; CJEU/BGH case law).
  - The interest in attractive fonts is legitimate, but the transfer was not necessary because the fonts can be hosted locally: "Bei dieser Variante kann die Verbindung zu Google gekappt werden."
  - No consent or Art. 13 information was given.
  - The loss of control was a compensable harm under Art. 82 GDPR.
  - The US was treated as a third country without an adequacy decision.
  - Source: [Dr. Datenschutz](https://www.dr-datenschutz.de/schadensersatz-urteil-google-fonts-und-die-dsgvo/)
- **Warning-letter wave.** Private persons and law firms then relied on the ruling for mass warning letters — [LfD Niedersachsen](https://lfd.niedersachsen.de/download/190184) (search-result summary)
- **Self-hosting as the fix.** Hosting font files locally (the "static" embedding) avoids contacting Google on page load — [Universität Regensburg](https://www.uni-regensburg.de/universitaet/aktuelles/nachrichten/nachricht/04-04-2022_dynamische-einbindung-von-google-fonts-ohne-einwilligung-verstoesst-gegen-dsgvo) (search-result summary)
- **LG München I, 2023** (dated 30.03.2023 per Lexware, reported 05.05.2023). Automated crawling for Google Fonts "violations" gave no claim to an injunction or damages. Provoking an infringement deliberately to base claims on it is contradictory, and the GDPR is not meant to be a source of income. LG Baden-Baden is also reported to have found the warning letters abusive — [Der Betrieb](https://der-betrieb.de/meldungen/google-fonts-abmahnwelle-war-rechtsmissbraeuchlich), [Lexware](https://www.lexware.de/wissen/unternehmensfuehrung/abmahnung-wegen-google-fonts/) (search-result summaries)
- **Austria.**
  - Over 30,000 letters were sent in 2022, each demanding €100 damages plus €90 fees.
  - BG Favoriten, confirmed by LG Wien on appeal, found the conduct "rechtsmissbräuchlich". The ruling is "nicht rechtskräftig", and a revision to the OGH was announced with a suggestion of a CJEU preliminary reference. Article of 10 June 2024 — [futurezone](https://futurezone.at/netzpolitik/google-fonts-abmahnungen-klage-gerichtsurteil-missbraeuchlich-berufungsgericht/402911253)
  - A later test case before the Landesgericht für Zivilrechtssachen Wien again found systematic profit-driven warning letters abusive, not final — [WKO](https://www.wko.at/noe/n-news/klares-signal-gegen-abmahnmissbrauch-in-causa-google-fonts) (search-result summary)
- **Data Privacy Framework.** The Commission adopted the EU–US DPF adequacy decision (Implementing Decision (EU) 2023/1795) on 10 July 2023. The General Court dismissed Latombe's annulment action (T-553/23) on 3 Sept 2025, and the decision can be appealed — [Hunton](https://www.hunton.com/privacy-and-information-security-law/eus-general-court-confirms-adequacy-of-eu-u-s-data-privacy-framework) (search-result summary)
- **Shopify library fonts.** These are loaded through Liquid filters that return Shopify CDN URLs (`font_url` "to access a CDN URL"), and the files themselves are not handed out ("Personal access to the font files isn't currently available") — [Shopify fonts doc](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts.md)
- **Theme code (Molding).** The theme has free-text "Google font" settings (`font_family_google`, `font_family2_google`) — [config/settings_schema.json](config/settings_schema.json) lines 283–310 (`font_family` 283, `font_family_google` 289, `font_family2` 304, `font_family2_google` 310).
  - If one is filled in, the theme emits `@import url('https://fonts.googleapis.com/css?family=…')` instead of the Shopify `font_face` — [snippets/header-css.liquid](snippets/header-css.liquid) lines 70, 100, 125.
  - The gift card template does the same — [templates/gift_card.liquid](templates/gift_card.liquid) lines 48, 74, 94.
  - Locally both fields are blank, so the theme currently uses Shopify-hosted fonts — [config/settings_data.json](config/settings_data.json) lines 38, 40 (possibly stale).

### Inferences
- **Status for an EU (Slovenian) shop.** The 2022 Munich reasoning has not been overturned. The later rulings only deny abusive, mass-generated claims; they do not legitimise hotlinking.
  - The DPF covers the Chapter V transfer question for DPF-certified recipients, but Art. 6(1)(f) still requires the transfer to be necessary. Self-hosting remains a "milder means", so the core argument against hotlinking without consent stands.
  - The GDPR applies the same way in Slovenia. A German regional court decision is persuasive, not binding.
- **Why the Shopify font CDN is the preferred route here:**
  - The visitor's browser contacts only Shopify, which already hosts and processes the store, so there is no additional third-party recipient.
  - The merchant can switch fonts in the theme editor.
  - Latin Extended-A is included.
  - No consent banner entry is needed for fonts.
- **Trade-offs of the Shopify CDN:** no variable axes, OpenType feature retention unknown, and Shopify can deprecate a font (as with Zurich Extended) and swap it automatically.
- **When to self-host instead** (theme `assets/` with `asset_url`, per Shopify's "Host fonts in your theme" section): when variable fonts, small caps (smcp) or a face missing from the library (Cormorant Garamond, Cormorant SC) are needed.
- **Action:** keep the theme's "Google font" text fields empty, including for any future font changes.

### Gaps
- I could not retrieve the full judgment text, or Google's current Fonts privacy FAQ (fonts.google.com/faq is JS-rendered).
- I did not check whether any appeal of Latombe was lodged, or the OGH outcome in Austria.
- I found no specific guidance on Google Fonts from the Slovenian DPA (Informacijski pooblaščenec); I did not search for it in depth.
- CJEU case law on Art. 82 thresholds was not verified in this session.

## 5. How should uppercase letterspaced labels, small caps and serif display be combined so it feels elegant and not generic?

### Takeaway
Give each typographic device one job:
- Mixed-case serif display for headings, with italic for emphasis.
- One uppercase sans label style (small size, medium weight, wide tracking).
- True small caps only where the font really has them.

Keep gold for ornament and use text-safe bronze for labels. Avoid the generic pattern of an uppercase eyebrow over every section, all-caps wide grotesque headings (the current heavy look), faux small caps, light-weight hairline type in low-contrast colours, and outline text.

### Cited Findings
- Cormorant is described by its designer as "a free display type family", and its subsets include Small Caps and Unicase styles — [Cormorant on GitHub](https://github.com/CatharsisFonts/Cormorant)
- Measured x-heights (OS/2 sxHeight / UPM): Cormorant 0.386, EB Garamond 0.400, Playfair 2.0 0.413, Fraunces 0.482; Jost 0.460, Figtree 0.500, Work Sans 0.500 — fontTools on the [google/fonts](https://github.com/google/fonts/tree/main/ofl) TTFs.
- True small caps (smcp, c2sc) and old-style figures (onum) exist in the full Cormorant, EB Garamond, Playfair, Bodoni Moda and Work Sans files. They are stripped from the Google css2 API and Fontsource subsets; Fraunces has no smcp at all — measured, see section 3.
- Thin or unusual fonts "may be rendered by user agents with a much fainter color", and "Fonts with extraordinarily thin strokes … are harder to read" — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- The project rule is no stroke-only or outline text, always solid fill — [project memory](C:/Users/Uporabnik/.claude/projects/c--Users-Uporabnik-Desktop-Work-Stranke-2026-prodaja-medu-website/memory/MEMORY.md)

### Inferences
These are my design rules for implementation.
1. **Headings in mixed case serif, never all caps.**
   - Use weight 500 at 40px and up, 600 at 22–32px (Cormorant's hairlines need the extra weight at small sizes).
   - Tracking: −0.01em at display sizes, 0 below 40px.
   - Set one emphasised word or phrase per heading in the italic of the same family, for example "Med *iz naših panjev*". Do not use bold for emphasis.
2. **One uppercase role only:** eyebrow/label, navigation and buttons, all in the text sans at weight 500 (never 300).
   - Tracking scales inversely with size: 11–12px uses +0.16–0.20em; 13–14px +0.12–0.14em; 16px and up +0.08–0.10em.
   - Line-height of at least 1.3, so the carons on Č Š Ž do not collide with the line above in two-line labels.
   - Never letterspace lowercase.
3. **Eyebrows on alternate sections at most.** On the other sections, open with an ornament from the brand: a 40×1px gold hairline (#C99A5C), or a small bee or laurel glyph cut from the crest. This is what keeps the page from looking like a Shopify template.
4. **True small caps** for short heritage lines: "od leta 1982", "Družina Šemen", variety lists, dates.
   - Settings: `font-variant-caps: all-small-caps; letter-spacing: .06–.08em; font-synthesis-small-caps: none`.
   - Only with self-hosted full-feature files (Cormorant or EB Garamond from the google/fonts repo, subset with features kept).
   - With Shopify-library or API files, fall back to the uppercase sans label rather than letting the browser fake small caps.
5. **Numerals.** Prices and weights use lining tabular figures in the sans (`font-variant-numeric: lining-nums tabular-nums`; Jost has tnum). Running serif text may use onum, only where self-hosted.
6. **Colour roles in type.**
   - Labels in text-safe gold (#8A6428 on light) or muted ink. Headings in ink.
   - Brand gold only as ornament; it fails as text on light backgrounds (section 2).
   - On the dark footer, labels in #D6B077 (5.89:1). Use solid fills only.
7. **Measure and rhythm.** Body text 16–17px, line-height 1.6–1.7, max 65–72 characters per line. Generous section padding (96–128px desktop) delivers "lightness" more than any colour.
8. **Families.** Two families plus at most one accent face (Marcellus) for crest-like lockups. The display serif never goes below 22px, and labels never exceed 14px.

### Gaps
- I found no authoritative public source with numeric letterspacing rules for uppercase or small caps. The values above are conventional typographic practice, not cited standards.
- I did not verify browser hyphenation support for Slovenian (`hyphens: auto` with `lang="sl"`).

## 6. Which complete token systems should be offered, with contrast tables and typography, and which one is recommended?

### Takeaway
Three systems follow:
- **A – Lipa & slonovina (Linden & Ivory):** ivory base, pale linden tint, deep linden-green accent and footer.
- **B – Pergament & črnilo (Parchment & Ink):** parchment and oat with ink blue.
- **C – Akacija (Acacia):** all light; white with an acacia-honey tint, buckwheat ink and no dark band.

All text and button pairs pass WCAG 2.2 AA, as computed below. The recommendation is **System A with Cormorant + Jost**: it is the lightest system that still has a confident CTA colour and one grounding anchor, it keeps gold exactly as on the jar labels, and both fonts can be chosen in Shopify's theme editor.

### Cited Findings
- All ratios below were computed by me with the WCAG 2.2 relative-luminance and contrast-ratio definitions ([WCAG 2.2](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)) and floored, not rounded, to two decimals ([Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)).
- Thresholds: text AA 4.5 / large 3; AAA 7 / large 4.5. Non-text (1.4.11 user-interface components and focus indicators) 3:1. Labelled buttons need no 3:1 boundary ([Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)).
- WCAG 2.2 SC 2.4.13 Focus Appearance (AAA): the focus indicator must be at least as large as a 2 CSS px perimeter and have 3:1 contrast between focused and unfocused states — [WCAG 2.2](https://www.w3.org/TR/WCAG22/#focus-appearance)

#### System A – "Lipa & slonovina" (Linden & Ivory) — RECOMMENDED

| Token | Hex | Role |
|---|---|---|
| bg (base) | #FAF7F0 | Ivory page background |
| bg-tint (band) | #EDF0E3 | Linden mist, used once per page (alternative honey band: #F6EDD3, see extra rows) |
| surface (card) | #FFFFFF | Product cards, header, drawers |
| ink (text) | #252320 | Headings and body (warm charcoal, replaces #222222) |
| ink-muted | #67625A | Secondary text, captions, meta |
| hairline | #E2DBCB | Decorative dividers only |
| border (inputs) | #8F8879 | Form fields, quantity steppers, checkboxes (3:1) |
| accent (primary) | #3E5234 | Deep linden green: links, primary buttons, active states |
| accent-hover | #33452B | Hover/pressed |
| gold (ornament) | #C99A5C | Crest, rules, icons, stars; never text on light |
| gold-text (accent text-safe) | #8A6428 | Eyebrows/labels "in gold" on light backgrounds |
| button primary | fill #3E5234 / text #FFFFFF | Main CTA ("Dodaj v košarico") |
| button secondary (honey) | fill #C99A5C / text #252320 | Secondary CTA, never white text |
| footer | bg #2E3A29 / text #F1EFE6 / muted #BFC3B2 / heading-gold #D6B077 | The only dark band |
| focus | #252320 on light; #F1EFE6 in the footer | 2px solid outline, 2px offset. Alternative single on-brand ring: amber #B0782C (passes everywhere, thin margins) |

Text pairs (A):

| Pair | FG on BG | Ratio | AA normal | AA large | AAA normal | AAA large |
|---|---|---|---|---|---|---|
| Ink on base | #252320 on #FAF7F0 | 14.64 | pass | pass | pass | pass |
| Ink on tint | #252320 on #EDF0E3 | 13.56 | pass | pass | pass | pass |
| Ink on surface | #252320 on #FFFFFF | 15.67 | pass | pass | pass | pass |
| Muted on base | #67625A on #FAF7F0 | 5.65 | pass | pass | FAIL | pass |
| Muted on tint | #67625A on #EDF0E3 | 5.23 | pass | pass | FAIL | pass |
| Muted on surface | #67625A on #FFFFFF | 6.04 | pass | pass | FAIL | pass |
| Accent link on base | #3E5234 on #FAF7F0 | 7.97 | pass | pass | pass | pass |
| Accent link on tint | #3E5234 on #EDF0E3 | 7.38 | pass | pass | pass | pass |
| Accent link on surface | #3E5234 on #FFFFFF | 8.53 | pass | pass | pass | pass |
| Accent hover on base | #33452B on #FAF7F0 | 9.68 | pass | pass | pass | pass |
| Gold-text on base | #8A6428 on #FAF7F0 | 4.98 | pass | pass | FAIL | pass |
| Gold-text on tint | #8A6428 on #EDF0E3 | 4.61 | pass | pass | FAIL | pass |
| Gold-text on surface | #8A6428 on #FFFFFF | 5.33 | pass | pass | FAIL | pass |
| Gold ornament on base (as text: don't) | #C99A5C on #FAF7F0 | 2.37 | FAIL | FAIL | FAIL | FAIL |
| Gold ornament on tint (as text: don't) | #C99A5C on #EDF0E3 | 2.20 | FAIL | FAIL | FAIL | FAIL |
| Gold ornament on surface (as text: don't) | #C99A5C on #FFFFFF | 2.54 | FAIL | FAIL | FAIL | FAIL |
| Primary button text | #FFFFFF on #3E5234 | 8.53 | pass | pass | pass | pass |
| Primary button text, hover | #FFFFFF on #33452B | 10.36 | pass | pass | pass | pass |
| Honey button text | #252320 on #C99A5C | 6.16 | pass | pass | FAIL | pass |
| White on honey button (anti-pattern) | #FFFFFF on #C99A5C | 2.54 | FAIL | FAIL | FAIL | FAIL |
| Footer text | #F1EFE6 on #2E3A29 | 10.39 | pass | pass | pass | pass |
| Footer muted | #BFC3B2 on #2E3A29 | 6.65 | pass | pass | FAIL | pass |
| Footer gold heading | #D6B077 on #2E3A29 | 5.89 | pass | pass | FAIL | pass |
| Brand gold in footer | #C99A5C on #2E3A29 | 4.71 | pass | pass | FAIL | pass |
| Gold-text in footer (don't) | #8A6428 on #2E3A29 | 2.24 | FAIL | FAIL | FAIL | FAIL |
| Extra: ink on alt honey band | #252320 on #F6EDD3 | 13.41 | pass | pass | pass | pass |
| Extra: muted on alt honey band | #67625A on #F6EDD3 | 5.17 | pass | pass | FAIL | pass |
| Extra: gold-text on alt honey band | #8A6428 on #F6EDD3 | 4.56 | pass | pass | FAIL | pass |
| Extra: accent on alt honey band | #3E5234 on #F6EDD3 | 7.30 | pass | pass | pass | pass |

Non-text pairs (A), threshold 3:1:

| Pair | Colours | Ratio | 3:1 |
|---|---|---|---|
| Primary button fill vs base / tint / surface | #3E5234 vs #FAF7F0 / #EDF0E3 / #FFFFFF | 7.97 / 7.38 / 8.53 | pass |
| Honey button fill vs base / tint / surface | #C99A5C vs #FAF7F0 / #EDF0E3 / #FFFFFF | 2.37 / 2.20 / 2.54 | FAIL; permitted for a text-labelled button, so use it as the secondary action |
| Input border vs base / tint / surface / alt honey band | #8F8879 vs #FAF7F0 / #EDF0E3 / #FFFFFF / #F6EDD3 | 3.29 / 3.04 / 3.52 / 3.01 | pass |
| Hairline vs base / tint / surface | #E2DBCB vs same | 1.28 / 1.19 / 1.37 | FAIL; decorative only, must not carry meaning |
| Focus ring vs base / tint / surface | #252320 vs same | 14.64 / 13.56 / 15.67 | pass |
| Focus ring vs primary button fill | #252320 vs #3E5234 | 1.83 | FAIL, so outline-offset ≥2px is needed to keep the ring on the page background |
| Footer focus ring | #F1EFE6 vs #2E3A29 | 10.39 | pass |
| Alternative amber focus vs base / tint / surface / footer / alt honey band | #B0782C vs #FAF7F0 / #EDF0E3 / #FFFFFF / #2E3A29 / #F6EDD3 | 3.52 / 3.26 / 3.77 / 3.17 / 3.22 | pass (thin margins) |

Typography (A): Cormorant (display) + Jost (text).
- Shopify handles: `cormorant_n5` (bold via font_modify gives n7, plus i5) and `jost_n4`.
- Self-host alternative: Cormorant Garamond[wght] + Jost[wght] variable, to get smcp.

| Role | Family / weight | Desktop | Mobile | CSS size | Line-height | Tracking | Case |
|---|---|---|---|---|---|---|---|
| Display / hero | Cormorant 500 | 72px | 42px | clamp(2.625rem, 1.965rem + 2.817vw, 4.5rem) | 1.04 | −0.01em | Sentence |
| H1 | Cormorant 500 | 54px | 36px | clamp(2.25rem, 1.854rem + 1.69vw, 3.375rem) | 1.08 | −0.005em | Sentence |
| H2 | Cormorant 500 | 40px | 30px | clamp(1.875rem, 1.655rem + 0.939vw, 2.5rem) | 1.12 | 0 | Sentence |
| H3 | Cormorant 600 | 30px | 25px | clamp(1.5625rem, 1.452rem + 0.47vw, 1.875rem) | 1.2 | 0 | Sentence |
| H4 / product title | Cormorant 600 | 24px | 22px | 1.5rem / 1.375rem | 1.25 | 0.005em | Sentence |
| Emphasis | Cormorant Italic 500 | inherits | inherits | — | — | 0 | Sentence |
| Small-caps line (self-hosted only) | Cormorant 600, all-small-caps | 18px | 16px | 1.125rem | 1.3 | 0.08em | small caps |
| Lead | Jost 400 | 20px | 18px | 1.25rem / 1.125rem | 1.6 | 0 | Sentence |
| Body | Jost 400 | 17px | 16px | clamp(1rem, 0.978rem + 0.094vw, 1.0625rem) | 1.65 | 0 | Sentence |
| Small / meta | Jost 400 | 14px | 14px | 0.875rem | 1.5 | 0.01em | Sentence |
| Label / eyebrow | Jost 500 | 12px | 12px | 0.75rem | 1.3 | 0.18em | UPPERCASE |
| Navigation | Jost 500 | 13px | 15px (drawer, sentence case) | 0.8125rem | 1.3 | 0.14em | UPPERCASE (desktop) |
| Button | Jost 500 | 13px | 13px | 0.8125rem | 1 | 0.14em | UPPERCASE |
| Price | Jost 500, lining tabular | 18px | 17px | 1.125rem | 1.3 | 0 | — |

```css
:root{ /* System A – Lipa & slonovina */
  --c-bg:#FAF7F0; --c-bg-tint:#EDF0E3; --c-surface:#FFFFFF;
  --c-ink:#252320; --c-ink-muted:#67625A; --c-hairline:#E2DBCB; --c-border:#8F8879;
  --c-accent:#3E5234; --c-accent-hover:#33452B;
  --c-gold:#C99A5C; /* ornament only */ --c-gold-text:#8A6428;
  --c-btn-bg:#3E5234; --c-btn-fg:#FFFFFF; --c-btn2-bg:#C99A5C; --c-btn2-fg:#252320;
  --c-footer-bg:#2E3A29; --c-footer-fg:#F1EFE6; --c-footer-muted:#BFC3B2; --c-footer-gold:#D6B077;
  --c-focus:#252320; --c-focus-on-dark:#F1EFE6;
  --ff-display:"Cormorant","Cormorant Garamond",Georgia,serif;
  --ff-text:"Jost",system-ui,sans-serif;
}
:focus-visible{outline:2px solid var(--c-focus);outline-offset:2px}
.site-footer :focus-visible{outline-color:var(--c-focus-on-dark)}
.label{font:500 .75rem/1.3 var(--ff-text);letter-spacing:.18em;text-transform:uppercase;color:var(--c-gold-text)}
.price{font-variant-numeric:lining-nums tabular-nums}
```

#### System B – "Pergament & črnilo" (Parchment & Ink)

| Token | Hex | Role |
|---|---|---|
| bg (base) | #F8F4EB | Parchment (continuity with current cream #F7F3EA) |
| bg-tint (band) | #EEE5D4 | Oat |
| surface | #FFFDF8 | Paper white cards |
| ink | #1D2631 | Ink blue-black text |
| ink-muted | #5A6270 | Secondary text |
| hairline | #DCD2BF | Decorative rules |
| border (inputs) | #7F7A6F | Darkened from #8A8478, which failed on oat (2.97) |
| accent | #2A3F5E | Ink blue: links, buttons |
| accent-hover | #22344E | Hover |
| gold (ornament) | #C3935B | Keeps current gold 1 |
| gold-text | #845D26 | Text-safe gold |
| button primary | fill #2A3F5E / text #FFFDF8 | Main CTA |
| button secondary | fill #C3935B / text #1D2631 | Secondary |
| footer | bg #1D2631 / text #EDE7DA / muted #A7AEB8 / gold #D3AB6E | Only dark band |
| focus | #2A3F5E on light; #EDE7DA in footer | 2px outline, 2px offset |
| optional trend swap | accent #1E4245 (deep teal) | 10.93 with white text; 9.96 on parchment |

| Pair | FG on BG | Ratio | AA normal | AA large | AAA normal | AAA large |
|---|---|---|---|---|---|---|
| Ink on base / tint / surface | #1D2631 on #F8F4EB / #EEE5D4 / #FFFDF8 | 13.92 / 12.22 / 15.03 | pass | pass | pass | pass |
| Muted on base | #5A6270 on #F8F4EB | 5.60 | pass | pass | FAIL | pass |
| Muted on tint | #5A6270 on #EEE5D4 | 4.91 | pass | pass | FAIL | pass |
| Muted on surface | #5A6270 on #FFFDF8 | 6.04 | pass | pass | FAIL | pass |
| Accent on base / tint / surface | #2A3F5E on same | 9.70 / 8.52 / 10.48 | pass | pass | pass | pass |
| Accent hover on base | #22344E on #F8F4EB | 11.46 | pass | pass | pass | pass |
| Gold-text on base | #845D26 on #F8F4EB | 5.35 | pass | pass | FAIL | pass |
| Gold-text on tint | #845D26 on #EEE5D4 | 4.69 | pass | pass | FAIL | pass |
| Gold-text on surface | #845D26 on #FFFDF8 | 5.77 | pass | pass | FAIL | pass |
| Gold ornament on base / tint / surface (as text: don't) | #C3935B on same | 2.50 / 2.19 / 2.70 | FAIL | FAIL | FAIL | FAIL |
| Primary button text / hover | #FFFDF8 on #2A3F5E / #22344E | 10.48 / 12.37 | pass | pass | pass | pass |
| Secondary button text | #1D2631 on #C3935B | 5.56 | pass | pass | FAIL | pass |
| White on gold (anti-pattern) | #FFFFFF on #C3935B | 2.74 | FAIL | FAIL | FAIL | FAIL |
| Footer text | #EDE7DA on #1D2631 | 12.40 | pass | pass | pass | pass |
| Footer muted | #A7AEB8 on #1D2631 | 6.83 | pass | pass | FAIL | pass |
| Footer gold heading | #D3AB6E on #1D2631 | 7.14 | pass | pass | pass | pass |
| Brand gold in footer | #C3935B on #1D2631 | 5.56 | pass | pass | FAIL | pass |

| Non-text pair (B) | Colours | Ratio | 3:1 |
|---|---|---|---|
| Primary fill vs base / tint / surface | #2A3F5E | 9.70 / 8.52 / 10.48 | pass |
| Gold fill vs base / tint / surface | #C3935B | 2.50 / 2.19 / 2.70 | FAIL (permitted for a labelled button) |
| Input border vs base / tint / surface | #7F7A6F | 3.89 / 3.41 / 4.20 | pass |
| Hairline vs base / tint / surface | #DCD2BF | 1.36 / 1.19 / 1.47 | decorative only |
| Focus vs base / tint / surface | #2A3F5E | 9.70 / 8.52 / 10.48 | pass; vs its own button fill 1.00, so offset required |
| Footer focus | #EDE7DA vs #1D2631 | 12.40 | pass |
| Alt amber focus vs base / tint / surface / footer | #B0782C | 3.43 / 3.01 / 3.70 / 4.05 | pass (tint barely) |

Typography (B): EB Garamond (display, Shopify `ebgaramond_n5`, italics i5) + Work Sans (text, `work_sans_n4`). Optional crest lockups in Marcellus (`marcellus_n4`).
- Display: EB Garamond 500, 68/40px, line-height 1.06, −0.01em.
- H1: EB Garamond 500, 52/34px, line-height 1.1.
- H2: EB Garamond 500, 38/28px, line-height 1.15.
- H3: EB Garamond 600, 28/23px, line-height 1.25.
- H4: EB Garamond 600, 22/20px, line-height 1.3.
- Lead: EB Garamond 400, 21/19px, line-height 1.5.
- Body: Work Sans 400, 16px, line-height 1.65.
- Small: Work Sans 400, 14px, line-height 1.5.
- Label: Work Sans 500, 12px, uppercase, 0.16em, line-height 1.3.
- Crest lockup: Marcellus 400, 14px, uppercase, 0.12em.
- Button: Work Sans 500, 13px, uppercase, 0.12em.
- Price: Work Sans 500, 17px, tabular.
- Cost: EB Garamond latin-ext is 55.6 KB per weight, so limit it to 500 roman and 500 italic.

#### System C – "Akacija" (Acacia, all-light, no dark band)

| Token | Hex | Role |
|---|---|---|
| bg (base) | #FFFFFF | White |
| bg-tint (band) | #F6EDD3 | Acacia honey wash |
| surface | #FBF7EE | Cream cards |
| ink | #2A2019 | Buckwheat ink (keeps the brown DNA, as text only) |
| ink-muted | #6C5F50 | Warm taupe |
| hairline | #EADFC8 | Decorative |
| border (inputs) | #94846D | 3:1 inputs |
| accent (text-safe) | #8A5A1C | Chestnut: links, eyebrows |
| accent-hover | #744A15 | Hover |
| gold (ornament) | #C99A5C | Crest, rules |
| gold-text | #8A5A1C | Same as accent |
| button primary | fill #2A2019 / text #FFFFFF (hover #3A2C22) | Main CTA |
| button secondary | fill #D8AC5E / text #2A2019 | Honey button (not on the tint band) |
| footer | bg #F3EBDA / text #2A2019 / muted #6C5F50 / heading #8A5A1C | Light wheat footer |
| focus | #2A2019 everywhere | 2px outline, 2px offset |

| Pair | FG on BG | Ratio | AA normal | AA large | AAA normal | AAA large |
|---|---|---|---|---|---|---|
| Ink on base / tint / surface | #2A2019 on #FFFFFF / #F6EDD3 / #FBF7EE | 15.92 / 13.62 / 14.88 | pass | pass | pass | pass |
| Muted on base | #6C5F50 on #FFFFFF | 6.19 | pass | pass | FAIL | pass |
| Muted on tint | #6C5F50 on #F6EDD3 | 5.30 | pass | pass | FAIL | pass |
| Muted on surface | #6C5F50 on #FBF7EE | 5.79 | pass | pass | FAIL | pass |
| Accent / gold-text on base | #8A5A1C on #FFFFFF | 5.89 | pass | pass | FAIL | pass |
| Accent / gold-text on tint | #8A5A1C on #F6EDD3 | 5.04 | pass | pass | FAIL | pass |
| Accent / gold-text on surface | #8A5A1C on #FBF7EE | 5.51 | pass | pass | FAIL | pass |
| Accent hover on base | #744A15 on #FFFFFF | 7.68 | pass | pass | pass | pass |
| Gold ornament on base / tint / surface (as text: don't) | #C99A5C on same | 2.54 / 2.17 / 2.37 | FAIL | FAIL | FAIL | FAIL |
| Primary button text / hover | #FFFFFF on #2A2019 / #3A2C22 | 15.92 / 13.43 | pass | pass | pass | pass |
| Honey button text | #2A2019 on #D8AC5E | 7.56 | pass | pass | pass | pass |
| White on honey (anti-pattern) | #FFFFFF on #D8AC5E | 2.10 | FAIL | FAIL | FAIL | FAIL |
| Footer text | #2A2019 on #F3EBDA | 13.42 | pass | pass | pass | pass |
| Footer muted | #6C5F50 on #F3EBDA | 5.22 | pass | pass | FAIL | pass |
| Footer heading | #8A5A1C on #F3EBDA | 4.97 | pass | pass | FAIL | pass |
| Brand gold in footer (as text: don't) | #C99A5C on #F3EBDA | 2.14 | FAIL | FAIL | FAIL | FAIL |

| Non-text pair (C) | Colours | Ratio | 3:1 |
|---|---|---|---|
| Primary fill vs base / tint / surface | #2A2019 | 15.92 / 13.62 / 14.88 | pass |
| Honey fill vs base / tint / surface | #D8AC5E | 2.10 / 1.80 / 1.96 | FAIL; permitted, but nearly invisible on the tint band, so use the dark button there |
| Input border vs base / tint / surface | #94846D | 3.63 / 3.10 / 3.39 | pass |
| Hairline vs base / tint / surface | #EADFC8 | 1.32 / 1.13 / 1.23 | decorative only |
| Focus vs base / tint / surface / footer | #2A2019 | 15.92 / 13.62 / 14.88 / 13.42 | pass; vs dark button fill 1.00, so offset required |

Typography (C): Fraunces (display, Shopify `fraunces_n4`, italics i4) + Figtree (text, `figtree_n4`).
- Self-hosting the variable Fraunces allows `font-optical-sizing:auto` and `font-variation-settings:"SOFT" 50, "WONK" 0` (soft, not quirky).
- Display: Fraunces 400, 64/40px, line-height 1.06, −0.015em.
- H1: Fraunces 400, 50/34px, line-height 1.1, −0.01em.
- H2: Fraunces 400, 38/28px, line-height 1.15.
- H3: Fraunces 500, 26/22px, line-height 1.25.
- H4: Figtree 600, 19/18px, line-height 1.35.
- Lead: Figtree 400, 19/18px, line-height 1.6.
- Body: Figtree 400, 17/16px, line-height 1.65.
- Small: Figtree 400, 14px, line-height 1.5.
- Label: Figtree 600, 12px, uppercase, 0.14em, line-height 1.3.
- Button: Figtree 600, 14px, sentence case.
- Price: Figtree 600, 18px, tabular.
- There are no true small caps in Fraunces.

### Inferences
- **Why A is the best fit for a heritage family honey brand that wants elegance and lightness:**
  1. **Lightness with structure.** An ivory base, white cards and one pale tint band make the page airy. A single deep linden footer gives the page an end without the repeated espresso bands the client finds heavy. It also complies with the project's "dark sparingly, never several in a row" rule.
  2. **Gold behaves as on the jar label.** The current brand gold #C99A5C is kept untouched as ornament. Gold-looking text uses #8A6428, which passes AA on every light base (4.61–5.33:1).
  3. **The accent does not compete with the honey.** Deep linden green #3E5234 is complementary to amber, so jars and honey photography stand out. It is heraldically classic with gold, reads botanical (meadow, forest, linden) rather than rustic, and sits close to 2026's deep-teal and green direction without chasing it. The CTA is strong: 8.53:1 with white text.
  4. **The typography is elegant and practical.** Cormorant's Garamond-derived display and calligraphic italic signal heritage. Jost keeps the shop UI crisp. Both are OFL, both cover Č Š Ž Ć Đ, both are in Shopify's library (selectable in the theme editor, served from Shopify's CDN, no GDPR hotlinking question), and they are light (about 41 + 15 KB per static weight).
  5. **Robust accessibility.** Every text pair passes AA, primary buttons pass AAA, and the focus ring is 13–15:1 on light backgrounds.
- **When to choose B or C instead:**
  - **B** if the client wants the most formal, "printed heritage" look; ink blue with gold is regal, but cooler and less food-like.
  - **C** if the client wants zero dark areas. It is the most literal echo of the cream-and-gold label, but risks honey-on-honey monotony, and its honey button fails visually on the acacia band (1.80:1).
- **Hybrid.** If the client likes a honey-coloured band, System A can use C's acacia #F6EDD3 as its single tint band. All A text tokens pass on it (ink 13.41, muted 5.17, gold-text 4.56, accent 7.30).
- **Implementation notes for this theme:**
  - Set the heading and body fonts via the existing font_picker settings `font_family` → `cormorant_n5` and `font_family2` → `jost_n4`, and leave the "Google font" fields blank.
  - The colour tokens map to CSS custom properties.
  - Content JSON changes (settings_data.json) should be made in the theme editor, per the project's CLAUDE.md rules.

### Gaps
- None of the systems were rendered on the actual store pages or with real product photography. Perceived "heaviness" and the tint-band choice should be checked visually on the dev server before final selection.
- APCA results were not computed.
- I could not measure Shopify-served file sizes or feature retention for Cormorant, Jost, EB Garamond, Work Sans, Fraunces or Figtree.
