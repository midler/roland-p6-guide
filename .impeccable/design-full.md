---
name: Тренажёр Roland P-6
description: Тетрадь битмейкера с приборными деталями — интерактивный курс по сэмплеру Roland P-6.
colors:
  step-light: "#1f6f86"
  step-light-ink: "#ffffff"
  step-light-soft: "#d6e8ee"
  paper: "#e7e9ec"
  page: "#f6f7f8"
  page-tint: "#eef0f2"
  ink: "#16181c"
  pencil: "#596170"
  rule-line: "#cbd0d7"
  done-green: "#2a7146"
  warning-amber: "#8a5000"
  key-graphite: "#2a2d33"
  key-legend: "#f1f2f4"
  key-edge: "#111316"
  lcd-glass: "#1a0d0a"
  lcd-red: "#ff5a36"
  step-light-dark: "#5fb7cf"
  step-light-ink-dark: "#0d1316"
  step-light-soft-dark: "#1d3540"
  paper-dark: "#121417"
  page-dark: "#1b1e23"
  page-tint-dark: "#22262c"
  ink-dark: "#e9ebef"
  pencil-dark: "#9aa3b2"
  rule-line-dark: "#2f343c"
  done-green-dark: "#5cc487"
  warning-amber-dark: "#e0a446"
  key-graphite-dark: "#3a3f47"
  lcd-red-dark: "#ff6a45"
typography:
  display:
    fontFamily: "Unbounded, Manrope, system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 5vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Unbounded, Manrope, system-ui, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.2
  title:
    fontFamily: "Manrope, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  body:
    fontFamily: "Manrope, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  body-small:
    fontFamily: "Manrope, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.08em"
  key-legend:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "0.78em"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.02em"
rounded:
  lcd: "3px"
  cell: "4px"
  key: "5px"
  control: "8px"
  note: "10px"
  sheet: "12px"
  pill: "999px"
spacing:
  hairline: "4px"
  tight: "8px"
  base: "12px"
  gutter: "16px"
  sheet: "18px"
  section: "40px"
components:
  button:
    backgroundColor: "{colors.page-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.control}"
    padding: "7px 12px"
  button-primary:
    backgroundColor: "{colors.step-light}"
    textColor: "{colors.step-light-ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.control}"
    padding: "7px 12px"
  tab:
    textColor: "{colors.pencil}"
    typography: "{typography.body-small}"
    rounded: "{rounded.control}"
    padding: "8px 12px"
  tab-active:
    backgroundColor: "{colors.step-light}"
    textColor: "{colors.step-light-ink}"
    rounded: "{rounded.control}"
  sheet:
    backgroundColor: "{colors.page}"
    rounded: "{rounded.sheet}"
    padding: "{spacing.sheet}"
  note:
    backgroundColor: "{colors.page-tint}"
    rounded: "{rounded.note}"
    padding: "12px 14px"
  key-chip:
    backgroundColor: "{colors.key-graphite}"
    textColor: "{colors.key-legend}"
    typography: "{typography.key-legend}"
    rounded: "{rounded.key}"
    padding: "0.12em 0.45em"
  lcd-chip:
    backgroundColor: "{colors.lcd-glass}"
    textColor: "{colors.lcd-red}"
    typography: "{typography.key-legend}"
    rounded: "{rounded.lcd}"
    padding: "0.08em 0.4em"
  step-cell:
    backgroundColor: "{colors.page}"
    rounded: "{rounded.cell}"
    height: "26px"
  step-cell-on:
    backgroundColor: "{colors.step-light}"
    rounded: "{rounded.cell}"
    height: "26px"
  branch-tile:
    backgroundColor: "{colors.page}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sheet}"
    padding: "14px 16px"
---

# Design System: Тренажёр Roland P-6

## Overview

**Creative North Star: "Тетрадь битмейкера"**

The guide is a beatmaker's study notebook kept next to the device. Its pages are ruled and orderly: numbered lessons, step grids drawn like squared paper, chord sketches on a one-octave keyboard, short fact lists with the term on its own line. Reading comes first; nothing on the page competes with the instruction the learner is following with the P-6 in hand.

The device lives in the details, the way stickers and margin sketches live in a real notebook. Button names are drawn as small graphite key chips with a hard bottom edge, display readouts as red seven-segment chips on dark glass, and the panel explorer as a faithful drawing of the hardware. These are the only raised, tactile things on the page: the interface is quiet, the instrument is tactile.

