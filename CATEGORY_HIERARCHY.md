# Category Hierarchy System

## Overview

The 613 mitzvot have been organized into a **two-tier category system**:

- **15 Main Categories** - Broad thematic groupings
- **70 Subcategories** - Detailed classifications

This provides both high-level filtering and detailed categorization.

## Main Categories (15)

### 1. **Faith and Belief** (45 mitzvot)

Core beliefs, monotheism, relationship with God, prohibition of idolatry and occult practices

- Subcategories: Faith and Belief, Faith and Sanctity, Thought and Belief, Belief and Blasphemy, Idolatry, Idolatry and Forbidden Practices, Worship and Idolatry, Occult Practices

### 2. **Torah and Study** (9 mitzvot)

Torah study, transmission, and prophets

- Subcategories: Torah Study, Torah Law, Prophets and Prophecy

### 3. **Temple and Worship** (135 mitzvot)

Temple service, sacrifices, and sacred worship

- Subcategories: Temple, Temple Service, Temple and Sacrifices, Sacrifices

### 4. **Priesthood** (34 mitzvot)

Kohanim and Levites: service, gifts, purity, and sanctity

- Subcategories: Priesthood and Levites, Priestly Service, Priestly Gifts, Priestly Sanctity, Priestly Purity, Priestly Marriage

### 5. **Purity and Ritual** (25 mitzvot)

Ritual purity laws, impurity, and purification

- Subcategories: Purity and Impurity, Ritual Purity, Camp Purity

### 6. **Shabbat and Festivals** (50 mitzvot)

Weekly Shabbat, festivals, and holy days

- Subcategories: Shabbat and Rest, Sabbath and Festivals, Festival Laws, Festivals and Holidays, Calendar and Time, Time and Calendar

### 7. **Daily Life and Observance** (15 mitzvot)

Daily mitzvot, covenant signs, and personal conduct

- Subcategories: Daily Observance, Covenant Signs, Personal Conduct, Modesty and Dress, Repentance

### 8. **Dietary Laws** (35 mitzvot)

Kashrut, forbidden foods, and eating restrictions

- Subcategories: Dietary Laws, Kashrut, Forbidden Mixtures, Animal Welfare

### 9. **Agriculture and Land** (44 mitzvot)

Agricultural laws, gifts, tithes, and land-based mitzvot

- Subcategories: Agricultural Laws, Agricultural Gifts, Agricultural Laws and Gifts

### 10. **Family and Relationships** (80 mitzvot)

Marriage, family law, and interpersonal relations

- Subcategories: Family Law, Personal Status, Sexual Prohibitions, Interpersonal Relations, Interpersonal Ethics

### 11. **Ethics and Character** (17 mitzvot)

Moral conduct, charity, kindness, and proper speech

- Subcategories: Ethics and Character, Charity and Kindness, Speech and Oaths, Vows and Oaths, Oaths and Vows, Respect for Authority

### 12. **Civil and Financial Law** (62 mitzvot)

Property, business, labor, and financial regulations

- Subcategories: Civil Law, Civil and Tort Law, Criminal and Civil Law, Property Law, Financial Law, Business Ethics, Labor Law, Slavery Laws

### 13. **Judicial System** (34 mitzvot)

Courts, judges, and legal procedure

- Subcategories: Judicial System, Judicial Law, Criminal Law

### 14. **National Life** (23 mitzvot)

Monarchy, warfare, conquest of Israel, and Amalek

- Subcategories: Monarchy, Warfare, Conquest of Israel, Amalek

### 15. **Life and Death** (5 mitzvot)

Safety, health, burial, and mourning

- Subcategories: Safety and Health, Burial, Mourning

## Data Structure

Each mitzvah now has:

```json
{
  "id": 1,
  "classification": {
    "main_category": "Daily Life and Observance",
    "sub_category": "Daily Observance",
    "applies_to": ["Men"],
    "location": "Anywhere",
    "time_scope": "Always"
  }
}
```

## Files

- **`category_hierarchy.json`** - Complete mapping of subcategories to main categories
  - `hierarchy` object: Main categories with their subcategories and descriptions
  - `subcategory_to_main` object: Quick lookup from any subcategory to its main category
- **`mitzvot_data.json`** - Updated with both `main_category` and `sub_category` fields

- **`add_main_categories.py`** - Script to apply the hierarchy to the data

## Usage in UI

The UI can now offer:

1. **Main Category Filter** - Select from 15 broad categories
2. **Subcategory Filter** - Drill down to 70 specific topics
3. **Hierarchical Display** - Group mitzvot by main category, then subcategory

This makes browsing more intuitive while preserving the detailed classification system.

## Benefits

✅ **Easier Navigation** - 15 main categories instead of 70 options  
✅ **Better Organization** - Logical grouping of related topics  
✅ **Flexible Filtering** - Filter by broad or specific categories  
✅ **Clearer Structure** - Hierarchical relationship explicit in data  
✅ **Backward Compatible** - Subcategories preserved for detailed filtering

## Largest Categories

1. **Temple and Worship**: 135 mitzvot (22% of total)
2. **Family and Relationships**: 80 mitzvot (13%)
3. **Civil and Financial Law**: 62 mitzvot (10%)
4. **Shabbat and Festivals**: 50 mitzvot (8%)
5. **Faith and Belief**: 45 mitzvot (7%)

## Smallest Categories

1. **Life and Death**: 5 mitzvot (1%)
2. **Torah and Study**: 9 mitzvot (1.5%)
3. **Daily Life and Observance**: 15 mitzvot (2.4%)
4. **Ethics and Character**: 17 mitzvot (2.8%)
5. **National Life**: 23 mitzvot (3.8%)
