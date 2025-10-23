#!/usr/bin/env python3
"""
Add classifications for mitzvot 491-515.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 491-515
    classifications = {
        491: {
            "category": "Judicial System",
            "sub_category": "Appointing Judges and Officers",
            "applies_to": ["Community"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 16:18", "Sefer HaChinukh 491"]
        },
        492: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Planting Tree-Idols",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 16:21", "Sefer HaChinukh 492"]
        },
        493: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Erecting Matsevah",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 16:22", "Sefer HaChinukh 493"]
        },
        494: {
            "category": "Sacrifices",
            "sub_category": "Not Sacrificing Temporary Blemish",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 17:1", "Sefer HaChinukh 494"]
        },
        495: {
            "category": "Judicial System",
            "sub_category": "Obeying Court",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 17:11", "Sefer HaChinukh 495"]
        },
        496: {
            "category": "Judicial System",
            "sub_category": "Not Straying from Court's Words",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 17:11", "Sefer HaChinukh 496"]
        },
        497: {
            "category": "Monarchy",
            "sub_category": "Appointing King",
            "applies_to": ["Community"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 17:15", "Sefer HaChinukh 497"]
        },
        498: {
            "category": "Monarchy",
            "sub_category": "Not Establishing Foreign King",
            "applies_to": ["Community"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 17:15", "Sefer HaChinukh 498"]
        },
        499: {
            "category": "Monarchy",
            "sub_category": "King Not Amassing Horses",
            "applies_to": ["King"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 17:16", "Sefer HaChinukh 499"]
        },
        500: {
            "category": "Conquest of Israel",
            "sub_category": "Not Dwelling in Egypt",
            "applies_to": ["All"],
            "location": "Egypt",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 17:16", "Sefer HaChinukh 500"]
        },
        501: {
            "category": "Monarchy",
            "sub_category": "King Not Amassing Wives",
            "applies_to": ["King"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 17:17", "Sefer HaChinukh 501"]
        },
        502: {
            "category": "Monarchy",
            "sub_category": "King Not Amassing Wealth",
            "applies_to": ["King"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 17:17", "Sefer HaChinukh 502"]
        },
        503: {
            "category": "Monarchy",
            "sub_category": "King Writing Torah Scroll",
            "applies_to": ["King"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 17:18", "Sefer HaChinukh 503"]
        },
        504: {
            "category": "Priesthood and Levites",
            "sub_category": "Levites Not Inheriting Land",
            "applies_to": ["Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 18:1", "Sefer HaChinukh 504"]
        },
        505: {
            "category": "Priesthood and Levites",
            "sub_category": "Levites Not Taking Spoils",
            "applies_to": ["Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 18:1", "Sefer HaChinukh 505"]
        },
        506: {
            "category": "Priesthood and Levites",
            "sub_category": "Giving Foreleg, Jaw, and Maw",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:3", "Sefer HaChinukh 506"]
        },
        507: {
            "category": "Priesthood and Levites",
            "sub_category": "Great Tithe for Priest (Terumah)",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 18:4", "Sefer HaChinukh 507"]
        },
        508: {
            "category": "Priesthood and Levites",
            "sub_category": "First Shearing",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 18:4", "Sefer HaChinukh 508"]
        },
        509: {
            "category": "Temple Service",
            "sub_category": "Priests and Levites Working in Shifts",
            "applies_to": ["Priests", "Levites"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 18:6-8", "Sefer HaChinukh 509"]
        },
        510: {
            "category": "Occult Practices",
            "sub_category": "Not Engaging in Clairvoyance",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:10", "Sefer HaChinukh 510"]
        },
        511: {
            "category": "Occult Practices",
            "sub_category": "Not Doing Magic",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:10", "Sefer HaChinukh 511"]
        },
        512: {
            "category": "Occult Practices",
            "sub_category": "Not Invoking Charm",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:11", "Sefer HaChinukh 512"]
        },
        513: {
            "category": "Occult Practices",
            "sub_category": "Not Asking Master of Ov",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:11", "Sefer HaChinukh 513"]
        },
        514: {
            "category": "Occult Practices",
            "sub_category": "Not Asking Yidaaoni",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:11", "Sefer HaChinukh 514"]
        },
        515: {
            "category": "Occult Practices",
            "sub_category": "Not Inquiring of Dead",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 18:11", "Sefer HaChinukh 515"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 491-515")

if __name__ == '__main__':
    main()
