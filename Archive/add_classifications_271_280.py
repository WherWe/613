#!/usr/bin/env python3
"""
Add classifications for mitzvot 271-280
Includes high priest marriage/purity laws, priestly blemishes,
impure priests, and priestly tithe restrictions
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 271-280
    classifications = {
        271: {
            "category": "Priestly Purity",
            "sub_category": "High Priest - Absolute Purity",
            "applies_to": ["Kohen Gadol"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:11"]
        },
        272: {
            "category": "Priestly Marriage",
            "sub_category": "High Priest - Marry Virgin",
            "applies_to": ["Kohen Gadol"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:13"]
        },
        273: {
            "category": "Priestly Marriage",
            "sub_category": "High Priest - Prohibition of Widow",
            "applies_to": ["Kohen Gadol"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:14"]
        },
        274: {
            "category": "Priestly Marriage",
            "sub_category": "High Priest - No Relations with Widow",
            "applies_to": ["Kohen Gadol"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:15"]
        },
        275: {
            "category": "Temple Service",
            "sub_category": "Blemished Priest - No Service",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 21:17"]
        },
        276: {
            "category": "Temple Service",
            "sub_category": "Temporary Blemish - No Service",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 21:18"]
        },
        277: {
            "category": "Temple Service",
            "sub_category": "Blemished - No Entry to Sanctuary",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 21:23"]
        },
        278: {
            "category": "Temple Service",
            "sub_category": "Impure Priest - No Service",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:2"]
        },
        279: {
            "category": "Priestly Gifts",
            "sub_category": "Impure Priest - No Terumah",
            "applies_to": ["Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:4"]
        },
        280: {
            "category": "Priestly Gifts",
            "sub_category": "Non-Priest - No Terumah",
            "applies_to": ["Non-Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:10"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 271-280")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
