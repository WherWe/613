#!/usr/bin/env python3
"""
Add classifications for mitzvot 181-190
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 181-190
    classifications = {
        181: {
            "category": "Ritual Purity",
            "sub_category": "Menstrual Impurity",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 15:19"]
        },
        182: {
            "category": "Ritual Purity",
            "sub_category": "Zavah (Irregular Discharge)",
            "applies_to": ["Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 15:25", "Niddah 72b"]
        },
        183: {
            "category": "Sacrifices",
            "sub_category": "Purification Offering",
            "applies_to": ["Women"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 16:28-29"]
        },
        184: {
            "category": "Temple Service",
            "sub_category": "Priestly Restrictions",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Always",
            "source_refs": ["Leviticus 16:2", "Mishnah Kelim 1:9", "Megillah 28a"]
        },
        185: {
            "category": "Temple Service",
            "sub_category": "Yom Kippur Service",
            "applies_to": ["Kohen Gadol"],
            "location": "Temple",
            "time_scope": "Festival",
            "source_refs": ["Leviticus 16:3", "Tractate Yoma"]
        },
        186: {
            "category": "Sacrifices",
            "sub_category": "Prohibition",
            "applies_to": ["All Israel"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 17:3-4", "Zevachim 106a"]
        },
        187: {
            "category": "Kashrut",
            "sub_category": "Ritual Slaughter",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 17:13", "Chullin 83b"]
        },
        188: {
            "category": "Sexual Prohibitions",
            "sub_category": "General Prohibition of Intimacy",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:6", "Leviticus 18:26", "Avot 3:13", "Kiddushin 80b"]
        },
        189: {
            "category": "Sexual Prohibitions",
            "sub_category": "Homosexual Relations",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:7", "Leviticus 18:22", "Sanhedrin 54a"]
        },
        190: {
            "category": "Sexual Prohibitions",
            "sub_category": "Incest",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 18:7", "Sanhedrin 54a", "Yevamot 21a"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 181-190")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
