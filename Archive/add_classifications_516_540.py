#!/usr/bin/env python3
"""
Add classifications for mitzvot 516-540.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 516-540
    classifications = {
        516: {
            "category": "Prophets and Prophecy",
            "sub_category": "Heeding True Prophet",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 18:15", "Sefer HaChinukh 516"]
        },
        517: {
            "category": "Prophets and Prophecy",
            "sub_category": "Not Prophesying Falsely",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:20", "Sefer HaChinukh 517"]
        },
        518: {
            "category": "Prophets and Prophecy",
            "sub_category": "Not Prophesying in Name of Idolatry",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:20", "Sefer HaChinukh 518"]
        },
        519: {
            "category": "Prophets and Prophecy",
            "sub_category": "Not Fearing False Prophet's Death",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 18:22", "Sefer HaChinukh 519"]
        },
        520: {
            "category": "Judicial System",
            "sub_category": "Preparing Cities of Refuge",
            "applies_to": ["Community"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 19:2-3", "Sefer HaChinukh 520"]
        },
        521: {
            "category": "Judicial System",
            "sub_category": "Not Showing Pity on Killer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 19:13", "Sefer HaChinukh 521"]
        },
        522: {
            "category": "Civil Law",
            "sub_category": "Not Removing Landmark",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 19:14", "Sefer HaChinukh 522"]
        },
        523: {
            "category": "Judicial System",
            "sub_category": "Not Establishing Matter with One Witness",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 19:15", "Sefer HaChinukh 523"]
        },
        524: {
            "category": "Judicial System",
            "sub_category": "Punishing Collusive Witness",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 19:19", "Sefer HaChinukh 524"]
        },
        525: {
            "category": "Warfare",
            "sub_category": "Not Being Terrified in War",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 20:3", "Sefer HaChinukh 525"]
        },
        526: {
            "category": "Warfare",
            "sub_category": "Anointing Priest for War",
            "applies_to": ["Community"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 20:2", "Sefer HaChinukh 526"]
        },
        527: {
            "category": "Warfare",
            "sub_category": "Sending Peace to Besieged Cities",
            "applies_to": ["Community"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 20:10", "Sefer HaChinukh 527"]
        },
        528: {
            "category": "Conquest of Israel",
            "sub_category": "Not Keeping Seven Nations Alive",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 20:16", "Sefer HaChinukh 528"]
        },
        529: {
            "category": "Warfare",
            "sub_category": "Not Destroying Fruit Trees",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 20:19", "Sefer HaChinukh 529"]
        },
        530: {
            "category": "Judicial System",
            "sub_category": "Beheading Calf (Eglah Arufah)",
            "applies_to": ["Community"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 21:4", "Sefer HaChinukh 530"]
        },
        531: {
            "category": "Judicial System",
            "sub_category": "Not Working Eglah Arufah Land",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 21:4", "Sefer HaChinukh 531"]
        },
        532: {
            "category": "Warfare",
            "sub_category": "Law of Beautiful Captive (Yefat Toar)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 21:11-13", "Sefer HaChinukh 532"]
        },
        533: {
            "category": "Warfare",
            "sub_category": "Not Selling Yefat Toar",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 21:14", "Sefer HaChinukh 533"]
        },
        534: {
            "category": "Warfare",
            "sub_category": "Not Enslaving Yefat Toar",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 21:14", "Sefer HaChinukh 534"]
        },
        535: {
            "category": "Judicial System",
            "sub_category": "Hanging Executed Person",
            "applies_to": ["Court"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 21:22", "Sefer HaChinukh 535"]
        },
        536: {
            "category": "Judicial System",
            "sub_category": "Not Leaving Hanged Overnight",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 21:23", "Sefer HaChinukh 536"]
        },
        537: {
            "category": "Burial",
            "sub_category": "Burying Dead Same Day",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 21:23", "Sefer HaChinukh 537"]
        },
        538: {
            "category": "Interpersonal Relations",
            "sub_category": "Returning Lost Item",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:1", "Sefer HaChinukh 538"]
        },
        539: {
            "category": "Interpersonal Relations",
            "sub_category": "Not Avoiding Lost Item",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:3", "Sefer HaChinukh 539"]
        },
        540: {
            "category": "Interpersonal Relations",
            "sub_category": "Helping Fellow's Fallen Beast",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 22:4", "Sefer HaChinukh 540"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 516-540")

if __name__ == '__main__':
    main()
