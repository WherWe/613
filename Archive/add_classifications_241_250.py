#!/usr/bin/env python3
"""
Add classifications for mitzvot 241-250
Includes prohibition of revenge/grudges, love of Israel, forbidden mixtures,
orlah, fourth-year produce, gluttony, and divination/sorcery prohibitions
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 241-250
    classifications = {
        241: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Revenge",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:18"]
        },
        242: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Bearing Grudge",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:18"]
        },
        243: {
            "category": "Interpersonal Ethics",
            "sub_category": "Love of Fellow Jews",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:18"]
        },
        244: {
            "category": "Agricultural Laws",
            "sub_category": "Prohibition of Mating Mixed Species",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:19"]
        },
        245: {
            "category": "Agricultural Laws",
            "sub_category": "Prohibition of Kilayim (Mixed Seeds)",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:19"]
        },
        246: {
            "category": "Agricultural Laws",
            "sub_category": "Prohibition of Orlah",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:23"]
        },
        247: {
            "category": "Agricultural Laws",
            "sub_category": "Neta Revai (Fourth-Year Produce)",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:24"]
        },
        248: {
            "category": "Ethics and Character",
            "sub_category": "Prohibition of Gluttony",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:26"]
        },
        249: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Divination",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:26"]
        },
        250: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Soothsaying",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:26"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 241-250")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
