#!/usr/bin/env python3
"""
Add classifications for mitzvot 211-220
Includes bestiality prohibition, reverence of parents, idolatry prohibitions,
notar prohibition, and agricultural gifts to the poor
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 211-220
    classifications = {
        211: {
            "category": "Sexual Prohibitions",
            "sub_category": "Bestiality",
            "applies_to": ["Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:23"]
        },
        212: {
            "category": "Family Law",
            "sub_category": "Honoring Parents",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:3", "Sifra, Kedoshim, Section 1:10", "Kiddushin 31b"]
        },
        213: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Following Idols",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:4", "Sifra, Kedoshim, Section 1:11"]
        },
        214: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Making Idols",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:4", "Sifra, Kedoshim, Section 1:12"]
        },
        215: {
            "category": "Sacrifices",
            "sub_category": "Prohibition of Notar",
            "applies_to": ["Men", "Women"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Exodus 29:33", "Meilah 17b"]
        },
        216: {
            "category": "Agricultural Gifts",
            "sub_category": "Pe'ah (Corner of Field)",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:10", "Leviticus 19:9", "Sifra Kedoshim 3:4"]
        },
        217: {
            "category": "Agricultural Gifts",
            "sub_category": "Prohibition Against Finishing Corner",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 23:22", "Leviticus 19:10"]
        },
        218: {
            "category": "Agricultural Gifts",
            "sub_category": "Leket (Gleanings)",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:10", "Mishnah Peah 6:5", "Mishnah Peah 4:10"]
        },
        219: {
            "category": "Agricultural Gifts",
            "sub_category": "Prohibition Against Taking Gleanings",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:9"]
        },
        220: {
            "category": "Agricultural Gifts",
            "sub_category": "Ollalot (Defective Grape Clusters)",
            "applies_to": ["Men", "Women", "Kohanim", "Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 19:10"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 211-220")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
