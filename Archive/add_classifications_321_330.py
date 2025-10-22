#!/usr/bin/env python3
"""
Add classifications for mitzvot 321-330
Includes Shemini Atzeret, lulav, sukkah, sabbatical year laws,
and counting toward jubilee.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 321-330
    classifications = {
        321: {
            "category": "Festivals and Holidays",
            "sub_category": "Shemini Atzeret Observance",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:36"]
        },
        322: {
            "category": "Sacrifices",
            "sub_category": "Shemini Atzeret Additional Offering",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 23:36", "Numbers 29:36-38"]
        },
        323: {
            "category": "Festivals and Holidays",
            "sub_category": "Shemini Atzeret - Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:36"]
        },
        324: {
            "category": "Festivals and Holidays",
            "sub_category": "Lulav and Four Species",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:40"]
        },
        325: {
            "category": "Festivals and Holidays",
            "sub_category": "Sukkah Dwelling",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 23:42"]
        },
        326: {
            "category": "Agricultural Laws",
            "sub_category": "Sabbatical Year - Land Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:4"]
        },
        327: {
            "category": "Agricultural Laws",
            "sub_category": "Sabbatical Year - Tree Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:4"]
        },
        328: {
            "category": "Agricultural Laws",
            "sub_category": "Sabbatical Year - Aftergrowth Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:5"]
        },
        329: {
            "category": "Agricultural Laws",
            "sub_category": "Sabbatical Year - Fruit Gathering Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:5"]
        },
        330: {
            "category": "Time and Calendar",
            "sub_category": "Jubilee Counting",
            "applies_to": ["Beit Din"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:8"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 321-330")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()