#!/usr/bin/env python3
"""
Add classifications for mitzvot 281-290
Includes priestly tithe restrictions, tevel prohibition,
and sacrificial animal blemish prohibitions
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 281-290
    classifications = {
        281: {
            "category": "Priestly Gifts",
            "sub_category": "Boarder/Hired Worker - No Terumah",
            "applies_to": ["Non-Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:10"]
        },
        282: {
            "category": "Priestly Gifts",
            "sub_category": "Uncircumcised - No Terumah",
            "applies_to": ["Uncircumcised"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:10"]
        },
        283: {
            "category": "Priestly Gifts",
            "sub_category": "Challalah - No Holy Food",
            "applies_to": ["Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:12"]
        },
        284: {
            "category": "Agricultural Gifts",
            "sub_category": "Prohibition of Tevel",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:15"]
        },
        285: {
            "category": "Sacrifices",
            "sub_category": "No Consecrating Blemished Animals",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:20"]
        },
        286: {
            "category": "Sacrifices",
            "sub_category": "Requirement of Unblemished Sacrifice",
            "applies_to": ["Men", "Women"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:21"]
        },
        287: {
            "category": "Sacrifices",
            "sub_category": "No Blemishing Consecrated Animals",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:21"]
        },
        288: {
            "category": "Sacrifices",
            "sub_category": "No Sprinkling Blood of Blemished",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:24"]
        },
        289: {
            "category": "Sacrifices",
            "sub_category": "No Slaughtering Blemished for Sacrifice",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:22"]
        },
        290: {
            "category": "Sacrifices",
            "sub_category": "No Burning Entrails of Blemished",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:22"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 281-290")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
