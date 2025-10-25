#!/usr/bin/env python3
"""
Add main_location field to each mitzvah based on location_hierarchy.json mapping.
The existing 'location' field stays intact, we add a new 'main_location' field with broader categories.
"""

import json

def add_main_location():
    # Load the hierarchy mapping
    with open('location_hierarchy.json', 'r', encoding='utf-8') as f:
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
        if 'classification' in mitzvah and 'location' in mitzvah['classification']:
            specific_location = mitzvah['classification']['location']
            
            if specific_location in specific_to_main:
                # Add main_location field
                mitzvah['classification']['main_location'] = specific_to_main[specific_location]
                updated_count += 1
            elif specific_location:
                missing_mapping.append(specific_location)
    
    # Save updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated {updated_count} mitzvot with main_location field")
    
    if missing_mapping:
        print(f"\n⚠️  Found {len(missing_mapping)} unmapped location values:")
        for loc in set(missing_mapping):
            print(f"   - {loc}")
    else:
        print("✅ All location values successfully mapped!")
    
    # Print summary of main locations
    main_location_counts = {}
    for mitzvah in data['mitzvot']:
        if 'classification' in mitzvah and 'main_location' in mitzvah['classification']:
            main_loc = mitzvah['classification']['main_location']
            main_location_counts[main_loc] = main_location_counts.get(main_loc, 0) + 1
    
    print(f"\n📊 Main Location Distribution:")
    for loc in sorted(main_location_counts.keys()):
        print(f"   {loc}: {main_location_counts[loc]} mitzvot")

if __name__ == '__main__':
    add_main_location()
