#!/usr/bin/env python3
"""
Add classifications for mitzvot 221-230
Includes more agricultural gifts, theft and fraud prohibitions, 
oath prohibitions, and worker's wages
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 221-230
    classifications = {
        221: {
            "category": "Agricultural Gifts",
            "sub_category": "Prohibition Against Finishing Vineyard Corner",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:10"]
        },
        222: {
            "category": "Agricultural Gifts",
            "sub_category": "Peret (Fallen Grapes)",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:10"]
        },
        223: {
            "category": "Agricultural Gifts",
            "sub_category": "Prohibition Against Gathering Peret",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:10"]
        },
        224: {
            "category": "Property Law",
            "sub_category": "Prohibition of Theft",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:11"]
        },
        225: {
            "category": "Property Law",
            "sub_category": "Prohibition of Denial of Claims",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:11"]
        },
        226: {
            "category": "Oaths and Vows",
            "sub_category": "Prohibition of False Oath Regarding Denial",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:11"]
        },
        227: {
            "category": "Oaths and Vows",
            "sub_category": "Prohibition of False Oaths",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:12"]
        },
        228: {
            "category": "Property Law",
            "sub_category": "Prohibition of Oppression/Withholding",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:13"]
        },
        229: {
            "category": "Property Law",
            "sub_category": "Prohibition of Robbery",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:13"]
        },
        230: {
            "category": "Labor Law",
            "sub_category": "Timely Payment of Wages",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:13", "Deuteronomy 24:15"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 221-230")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
