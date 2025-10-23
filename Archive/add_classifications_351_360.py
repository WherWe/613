#!/usr/bin/env python3
"""
Add classifications for mitzvot 351-360
Includes laws of consecration, exchange, appraisals, dedications, and tithes.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 351-360
    classifications = {
        351: {
            "category": "Temple Service",
            "sub_category": "Exchange Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 27:10"]
        },
        352: {
            "category": "Temple Service",
            "sub_category": "Exchange Consecration",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 27:10"]
        },
        353: {
            "category": "Temple Service",
            "sub_category": "Beast Appraisal",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 27:11-12"]
        },
        354: {
            "category": "Temple Service",
            "sub_category": "House Appraisal",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 27:14"]
        },
        355: {
            "category": "Temple Service",
            "sub_category": "Field Appraisal",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 27:16"]
        },
        356: {
            "category": "Temple Service",
            "sub_category": "Sacrifice Type Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 27:26"]
        },
        357: {
            "category": "Temple Service",
            "sub_category": "Dedications to Priests",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 27:28"]
        },
        358: {
            "category": "Temple Service",
            "sub_category": "Dedicated Land - Sale Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 27:28"]
        },
        359: {
            "category": "Temple Service",
            "sub_category": "Dedicated Field - Redemption Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 27:28"]
        },
        360: {
            "category": "Agricultural Laws",
            "sub_category": "Animal Tithe",
            "applies_to": ["Men", "Women", "Priests", "Levites"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 27:32"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 351-360")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()
