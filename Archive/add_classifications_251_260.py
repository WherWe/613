#!/usr/bin/env python3
"""
Add classifications for mitzvot 251-260
Includes prohibitions on altering appearance, idolatry/occult,
honoring sages and Temple, honest measures, and cursing parents
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 251-260
    classifications = {
        251: {
            "category": "Personal Conduct",
            "sub_category": "Prohibition of Rounding Head Corners",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:27"]
        },
        252: {
            "category": "Personal Conduct",
            "sub_category": "Prohibition of Destroying Beard Corners",
            "applies_to": ["Men"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:27"]
        },
        253: {
            "category": "Personal Conduct",
            "sub_category": "Prohibition of Tattoos",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:28"]
        },
        254: {
            "category": "Temple Service",
            "sub_category": "Awe of Temple",
            "applies_to": ["Men", "Women"],
            "location": "Temple",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:30"]
        },
        255: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Ov (Necromancy)",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:31"]
        },
        256: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Yidoni (Fortune-telling)",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:31"]
        },
        257: {
            "category": "Respect for Authority",
            "sub_category": "Honoring Sages",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:32"]
        },
        258: {
            "category": "Business Ethics",
            "sub_category": "Prohibition of False Measures",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:35"]
        },
        259: {
            "category": "Business Ethics",
            "sub_category": "Command for Honest Measures",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:36"]
        },
        260: {
            "category": "Family Law",
            "sub_category": "Prohibition of Cursing Parents",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 20:9"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 251-260")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
