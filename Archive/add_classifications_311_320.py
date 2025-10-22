#!/usr/bin/env python3
"""
Add classifications for mitzvot 311-320
Includes Rosh Hashanah prohibitions, Yom Kippur observance and sacrifice,
and Sukkot observance.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 311-320
    classifications = {
        311: {
            "category": "Festivals and Holidays",
            "sub_category": "Rosh Hashanah - Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:24-25"]
        },
        312: {
            "category": "Sacrifices",
            "sub_category": "Rosh Hashanah Additional Offering",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:24-25", "Numbers 29:2-5"]
        },
        313: {
            "category": "Festivals and Holidays",
            "sub_category": "Yom Kippur Fasting",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:27"]
        },
        314: {
            "category": "Sacrifices",
            "sub_category": "Yom Kippur Additional Offering",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:27", "Numbers 29:8"]
        },
        315: {
            "category": "Festivals and Holidays",
            "sub_category": "Yom Kippur - Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:28"]
        },
        316: {
            "category": "Festivals and Holidays",
            "sub_category": "Yom Kippur - Eating and Drinking Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:29"]
        },
        317: {
            "category": "Festivals and Holidays",
            "sub_category": "Yom Kippur Rest",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 23:32"]
        },
        318: {
            "category": "Festivals and Holidays",
            "sub_category": "Sukkot Observance",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:35"]
        },
        319: {
            "category": "Festivals and Holidays",
            "sub_category": "Sukkot - Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:35"]
        },
        320: {
            "category": "Sacrifices",
            "sub_category": "Sukkot Additional Offerings",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:36", "Numbers 29:13-35"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 311-320")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()