#!/usr/bin/env python3
"""
Add classifications for mitzvot 231-240
Includes prohibitions of cursing, causing harm, judicial misconduct,
talebearing, hatred, and commandment of rebuke
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 231-240
    classifications = {
        231: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Cursing",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:14"]
        },
        232: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Misleading",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:14"]
        },
        233: {
            "category": "Judicial Law",
            "sub_category": "Prohibition of Perverting Justice",
            "applies_to": ["Judges"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:15"]
        },
        234: {
            "category": "Judicial Law",
            "sub_category": "Prohibition of Favoring Great Person",
            "applies_to": ["Judges"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:15"]
        },
        235: {
            "category": "Judicial Law",
            "sub_category": "Command to Judge Righteously",
            "applies_to": ["Judges"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:15"]
        },
        236: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Talebearing",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:16"]
        },
        237: {
            "category": "Interpersonal Ethics",
            "sub_category": "Obligation to Save Life",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:16"]
        },
        238: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Hatred",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:17"]
        },
        239: {
            "category": "Interpersonal Ethics",
            "sub_category": "Command to Rebuke",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:17"]
        },
        240: {
            "category": "Interpersonal Ethics",
            "sub_category": "Prohibition of Embarrassing",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 19:17"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 231-240")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
