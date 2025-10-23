#!/usr/bin/env python3
"""
Add classifications for mitzvot 361-370
Includes tithe prohibition, purity laws, confession, sotah laws, and nazirite prohibitions.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 361-370
    classifications = {
        361: {
            "category": "Agricultural Laws",
            "sub_category": "Animal Tithe - Sale Prohibition",
            "applies_to": ["Men", "Women", "Priests", "Levites"],
            "location": "Jerusalem",
            "time_scope": "Always",
            "source_refs": ["Leviticus 27:33"]
        },
        362: {
            "category": "Purity and Impurity",
            "sub_category": "Temple Exclusion - Impure Persons",
            "applies_to": ["Men", "Women"],
            "location": "Temple",
            "time_scope": "Always",
            "source_refs": ["Numbers 5:2", "Deuteronomy 23:11"]
        },
        363: {
            "category": "Purity and Impurity",
            "sub_category": "Temple Entry Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Temple",
            "time_scope": "Always",
            "source_refs": ["Numbers 5:3", "Numbers 19:13"]
        },
        364: {
            "category": "Repentance",
            "sub_category": "Confession of Sin",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 5:6", "Leviticus 5:5"]
        },
        365: {
            "category": "Family Law",
            "sub_category": "Suspected Adulteress (Sotah)",
            "applies_to": ["Men"],
            "location": "Temple",
            "time_scope": "Conditional",
            "source_refs": ["Numbers 5:12-15"]
        },
        366: {
            "category": "Temple Service",
            "sub_category": "Sotah Sacrifice - Oil Prohibition",
            "applies_to": ["Priests"],
            "location": "Temple",
            "time_scope": "Conditional",
            "source_refs": ["Numbers 5:15"]
        },
        367: {
            "category": "Temple Service",
            "sub_category": "Sotah Sacrifice - Frankincense Prohibition",
            "applies_to": ["Priests"],
            "location": "Temple",
            "time_scope": "Conditional",
            "source_refs": ["Numbers 5:15"]
        },
        368: {
            "category": "Personal Status",
            "sub_category": "Nazirite - Wine Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 6:3"]
        },
        369: {
            "category": "Personal Status",
            "sub_category": "Nazirite - Fresh Grapes Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 6:3"]
        },
        370: {
            "category": "Personal Status",
            "sub_category": "Nazirite - Raisins Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 6:3"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 361-370")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()
