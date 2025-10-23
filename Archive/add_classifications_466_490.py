#!/usr/bin/env python3
"""
Add classifications for mitzvot 466-490.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 466-490
    classifications = {
        466: {
            "category": "Conquest of Israel",
            "sub_category": "Property of Enticed City",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:18", "Sefer HaChinukh 466"]
        },
        467: {
            "category": "Mourning",
            "sub_category": "Not Gashing Oneself",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 14:1", "Sefer HaChinukh 467"]
        },
        468: {
            "category": "Mourning",
            "sub_category": "Not Making Bald Spot for Dead",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 14:1", "Sefer HaChinukh 468"]
        },
        469: {
            "category": "Sacrifices",
            "sub_category": "Not Eating Disqualified Consecrated",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 14:3", "Sefer HaChinukh 469"]
        },
        470: {
            "category": "Dietary Laws",
            "sub_category": "Checking Signs of Bird",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 14:11", "Sefer HaChinukh 470"]
        },
        471: {
            "category": "Dietary Laws",
            "sub_category": "Not Eating Flying Swarming Creatures",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 14:19", "Sefer HaChinukh 471"]
        },
        472: {
            "category": "Dietary Laws",
            "sub_category": "Not Eating Dead Animal (Nevelah)",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 14:21", "Sefer HaChinukh 472"]
        },
        473: {
            "category": "Agricultural Laws",
            "sub_category": "Second Tithe",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 14:22-23", "Sefer HaChinukh 473"]
        },
        474: {
            "category": "Agricultural Laws",
            "sub_category": "Poor Tithe",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 14:28-29", "Sefer HaChinukh 474"]
        },
        475: {
            "category": "Time and Calendar",
            "sub_category": "Not Claiming Debt After Sabbatical",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 15:2", "Sefer HaChinukh 475"]
        },
        476: {
            "category": "Business Ethics",
            "sub_category": "Pressing Foreigner for Debt",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 15:3", "Sefer HaChinukh 476"]
        },
        477: {
            "category": "Time and Calendar",
            "sub_category": "Releasing Loans in Seventh Year",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 15:2", "Sefer HaChinukh 477"]
        },
        478: {
            "category": "Interpersonal Relations",
            "sub_category": "Not Hardening Heart Against Poor",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 15:7", "Sefer HaChinukh 478"]
        },
        479: {
            "category": "Interpersonal Relations",
            "sub_category": "Charity",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 15:8", "Sefer HaChinukh 479"]
        },
        480: {
            "category": "Business Ethics",
            "sub_category": "Not Refraining from Lending Before Sabbatical",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 15:9", "Sefer HaChinukh 480"]
        },
        481: {
            "category": "Slavery Laws",
            "sub_category": "Not Sending Hebrew Slave Empty",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 15:13", "Sefer HaChinukh 481"]
        },
        482: {
            "category": "Slavery Laws",
            "sub_category": "Endowing Departing Slave",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 15:14", "Sefer HaChinukh 482"]
        },
        483: {
            "category": "Sacrifices",
            "sub_category": "Not Working with Consecrated Animals",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 15:19", "Sefer HaChinukh 483"]
        },
        484: {
            "category": "Sacrifices",
            "sub_category": "Not Shearing Consecrated Animals",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 15:19", "Sefer HaChinukh 484"]
        },
        485: {
            "category": "Festivals and Holidays",
            "sub_category": "Not Eating Chametz After Midday",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Festival",
            "source_refs": ["Deuteronomy 16:3", "Sefer HaChinukh 485"]
        },
        486: {
            "category": "Festivals and Holidays",
            "sub_category": "Not Leaving Festival Sacrifice to Third Day",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 16:4", "Sefer HaChinukh 486"]
        },
        487: {
            "category": "Festivals and Holidays",
            "sub_category": "Not Sacrificing Pesach on Individual Altar",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 16:5", "Sefer HaChinukh 487"]
        },
        488: {
            "category": "Festivals and Holidays",
            "sub_category": "Rejoicing on Festivals",
            "applies_to": ["Men"],
            "location": "Jerusalem",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 16:14", "Sefer HaChinukh 488"]
        },
        489: {
            "category": "Festivals and Holidays",
            "sub_category": "Appearing on Festivals",
            "applies_to": ["Men"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 16:16", "Sefer HaChinukh 489"]
        },
        490: {
            "category": "Festivals and Holidays",
            "sub_category": "Not Appearing Without Sacrifice",
            "applies_to": ["Men"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 16:16", "Sefer HaChinukh 490"]
        }
    }
    
    # Update the mitzvot with classifications
    for mitzvah in data['mitzvot']:
        mitzvah_id = mitzvah['id']
        if mitzvah_id in classifications:
            mitzvah['classification'] = classifications[mitzvah_id]
            print(f"Added classification for mitzvah {mitzvah_id}")
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nSuccessfully added classifications for mitzvot 466-490")

if __name__ == '__main__':
    main()
