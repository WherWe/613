#!/usr/bin/env python3
"""
Add classifications for mitzvot 441-465.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 441-465
    classifications = {
        441: {
            "category": "Sacrifices",
            "sub_category": "Redeeming Blemished Consecrated Animals",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:15-16", "Sefer HaChinukh 441"]
        },
        442: {
            "category": "Agricultural Laws",
            "sub_category": "Second Tithe Grain Outside Jerusalem",
            "applies_to": ["All"],
            "location": "Jerusalem",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 442"]
        },
        443: {
            "category": "Agricultural Laws",
            "sub_category": "Second Tithe Wine Outside Jerusalem",
            "applies_to": ["All"],
            "location": "Jerusalem",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 443"]
        },
        444: {
            "category": "Agricultural Laws",
            "sub_category": "Second Tithe Oil Outside Jerusalem",
            "applies_to": ["All"],
            "location": "Jerusalem",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 444"]
        },
        445: {
            "category": "Priesthood and Levites",
            "sub_category": "Firstborn Outside Jerusalem",
            "applies_to": ["Priests", "Non-Priests"],
            "location": "Jerusalem",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 445"]
        },
        446: {
            "category": "Sacrifices",
            "sub_category": "Higher-Level Consecrated Foods Outside Yard",
            "applies_to": ["Priests"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 446"]
        },
        447: {
            "category": "Sacrifices",
            "sub_category": "Meat of Burnt-Offering",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 447"]
        },
        448: {
            "category": "Sacrifices",
            "sub_category": "Lower-Level Consecrated Before Sprinkling",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 448"]
        },
        449: {
            "category": "Agricultural Laws",
            "sub_category": "First-Fruits Before Placement",
            "applies_to": ["Priests", "Israelites"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:17", "Sefer HaChinukh 449"]
        },
        450: {
            "category": "Priesthood and Levites",
            "sub_category": "Not Forsaking Levite",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 12:19", "Sefer HaChinukh 450"]
        },
        451: {
            "category": "Dietary Laws",
            "sub_category": "Slaughter",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 12:21", "Sefer HaChinukh 451"]
        },
        452: {
            "category": "Dietary Laws",
            "sub_category": "Limb from Living Animal",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 12:23", "Sefer HaChinukh 452"]
        },
        453: {
            "category": "Temple",
            "sub_category": "Bringing Consecrated Things to Temple",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:26", "Sefer HaChinukh 453"]
        },
        454: {
            "category": "Torah Law",
            "sub_category": "Not Adding to Commandments",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 13:1", "Sefer HaChinukh 454"]
        },
        455: {
            "category": "Torah Law",
            "sub_category": "Not Subtracting from Commandments",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 13:1", "Sefer HaChinukh 455"]
        },
        456: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Listening to False Prophet",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:2-4", "Sefer HaChinukh 456"]
        },
        457: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Loving Seducer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:9", "Sefer HaChinukh 457"]
        },
        458: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Ceasing Hatred of Seducer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:9", "Sefer HaChinukh 458"]
        },
        459: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Saving Seducer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:9", "Sefer HaChinukh 459"]
        },
        460: {
            "category": "Judicial System",
            "sub_category": "Not Advocating Innocence for Seducer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:9", "Sefer HaChinukh 460"]
        },
        461: {
            "category": "Judicial System",
            "sub_category": "Not Refraining from Guilt for Seducer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:9", "Sefer HaChinukh 461"]
        },
        462: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Seducing to Idolatry",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 13:12", "Sefer HaChinukh 462"]
        },
        463: {
            "category": "Judicial System",
            "sub_category": "Investigating Witnesses",
            "applies_to": ["Courts"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 13:15", "Sefer HaChinukh 463"]
        },
        464: {
            "category": "Conquest of Israel",
            "sub_category": "Burning Enticed City",
            "applies_to": ["Community"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:16-17", "Sefer HaChinukh 464"]
        },
        465: {
            "category": "Conquest of Israel",
            "sub_category": "Not Rebuilding Enticed City",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 13:17", "Sefer HaChinukh 465"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 441-465")

if __name__ == '__main__':
    main()
