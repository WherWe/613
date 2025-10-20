#!/usr/bin/env python3
"""
Sync parasha fields in mitzvot_data.json and mitzvot_data_he.json
to match the mapping implied by contents.html and contents-he.html.

Source of truth:
- contents.html (English parasha names)
- contents-he.html (Hebrew parasha names)

Extraction logic:
- Each parasha block is a <div class="schema-node-toc" data-ref="Sefer HaChinukh, <PARASHA>"> ...
  with a list of <a href="/Sefer_HaChinukh.<ID>"> items inside.
- For Hebrew names, use the first <span class="contentSpan he"> under the parasha header.

Outputs:
- Updates JSON files in place.
- Prints a short mismatch summary (counts + a few examples).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EN_CONTENTS = ROOT / "contents.html"
HE_CONTENTS = ROOT / "contents-he.html"
EN_JSON = ROOT / "mitzvot_data.json"
HE_JSON = ROOT / "mitzvot_data_he.json"


def parse_parasha_map_en(html: str) -> dict[int, str]:
    """Parse contents.html -> {mitzvah_id: parasha_en}.

    Relies on data-ref="Sefer HaChinukh, <PARASHA>" and anchors with href /Sefer_HaChinukh.<ID>.
    """
    mapping: dict[int, str] = {}

    # Find each parasha block start
    block_iter = list(re.finditer(r'<div\s+class="schema-node-toc"[^>]*data-ref="Sefer HaChinukh,\s*([^"]+)"', html))
    for i, m in enumerate(block_iter):
        parasha = m.group(1).strip()
        start = m.end()
        end = block_iter[i + 1].start() if i + 1 < len(block_iter) else len(html)
        block = html[start:end]
        for id_m in re.finditer(r'href="/Sefer_HaChinukh\.(\d+)"', block):
            mitzvah_id = int(id_m.group(1))
            mapping[mitzvah_id] = parasha
    return mapping


def parse_parasha_map_he(html: str) -> dict[int, str]:
    """Parse contents-he.html -> {mitzvah_id: parasha_he}.

    For Hebrew names, prefer the visible hebrew title under the parasha header
    (span.contentSpan.he before the list). If not found, fallback to the data-ref value.
    """
    mapping: dict[int, str] = {}

    # Find each parasha container with both data-ref and the header span nearby
    block_iter = list(re.finditer(r'<div\s+class="schema-node-toc"[^>]*data-ref="Sefer HaChinukh,\s*([^"]+)"', html))
    for i, m in enumerate(block_iter):
        # Default (fallback) from data-ref (English transliteration)
        fallback_parasha = m.group(1).strip()
        start = m.end()
        end = block_iter[i + 1].start() if i + 1 < len(block_iter) else len(html)
        block = html[start:end]

        # Try to capture the Hebrew parasha title that appears in the header before the list
        # Limit search to header area (before the schema-node-contents div) to avoid mitzvah item titles
        header_end = block.find('<div class="schema-node-contents"')
        header_chunk = block[: header_end if header_end != -1 else min(len(block), 1000)]
        he_title_m = re.search(r'<span\s+class="contentSpan\s+he"[^>]*>([^<]+)</span>', header_chunk)
        parasha_he = he_title_m.group(1).strip() if he_title_m else fallback_parasha

        for id_m in re.finditer(r'href="/Sefer_HaChinukh\.(\d+)"', block):
            mitzvah_id = int(id_m.group(1))
            mapping[mitzvah_id] = parasha_he
    return mapping


def update_json_parasha(json_path: Path, parasha_map: dict[int, str]) -> tuple[int, list[tuple[int, str, str]]]:
    """Update the parasha field in a JSON file using the provided map.

    Returns (updated_count, examples) where examples is a list of (id, old, new).
    """
    data = json.loads(json_path.read_text(encoding="utf-8"))
    examples: list[tuple[int, str, str]] = []
    updated = 0

    for item in data.get("mitzvot", []):
        mitzvah_id = item.get("id")
        if isinstance(mitzvah_id, int) and mitzvah_id in parasha_map:
            new_parasha = parasha_map[mitzvah_id]
            old_parasha = item.get("parasha")
            if old_parasha != new_parasha:
                item["parasha"] = new_parasha
                updated += 1
                if len(examples) < 10:
                    examples.append((mitzvah_id, str(old_parasha), new_parasha))

    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return updated, examples


def main() -> None:
    # Read contents files
    en_html = EN_CONTENTS.read_text(encoding="utf-8")
    he_html = HE_CONTENTS.read_text(encoding="utf-8")

    en_map = parse_parasha_map_en(en_html)
    he_map = parse_parasha_map_he(he_html)

    # Sanity check: there should be at least a few hundred ids mapped
    print(f"Parsed {len(en_map)} English mappings and {len(he_map)} Hebrew mappings.")

    # Update JSON files
    en_updated, en_examples = update_json_parasha(EN_JSON, en_map)
    he_updated, he_examples = update_json_parasha(HE_JSON, he_map)

    print(f"Updated {en_updated} parasha fields in {EN_JSON.name}.")
    if en_examples:
        print("Examples (EN):")
        for i, old, new in en_examples:
            print(f"  id={i}: '{old}' -> '{new}'")

    print(f"Updated {he_updated} parasha fields in {HE_JSON.name}.")
    if he_examples:
        print("Examples (HE):")
        for i, old, new in he_examples:
            print(f"  id={i}: '{old}' -> '{new}'")


if __name__ == "__main__":
    main()
