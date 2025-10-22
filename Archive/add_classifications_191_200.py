#!/usr/bin/env python3
"""
Add classifications for mitzvot 191-200
All are sexual prohibitions (incest laws) from Leviticus 18
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 191-200 (all incest prohibitions)
    classifications = {
        191: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Stepmother",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:8"]
        },
        192: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Sister",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:9", "Leviticus 18:11"]
        },
        193: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Granddaughter (Son's Daughter)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:10", "Sanhedrin 75a"]
        },
        194: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Granddaughter (Daughter's Daughter)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:10"]
        },
        195: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Daughter",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:10 (kal vachomer)", "Sanhedrin 76a"]
        },
        196: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Paternal Half-Sister",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:11"]
        },
        197: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Father's Sister (Aunt)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:12"]
        },
        198: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Mother's Sister (Aunt)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:13"]
        },
        199: {
            "category": "Sexual Prohibitions",
            "sub_category": "Homosexual Relations - Uncle",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:14", "Leviticus 18:22"]
        },
        200: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Uncle's Wife (Aunt)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:14", "Yevamot 97a"]
        }
    }
    
    # Add classifications to mitzvot
    for mitzvah in data['mitzvot']:
        mitzvah_id = mitzvah['id']
        if mitzvah_id in classifications:
            mitzvah['classification'] = classifications[mitzvah_id]
            print(f"Added classification for mitzvah #{mitzvah_id}: {mitzvah['title'][:60]}...")
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Successfully added classifications for mitzvot 191-200")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
