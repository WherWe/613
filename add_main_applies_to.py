#!/usr/bin/env python3
"""
Add main_applies_to field to each mitzvah based on applies_to_hierarchy.json mapping.
The existing 'applies_to' array stays intact, we add a new 'main_applies_to' array with broader groups.
"""

import json

def add_main_applies_to():
    # Load the hierarchy mapping
    with open('applies_to_hierarchy.json', 'r', encoding='utf-8') as f:
        hierarchy = json.load(f)
    
    specific_to_main = hierarchy['specific_to_main']
    
    # Load mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Track statistics
    updated_count = 0
    missing_mapping = []
    
    # Update each mitzvah
    for mitzvah in data['mitzvot']:
        if 'classification' in mitzvah and 'applies_to' in mitzvah['classification']:
            applies_to_list = mitzvah['classification']['applies_to']
            
            if isinstance(applies_to_list, list) and applies_to_list:
                # Map each specific value to its main group
                main_groups = set()
                for specific in applies_to_list:
                    if specific in specific_to_main:
                        main_groups.add(specific_to_main[specific])
                    elif specific:
                        missing_mapping.append(specific)
                
                if main_groups:
                    # Add main_applies_to as a sorted list (for consistency)
                    mitzvah['classification']['main_applies_to'] = sorted(list(main_groups))
                    updated_count += 1
    
    # Save updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated {updated_count} mitzvot with main_applies_to field")
    
    if missing_mapping:
        print(f"\n⚠️  Found {len(missing_mapping)} unmapped applies_to values:")
        for val in set(missing_mapping):
            print(f"   - {val}")
    else:
        print("✅ All applies_to values successfully mapped!")
    
    # Print summary of main groups
    main_group_counts = {}
    for mitzvah in data['mitzvot']:
        if 'classification' in mitzvah and 'main_applies_to' in mitzvah['classification']:
            for group in mitzvah['classification']['main_applies_to']:
                main_group_counts[group] = main_group_counts.get(group, 0) + 1
    
    print(f"\n📊 Main 'Applies To' Group Distribution:")
    for group in sorted(main_group_counts.keys()):
        print(f"   {group}: {main_group_counts[group]} mitzvot")

if __name__ == '__main__':
    add_main_applies_to()
