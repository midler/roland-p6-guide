# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Russian-speaking beginners with a Roland AIRA Compact P-6 who start from zero: no music theory, little or no experience with samplers or DAWs. The primary user is the author: a beginner who studies in 30-minute sessions, switches between a phone (often held next to the device, sometimes offline in transit or on a plane) and a desktop (Windows, Ableton Live). The guide is built for this person first and kept useful for any other P-6 beginner it is shared with.

Their job: learn the P-6 hands-on, step by step, with the device in front of them, and get from "I don't understand the buttons" to making music on it.

## Product Purpose

An interactive Russian-language course for the Roland P-6: exact button presses for every step, a panel explorer that mirrors the real device, playable step grids and chord diagrams, genre recipes, creative challenges, a cheat sheet and curated videos.

Success after 2–3 months of use means the learner:

- operates the P-6 fluently without looking up basic actions in the manual;
- has finished tracks or sets in lo-fi hip-hop, ambient and drum and bass;
- can play a live set on the P-6 without preparing it on a computer;
- records, collects and processes their own sounds and sound packs.

## Positioning

Every button press is checked against the official Roland P-6 online manual (system Ver. 1.02); techniques taken from YouTube tutorials are marked as such and linked with timestamps, and undocumented shortcuts are labelled as shown in videos, not in the manual. The course is structured around the real device: its 16 step keys, its panel layout, its factory samples and patterns.

## Operating Context

- Used with the P-6 in hand: one hand on the device, the other on the phone or keyboard.
- Sessions of about 30 minutes; the learner sets their own pace, there is no week-based schedule.
- Structure: a base track (lessons 00–08 plus two theory lessons, labelled by order: T1 notes and chords, T2 rhythm; their internal ids are T2 and T1), then four branches taken in any order (Beats Б1–Б5, Sound design С1–С3, Live Ж1–Ж3, Computer and order К1–К4), then genre recipes (lo-fi → ambient → drum and bass).
- Desktop side: Windows, Ableton Live, P-6 over USB-C (audio and MIDI); free tools DigiChain, Audacity, P-6 SampleTool; sound sources Freesound (CC0), Pixabay, 99Sounds, AKWF.
- Published two ways: a private claude.ai artifact and a public GitHub Pages site (github.com/midler/roland-p6-guide) that installs as an offline web app.

## Capabilities and Constraints

- Button presses come only from the official Roland manual; anything else is marked with its source. Never invent a shortcut.
- Works offline: the GitHub Pages build caches the page (service worker, manifest); external links (manual, YouTube) are the only things that need a connection.
- No data on a server: progress lives in the browser and moves between devices only through a copy-paste progress code. No accounts, no analytics, no data collection.
- Single static HTML page (`src/guide.html`), built into `index.html` + `sw.js` by `tools/build_site.py`; no framework, no build step beyond that script.
- Sounds in grids and chord buttons are synthesized in the browser; Roland's factory samples are not redistributed.
- Lesson ids are stable internal keys for saved progress; branch lessons show their own labels (Б1, С1, Ж1, К1) without changing the keys.
- Open: whether to offer languages other than Russian (Russian was not made a binding constraint).

## Brand Commitments

- Name: «Тренажёр Roland P-6».
- Unofficial learning material; Roland, AIRA and P-6 are trademarks of Roland Corporation. No Roland logos or brand assets are used.

## Evidence on Hand

- Official Roland P-6 online manual (Ver. 1.02), read in full; source for all presses.
- Roland factory sample and pattern archive, analysed to map kicks, snares and hats per bank (lesson 04 table).
- Subtitles of 31 YouTube tutorials (Russian and English) and a notes digest, used for marked techniques and timestamped links.
- The author's own photo of the P-6 panel, used for the panel layout and step-key mapping.
- No testimonials, user counts or reviews exist; do not fabricate them.

## Product Principles

1. Accuracy before breadth: a press that is not in the manual is either marked with its source or left out.
2. Hands on the device: every lesson ends in something done on the P-6, not just read.
3. The learner sets the pace: sessions of 30 minutes, no deadlines, progress the learner owns.
4. Works where the learner is: phone or desktop, online or offline.
5. Show, then explain: grids, chords and the panel come before long text.

## Accessibility & Inclusion

- Readable on a phone held in one hand: body text 16 px, touch targets 44 px for primary controls and 24 px minimum elsewhere, no horizontal scroll at text sizes up to 200%.
- WCAG AA contrast in both light and dark themes; reduced motion respected; keyboard focus never hidden under the sticky tab bar.
