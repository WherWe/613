#!/usr/bin/env python3
"""
Apply parasha→book mapping to datasets.
- Reads parasha_book_map.json (EN/HE canonical names and order)
- Adds fields to each mitzvah:
  - book_en, book_he
  - parasha_en (normalized via aliases), parasha_he (unchanged if already Hebrew)
  - book_order (1..5), parasha_order_within_book (1..N), global_order (1..54)

Assumptions:
- mitzvot_data.json uses English parasha names; mitzvot_data_he.json uses Hebrew parasha names.
- Both files already have correct parasha values (synced from contents).

Outputs:
- Updates mitzvot_data.json and mitzvot_data_he.json in place.
- Writes a quick summary of counts per book.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent
MAP_PATH = ROOT / 'parasha_book_map.json'
EN_PATH = ROOT / 'mitzvot_data.json'
HE_PATH = ROOT / 'mitzvot_data_he.json'


def load_mapping():
    data = json.loads(MAP_PATH.read_text(encoding='utf-8'))
    # Build lookup dicts
    parasha_to_book_en = {}
    parasha_to_book_he = {}
    parasha_en_to_order = {}
    aliases = {k.lower(): v for k, v in data.get('aliases', {}).items()}

    global_list = []
    global_idx = 0
    for book in data['books']:
        book_order = book['order']
        book_en = book['en']
        book_he = book['he']
        for p in book['parashot']:
            parasha_en = p['en']
            parasha_he = p['he']
            order_in_book = p['order']
            global_idx += 1
            parasha_to_book_en[parasha_en] = (book_en, book_he, book_order, order_in_book, global_idx)
            parasha_to_book_he[parasha_he] = (book_en, book_he, book_order, order_in_book, global_idx)
            parasha_en_to_order[parasha_en.lower()] = parasha_en
            global_list.append((book_en, parasha_en))
    return {
        'parasha_to_book_en': parasha_to_book_en,
        'parasha_to_book_he': parasha_to_book_he,
        'aliases': aliases,
        'parasha_en_to_order': parasha_en_to_order,
    }


def normalize_parasha_en(name: str, aliases: dict, parasha_en_to_order: dict) -> str:
    if not name:
        return name
    key = name.strip().lower()
    # First resolve alias
    if key in aliases:
        key = aliases[key].lower()
    # Then map to canonical casing
    canonical = parasha_en_to_order.get(key)
    return canonical or name


def apply_to_file(path: Path, lang: str, mapping: dict):
    root_data = json.loads(path.read_text(encoding='utf-8'))
    # Handle structure: root_data['mitzvot'] is the array
    data = root_data.get('mitzvot', [])
    counts = defaultdict(int)

    parasha_to_book_en = mapping['parasha_to_book_en']
    parasha_to_book_he = mapping['parasha_to_book_he']
    aliases = mapping['aliases']
    parasha_en_to_order = mapping['parasha_en_to_order']

    updated = 0
    missing = []
    for item in data:
        parasha = item.get('parasha')
        if lang == 'en':
            parasha_norm = normalize_parasha_en(parasha, aliases, parasha_en_to_order)
            info = parasha_to_book_en.get(parasha_norm)
        else:
            info = parasha_to_book_he.get(parasha)
        if not info:
            missing.append(parasha)
            continue
        book_en, book_he, book_order, order_in_book, global_order = info
        item['book_en'] = book_en
        item['book_he'] = book_he
        item['book_order'] = book_order
        item['parasha_order_within_book'] = order_in_book
        item['global_parasha_order'] = global_order
        if lang == 'en':
            item['parasha'] = parasha_norm
        counts[book_en] += 1
        updated += 1
    # Write back the entire structure
    path.write_text(json.dumps(root_data, ensure_ascii=False, indent=2), encoding='utf-8')
    return updated, counts, sorted(set(missing))


def main():
    mapping = load_mapping()
    results = {}
    updated_en, counts_en, missing_en = apply_to_file(EN_PATH, 'en', mapping)
    updated_he, counts_he, missing_he = apply_to_file(HE_PATH, 'he', mapping)
    results['en'] = {
        'updated': updated_en,
        'counts': dict(counts_en),
        'missing_parasha_names': missing_en,
    }
    results['he'] = {
        'updated': updated_he,
        'counts': dict(counts_he),
        'missing_parasha_names': missing_he,
    }
    # Sort books by book_order manually for clean output
    # Build a mapping of book_en → book_order from the mapping data
    book_to_order_en = {book_en: book_order for book_en, _, book_order, _, _ in mapping['parasha_to_book_en'].values()}
    
    summary_lines = [
        f"EN updated: {updated_en}",
        *(f"  {book}: {count}" for book, count in sorted(counts_en.items(), key=lambda x: book_to_order_en.get(x[0], 999))),
        f"EN missing parasha names: {missing_en}",
        f"HE updated: {updated_he}",
        *(f"  {book}: {count}" for book, count in sorted(counts_he.items(), key=lambda x: book_to_order_en.get(x[0], 999))),
        f"HE missing parasha names: {missing_he}",
    ]
    print("\n".join(summary_lines))


if __name__ == '__main__':
    main()
