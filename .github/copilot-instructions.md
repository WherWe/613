# Copilot Instructions for 613 Mitzvot Codebase

## Overview

This project is a static web app for exploring the 613 mitzvot (commandments) from Sefer HaChinukh, with dynamic filtering, search, and Hebrew/English support. The app is designed for static hosting (Vercel) and uses JSON files loaded via HTTP.

## Key Components

- **index.html**: Main interactive UI (search, filter, sort, pagination)
- **mitzvot_data.json / mitzvot_data_he.json**: English and Hebrew mitzvah data (see Data Model below)
- **scripts/build-vendor.js**: Copies runtime assets from node_modules to `vendor/` for static hosting
- **styles/fonts.css**: Loads self-hosted fonts via Fontsource

## Data Model

- Top-level JSON: `{ metadata, mitzvot: [ ... ] }`
- Each mitzvah: `{ id, title, description, type, parasha, full_text, details }`
- Hebrew titles are merged at runtime by matching `id` from `mitzvot_data_he.json`
- Optional `classification` object per mitzvah enables advanced filtering (see below)

## Classification Pattern

```json
"classification": {
  "category": "string",
  "sub_category": "string",
  "applies_to": ["Men", "Women", ...],
  "location": "Anywhere | Eretz Yisrael | Temple",
  "time_scope": "Always | Temple Era | Festival | Conditional",
  "source_refs": [ ... ]
}
```

- This is language-agnostic and keyed by `id`.
- Can be embedded in `mitzvot_data.json` or merged at load time.

## Developer Workflows

- **Local Preview**: Use VS Code's "Simple Browser" extension to preview at http://localhost (or any local web server)
- **Static Hosting**: Deploy to Vercel - just push to GitHub and Vercel auto-deploys
- **Vendor Assets**: Run `node scripts/build-vendor.js` after adding/updating dependencies to refresh `vendor/`

## Project Conventions

- Data is loaded via `fetch()` from JSON files (requires HTTP serving - use Simple Browser or deploy to Vercel)
- All data merges and enrichments (e.g., Hebrew titles, classifications) are done at runtime in the browser
- Font and JS/CSS dependencies are vendored for portability; no CDN dependencies in production
- Data files (`mitzvot_data.json`, `mitzvot_data_he.json`) are the single source of truth
- All Python scripts modify the JSON files directly; no build step for data

## Examples

- See `index.html` for UI logic and data loading patterns.
- See `add_classifications.py` for classification structure and enrichment logic.

## Classification Workflow

- Classifications are manually created by reading `Archive/Sefer HaChinukh - en - merged.json` (the original source text)
- Each mitzvah entry in Sefer HaChinukh contains:
  - "Roots" section explaining the reason/purpose
  - "Laws" section describing who it applies to, when, where, and how
  - Source references (Torah verses, Talmud, Shulchan Arukh, etc.)
- To add classifications:
  1. Read the relevant mitzvah entry in the source JSON
  2. Extract structured metadata into the classification fields (`category`, `applies_to`, `location`, `time_scope`, `source_refs`)
  3. Use `add_classifications.py` as a template to create a new classification script
  4. Run the script to merge classifications into `mitzvot_data.json`
- Example: For mitzvah #1, the text says "practiced in every place and at all times" and "not incumbent upon women" → becomes `location: "Anywhere"`, `time_scope: "Always"`, `applies_to: ["Men"]`

## Tips for AI Agents

- When adding new mitzvah data, ensure `id` is unique and matches across English/Hebrew files.
- When creating classifications, always reference the original Sefer HaChinukh text in `Archive/` as the source of truth.
- For new dependencies, update `scripts/build-vendor.js` and run it to refresh `vendor/`.
- To preview locally, use VS Code's Simple Browser or deploy to Vercel for testing.

---

For questions or feedback, see the contact in the project README.
