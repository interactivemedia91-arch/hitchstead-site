# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS, no framework, no build step. Hosted on GitHub Pages (public repo, custom domain `hitchstead.com` with DNS at Cloudflare), like the Billdar site. Confirmed by the owner, 20 Nov 2026.

## Users

- **Rotation workers**: oilfield, offshore, mining and drilling crews in the US; FIFO workers in Australia. They work fixed rotations (7/7, 14/7, 14/14, 21/21, 28/28, 8/6, 20/10, days then nights) and need to know which days they work, travel and are home, often without signal on the rig, offshore or at camp.
- **Their partners and families**: the people at home who plan around the rotation. They follow the worker's schedule free in the app.

One English site (US English) for both markets; uses both terms where they matter ("rotation or roster", "hitch or swing"). Confirmed by the owner.

## Product Purpose

Hitchstead is an iPhone calendar built for rotation work. Pick a rotation, say where you are in it, and see every day: day shifts, night shifts, travel and home. The site exists to explain it to workers and families and send them to the App Store, and to host the privacy policy and support.

## Positioning

- **Change a hitch that ran long without breaking the rotation**: add holdover days, time off, a swap or a travel day; only the picked dates change and the rest stays where it was; see the effect before saving ("Next hitch still starts Thu, Oct 29").
- **Family follows free through iCloud**: a private invite link, no account, updates by itself, a notification when the homecoming moves.
- **Pay once**: $9.99, no subscription. Free to start.
- **Works with no signal**: schedule, countdown and widgets live on the iPhone.

## Operating Context

Workers check it on the rig, offshore, at camp or at home; families check it at home and get notified of changes. Typical moments: counting down to the next travel day, a holdover being announced, planning holidays and birthdays around the roster, deciding who is home at Christmas.

## Capabilities and Constraints

Source of truth: the App Store description in `~/Code/hitchstead/docs/app-store-listing.md` (1.1, live 20 Nov 2026).

- Rotations: presets and custom, days then nights; hitch bar, countdown, "Next up".
- Changes: holdover, time off, swap, travel day; preview; undo; restart from a date.
- Keep home in the loop: invite by private link (iCloud), followers free, notifications on change, "days you're both home" when both work rotations; publish to Apple Calendar; ICS export.
- Holidays (US and Australian sets) and personal dates with who's home; Christmas five years ahead; plan time off or ask to be home with a ready-made message.
- Year view; send a month or the year as a picture.
- Widgets: Home Screen and Lock Screen, for yourself or someone you follow.
- Free tier: set up the rotation, the next 90 days, preview changes, widgets. Unlock ($9.99 once): save changes, every month, invite home, publish to Apple Calendar, export. Followers free.
- iPhone only. App Store id 6827233338; US name "Hitchstead: Oilfield Calendar", AU name "Hitchstead: FIFO Roster".
- Support email today: interactivemedia91@gmail.com (a hello@hitchstead.com address is planned, not set up yet).

## Brand Commitments

- Name: Hitchstead. The app's "Hard Hat" visual identity (shipped in 1.0, owner-approved): see `~/Code/hitchstead/design/01-design-system.md` and the App Store screenshots in `~/Code/hitchstead/design/appstore/out/`.
- Voice: plain, practical, worker's language (hitch, holdover, R&R, swing); gender-neutral (confirmed for the app).
- Privacy promise: no accounts, no ads, no tracking; data on the iPhone and the user's own iCloud.

## Evidence on Hand

- 14 App Store screenshots (US and AU, 1320×2868): `~/Code/hitchstead/design/appstore/out/`.
- App icon: `~/Code/hitchstead/Hitchstead/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon.png`.
- Privacy policy and support FAQ text: `~/Code/scratchpad/pages-site/hitchstead/privacy.html` (live at interactivemedia91-arch.github.io/hitchstead/privacy.html).
- No ratings, reviews, testimonials, press or user counts to quote. Never invent any.

## Product Principles

1. The rotation is the user's life plan: dates must read as exact and trustworthy.
2. Built for the people at home as much as for the worker.
3. One price, no account, no tracking; say so plainly.
4. Works where the job is: no signal, small screens, quick glances.
