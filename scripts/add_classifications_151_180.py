import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "mitzvot_data.json"


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    data = load_data()
    items = {m["id"]: m for m in data.get("mitzvot", [])}

    classifications = {
        151: {
            "category": "Temple and Sacrifices",
            "sub_category": "Priesthood conduct and service protocol",
            "applies_to": "Priests (Kohanim); High Priest (extension)",
            "location": "Temple",
            "time_scope": "When the Temple stands; during service",
            "source_refs": ["Leviticus 10:7", "Leviticus 21:12"]
        },
        152: {
            "category": "Temple and Sacrifices",
            "sub_category": "Entry/service restrictions; rulings while intoxicated",
            "applies_to": "Priests (service); all judges/deciders (rulings)",
            "location": "Temple (service); Anywhere (rulings)",
            "time_scope": "When the Temple stands (service); Always (rulings)",
            "source_refs": ["Leviticus 10:9-11"]
        },
        153: {
            "category": "Dietary Laws",
            "sub_category": "Kashrut signs — land animals",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:2-3", "Leviticus 11:47", "Leviticus 20:25"]
        },
        154: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited species — land animals",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:4-7"]
        },
        155: {
            "category": "Dietary Laws",
            "sub_category": "Kashrut signs — fish",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:9"]
        },
        156: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited species — fish without fins and scales",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:11"]
        },
        157: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited species — impure birds",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:13"]
        },
        158: {
            "category": "Dietary Laws",
            "sub_category": "Kashrut signs — locusts/grasshoppers",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:21-22"]
        },
        159: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — eight swarming creatures (sheratzim)",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "When the Temple stands (practical implications)",
            "source_refs": ["Leviticus 11:29-31"]
        },
        160: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — foods and drinks",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "When the Temple stands (practical implications)",
            "source_refs": ["Leviticus 11:34"]
        },
        161: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — carcass (nevelah)",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "When the Temple stands (practical implications)",
            "source_refs": ["Leviticus 11:39-40"]
        },
        162: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited species — swarming things of the ground",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:41-42"]
        },
        163: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited — insects from produce (when considered ‘of the ground’)",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:42"]
        },
        164: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited species — swarming creatures of the waters",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:10", "Leviticus 11:43"]
        },
        165: {
            "category": "Dietary Laws",
            "sub_category": "Prohibited species — creatures from decay",
            "applies_to": "All Israelites",
            "location": "Anywhere",
            "time_scope": "Always",
            "source_refs": ["Leviticus 11:44-45"]
        },
        166: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — woman after childbirth (yoledet)",
            "applies_to": "Women postpartum",
            "location": "Anywhere",
            "time_scope": "When the Temple stands (practical implications)",
            "source_refs": ["Leviticus 12:2", "Leviticus 12:5"]
        },
        167: {
            "category": "Temple and Sacrifices",
            "sub_category": "Consumption of consecrated foods — purity required",
            "applies_to": "All who eat consecrated foods (priests and Israelites)",
            "location": "Sancta consumption",
            "time_scope": "When the Temple stands",
            "source_refs": ["Leviticus 12:4", "Leviticus 7:20"]
        },
        168: {
            "category": "Temple and Sacrifices",
            "sub_category": "Offerings — woman after childbirth",
            "applies_to": "Women postpartum",
            "location": "Temple",
            "time_scope": "When the Temple stands",
            "source_refs": ["Leviticus 12:6-8"]
        },
        169: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — tzaraat of a person (metsora)",
            "applies_to": "Anyone with suspected tzaraat; priests for determination",
            "location": "Anywhere (requires priestly determination)",
            "time_scope": "When priests qualified to inspect are available",
            "source_refs": ["Leviticus 13:2"]
        },
        170: {
            "category": "Ritual Purity",
            "sub_category": "Tzaraat — prohibition to shave netek lesion",
            "applies_to": "Anyone with a netek (scalp/beard scab)",
            "location": "Anywhere",
            "time_scope": "When priests adjudicate tzaraat",
            "source_refs": ["Leviticus 13:33"]
        },
        171: {
            "category": "Ritual Purity",
            "sub_category": "Tzaraat — conduct and public declaration",
            "applies_to": "Metzora (confirmed)",
            "location": "Outside the camp/city; public spaces",
            "time_scope": "When applicable (during affliction)",
            "source_refs": ["Leviticus 13:45-46"]
        },
        172: {
            "category": "Ritual Purity",
            "sub_category": "Tzaraat — garments",
            "applies_to": "Owners of affected garments; priests (inspection)",
            "location": "Anywhere",
            "time_scope": "When priests adjudicate tzaraat",
            "source_refs": ["Leviticus 13:47-59"]
        },
        173: {
            "category": "Ritual Purity",
            "sub_category": "Tzaraat — purification procedure (cedar, hyssop, birds)",
            "applies_to": "Metzora (person/garment/house) in purification",
            "location": "Outside/near Temple as prescribed",
            "time_scope": "When the Temple stands / priests officiate",
            "source_refs": ["Leviticus 14:2-9"]
        },
        174: {
            "category": "Ritual Purity",
            "sub_category": "Tzaraat — second shaving on seventh day",
            "applies_to": "Metzora in purification",
            "location": "Anywhere",
            "time_scope": "When priests adjudicate tzaraat",
            "source_refs": ["Leviticus 14:9"]
        },
        175: {
            "category": "Ritual Purity",
            "sub_category": "General — immersion (mikveh)",
            "applies_to": "All Israelites",
            "location": "Mikveh or flowing spring",
            "time_scope": "Always (for purification)",
            "source_refs": ["Leviticus 14:9"]
        },
        176: {
            "category": "Temple and Sacrifices",
            "sub_category": "Offerings — metzora on the eighth day",
            "applies_to": "Metzora (lacking atonement)",
            "location": "Temple",
            "time_scope": "When the Temple stands",
            "source_refs": ["Leviticus 14:10-20", "Leviticus 14:21-32"]
        },
        177: {
            "category": "Ritual Purity",
            "sub_category": "Tzaraat — houses",
            "applies_to": "Homeowners in Eretz Israel; priests (inspection)",
            "location": "Eretz Israel",
            "time_scope": "When priests adjudicate tzaraat",
            "source_refs": ["Leviticus 14:35-53"]
        },
        178: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — zav (male discharge)",
            "applies_to": "Men experiencing zav discharge",
            "location": "Anywhere",
            "time_scope": "When the Temple stands (practical implications)",
            "source_refs": ["Leviticus 15:2-15"]
        },
        179: {
            "category": "Temple and Sacrifices",
            "sub_category": "Offerings — zav on the eighth day",
            "applies_to": "Men who were zav and recovered (lacking atonement)",
            "location": "Temple",
            "time_scope": "When the Temple stands",
            "source_refs": ["Leviticus 15:13-15"]
        },
        180: {
            "category": "Ritual Purity",
            "sub_category": "Tumah — semen emission",
            "applies_to": "Men (and those who come in contact)",
            "location": "Anywhere",
            "time_scope": "When the Temple stands (practical implications)",
            "source_refs": ["Leviticus 15:16-18"]
        },
    }

    updated = 0
    for mitzvah_id, classification in classifications.items():
        mitzvah = items.get(mitzvah_id)
        if not mitzvah:
            print(f"Warning: mitzvah id {mitzvah_id} not found; skipping")
            continue
        mitzvah["classification"] = classification
        updated += 1

    save_data(data)
    print(f"Updated classifications for {updated} mitzvot (151–180)")


if __name__ == "__main__":
    main()
