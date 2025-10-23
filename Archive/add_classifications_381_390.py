#!/usr/bin/env python3
"""
Add classifications for mitzvot 381-390
Source: Sefer HaChinukh - en - merged.json
"""

import json

# Load the mitzvot data
with open('mitzvot_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Classifications for mitzvot 381-390
classifications = {
    381: {
        "category": "Festivals and Holidays",
        "sub_category": "Pesach Sheni",
        "applies_to": ["Men"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 9:11", "Pesachim 40a", "Pesachim 39a", "Pesachim 95a"]
    },
    382: {
        "category": "Festivals and Holidays",
        "sub_category": "Pesach Sheni",
        "applies_to": ["Men"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 9:12"]
    },
    383: {
        "category": "Festivals and Holidays",
        "sub_category": "Pesach Sheni",
        "applies_to": ["Men"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 9:12"]
    },
    384: {
        "category": "Temple Service",
        "sub_category": "Priestly Duties",
        "applies_to": ["Kohanim"],
        "location": "Temple",
        "time_scope": "Always (during sacrifices and war)",
        "source_refs": ["Numbers 10:9-10", "Numbers 10:8", "Rosh HaShanah 29a", "Arakhin 13a", "Menachot 28a", "Mishnah Tamid 7:3", "Taanit 19a"]
    },
    385: {
        "category": "Agricultural Laws",
        "sub_category": "Priestly Gifts",
        "applies_to": ["Men", "Women"],
        "location": "Eretz Yisrael (Torah), Anywhere (Rabbinic)",
        "time_scope": "Always",
        "source_refs": ["Numbers 15:20", "Eruvin 93a", "Mishnah Challah 3:1", "Mishnah Challah 2:7", "Ketubot 20a"]
    },
    386: {
        "category": "Daily Observance",
        "sub_category": "Tzitzit",
        "applies_to": ["Men"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Numbers 15:18", "Numbers 15:39", "Deuteronomy 22:12", "Menachot 43b", "Menachot 38a-42a", "Shabbat 32b", "Menachot 41a"]
    },
    387: {
        "category": "Thought and Belief",
        "sub_category": "Forbidden Thoughts",
        "applies_to": ["Men", "Women"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Numbers 15:39", "Berakhot 12b", "Kiddushin 40a", "Judges 14:3", "Avot 4:2"]
    },
    388: {
        "category": "Temple Service",
        "sub_category": "Temple Guard",
        "applies_to": ["Kohanim", "Levites"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 18:4", "Mishnah Middot 1:1-2"]
    },
    389: {
        "category": "Temple Service",
        "sub_category": "Service Boundaries",
        "applies_to": ["Kohanim", "Levites"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 4:19", "Numbers 18:3", "Mishnah Shekalim 5:1", "Taanit 27a"]
    },
    390: {
        "category": "Temple Service",
        "sub_category": "Service Restrictions",
        "applies_to": ["All non-Kohanim"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 18:4", "Numbers 18:22", "Zevachim 32a", "Yoma 24a"]
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

print("\nSuccessfully added classifications for mitzvot 381-390")
