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

<!-- impeccable:design-map -->
Name: Тренажёр Roland P-6
Colors: primary: step-light #1f6f86; tertiary: lcd-glass #1a0d0a; neutral: paper #e7e9ec; primary: step-light-ink #ffffff; primary: step-light-soft #d6e8ee; primary: step-light-dark #5fb7cf (+23 more in the sidecar)
Fonts: Unbounded (display, headline); Manrope (title, body, body-small); JetBrains Mono (label, key-legend)
Spacing: hairline 4px, tight 8px, base 12px, gutter 16px, sheet 18px, section 40px
Radius: lcd 3px, cell 4px, key 5px, control 8px, note 10px, sheet 12px, pill 999px
North Star: "Тетрадь битмейкера"
Rules:
- The One Lit Step Rule. Step Light means "on, current or follow this".
- The Display Is The Device Rule. LCD Red appears only where the P-6 display is being reproduced.
- The Six Sizes Rule. Text uses the six scale steps (12/14/16/18/22 px and the fluid title).
- The Device Voice Rule. Mono type means "this is on the P-6 or about the P-6 grid".
- The Notebook Rhythm Rule. One idea per line group: a short heading on its own line, the explanation under it, space or a hairline before the next.
- The Hardware-Only Relief Rule. Only elements that depict the P-6 (key chips, LCD chips, the panel drawing) may have bottom edges, glows or inset rings.
Don't:
- Don't add box shadows, lifts or glows to interface components; relief belongs to the device only.
- Don't use LCD Red outside display reproductions.
- Don't use emoji as icons; use inline SVG in currentColor.
- Don't bring card chrome back on phones.
- Don't set prose in mono or headings in mono.
Do:
- Do reserve Step Light (#1f6f86 / #5fb7cf) for on, current and link states.
- Do write every P-6 control as a key chip and every display readout as an LCD chip.
- Do keep headings on their own line in fact lists, with 18px rhythm and hairline dividers on phones.
- Do keep text on the six-step scale and body copy at 16px with 1.55 line height, 68ch max.
- Do keep primary controls at 44px and checkboxes at 24px on phones.
- Do check both themes: secondary text and warning colors stay at 4.5:1 or better.
Full: .impeccable/design-full.md (read a section when you need its detail)
