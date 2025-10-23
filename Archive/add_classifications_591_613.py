#!/usr/bin/env python3
"""
Add classifications for mitzvot 591-613 (FINAL BATCH).
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 591-613
    classifications = {
        591: {
            "category": "Business Ethics",
            "sub_category": "Not Taking Widow's Garment as Surety",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:17", "Sefer HaChinukh 591"]
        },
        592: {
            "category": "Agricultural Laws",
            "sub_category": "Leaving Forgotten for Poor",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 24:19", "Sefer HaChinukh 592"]
        },
        593: {
            "category": "Agricultural Laws",
            "sub_category": "Not Returning for Forgotten",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 24:19", "Sefer HaChinukh 593"]
        },
        594: {
            "category": "Judicial System",
            "sub_category": "Lashing Evildoer",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:2", "Sefer HaChinukh 594"]
        },
        595: {
            "category": "Judicial System",
            "sub_category": "Not Exceeding Forty Lashes",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:3", "Sefer HaChinukh 595"]
        },
        596: {
            "category": "Animal Welfare",
            "sub_category": "Not Muzzling Working Animal",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 25:4", "Sefer HaChinukh 596"]
        },
        597: {
            "category": "Family Law",
            "sub_category": "Levirate Wife Not Marrying Until Released",
            "applies_to": ["Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:5", "Sefer HaChinukh 597"]
        },
        598: {
            "category": "Family Law",
            "sub_category": "Levirate Marriage (Yibum)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:5", "Sefer HaChinukh 598"]
        },
        599: {
            "category": "Family Law",
            "sub_category": "Chalitzah (Release from Levirate)",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:9", "Sefer HaChinukh 599"]
        },
        600: {
            "category": "Judicial System",
            "sub_category": "Saving Pursued by Killing Pursuer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:12", "Sefer HaChinukh 600"]
        },
        601: {
            "category": "Judicial System",
            "sub_category": "Not Pitying Pursuer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:12", "Sefer HaChinukh 601"]
        },
        602: {
            "category": "Business Ethics",
            "sub_category": "Not Having Deficient Weights",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 25:14", "Sefer HaChinukh 602"]
        },
        603: {
            "category": "Amalek",
            "sub_category": "Remembering What Amalek Did",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 25:17", "Sefer HaChinukh 603"]
        },
        604: {
            "category": "Amalek",
            "sub_category": "Blotting Out Amalek",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 25:19", "Sefer HaChinukh 604"]
        },
        605: {
            "category": "Amalek",
            "sub_category": "Not Forgetting Amalek",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 25:19", "Sefer HaChinukh 605"]
        },
        606: {
            "category": "Agricultural Laws",
            "sub_category": "Recital Over First-Fruits",
            "applies_to": ["Men"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 26:5-10", "Sefer HaChinukh 606"]
        },
        607: {
            "category": "Agricultural Laws",
            "sub_category": "Declaration of Tithes",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 26:13", "Sefer HaChinukh 607"]
        },
        608: {
            "category": "Agricultural Laws",
            "sub_category": "Not Eating Second Tithe in Bereavement",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 26:14", "Sefer HaChinukh 608"]
        },
        609: {
            "category": "Agricultural Laws",
            "sub_category": "Not Eating Second Tithe in Impurity",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 26:14", "Sefer HaChinukh 609"]
        },
        610: {
            "category": "Agricultural Laws",
            "sub_category": "Second Tithe Only for Food/Drink",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 26:14", "Sefer HaChinukh 610"]
        },
        611: {
            "category": "Thought and Belief",
            "sub_category": "Walking in God's Ways (Imitatio Dei)",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 28:9", "Sefer HaChinukh 611"]
        },
        612: {
            "category": "Festivals and Holidays",
            "sub_category": "Hakhel (Gathering on Sukkot)",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 31:12", "Sefer HaChinukh 612"]
        },
        613: {
            "category": "Torah Law",
            "sub_category": "Writing Torah Scroll",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 31:19", "Sefer HaChinukh 613"]
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
    
    print(f"\n🎉 Successfully added classifications for mitzvot 591-613")
    print(f"🎊 ALL 613 MITZVOT ARE NOW CLASSIFIED! 🎊")

if __name__ == '__main__':
    main()
