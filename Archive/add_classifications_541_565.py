#!/usr/bin/env python3
"""
Add classifications for mitzvot 541-565.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 541-565
    classifications = {
        541: {
            "category": "Interpersonal Relations",
            "sub_category": "Helping Load Burden",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:4", "Sefer HaChinukh 541"]
        },
        542: {
            "category": "Modesty and Dress",
            "sub_category": "Woman Not Wearing Men's Adornments",
            "applies_to": ["Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:5", "Sefer HaChinukh 542"]
        },
        543: {
            "category": "Modesty and Dress",
            "sub_category": "Man Not Wearing Women's Clothes",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:5", "Sefer HaChinukh 543"]
        },
        544: {
            "category": "Animal Welfare",
            "sub_category": "Not Taking Mother with Young",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:6", "Sefer HaChinukh 544"]
        },
        545: {
            "category": "Animal Welfare",
            "sub_category": "Sending Away Mother Bird",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:7", "Sefer HaChinukh 545"]
        },
        546: {
            "category": "Safety and Health",
            "sub_category": "Parapet on Roof",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:8", "Sefer HaChinukh 546"]
        },
        547: {
            "category": "Safety and Health",
            "sub_category": "Not Leaving Stumbling Block",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:8", "Sefer HaChinukh 547"]
        },
        548: {
            "category": "Forbidden Mixtures",
            "sub_category": "Not Planting Kilayim in Vineyard",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:9", "Sefer HaChinukh 548"]
        },
        549: {
            "category": "Forbidden Mixtures",
            "sub_category": "Not Eating Kilayim of Vineyard",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:9", "Sefer HaChinukh 549"]
        },
        550: {
            "category": "Forbidden Mixtures",
            "sub_category": "Not Working Two Species Together",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:10", "Sefer HaChinukh 550"]
        },
        551: {
            "category": "Forbidden Mixtures",
            "sub_category": "Not Wearing Shaatnez",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:11", "Sefer HaChinukh 551"]
        },
        552: {
            "category": "Family Law",
            "sub_category": "Marriage Contract and Betrothal",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:13", "Sefer HaChinukh 552"]
        },
        553: {
            "category": "Family Law",
            "sub_category": "Slanderer's Wife Remaining Married",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:19", "Sefer HaChinukh 553"]
        },
        554: {
            "category": "Family Law",
            "sub_category": "Slanderer Not Divorcing Wife",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:19", "Sefer HaChinukh 554"]
        },
        555: {
            "category": "Judicial System",
            "sub_category": "Stoning for Capital Crime",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:24", "Sefer HaChinukh 555"]
        },
        556: {
            "category": "Judicial System",
            "sub_category": "Not Punishing Coerced Person",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:26", "Sefer HaChinukh 556"]
        },
        557: {
            "category": "Family Law",
            "sub_category": "Rapist Marrying Victim",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:29", "Sefer HaChinukh 557"]
        },
        558: {
            "category": "Family Law",
            "sub_category": "Rapist Not Divorcing Wife",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 22:29", "Sefer HaChinukh 558"]
        },
        559: {
            "category": "Family Law",
            "sub_category": "Eunuch Not Marrying Israelite",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:2", "Sefer HaChinukh 559"]
        },
        560: {
            "category": "Family Law",
            "sub_category": "Mamzer Not Marrying Israelite",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:3", "Sefer HaChinukh 560"]
        },
        561: {
            "category": "Family Law",
            "sub_category": "Ammonite/Moabite Not Entering Congregation",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:4", "Sefer HaChinukh 561"]
        },
        562: {
            "category": "Warfare",
            "sub_category": "Not Seeking Peace with Ammon/Moab",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 23:7", "Sefer HaChinukh 562"]
        },
        563: {
            "category": "Family Law",
            "sub_category": "Not Distancing Third-Generation Edomite",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:8", "Sefer HaChinukh 563"]
        },
        564: {
            "category": "Family Law",
            "sub_category": "Not Distancing Third-Generation Egyptian",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:8", "Sefer HaChinukh 564"]
        },
        565: {
            "category": "Purity and Impurity",
            "sub_category": "Impure Not Entering Temple Mount",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 23:11", "Sefer HaChinukh 565"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 541-565")

if __name__ == '__main__':
    main()
