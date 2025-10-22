#!/usr/bin/env python3
"""
Add classifications for mitzvot 331-340
Includes jubilee laws (shofar blowing, land sanctification, work prohibitions),
business and civil laws (adjudication, fraud, verbal mistreatment),
and land return on jubilee.
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 331-340
    classifications = {
        331: {
            "category": "Time and Calendar",
            "sub_category": "Jubilee Shofar",
            "applies_to": ["Beit Din"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:9-10"]
        },
        332: {
            "category": "Agricultural Laws",
            "sub_category": "Jubilee Year Sanctification",
            "applies_to": ["All Israel"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:10"]
        },
        333: {
            "category": "Agricultural Laws",
            "sub_category": "Jubilee Year - Land Work Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:11"]
        },
        334: {
            "category": "Agricultural Laws",
            "sub_category": "Jubilee Year - Aftergrowth Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:11"]
        },
        335: {
            "category": "Agricultural Laws",
            "sub_category": "Jubilee Year - Fruit Gathering Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:11"]
        },
        336: {
            "category": "Civil Law",
            "sub_category": "Commercial Adjudication",
            "applies_to": ["Beit Din"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:14"]
        },
        337: {
            "category": "Business Ethics",
            "sub_category": "Commercial Fraud Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:14"]
        },
        338: {
            "category": "Interpersonal Relations",
            "sub_category": "Verbal Mistreatment Prohibition",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 25:17"]
        },
        339: {
            "category": "Agricultural Laws",
            "sub_category": "Land Sale Limitation",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:23"]
        },
        340: {
            "category": "Agricultural Laws",
            "sub_category": "Jubilee Land Return",
            "applies_to": ["Men", "Women"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 25:24", "Leviticus 25:13"]
        }
    }
    
    # Add classifications to the data
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added classifications for mitzvot 331-340")
    print("Classifications added:")
    for id_num, classification in classifications.items():
        print(f"  {id_num}: {classification['category']} - {classification['sub_category']}")

if __name__ == "__main__":
    add_classifications()