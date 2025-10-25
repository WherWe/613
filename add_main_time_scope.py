#!/usr/bin/env python3
"""
Add main_time_scope field to each mitzvah based on time_scope_hierarchy.json mapping.
The existing 'time_scope' field stays intact, we add a new 'main_time_scope' field with broader categories.
"""

import json

def add_main_time_scope():
    # Load the hierarchy mapping
    with open('time_scope_hierarchy.json', 'r', encoding='utf-8') as f:
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
        if 'classification' in mitzvah and 'time_scope' in mitzvah['classification']:
            specific_time_scope = mitzvah['classification']['time_scope']
            
            if specific_time_scope in specific_to_main:
                # Add main_time_scope field
                mitzvah['classification']['main_time_scope'] = specific_to_main[specific_time_scope]
                updated_count += 1
            elif specific_time_scope:
                missing_mapping.append(specific_time_scope)
    
    # Save updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated {updated_count} mitzvot with main_time_scope field")
    
    if missing_mapping:
        print(f"\n⚠️  Found {len(missing_mapping)} unmapped time_scope values:")
        for ts in set(missing_mapping):
            print(f"   - {ts}")
    else:
        print("✅ All time_scope values successfully mapped!")
    
    # Print summary of main time scopes
    main_time_scope_counts = {}
    for mitzvah in data['mitzvot']:
        if 'classification' in mitzvah and 'main_time_scope' in mitzvah['classification']:
            main_ts = mitzvah['classification']['main_time_scope']
            main_time_scope_counts[main_ts] = main_time_scope_counts.get(main_ts, 0) + 1
    
    print(f"\n📊 Main Time Scope Distribution:")
    for ts in sorted(main_time_scope_counts.keys()):
        print(f"   {ts}: {main_time_scope_counts[ts]} mitzvot")

if __name__ == '__main__':
    add_main_time_scope()
