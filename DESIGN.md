---
name: Hitchstead (hitchstead.com)
description: The Hitchstead app's Hard Hat world on the web; the roster on the fridge, a whole rotation year coloured day by day.
colors:
  band-top: "#1E7F72"
  band-bottom: "#10564C"
  on-band: "#FFFCF4"
  ground: "#F7F3E8"
  surface: "#FFFCF4"
  ink: "#20333F"
  ink-soft: "#52626B"
  accent: "#17675D"
  rule: "#D9D2C1"
  day: "#E6D3A6"
  night: "#B8C5E8"
  home: "#A6D9C7"
  travel: "#D4DE7C"
  held: "#EE7F33"
  held-label: "#8D451A"
  held-wash: "#F8E4D0"
typography:
  display:
    fontFamily: "\"New York\", ui-serif, Georgia, \"Times New Roman\", serif"
    fontSize: "clamp(40px, 4.3vw, 66px)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "\"New York\", ui-serif, Georgia, \"Times New Roman\", serif"
    fontSize: "clamp(32px, 3.4vw, 50px)"
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.03em"
  title:
    fontFamily: "\"New York\", ui-serif, Georgia, \"Times New Roman\", serif"
    fontSize: "clamp(24px, 2.2vw, 32px)"
    fontWeight: 700
    letterSpacing: "-0.02em"
  amount:
    fontFamily: "\"New York\", ui-serif, Georgia, \"Times New Roman\", serif"
    fontSize: "38px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Helvetica Neue\", Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.55
  intro:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Helvetica Neue\", Arial, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Helvetica Neue\", Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 650
  day-numeral:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Helvetica Neue\", Arial, sans-serif"
    fontSize: "10px"
    fontWeight: 400
    fontFeature: "\"tnum\""
rounded:
  day: "4px"
  strip-day: "5px"
  badge: "10px"
  note: "12px"
  chip: "14px"
  strip: "24px"
  sheet: "28px"
  screen: "38px"
  phone: "46px"
spacing:
  section-block: "clamp(72px, 9vw, 128px)"
  section-inline: "clamp(22px, 5vw, 72px)"
  sheet-pad: "clamp(22px, 2.4vw, 36px)"
  split-gap: "clamp(40px, 7vw, 112px)"
  inner: "1120px"
  doc: "760px"
components:
  band:
    backgroundColor: "{colors.band-top}"
    textColor: "{colors.on-band}"
  sheet:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sheet}"
    padding: "{spacing.sheet-pad}"
  day-cell:
    backgroundColor: "{colors.home}"
    textColor: "{colors.ink}"
    rounded: "{rounded.day}"
    typography: "{typography.day-numeral}"
  day-cell-held:
    backgroundColor: "{colors.held}"
    textColor: "{colors.ink}"
    rounded: "{rounded.day}"
  held-note:
    backgroundColor: "{colors.held-wash}"
    textColor: "{colors.held-label}"
    rounded: "{rounded.note}"
    padding: "10px 14px"
  quote-chip:
    backgroundColor: "{colors.held-wash}"
    textColor: "{colors.held-label}"
    rounded: "{rounded.chip}"
    padding: "12px 16px"
  phone-frame:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.phone}"
    padding: "9px"
    width: "340px"
  store-badge:
    rounded: "{rounded.badge}"
    width: "168px"
---

# Design System: Hitchstead (hitchstead.com)

## Overview

**Creative North Star: "The Roster on the Fridge"**

The site is the Hitchstead app's Hard Hat world carried onto the web without translation loss: a teal band like the app's Home header, a cream ground with cream sheets lifted off it, ink type, and the app's own year colours for the four kinds of day. The proof is the calendar itself. A whole year of a real rotation, coloured day by day, sits where other app sites put a hero mockup, and real app screens in a plain ink phone frame carry everything below the fold.

Density is calm and practical, worker's-tool rather than lifestyle-brand. Serif headlines (New York, falling back to Georgia) give the dates an almanac's authority; SF system text keeps everything else plain and fast. Colour is meaning, not decoration: tan, periwinkle, sage and lime say day, night, home and travel; one orange says "this changed." Nothing else on the page competes with that orange.

Read pages (support, privacy, 404) are the same world reduced: a band header with the wordmark and serif title, then a single cream column of text.

**Key Characteristics:**
- Teal band gradient (165deg, band-top to band-bottom) as the page's anchor: the left 36% of the first viewport on desktop, a full-width header on phones and Read pages.
- Cream ground, cream surface sheets with a soft two-layer ink shadow and 28px corners.
- Day-kind colours from the app's year view; orange reserved for held-over days and the focus ring.
- Serif headlines, system sans everything else; tabular numerals in every day grid.
- Real app screens in a plain ink phone frame; no device renders, no invented UI.
- One motion moment: held-over days settle from home green to orange on load.

## Colors

A warm, papery palette from the app: teal for the brand, cream for paper, ink for words, and the app's year colours as a functional legend.

