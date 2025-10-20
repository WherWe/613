# 613 Mitzvot - Developer Notes

A lightweight, static web app to explore the 613 mitzvot from Sefer HaChinukh, with a dynamic table and Hebrew title support.

## Tech Stack

- Frontend: Static HTML + vanilla JavaScript + CSS
- Data: JSON files (English and Hebrew variants)
- Local server: Python `http.server` via `serve.py` (adds CORS headers)
- Shell helper: `start_server.sh` (starts the local server)

## Repository Structure

```
613/
├─ 613_mitzvot_dynamic.html     # Main interactive UI (search, filter, sort, pagination)
├─ mitzvot_data.json            # English data (metadata + mitzvot array)
├─ mitzvot_data_he.json         # Hebrew data (metadata + mitzvot array)
├─ Sefer HaChinukh - en - merged.json  # Source (English) - reference
├─ Sefer HaChinukh - he - merged.json  # Source (Hebrew)  - reference
├─ serve.py                     # Local HTTP server with permissive CORS
├─ start_server.sh              # Convenience script to start the server
├─ 613.code-workspace           # VS Code workspace file
└─ .vscode/                     # VS Code tasks, etc.
```

## Data Model (JSON)

Top-level shape:

- `metadata`: title, source, counts, last_updated
- `mitzvot`: array of entries with:
  - `id` (number)
  - `title` (string) — English in `mitzvot_data.json`, Hebrew in `mitzvot_data_he.json`
  - `description` (string)
  - `type` ("Positive" | "Negative")
  - `parasha` (string)
  - `full_text` (HTML string)
  - `details` (string[])

In the dynamic app, each mitzvah is augmented at runtime with `title_he` (from the Hebrew JSON) by matching `id`.

## Dynamic App (613_mitzvot_dynamic.html)

- Fetches `mitzvot_data.json` (base) and `mitzvot_data_he.json` (optional).
- Maps Hebrew titles by `id` and adds `title_he` to items when available.
- Renders a table with columns: `#`, `Type`, `Mitzvah`, `Description`, `Parasha`, `Details`.
- In the `Mitzvah` column, shows English title and, if present, the Hebrew title below it (RTL styled).
- Supports:
  - Search (English title, Hebrew title, description)
  - Filters (Type, Parasha)
  - Sorting (Number, Title, Type, Parasha)
  - Pagination (default 50 per page)
  - Expand/collapse details per row

## Running Locally

Option A — if no server is running:

```bash
bash start_server.sh
```

Then open:

- http://localhost:8000/613_mitzvot_dynamic.html

Option B — if a server is already running on port 8000:

- Just open the URL directly without restarting.

## Notes on CORS and Serving

`serve.py` starts a simple HTTP server on `http://localhost:8000`, with permissive CORS headers so the dynamic page can fetch JSON from the same root without issues.

## Recent Cleanup

- Removed debug/analysis scripts (debug*\*.py, test*\*.py) that were not part of the runtime flow.
- Simplified `serve.py` output and fixed indentation.
- Simplified `start_server.sh` with safer defaults and reduced noise.
- Search now includes Hebrew titles; titles render with RTL where applicable.

## Core Classifications (Base Layer)

Before adding collectible/game metadata, every mitzvah can be enriched with basic halakhic classifications to enable meaningful filtering, grouping, and study views.

Optional per-mitzvah object:

```json
"classification": {
  "category": "string",
  "sub_category": "string",
  "applies_to": ["Men", "Women", "Kohanim", "Levites", "All Israel", "Kings"],
  "location": "Anywhere | Eretz Yisrael | Temple",
  "time_scope": "Always | Temple Era | Festival | Conditional",
  "source_refs": ["Talmud:Yevamot 61b", "Shulchan Arukh:EH 1"]
}
```

Notes:

- This classification is language-agnostic and should be keyed by `id`.
- It can be embedded directly in `mitzvot_data.json` entries or maintained in a separate mapping and merged at load time.
- `applies_to` is a set-like array; order is not significant.
- `source_refs` are free-form references; a future enhancement can normalize them.

## Future Enhancements (Optional)

- Add a toggle to show/hide Hebrew titles or a dedicated Hebrew column.
- Add sorting by Hebrew title.
- Add UI filters for classification (applies_to, location, time_scope, category).
- Parameterize source file paths for better portability.
- Add a small unit test harness for data integrity checks.

```

```
