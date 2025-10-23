#!/usr/bin/env python3
"""
Add classifications for mitzvot 371-380
Source: Sefer HaChinukh - en - merged.json
"""

import json

# Load the mitzvot data
with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Classifications for mitzvot 371-380
classifications = {
    371: {
        "category": "Personal Status",
        "sub_category": "Nazirite Laws",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "During Nazirite Term",
        "source_refs": ["Numbers 6:4", "Nazir 38b"]
    },
    372: {
        "category": "Personal Status",
        "sub_category": "Nazirite Laws",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "During Nazirite Term",
        "source_refs": ["Numbers 6:4", "Nazir 38b"]
    },
    373: {
        "category": "Personal Status",
        "sub_category": "Nazirite Laws",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "During Nazirite Term",
        "source_refs": ["Numbers 6:5", "Nazir 39a-40a"]
    },
    374: {
        "category": "Personal Status",
        "sub_category": "Nazirite Laws",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "During Nazirite Term",
        "source_refs": ["Numbers 6:5", "Nazir 4b", "Nazir 19a", "Nazir 19b"]
    },
    375: {
        "category": "Personal Status",
        "sub_category": "Nazirite Laws",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "During Nazirite Term",
        "source_refs": ["Numbers 6:6", "Nazir 43a"]
    },
    376: {
        "category": "Personal Status",
        "sub_category": "Nazirite Laws",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "During Nazirite Term",
        "source_refs": ["Numbers 6:7", "Numbers 6:9", "Leviticus 21:22", "Nazir 49b", "Nazir 44a"]
    },
    377: {
        "category": "Personal Status",
        "sub_category": "Nazirite Completion",
        "applies_to": ["Men", "Women"],
        "location": "Temple (for sacrifices)",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 6:13", "Numbers 6:9", "Mishnah Middot 2:5", "Nazir 46a"]
    },
    378: {
        "category": "Temple Service",
        "sub_category": "Priestly Blessing",
        "applies_to": ["Kohanim"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Numbers 6:23", "Megillah 23b", "Sotah 38b", "Taanit 26b"]
    },
    379: {
        "category": "Temple Service",
        "sub_category": "Ark Transportation",
        "applies_to": ["Kohanim", "Levites"],
        "location": "Eretz Yisrael",
        "time_scope": "When Ark Moved",
        "source_refs": ["Numbers 7:9", "Joshua 3:3-6", "I Chronicles 15:14-15", "II Chronicles 35:3", "Sotah 33b-34a"]
    },
    380: {
        "category": "Festivals and Holidays",
        "sub_category": "Pesach Sheni",
        "applies_to": ["Men"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 9:11", "Pesachim 73a", "Pesachim 93a-95a"]
    }
}

# Update the mitzvot with classifications
for mitzvah in data['mitzvot']:
    mitzvah_id = mitzvah['id']
    if mitzvah_id in classifications:
        mitzvah['classification'] = classifications[mitzvah_id]
        print(f"Added classification for mitzvah {mitzvah_id}: {mitzvah['title']}")

# Save the updated data
with open('mitzvot_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully added classifications for mitzvot 371-380")
