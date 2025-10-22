#!/usr/bin/env python3
"""
Add classifications for mitzvot 261-270
Includes capital punishment, prohibition of gentile practices,
priestly purity laws, marriage restrictions for priests
Based on Sefer HaChinukh source text analysis
"""

import json

def add_classifications():
    # Load the current mitzvot data
    with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Classifications for mitzvot 261-270
    classifications = {
        261: {
            "category": "Criminal Law",
            "sub_category": "Capital Punishment by Burning",
            "applies_to": ["Courts"],
            "location": "Eretz Yisrael",
            "time_scope": "Conditional",
            "source_refs": ["Leviticus 20:14"]
        },
        262: {
            "category": "Idolatry",
            "sub_category": "Prohibition of Gentile Practices",
            "applies_to": ["Men", "Women"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 20:23"]
        },
        263: {
            "category": "Priestly Purity",
            "sub_category": "Prohibition of Defilement to Dead",
            "applies_to": ["Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:1"]
        },
        264: {
            "category": "Priestly Purity",
            "sub_category": "Defilement for Close Relatives",
            "applies_to": ["Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:2-3"]
        },
        265: {
            "category": "Temple Service",
            "sub_category": "Tevul Yom Service Prohibition",
            "applies_to": ["Kohanim"],
            "location": "Temple",
            "time_scope": "Temple Era",
            "source_refs": ["Leviticus 21:6"]
        },
        266: {
            "category": "Priestly Marriage",
            "sub_category": "Prohibition of Marrying Zonah",
            "applies_to": ["Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:7"]
        },
        267: {
            "category": "Priestly Marriage",
            "sub_category": "Prohibition of Marrying Challalah",
            "applies_to": ["Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:7"]
        },
        268: {
            "category": "Priestly Marriage",
            "sub_category": "Prohibition of Marrying Divorcee",
            "applies_to": ["Kohanim"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:7"]
        },
        269: {
            "category": "Priestly Sanctity",
            "sub_category": "Sanctifying Priests",
            "applies_to": ["All Israel"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:8"]
        },
        270: {
            "category": "Priestly Purity",
            "sub_category": "High Priest - No Defilement to Dead",
            "applies_to": ["Kohen Gadol"],
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 21:11"]
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
    
    print(f"\n✓ Successfully added classifications for mitzvot 261-270")
    print(f"Total classified: {sum(1 for m in data['mitzvot'] if 'classification' in m and m['classification'])}/{len(data['mitzvot'])}")

if __name__ == '__main__':
    add_classifications()
