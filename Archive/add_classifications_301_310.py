#!/usr/bin/env python3
"""
Add classifications for mitzvot 301-310
Includes the conclusion of Pesach observance, omer sacrifice and counting,
Shavuot observance and Rosh Hashanah.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 301-310
    classifications = {
        301: {
            "category": "Festivals and Holidays",
            "sub_category": "Pesach - Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:8"]
        },
        302: {
            "category": "Sacrifices",
            "sub_category": "Omer Offering",
            "applies_to": ["Kohanim", "All Israel"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:10-11"]
        },
        303: {
            "category": "Dietary Laws",
            "sub_category": "New Grain Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:14"]
        },
        304: {
            "category": "Dietary Laws",
            "sub_category": "New Grain Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:14"]
        },
        305: {
            "category": "Dietary Laws",
            "sub_category": "New Grain Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:14"]
        },
        306: {
            "category": "Time and Calendar",
            "sub_category": "Omer Counting",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:15", "Deuteronomy 16:9"]
        },
        307: {
            "category": "Sacrifices",
            "sub_category": "Shavuot Offering",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:16"]
        },
        308: {
            "category": "Festivals and Holidays",
            "sub_category": "Shavuot Observance",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:21"]
        },
        309: {
            "category": "Festivals and Holidays",
            "sub_category": "Shavuot - Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:21"]
        },
        310: {
            "category": "Festivals and Holidays",
            "sub_category": "Rosh Hashanah Observance",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:24"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 301-310")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()