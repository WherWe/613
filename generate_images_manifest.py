#!/usr/bin/env python3
import json
import os
from pathlib import Path

ROOT = Path(__file__).parent
IMG_DIR = ROOT / "images"

# Map of mitzvah id (string) -> available extension (prefer png, then jpg, then jpeg)
priority = ["png", "jpg", "jpeg"]
by_id = {}

for entry in IMG_DIR.iterdir():
    if not entry.is_file():
        continue
    name = entry.name
    # Only consider exact numeric base names like 123.png (ignore 123_2.png)
    parts = name.rsplit(".", 1)
    if len(parts) != 2:
        continue
    base, ext = parts
    ext = ext.lower()
    if not base.isdigit():
        continue
    if ext not in priority:
        continue
    # Choose highest priority ext
    existing = by_id.get(base)
    if existing is None or priority.index(ext) < priority.index(existing):
        by_id[base] = ext

manifest = {
    "count": len(by_id),
    "byId": by_id,
    "ids": sorted([int(k) for k in by_id.keys()]),
}

# Write JSON and JS versions
json_path = ROOT / "images_manifest.json"
js_path = ROOT / "images_manifest.js"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

with open(js_path, "w", encoding="utf-8") as f:
    f.write("window.MITZVOT_IMAGES_MANIFEST = ")
    json.dump(manifest, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";")

print(f"Wrote {json_path} and {js_path} with {manifest['count']} entries.")
