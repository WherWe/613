#!/usr/bin/env python3
"""
Add classifications for mitzvot 416-440.
"""

import json
import sys

def main():
    # Load the existing data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 416-440
    classifications = {
        416: {
            "category": "Interpersonal Relations",
            "sub_category": "Not Desiring",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 5:18", "Sefer HaChinukh 416"]
        },
        417: {
            "category": "Thought and Belief",
            "sub_category": "Unification of God",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 6:4", "Sefer HaChinukh 417"]
        },
        418: {
            "category": "Thought and Belief",
            "sub_category": "Loving God",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 6:5", "Sefer HaChinukh 418"]
        },
        419: {
            "category": "Daily Observance",
            "sub_category": "Torah Study",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 6:7", "Sefer HaChinukh 419"]
        },
        420: {
            "category": "Daily Observance",
            "sub_category": "Recitation of Shema",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 6:7", "Sefer HaChinukh 420"]
        },
        421: {
            "category": "Daily Observance",
            "sub_category": "Tefillin of Arm",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Weekdays",
            "source_refs": ["Deuteronomy 6:8", "Sefer HaChinukh 421"]
        },
        422: {
            "category": "Daily Observance",
            "sub_category": "Tefillin of Head",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Weekdays",
            "source_refs": ["Deuteronomy 6:8", "Sefer HaChinukh 422"]
        },
        423: {
            "category": "Daily Observance",
            "sub_category": "Mezuzah",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 6:9", "Sefer HaChinukh 423"]
        },
        424: {
            "category": "Prophets and Prophecy",
            "sub_category": "Not Testing True Prophet",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 6:16", "Sefer HaChinukh 424"]
        },
        425: {
            "category": "Conquest of Israel",
            "sub_category": "Killing Seven Nations",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 7:2", "Deuteronomy 20:17", "Sefer HaChinukh 425"]
        },
        426: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Favoring Idolater",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 7:2", "Sefer HaChinukh 426"]
        },
        427: {
            "category": "Family Law",
            "sub_category": "Not Marrying Idolaters",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 7:3", "Sefer HaChinukh 427"]
        },
        428: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Benefiting from Idolatry Coverings",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 7:25", "Sefer HaChinukh 428"]
        },
        429: {
            "category": "Worship and Idolatry",
            "sub_category": "Not Benefiting from Idolatry Offering",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 7:26", "Sefer HaChinukh 429"]
        },
        430: {
            "category": "Daily Observance",
            "sub_category": "Blessing After Food",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 8:10", "Sefer HaChinukh 430"]
        },
        431: {
            "category": "Interpersonal Relations",
            "sub_category": "Loving Converts",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 10:19", "Sefer HaChinukh 431"]
        },
        432: {
            "category": "Thought and Belief",
            "sub_category": "Fearing God",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 10:20", "Sefer HaChinukh 432"]
        },
        433: {
            "category": "Daily Observance",
            "sub_category": "Prayer",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 10:20", "Sefer HaChinukh 433"]
        },
        434: {
            "category": "Torah Study",
            "sub_category": "Clinging to Torah Sages",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 10:20", "Sefer HaChinukh 434"]
        },
        435: {
            "category": "Vows and Oaths",
            "sub_category": "Swearing Truthfully in His Name",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 10:20", "Sefer HaChinukh 435"]
        },
        436: {
            "category": "Worship and Idolatry",
            "sub_category": "Destroying Idolatry",
            "applies_to": ["All"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Deuteronomy 12:2-3", "Sefer HaChinukh 436"]
        },
        437: {
            "category": "Temple",
            "sub_category": "Not Destroying Holy Things",
            "applies_to": ["All"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Deuteronomy 12:4", "Sefer HaChinukh 437"]
        },
        438: {
            "category": "Sacrifices",
            "sub_category": "Bringing Vows on First Festival",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:5-6", "Sefer HaChinukh 438"]
        },
        439: {
            "category": "Sacrifices",
            "sub_category": "Not Sacrificing Outside Temple",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:13", "Sefer HaChinukh 439"]
        },
        440: {
            "category": "Sacrifices",
            "sub_category": "Sacrificing in Choice House",
            "applies_to": ["All"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Deuteronomy 12:14", "Sefer HaChinukh 440"]
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
    
    print(f"\nSuccessfully added classifications for mitzvot 416-440")

if __name__ == '__main__':
    main()
