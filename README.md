# 613 Mitzvot

A lightweight, static web app to explore the 613 mitzvot from Sefer HaChinukh, with dynamic filtering, search, and Hebrew/English support.

## Tech Stack

- **Static HTML/CSS/JavaScript** - No build step required for the app itself
- **Vercel** - Static hosting and deployment
- **Bootstrap 5** - UI framework
- **Tom Select** - Advanced select/filter controls
- **Lucide Icons** - Icon set
- **SweetAlert2** - Modal dialogs
- **Fontsource** - Self-hosted fonts (Cardo, Noto Serif Hebrew, Roboto)

## Repository Structure

```
613/
├─ index.html                   # Main interactive UI (search, filter, sort, pagination)
├─ mitzvot_data.json            # English data (metadata + mitzvot array)
├─ mitzvot_data_he.json         # Hebrew data (metadata + mitzvot array)
├─ parasha_book_map.json        # Parasha-to-book mapping data
├─ package.json                 # Node.js dependencies for tooling
├─ vercel.json                  # Vercel deployment configuration
├─ styles/
│   ├─ app.css                  # Main application styles
│   └─ fonts.css                # Font definitions
├─ scripts/
│   └─ build-vendor.js          # Copies dependencies to vendor/
├─ vendor/                      # Self-hosted dependencies (generated)
│   ├─ @fontsource/
│   ├─ bootstrap/
│   ├─ lucide/
│   ├─ sweetalert2/
│   └─ tom-select/
├─ Sefer HaChinukh/             # Source data files
│   ├─ Sefer HaChinukh - en - merged.json  # English source
│   ├─ Sefer HaChinukh - he - merged.json  # Hebrew source
│   ├─ contents.html            # English table of contents
│   └─ contents-he.html         # Hebrew table of contents
├─ Archive/                     # Data processing scripts
│   ├─ add_classifications.py
│   ├─ add_classifications_151_180.py
│   ├─ apply_parasha_book_mapping.py
│   └─ sync_parasha_from_contents.py
└─ 613.code-workspace           # VS Code workspace file
```

## Data Model

Top-level JSON structure:

```json
{
  "metadata": {
    "title": "string",
    "source": "string",
    "counts": {...},
    "last_updated": "date"
  },
  "mitzvot": [...]
}
```

Each mitzvah entry:

```json
{
  "id": 1,
  "title": "string",
  "description": "string",
  "type": "Positive" | "Negative",
  "parasha": "string",
  "full_text": "HTML string",
  "details": ["string"],
  "classification": {
    "category": "string",
    "sub_category": "string",
    "applies_to": ["Men", "Women", "Kohanim", ...],
    "location": "Anywhere | Eretz Yisrael | Temple",
    "time_scope": "Always | Temple Era | Festival | Conditional",
    "source_refs": ["reference strings"]
  }
}
```

**Data Loading:**

- `index.html` fetches `mitzvot_data.json` (English) and `mitzvot_data_he.json` (Hebrew)
- Hebrew titles are merged at runtime by matching `id`
- Each mitzvah displays with both English and Hebrew titles (Hebrew styled RTL)

## Features

- **Search**: Full-text search across English title, Hebrew title, and description
- **Filtering**: Filter by Type (Positive/Negative), Parasha, and classification metadata
- **Sorting**: Sort by Number, Title, Type, or Parasha
- **Pagination**: Configurable items per page (default 50)
- **Details**: Expandable rows showing full text and additional details
- **Bilingual**: Displays Hebrew and English titles side-by-side

## Development

### Local Preview

The app requires HTTP serving to load JSON files via `fetch()`. Use one of these methods:

**Option 1: VS Code Simple Browser Extension**

1. Install the "Simple Browser" extension in VS Code
2. Open `index.html`
3. Right-click and select "Preview in Simple Browser"

**Option 2: Python HTTP Server**

```bash
python3 Archive/server/serve.py
# Then open http://localhost:8000
```

**Option 3: Any HTTP Server**

```bash
npx serve .
# or
python3 -m http.server 8000
```

### Managing Dependencies

After adding or updating npm dependencies:

```bash
npm install
node scripts/build-vendor.js
```

This copies necessary files from `node_modules/` to `vendor/` for static hosting.

### Deployment

The app is deployed to Vercel with automatic deployment on push to the main branch:

- Production: [Your Vercel URL]
- Configuration: `vercel.json`

## Classification System

Each mitzvah can include structured metadata for advanced filtering and study:

**Classification Structure:**

- `category`: Main category (e.g., "Prayer", "Tzedakah", "Shabbat")
- `sub_category`: Specific subcategory
- `applies_to`: Array of who it applies to (e.g., ["Men"], ["Women"], ["Kohanim"])
- `location`: Where it applies ("Anywhere", "Eretz Yisrael", "Temple")
- `time_scope`: When it applies ("Always", "Temple Era", "Festival", "Conditional")
- `source_refs`: Array of source references (Torah, Talmud, Shulchan Arukh, etc.)

**Classification Workflow:**

1. Read the original mitzvah entry in `Sefer HaChinukh/Sefer HaChinukh - en - merged.json`
2. Extract structured metadata from the "Roots" and "Laws" sections
3. Create a Python script (see `Archive/add_classifications.py` as template)
4. Run the script to merge classifications into `mitzvot_data.json`

Classifications are language-agnostic and keyed by `id`, allowing them to work with both English and Hebrew data.

## Data Processing Scripts

Python scripts in `Archive/` are used to enrich and maintain the mitzvah data:

- `add_classifications.py` - Template for adding classification metadata
- `add_classifications_151_180.py` - Example classification script for mitzvot 151-180
- `apply_parasha_book_mapping.py` - Maps parasha names to Torah books
- `sync_parasha_from_contents.py` - Syncs parasha data from source files

These scripts modify `mitzvot_data.json` directly. There is no build step for data files.

## Project Conventions

- **No CDN Dependencies**: All assets are self-hosted in `vendor/` for portability
- **No Build Step for Data**: JSON files are the single source of truth and loaded directly
- **Runtime Data Merging**: Hebrew titles and classifications are merged in the browser at load time
- **Static-First**: Designed for static hosting (Vercel) with no backend required
- **Self-Hosted Fonts**: Fonts loaded via Fontsource from `vendor/` directory

## Future Enhancements

- Add UI filters for classification fields (applies_to, location, time_scope, category)
- Add sorting by Hebrew title
- Add toggle to show/hide Hebrew titles
- Add keyboard navigation and shortcuts
- Add bookmarking/favorites functionality
- Add study mode with progress tracking
- Add export functionality (PDF, CSV, etc.)
- Add source reference linking to Sefaria or other Torah databases

```

```
