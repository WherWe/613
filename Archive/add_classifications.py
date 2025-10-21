#!/usr/bin/env python3
"""
Add classification metadata to mitzvot 1-50 in mitzvot_data.json
"""

import json
from pathlib import Path

# Classifications for mitzvot 1-13 based on halakhic sources
classifications = {
    1: {
        "category": "Family Law",
        "sub_category": "Marriage and Procreation",
        "applies_to": ["Men"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Genesis 1:28", "Talmud:Yevamot 61b-62b", "Talmud:Gittin 41b", "Shulchan Arukh:EH 1"]
    },
    2: {
        "category": "Covenant Signs",
        "sub_category": "Circumcision",
        "applies_to": ["Men", "All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Genesis 17:10-14", "Leviticus 12:3", "Talmud:Shabbat 132a", "Talmud:Yevamot 71a", "Shulchan Arukh:YD 260-266"]
    },
    3: {
        "category": "Dietary Laws",
        "sub_category": "Forbidden Foods",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Genesis 32:33", "Talmud:Chullin 89b-96a", "Shulchan Arukh:YD 65"]
    },
    4: {
        "category": "Calendar and Time",
        "sub_category": "Sanctification of Months",
        "applies_to": ["Court/Sanhedrin"],
        "location": "Eretz Yisrael",
        "time_scope": "Always (with ordained judges)",
        "source_refs": ["Exodus 12:2", "Exodus 13:10", "Deuteronomy 16:1", "Talmud:Rosh Hashanah 22a", "Talmud:Sanhedrin 10b"]
    },
    5: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "14th Nissan (Temple Era)",
        "source_refs": ["Exodus 12:6", "Talmud:Pesachim 58a-70a", "Mishneh Torah:Korban Pesach 1:12"]
    },
    6: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "15th Nissan Evening (Temple Era)",
        "source_refs": ["Exodus 12:8", "Talmud:Pesachim 69a-120a", "Mishneh Torah:Korban Pesach 1"]
    },
    7: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:9", "Talmud:Pesachim 41a", "Mishneh Torah:Korban Pesach 8"]
    },
    8: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:10", "Talmud:Pesachim", "Mishneh Torah:Korban Pesach 9-10"]
    },
    9: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Chametz Removal",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "14th Nissan",
        "source_refs": ["Exodus 12:15", "Talmud:Pesachim 5a-21a", "Shulchan Arukh:OC 431-440"]
    },
    10: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Matzah",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "15th Nissan Evening",
        "source_refs": ["Exodus 12:18", "Talmud:Pesachim 35a-42a", "Shulchan Arukh:OC 453-466"]
    },
    11: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Chametz Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Pesach (7 days)",
        "source_refs": ["Exodus 12:19", "Exodus 12:39", "Talmud:Pesachim 5b-45b", "Shulchan Arukh:OC 440-442"]
    },
    12: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Chametz Mixtures",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Pesach (7 days)",
        "source_refs": ["Exodus 12:20", "Talmud:Pesachim 28b-43a", "Shulchan Arukh:OC 446"]
    },
    13: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice Eligibility",
        "applies_to": ["Jews only"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:43", "Mekhilta DeRabbi Shimon Bar Yochai 12:43", "Mishneh Torah:Korban Pesach 9"]
    },
    14: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice Eligibility",
        "applies_to": ["Jews only"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:45", "Talmud:Yevamot 71a"]
    },
    15: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:46", "Talmud:Pesachim 60b-85b", "Mishneh Torah:Korban Pesach 9:3"]
    },
    16: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:46", "Talmud:Pesachim 85a", "Talmud:Makkot 23b"]
    },
    17: {
        "category": "Temple Service",
        "sub_category": "Pesach Sacrifice Eligibility",
        "applies_to": ["Circumcised Jews only"],
        "location": "Temple",
        "time_scope": "Pesach (Temple Era)",
        "source_refs": ["Exodus 12:48", "Talmud:Pesachim"]
    },
    18: {
        "category": "Temple Service",
        "sub_category": "Firstborn Animals",
        "applies_to": ["All Israel"],
        "location": "Eretz Yisrael (primarily)",
        "time_scope": "Always",
        "source_refs": ["Exodus 13:2", "Deuteronomy 15:19-22", "Talmud:Bekhorot 10a-13a", "Shulchan Arukh:YD 306-320"]
    },
    19: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Chametz Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Pesach (7 days)",
        "source_refs": ["Exodus 13:3", "Talmud:Pesachim 35a", "Shulchan Arukh:OC 446-468"]
    },
    20: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Chametz Not Seen",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Pesach (7 days)",
        "source_refs": ["Exodus 13:7", "Talmud:Beitzah 7b", "Shulchan Arukh:OC 434"]
    },
    21: {
        "category": "Festival Laws",
        "sub_category": "Pesach - Haggadah",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "15th Nissan Evening",
        "source_refs": ["Exodus 13:8", "Talmud:Pesachim 116a", "Shulchan Arukh:OC 469-482"]
    },
    22: {
        "category": "Temple Service",
        "sub_category": "Firstborn Donkeys",
        "applies_to": ["Israelites (not Kohanim/Levites)"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 13:13", "Talmud:Bekhorot 11a", "Shulchan Arukh:YD 221"]
    },
    23: {
        "category": "Temple Service",
        "sub_category": "Firstborn Donkeys",
        "applies_to": ["Israelites (not Kohanim/Levites)"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 13:13", "Talmud:Bekhorot 13a", "Shulchan Arukh:YD 221"]
    },
    24: {
        "category": "Shabbat and Rest",
        "sub_category": "Shabbat Boundaries",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Shabbat",
        "source_refs": ["Exodus 16:29", "Talmud:Eruvin 17b-61b", "Mishneh Torah:Shabbat 27:1-2"]
    },
    25: {
        "category": "Faith and Belief",
        "sub_category": "Belief in God",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:2", "Mishneh Torah:Yesodei HaTorah 1"]
    },
    26: {
        "category": "Faith and Belief",
        "sub_category": "Prohibition of Idolatry",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:3", "Talmud:Sanhedrin 56a-60b", "Talmud:Avodah Zarah"]
    },
    27: {
        "category": "Faith and Belief",
        "sub_category": "Prohibition of Idolatry",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:4", "Leviticus 19:4", "Talmud:Avodah Zarah 43b", "Shulchan Arukh:YD 139-141"]
    },
    28: {
        "category": "Faith and Belief",
        "sub_category": "Prohibition of Idolatry",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:5"]
    },
    29: {
        "category": "Faith and Belief",
        "sub_category": "Prohibition of Idolatry",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:5"]
    },
    30: {
        "category": "Speech and Oaths",
        "sub_category": "False Oaths",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:7", "Talmud:Shevuot", "Shulchan Arukh:YD 236"]
    },
    31: {
        "category": "Shabbat and Rest",
        "sub_category": "Shabbat Observance",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Shabbat",
        "source_refs": ["Exodus 20:8", "Talmud:Shabbat", "Shulchan Arukh:OC 242-416"]
    },
    32: {
        "category": "Shabbat and Rest",
        "sub_category": "Shabbat Work Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Shabbat",
        "source_refs": ["Exodus 20:10", "Talmud:Shabbat", "Shulchan Arukh:OC 242-416"]
    },
    33: {
        "category": "Family Law",
        "sub_category": "Honoring Parents",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:12", "Deuteronomy 5:16", "Talmud:Kiddushin 30b-32a", "Shulchan Arukh:YD 240"]
    },
    34: {
        "category": "Criminal Law",
        "sub_category": "Murder Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:13", "Deuteronomy 5:17", "Talmud:Sanhedrin 72b-85b"]
    },
    35: {
        "category": "Family Law",
        "sub_category": "Adultery Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:13", "Leviticus 18:20", "Talmud:Sanhedrin 52b-55a"]
    },
    36: {
        "category": "Property Law",
        "sub_category": "Theft Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:13", "Leviticus 19:11", "Talmud:Bava Kamma"]
    },
    37: {
        "category": "Judicial Law",
        "sub_category": "False Testimony",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:13", "Deuteronomy 19:16-21", "Talmud:Sanhedrin 29a"]
    },
    38: {
        "category": "Ethics and Character",
        "sub_category": "Coveting Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 20:14", "Deuteronomy 5:18"]
    },
    39: {
        "category": "Ethics and Character",
        "sub_category": "Desiring Prohibition",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Deuteronomy 5:18"]
    },
    40: {
        "category": "Temple Service",
        "sub_category": "Sanctuary Construction",
        "applies_to": ["All Israel"],
        "location": "Eretz Yisrael",
        "time_scope": "Temple Era",
        "source_refs": ["Exodus 25:8", "Mishneh Torah:Beit HaBechirah"]
    },
    41: {
        "category": "Temple Service",
        "sub_category": "Respect for Sanctuary",
        "applies_to": ["All Israel"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Leviticus 19:30", "Talmud:Yevamot 6b"]
    },
    42: {
        "category": "Temple Service",
        "sub_category": "Guarding the Temple",
        "applies_to": ["Kohanim and Levites"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 18:2-4", "Mishneh Torah:Beit HaBechirah 8"]
    },
    43: {
        "category": "Priestly Service",
        "sub_category": "Levite Service",
        "applies_to": ["Levites"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 18:23"]
    },
    44: {
        "category": "Priestly Service",
        "sub_category": "Priestly Service",
        "applies_to": ["Kohanim"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Exodus 30:19-20", "Numbers 18:7"]
    },
    45: {
        "category": "Priestly Service",
        "sub_category": "Service Restrictions",
        "applies_to": ["Kohanim"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Numbers 18:3"]
    },
    46: {
        "category": "Temple Service",
        "sub_category": "Priestly Gifts",
        "applies_to": ["All Israel"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Exodus 30:13", "Mishneh Torah:Shekalim"]
    },
    47: {
        "category": "Priestly Service",
        "sub_category": "High Priest Requirements",
        "applies_to": ["Kohen Gadol"],
        "location": "Temple",
        "time_scope": "Temple Era",
        "source_refs": ["Leviticus 21:10-12"]
    },
    48: {
        "category": "Priestly Service",
        "sub_category": "Priestly Conduct",
        "applies_to": ["Kohanim"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Leviticus 21:1-6", "Shulchan Arukh:YD 369-373"]
    },
    49: {
        "category": "Priestly Service",
        "sub_category": "High Priest Conduct",
        "applies_to": ["Kohen Gadol"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Leviticus 21:11"]
    },
    50: {
        "category": "Priestly Service",
        "sub_category": "Priestly Marriage",
        "applies_to": ["Kohanim"],
        "location": "Anywhere",
        "time_scope": "Always",
        "source_refs": ["Leviticus 21:7", "Shulchan Arukh:EH 6"]
    }
}

def main():
    json_path = Path('/Users/aaronhayden/Desktop/613/mitzvot_data.json')
    
    print(f"Reading {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add classification to mitzvot 1-50
    count = 0
    for mitzvah in data['mitzvot']:
        if mitzvah['id'] in classifications:
            mitzvah['classification'] = classifications[mitzvah['id']]
            count += 1
            print(f"✓ Added classification to mitzvah #{mitzvah['id']}: {mitzvah['title'][:50]}...")
        
        if count >= 50:
            break
    
    print(f"\nWriting updated JSON...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Successfully classified {count} mitzvot")
    print(f"\nClassifications added:")
    for mitzvah_id, classification in sorted(classifications.items()):
        print(f"  #{mitzvah_id}: {classification['category']} > {classification['sub_category']}")
        print(f"         Applies to: {', '.join(classification['applies_to'])}")
        print(f"         Location: {classification['location']}, Time: {classification['time_scope']}")
        print()

if __name__ == "__main__":
    main()
