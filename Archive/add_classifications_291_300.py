#!/usr/bin/env python3
"""
Add classifications for mitzvot 291-300
Includes prohibition of castration, sacrifice laws, profaning/sanctifying God's name,
and Pesach observance laws
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 291-300
    classifications = {
        291: {
            "category": "Animal Welfare",
            "sub_category": "Prohibition of Castration",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:24"]
        },
        292: {
            "category": "Sacrifices",
            "sub_category": "No Blemished from Gentile",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:25"]
        },
        293: {
            "category": "Sacrifices",
            "sub_category": "Minimum Age of Eight Days",
            "applies_to": ["All Israel"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 22:27"]
        },
        294: {
            "category": "Animal Welfare",
            "sub_category": "Prohibition of Slaughtering Parent and Child Same Day",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:28"]
        },
        295: {
            "category": "Faith and Sanctity",
            "sub_category": "Prohibition of Desecrating God's Name",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:32"]
        },
        296: {
            "category": "Faith and Sanctity",
            "sub_category": "Command to Sanctify God's Name",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 22:32"]
        },
        297: {
            "category": "Festival Laws",
            "sub_category": "Rest on First Day of Pesach",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:7"]
        },
        298: {
            "category": "Festival Laws",
            "sub_category": "No Work on First Day of Pesach",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:7"]
        },
        299: {
            "category": "Sacrifices",
            "sub_category": "Pesach Musaf Offerings",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:8", "Numbers 28:19-24"]
        },
        300: {
            "category": "Festival Laws",
            "sub_category": "Rest on Seventh Day of Pesach",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:8"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 291-300")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
