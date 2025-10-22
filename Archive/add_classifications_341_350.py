#!/usr/bin/env python3
"""
Add classifications for mitzvot 341-350
Includes property laws (walled city redemption, Levite areas), business ethics,
Hebrew slave regulations, Canaanite slave laws, worship restrictions, and valuation laws.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 341-350
    classifications = {
        341: {
            "category": "Civil Law",
            "sub_category": "Property Redemption",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:29"]
        },
        342: {
            "category": "Civil Law",
            "sub_category": "Levite City Preservation",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:34", "Numbers 35:2-7"]
        },
        343: {
            "category": "Business Ethics",
            "sub_category": "Interest Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:37"]
        },
        344: {
            "category": "Slavery Laws",
            "sub_category": "Hebrew Slave - Dignified Work",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:39"]
        },
        345: {
            "category": "Slavery Laws",
            "sub_category": "Hebrew Slave - Sale Dignity",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:42"]
        },
        346: {
            "category": "Slavery Laws",
            "sub_category": "Hebrew Slave - Oppressive Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:43"]
        },
        347: {
            "category": "Slavery Laws",
            "sub_category": "Canaanite Slave - Perpetual Service",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:46"]
        },
        348: {
            "category": "Slavery Laws",
            "sub_category": "Hebrew Slave - Protection from Gentiles",
            "applies_to": ["All Israel"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:53"]
        },
        349: {
            "category": "Worship and Idolatry",
            "sub_category": "Figured Stone Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 26:1"]
        },
        350: {
            "category": "Temple Service",
            "sub_category": "Personal Valuations",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 27:2"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 341-350")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()