### Primary
- **Rig Teal, top** (band-top): the light end of the band gradient; also the page `theme-color`.
- **Rig Teal, deep** (band-bottom): the dark end of the band gradient. Below-the-fold band sections run the gradient vertically (180deg, deep to top) instead of 165deg.
- **Spruce Link** (accent): links on cream, the secondary span beside a price amount ("to start", "once · no subscription"). Underlined links, 1px at rest, 2px on hover.

### Secondary
- **Holdover Orange** (held): held-over days in every grid and strip, and the 3px focus ring. The only saturated warm colour on the site.
- **Holdover Wash** (held-wash) with **Holdover Brown** (held-label): the app's change-override pair, used for the held-over note above the year, the quote chip under the holdover section, and the held-over word in the day caption.

### Tertiary (day kinds, from the app's year palette)
- **Day Tan** (day): day shifts.
- **Night Periwinkle** (night): night shifts.
- **Home Sage** (home): days home; also the text-selection colour.
- **Travel Lime** (travel): travel days.

### Neutral
- **Cream Ground** (ground): page background.
- **Cream Paper** (surface): sheets, the before/after strip, the offer section; also every piece of text on the band (on-band).
- **Ink** (ink): body text, day numerals on every day colour including orange, the phone frame, the hover/picked ring on days, the 2px rule above the price tiers.
- **Ink Soft** (ink-soft): secondary copy, intros, weekday letters, strip labels, FAQ answers.
- **Rule** (rule): 1px dividers between fact rows, between tiers. On the band, fact dividers use cream at 22% opacity.

### Named Rules
**The One Orange Rule.** Holdover Orange marks a change and nothing else: held-over days, the held-over note family, and the focus ring. No orange buttons, headings, icons or decoration.

**The Legend Is the Palette Rule.** The four day colours always mean the same day kind as in the app, and wherever they appear together a legend (14px swatches, 4px corners) names them.

**The Full-Cream Band Rule.** Every piece of text on the teal band is full Cream Paper, including ledes, price lines and band footers. Do not lower its opacity or swap it for a muted tint, which fails contrast on the lighter band-top.

Deviations from the app tokens, recorded on purpose: the web uses the app's saturated year colours (not its pale day backgrounds) for day cells; held-over numerals are Ink on full orange rather than the app's change-mark treatment; dividers use a lighter warm rule than the app's separator; dark mode is not shipped (`color-scheme: light`).

## Typography

**Display Font:** New York (with ui-serif, Georgia, Times New Roman)
**Body Font:** SF Pro via -apple-system (with Helvetica Neue, Arial)

**Character:** An almanac serif for statements and amounts, set bold and tightly tracked, over the iPhone's own system text. The pairing reads as the app talking, not a marketing voice.

### Hierarchy
- **Display** (700, clamp 40 to 66px, 1.02, -0.035em, max 10.5ch): the hero headline only. 36px on phones.
- **Headline** (700, clamp 32 to 50px, 1.06, -0.03em): section titles. Read-page titles use clamp 36 to 52px.
- **Title** (700, clamp 24 to 32px, -0.02em): the sheet title. Serif h3s step down from here: 26px (paired features), 22px (tiers), 21px (doc), 20px (FAQ questions).
- **Amount** (700, 38px serif): prices in the tiers, with a 15px/650 sans span in Spruce Link beside it.
- **Body** (400, 17px, 1.55): all running text; doc paragraphs cap at 68ch, section copy at 44 to 52ch.
- **Intro** (400, 19px, Ink Soft, max 46ch): the paragraph under a section headline. The hero lede is clamp 18 to 21px at 1.45, max 30ch.
- **Label** (650, 14px, sans): month names, legend, strip labels, band footer. Captions and the price line are 15px/600.
- **Day numeral** (10px, tabular numerals; 12px in the strip, 9px/650 for weekday letters): every date in a grid.

### Named Rules
**The Serif Speaks, Sans Works Rule.** Serif is for headings, FAQ questions and price amounts. Month names, labels, legends, captions and every numeral in a grid are sans.

**The Tabular Dates Rule.** Any number that sits in a day grid or countdown uses tabular numerals.

## Layout

The first viewport is a two-column grid: the band at `minmax(360px, 36%)`, full height (100svh), and the year sheet filling the rest, centred. Hero copy sits vertically centred in the band with the wordmark at the top and a Support/Privacy footer at the bottom.

Below the fold, sections pad `section-block` top and bottom and `section-inline` at the sides, with content in a 1120px column. The working layout is a split: text and a 260 to 340px phone column, with `split-gap` between; `.flip` puts the phone first; a wide variant runs 5fr/7fr for text beside the before/after strip. Sections that follow each other on the same ground drop their top padding to read as one run. Pairs, tiers and the FAQ are two equal columns.

Read pages: band header (28px top, 56px bottom padding) then a 760px text column.

