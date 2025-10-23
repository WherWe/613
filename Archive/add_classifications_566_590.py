#!/usr/bin/env python3
"""
Add classifications for mitzvot 566-590.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 566-590
    classifications = {
        566: {
            "category": "Camp Purity",
            "sub_category": "Designated Place for Defecation",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 23:13", "Sefer HaChinukh 566"]
        },
        567: {
            "category": "Camp Purity",
            "sub_category": "Spike for Digging",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 23:14", "Sefer HaChinukh 567"]
        },
        568: {
            "category": "Slavery Laws",
            "sub_category": "Not Returning Escaped Slave",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 23:16", "Sefer HaChinukh 568"]
        },
        569: {
            "category": "Slavery Laws",
            "sub_category": "Not Oppressing Escaped Slave",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 23:17", "Sefer HaChinukh 569"]
        },
        570: {
            "category": "Sexual Prohibitions",
            "sub_category": "No Relations Without Marriage",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:18", "Sefer HaChinukh 570"]
        },
        571: {
            "category": "Sacrifices",
            "sub_category": "Not Bringing Prostitute Fee or Dog Price",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 23:19", "Sefer HaChinukh 571"]
        },
        572: {
            "category": "Business Ethics",
            "sub_category": "Not Giving Interest to Israelite",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:20", "Sefer HaChinukh 572"]
        },
        573: {
            "category": "Business Ethics",
            "sub_category": "Lending to Gentile with Interest",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:21", "Sefer HaChinukh 573"]
        },
        574: {
            "category": "Vows and Oaths",
            "sub_category": "Not Delaying Vows",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:22", "Sefer HaChinukh 574"]
        },
        575: {
            "category": "Vows and Oaths",
            "sub_category": "Fulfilling Vows",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:24", "Sefer HaChinukh 575"]
        },
        576: {
            "category": "Business Ethics",
            "sub_category": "Worker Eating from Produce",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:25", "Sefer HaChinukh 576"]
        },
        577: {
            "category": "Business Ethics",
            "sub_category": "Worker Not Taking More Than Eating",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:25", "Sefer HaChinukh 577"]
        },
        578: {
            "category": "Business Ethics",
            "sub_category": "Worker Not Eating During Work",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 23:26", "Sefer HaChinukh 578"]
        },
        579: {
            "category": "Family Law",
            "sub_category": "Divorcing with Get",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 24:1", "Sefer HaChinukh 579"]
        },
        580: {
            "category": "Family Law",
            "sub_category": "Not Remarrying Divorced Wife",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 24:4", "Sefer HaChinukh 580"]
        },
        581: {
            "category": "Family Law",
            "sub_category": "Groom Not Leaving Home First Year",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:5", "Sefer HaChinukh 581"]
        },
        582: {
            "category": "Family Law",
            "sub_category": "Groom Rejoicing with Wife First Year",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:5", "Sefer HaChinukh 582"]
        },
        583: {
            "category": "Business Ethics",
            "sub_category": "Not Taking Food-Making Vessels as Surety",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:6", "Sefer HaChinukh 583"]
        },
        584: {
            "category": "Purity and Impurity",
            "sub_category": "Not Removing Tzaraat Signs",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:8", "Sefer HaChinukh 584"]
        },
        585: {
            "category": "Business Ethics",
            "sub_category": "Not Taking Surety by Force",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:10", "Sefer HaChinukh 585"]
        },
        586: {
            "category": "Business Ethics",
            "sub_category": "Not Withholding Surety from Owner",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:12", "Sefer HaChinukh 586"]
        },
        587: {
            "category": "Business Ethics",
            "sub_category": "Returning Surety When Needed",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:13", "Sefer HaChinukh 587"]
        },
        588: {
            "category": "Business Ethics",
            "sub_category": "Paying Worker Same Day",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:15", "Sefer HaChinukh 588"]
        },
        589: {
            "category": "Judicial System",
            "sub_category": "Relatives Not Testifying",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:16", "Sefer HaChinukh 589"]
        },
        590: {
            "category": "Judicial System",
            "sub_category": "Not Perverting Stranger/Orphan Judgment",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 24:17", "Sefer HaChinukh 590"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 566-590")

if __name__ == '__main__':
    main()
