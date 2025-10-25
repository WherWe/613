#!/usr/bin/env python3
"""
Add main_category field to each mitzvah based on category_hierarchy.json mapping.
The existing 'category' field becomes the subcategory, and we add a new 'main_category' field.
"""

import json

def add_main_categories():
    # Load the hierarchy mapping
    with open('category_hierarchy.json', 'r', encoding='utf-8') as f:
        hierarchy = json.load(f)
    
    subcategory_to_main = hierarchy['subcategory_to_main']
    
    # Load mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Track statistics
    updated_count = 0
    missing_mapping = []
    
    # Update each mitzvah
    for mitzvah in data['mitzvot']:
        if 'classification' in mitzvah and 'category' in mitzvah['classification']:
            subcategory = mitzvah['classification']['category']
            
            if subcategory in subcategory_to_main:
                # Add main_category field
                mitzvah['classification']['main_category'] = subcategory_to_main[subcategory]
                # Rename category to sub_category for clarity
                mitzvah['classification']['sub_category'] = subcategory
                del mitzvah['classification']['category']
                updated_count += 1
            elif subcategory:
                missing_mapping.append(subcategory)
    
    # Save updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated {updated_count} mitzvot with main_category field")
    
    if missing_mapping:
        print(f"\n⚠️  Found {len(missing_mapping)} mitzvot with unmapped categories:")
        for cat in set(missing_mapping):
            print(f"   - {cat}")
    else:
        print("✅ All categories successfully mapped!")
    
    # Print summary of main categories
    main_cat_counts = {}
    for mitzvah in data['mitzvot']:
        if 'classification' in mitzvah and 'main_category' in mitzvah['classification']:
            main_cat = mitzvah['classification']['main_category']
            main_cat_counts[main_cat] = main_cat_counts.get(main_cat, 0) + 1
    
    print(f"\n📊 Main Category Distribution:")
    for cat in sorted(main_cat_counts.keys()):
        print(f"   {cat}: {main_cat_counts[cat]} mitzvot")

if __name__ == '__main__':
    add_main_categories()
