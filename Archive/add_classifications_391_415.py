#!/usr/bin/env python3
"""
Add classifications for mitzvot 391-415.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 391-415
    classifications = {
        391: {
            "category": "Temple Service",
            "sub_category": "Temple Guard Nullification",
            "applies_to": ["Levites"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 18:22", "Sefer HaChinukh 391"]
        },
        392: {
            "category": "Priesthood and Levites",
            "sub_category": "Firstborn Redemption",
            "applies_to": ["Israelites"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 18:15-16", "Sefer HaChinukh 392"]
        },
        393: {
            "category": "Priesthood and Levites",
            "sub_category": "Firstborn Pure Animal",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 18:17", "Sefer HaChinukh 393"]
        },
        394: {
            "category": "Temple Service",
            "sub_category": "Levite Service",
            "applies_to": ["Levites"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 18:23", "Numbers 8:24-25", "Sefer HaChinukh 394"]
        },
        395: {
            "category": "Agricultural Laws",
            "sub_category": "First Tithe",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Numbers 18:24", "Leviticus 27:30", "Sefer HaChinukh 395"]
        },
        396: {
            "category": "Priesthood and Levites",
            "sub_category": "Tithe from Tithe (Terumot Maaser)",
            "applies_to": ["Levites"],
            "location": "Eretz Yisrael",
            "time_scope": "Always",
            "source_refs": ["Numbers 18:26-29", "Sefer HaChinukh 396"]
        },
        397: {
            "category": "Purity and Impurity",
            "sub_category": "Red Heifer",
            "applies_to": ["Community"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 19:2-10", "Sefer HaChinukh 397"]
        },
        398: {
            "category": "Purity and Impurity",
            "sub_category": "Impurity of Dead Body",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 19:14", "Sefer HaChinukh 398"]
        },
        399: {
            "category": "Purity and Impurity",
            "sub_category": "Niddah Waters (Sprinkling)",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 19:19-21", "Sefer HaChinukh 399"]
        },
        400: {
            "category": "Civil Law",
            "sub_category": "Laws of Inheritance",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 27:8-11", "Sefer HaChinukh 400"]
        },
        401: {
            "category": "Sacrifices",
            "sub_category": "Regular Daily Sacrifices",
            "applies_to": ["Community"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 28:2-8", "Sefer HaChinukh 401"]
        },
        402: {
            "category": "Sacrifices",
            "sub_category": "Additional Shabbat Sacrifice",
            "applies_to": ["Community"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 28:9-10", "Sefer HaChinukh 402"]
        },
        403: {
            "category": "Sacrifices",
            "sub_category": "Additional Monthly Sacrifice (Rosh Chodesh)",
            "applies_to": ["Community"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 28:11-15", "Sefer HaChinukh 403"]
        },
        404: {
            "category": "Festivals and Holidays",
            "sub_category": "Additional Shavuot Sacrifice",
            "applies_to": ["Community"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 28:26-31", "Sefer HaChinukh 404"]
        },
        405: {
            "category": "Festivals and Holidays",
            "sub_category": "Shofar on Rosh Hashanah",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 29:1", "Leviticus 25:9", "Sefer HaChinukh 405"]
        },
        406: {
            "category": "Vows and Oaths",
            "sub_category": "Abrogation of Vows",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 30:3", "Sefer HaChinukh 406"]
        },
        407: {
            "category": "Vows and Oaths",
            "sub_category": "Not Profaning Words from Vows",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 30:3", "Sefer HaChinukh 407"]
        },
        408: {
            "category": "Priesthood and Levites",
            "sub_category": "Cities for Levites",
            "applies_to": ["Community"],
            "location": "Eretz Yisrael",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 35:2-8", "Sefer HaChinukh 408"]
        },
        409: {
            "category": "Judicial System",
            "sub_category": "Not Killing Liable Person Before Trial",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Numbers 35:12", "Sefer HaChinukh 409"]
        },
        410: {
            "category": "Judicial System",
            "sub_category": "Cities of Refuge",
            "applies_to": ["Courts"],
            "location": "Eretz Yisrael",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 35:25-28", "Sefer HaChinukh 410"]
        },
        411: {
            "category": "Judicial System",
            "sub_category": "Witness Not Ruling",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 35:30", "Deuteronomy 17:6", "Sefer HaChinukh 411"]
        },
        412: {
            "category": "Civil Law",
            "sub_category": "No Ransom for Murderer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 35:31", "Sefer HaChinukh 412"]
        },
        413: {
            "category": "Civil Law",
            "sub_category": "No Ransom for Exile",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Temple Era",
            "source_refs": ["Numbers 35:32", "Sefer HaChinukh 413"]
        },
        414: {
            "category": "Judicial System",
            "sub_category": "Not Appointing Ignorant Judge",
            "applies_to": ["Courts"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 1:17", "Sefer HaChinukh 414"]
        },
        415: {
            "category": "Judicial System",
            "sub_category": "Judge Not Fearing",
            "applies_to": ["Judges"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 1:17", "Sefer HaChinukh 415"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 391-415")

if __name__ == '__main__':
    main()