Responsive: at 1080px the band stacks above the sheet and the year goes to three columns. At 760px the year goes to two columns and shows only July to December (labelled "Illustrated example, July to December"), the held-over note moves under the grid, the long price line swaps for a one-line short version, splits/pairs/tiers/FAQ collapse to one column, the strip trims to 16 days, the phone caps at 300px, the band footer hides, and sections pad 56px vertically.

## Elevation & Depth

Hybrid: the page is flat colour fields (band, ground, surface section), and exactly three kinds of object lift off it with one shared shadow: the year sheet, the before/after strip, and the phone frame. The shadow is soft and ink-tinted, never black and never offset hard.

### Shadow Vocabulary
- **Sheet lift** (`box-shadow: 0 22px 48px rgba(32, 51, 63, .14), 0 3px 8px rgba(32, 51, 63, .06)`): sheets, the strip, the phone frame. The only shadow on the site.
- **Day ring** (`box-shadow: inset 0 0 0 2px #20333F`): a day under the pointer or picked; 150ms ease-out.

### Named Rules
**The One Lift Rule.** One shadow value for everything that lifts. Cards, chips, notes and buttons stay flat.

## Shapes

Soft, rounded, app-like. Radii step from the smallest cell to the device: day cells 4px (5px in the strip), the App Store badge and wordmark icon 10px, the held-over note 12px, the quote chip 14px, the strip 24px, the sheet 28px, the phone screen 38px inside a 46px frame. Lines are thin and warm (1px Rule); the one heavy line is the 2px ink rule over the price tiers. No outlines around cards; the sheet and shadow do the work.

## Components

### Store badge (primary action)
- **Character:** Apple's official badge, unchanged; it is the only call to action.
- **Shape:** 10px corner clip, 168px wide.
- **Placement:** in the band under the lede, in the family section, and in the close row. No custom CTA buttons exist.

### Year sheet (signature)
- **Character:** the roster on the fridge.
- **Corner Style / Background / Shadow:** 28px, Cream Paper, Sheet lift.
- **Internal Padding:** clamp 22 to 36px (18px on phones).
- **Content:** serif title and example label in the head, an optional held-over note, twelve month grids (4 / 3 / 2 columns), then legend and live caption in the foot.
- **Day cells:** 7-column grid, 2px gap, aspect 1.25, day colour fill, Ink numeral. Hover or tap draws the 2px ink ring and writes the day's kind into the caption (aria-live), the way the app labels a day.
- **Generated:** month grids and the strip are produced by `tools/year.py`; edit the generator, not the HTML.

### Before/after strip
- **Style:** a 24px-cornered Cream Paper figure with Sheet lift; two rows (Before, After) of 21 day cells, aspect 0.78, 12px numerals, 5px corners; legend in the figcaption, indented to the cells.

### Held-over note and quote chip
- **Style:** Holdover Wash fill, Holdover Brown text, 12px and 14px corners, flat. The note states the change in one line; the chip quotes the app's preview sentence.

### Phone frame
- **Style:** Ink fill, 46px corners, 9px padding, Sheet lift, real app screenshot inside at 38px corners, 340px max (300px on phones). No notch, buttons or device render.

### Fact list
- **Style:** unbulleted rows, 14px vertical padding, 1px Rule between and around; bold lead-in at 650. On the band, dividers are cream at 22%.

### Price tiers
- **Style:** two columns under a 2px ink rule, 1px Rule between; serif tier name, serif amount, plain bulleted list. No boxed pricing cards.

### Navigation
- **Style:** there is no top nav. The wordmark (40px icon, 20px/650 name) links home; Support and Privacy sit at the bottom of the band and in the footer (14px, Ink links on Ink Soft text).

### Focus
- 3px Holdover Orange outline, 3px offset, 6px radius, on every focusable element.

### Motion
- One moment: held-over day cells animate from Home Sage to Holdover Orange (900ms, `cubic-bezier(.16, 1, .3, 1)`, 700ms delay) on load, telling the holdover story in a glance. Under reduced motion they are simply orange. Nothing else animates except the 150ms day ring and smooth anchor scrolling.

## Do's and Don'ts

### Do:
- **Do** prove features with the real calendar or real app screens in the plain ink phone frame.
- **Do** keep the four day colours and orange exactly as the app uses them, with a legend wherever they appear together.
- **Do** set all text on the band in full Cream Paper (#FFFCF4).
- **Do** use the single Sheet lift shadow (`0 22px 48px rgba(32,51,63,.14), 0 3px 8px rgba(32,51,63,.06)`) for anything that lifts, and nothing else.
- **Do** keep the App Store badge as the only call to action, and state the price plainly ($9.99 once, free to start).
- **Do** use tabular numerals for every date in a grid.

### Don't:
- **Don't** use orange for anything but held-over days, the holdover note family, and focus.
- **Don't** put muted or translucent text on the teal band.
- **Don't** add device renders, mockup angles, or invented app UI; screens are real captures.
- **Don't** build rows of icon feature cards or boxed pricing cards; use splits, fact lists and ruled tiers.
- **Don't** set month names, labels or grid numerals in the serif.
- **Don't** add ratings, review counts or testimonials; none exist.
