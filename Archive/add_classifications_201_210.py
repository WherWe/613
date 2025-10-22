#!/usr/bin/env python3
"""
Add classifications for mitzvot 201-210
Includes more incest laws, prohibition of Molekh worship, and other sexual prohibitions
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 201-210
    classifications = {
        201: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Daughter-in-Law",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:15"]
        },
        202: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Sister-in-Law",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:16"]
        },
        203: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Woman and Her Daughter",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:17", "Leviticus 20:14"]
        },
        204: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Woman and Her Granddaughter (Son's Daughter)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:17"]
        },
        205: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Woman and Her Granddaughter (Daughter's Daughter)",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:17"]
        },
        206: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest - Two Sisters",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:18"]
        },
        207: {
            "category": "Sexual Prohibitions",
            "sub_category": "Menstruant",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:19", "Leviticus 15:19", "Niddah 73a"]
        },
        208: {
            "category": "Idolatry",
            "sub_category": "Molekh Worship",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:21", "Deuteronomy 18:10", "Sifra, Kedoshim, Section 4:1"]
        },
        209: {
            "category": "Sexual Prohibitions",
            "sub_category": "Homosexual Relations",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:22", "Deuteronomy 23:18"]
        },
        210: {
            "category": "Sexual Prohibitions",
            "sub_category": "Bestiality",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:23", "Sanhedrin 54b"]
        }
    }
    
    # Add classifications to mitzvot
    for mitzvah in data['mitzvot']:
        mitzvah_id = mitzvah['id']
        if mitzvah_id in classifications:
            mitzvah['classification'] = classifications[mitzvah_id]
            print(f"Added classification for mitzvah #{mitzvah_id}: {mitzvah['title'][:60]}...")
    
    # Save the updated data
    with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Successfully added classifications for mitzvot 201-210")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