One accent carries meaning. Teal "step light" marks what is on: the current tab, a lit sequencer step, a link to follow, the trunk of the branch tree. Pages are flat; depth is two tonal steps of paper, a hairline rule and nothing else. Density stays calm on phones: no card chrome below 560px, hairline dividers instead.

**Key Characteristics:**
- Notebook structure first: numbered lessons, ruled step grids, fact lists, one-octave chord sketches.
- Hardware details as the only relief: graphite key chips and red LCD chips inside running text, a faithful panel drawing.
- One meaningful accent, "step light", for on, current and link.
- Flat paper surfaces in two tones with hairline rules; no shadows anywhere.
- Six type sizes, three families with fixed roles: display, reading, device.

## Colors

A cool graphite-and-paper neutral palette with one teal signal color and the P-6's own red display.

### Primary
- **Step Light** (#1f6f86 light / #5fb7cf dark): the color of things that are on. Active tab, lit step in a grid, primary button, progress fill, links, the branch-tree trunk. Text on it is Step Light Ink (#ffffff light / #0d1316 dark). Step Light Soft (#d6e8ee / #1d3540) is its quiet tint for selected backgrounds.

### Tertiary
- **LCD Red** (#ff5a36 light / #ff6a45 dark) on **LCD Glass** (#1a0d0a): reserved for reproductions of the P-6 seven-segment display (display readouts in text, the hero display, the panel drawing). Never used as a UI accent.

### Neutral
- **Ink** (#16181c / #e9ebef): body text and headings.
- **Pencil** (#596170 / #9aa3b2): secondary text, metadata, inactive tabs. Meets 4.5:1 on every surface in both themes.
- **Paper** (#e7e9ec / #121417): the page background.
- **Page** (#f6f7f8 / #1b1e23): sheets, lessons, branch tiles on desktop.
- **Page Tint** (#eef0f2 / #22262c): notes inside a lesson, secondary buttons, grid wells.
- **Rule Line** (#cbd0d7 / #2f343c): hairline borders and dividers.
- **Key Graphite** (#2a2d33 / #3a3f47) with **Key Legend** (#f1f2f4) and **Key Edge** (#111316): button chips that name a P-6 control.
- **Done Green** (#2a7146 / #5cc487): completed steps and lessons, checkbox accent.
- **Warning Amber** (#8a5000 / #e0a446): "Важно" labels only.

### Named Rules
**The One Lit Step Rule.** Step Light means "on, current or follow this". It is never decoration: no accent headings, borders or backgrounds without a state behind them.

**The Display Is The Device Rule.** LCD Red appears only where the P-6 display is being reproduced. If it is not something the screen of the device would show, it is not red.

## Typography

**Display Font:** Unbounded (with Manrope, system-ui)
**Body Font:** Manrope (with system-ui, -apple-system, Segoe UI)
**Label/Mono Font:** JetBrains Mono (with ui-monospace, Menlo)

**Character:** Unbounded is the wide notebook cover lettering, used only for the page title and section headings. Manrope does all the reading, including lesson titles in bold. JetBrains Mono is the device voice: key legends, display text, eyebrow labels, step numbers.

### Hierarchy
- **Display** (700, clamp(1.75rem, 5vw, 2.5rem), 1.2): the page title only.
- **Headline** (700, 1.375rem, 1.2; 1.25rem on phones): section and branch headings.
- **Title** (700, 1.125rem, 1.2; 1.0625rem on phones): lesson titles, fact headings at 1rem.
- **Body** (400, 1rem, 1.55): lesson steps and explanations, capped at 68ch.
- **Body Small** (400, 0.875rem, 1.5): metadata, notes, tables, buttons.
- **Label** (700, 0.75rem, 0.08em, uppercase): eyebrows like «ЗАНЯТИЕ 1», «ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ», table headers.
- **Key Legend** (700, 0.78em, 0.02em, line-height 1.3): button and display chips inside running text; they never push lines apart.

### Named Rules
**The Six Sizes Rule.** Text uses the six scale steps (12/14/16/18/22 px and the fluid title). Step-grid labels (9–11 px) are the only exception, because 16 columns must fit a phone.

**The Device Voice Rule.** Mono type means "this is on the P-6 or about the P-6 grid". Do not set prose in mono.

## Layout

A single reading column (max 980px) with a 16px side gutter, sticky tab bar at the top, content as a vertical sequence of sheets. Lesson bodies keep text at 68ch; fact lists run in two balanced columns on wide screens and one column with hairline dividers on phones. Branch tiles hang off a vertical trunk line, one per row. Step grids are 16 equal columns with a gap between every four steps; the triplet grid groups by three.

Below 560px the page goes flat: sheets, lessons, notes, grids and chord cards lose background, border and radius, and hairline rules separate them. Primary controls grow to 44px, checkboxes to 24px. Anchored jumps and keyboard focus stop below the sticky tab bar (64px scroll padding). No horizontal scroll at 375px with text at 200%, except inside grids, tables and the panel drawing, which scroll in their own containers.

### Named Rules
**The Notebook Rhythm Rule.** One idea per line group: a short heading on its own line, the explanation under it, space or a hairline before the next. Never a bold lead-in buried in a paragraph run.

## Elevation & Depth

Flat by default. Depth is tonal: Paper behind Page, Page Tint for notes inside a page, a 1px Rule Line where two surfaces meet. There are no box shadows in the interface. The only relief in the system belongs to the device: the 2px Key Edge under key chips and the soft red glow of LCD text (text-shadow 0 0 6px at 50% of LCD Red).

### Named Rules
**The Hardware-Only Relief Rule.** Only elements that depict the P-6 (key chips, LCD chips, the panel drawing) may have bottom edges, glows or inset rings. Interface components stay flat; pressed feedback is a brightness change, never a lift or shadow.

## Shapes

Soft, small radii that step up with the size of the surface: LCD chips 3px, step cells 4px, key chips 5px, controls and tabs 8px, notes 10px, sheets and tiles 12px, progress bars and tags fully round. Knobs, jacks and round buttons in the panel drawing are circles. Borders are 1px hairlines; the branch trunk and its connectors are the only heavy strokes (4px and 2px in Step Light).

## Components

### Buttons
- **Shape:** gently rounded (8px).
- **Default:** Page Tint background, Ink text, 1px Rule Line, Body Small bold, padding 7px 12px; 44px minimum height on phones.
- **Primary:** Step Light background and border, Step Light Ink text. Used for one action per block (play, roll the dice, load code).
- **Pressed / Focus:** brightness 0.88 while pressed, 0.12s; a 2px Step Light focus ring offset 2px. Toggle buttons expose aria-pressed.

### Chips
- **Key chip:** Key Graphite fill, Key Legend text in Key Legend type, 5px radius, 2px Key Edge bottom border. The secondary function is set lighter after the key name: `G VOICE`.
- **LCD chip:** LCD Glass fill, LCD Red mono text with 0.08em tracking and a soft glow, 3px radius. Shows exactly what the P-6 display shows.

### Cards / Containers
- **Sheet:** Page background, 1px Rule Line, 12px radius, 18px padding; flat on phones.
- **Note:** Page Tint, 10px radius, padding 12px 14px, Label eyebrow on top («ВАЖНО» in Warning Amber, «ТВОРЧЕСКОЕ ЗАДАНИЕ» in Step Light).
- **Lesson:** a collapsible sheet; the summary row holds a mono number badge (6px radius, Page Tint; Done Green when complete), the title, the session estimate and a step counter.

### Navigation
- **Tab bar:** sticky, Page background, Pencil bold Body Small tabs with 8px radius; the active tab is a Step Light pill. On phones it scrolls sideways with a fade at the right edge and keeps the active tab in view.

### Step Grid (signature)
16 cells per row in a Page Tint well, 26px tall, 4px radius, 1px Rule Line. A lit cell is Step Light; probability shows as a 45% lit cell with its percentage, ratchets as ×N, velocity and level as a Step Light bar from the bottom. Step numbers sit on top in mono, the beat numbers (1, 5, 9, 13) in Step Light, the P-6 key names under them. The playhead is a 2px LCD Red outline.

### Branch Tree (signature)
A 4px Step Light trunk with 2px connectors to branch tiles: Page sheets with a Unbounded name, «Открыть →» in Step Light, a lesson list and a progress line.

## Do's and Don'ts

### Do:
- **Do** reserve Step Light (#1f6f86 / #5fb7cf) for on, current and link states.
- **Do** write every P-6 control as a key chip and every display readout as an LCD chip.
- **Do** keep headings on their own line in fact lists, with 18px rhythm and hairline dividers on phones.
- **Do** keep text on the six-step scale and body copy at 16px with 1.55 line height, 68ch max.
- **Do** keep primary controls at 44px and checkboxes at 24px on phones.
- **Do** check both themes: secondary text and warning colors stay at 4.5:1 or better.

### Don't:
- **Don't** add box shadows, lifts or glows to interface components; relief belongs to the device only.
- **Don't** use LCD Red outside display reproductions.
- **Don't** use emoji as icons; use inline SVG in currentColor.
- **Don't** bring card chrome back on phones.
- **Don't** set prose in mono or headings in mono.
