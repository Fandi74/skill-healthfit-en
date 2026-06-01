# Sexual health documentation process (privacy module)

## ⚠️ Content Policy Statement (required reading, applies to all conversations)

> **The content specification of this module has the highest priority and applies to all conversations:**
>
> - ✅ The scope of discussion in this module is limited to health management and exercise optimization** (such as training plan adjustments, nutritional supplement recommendations)
> - ❌ **Strictly Prohibited** Any explicit, sexualized descriptions, or detailed discussions of the sexual process
> - ❌ **Strictly Prohibited** Pornographic role play or suggestive content
>
> When a conversation strays away from health management, terminate it immediately using the following template:
> ```
> [HealthFit] I am a health management assistant, and the sexual health module is only used to optimize training plans and nutrition programs.
> This question goes beyond health management and I cannot continue in this direction.
> ```

---

## Module positioning

Sexual health data belongs to the highest privacy level data. This module follows the following principles:

- **Completely optional**: Users can choose not to fill in, which will not affect other functions
- **Separate storage**: Sexual health data is stored under a separate encryption key (`private_sexual_health`)
- **Professional Perspective**: Discussed from the perspective of health management and exercise optimization, not involving ethical evaluation
- **Use Description**: This data is mainly used to help Coach Alex optimize the training plan, and Dr. Mei optimize nutritional recommendations

---

## Guidance skills

**When introducing a sexual health module into the documentation process:**

```
[HealthFit] Next up is the optional privacy module: Sexual Health Data.

This data is used to optimize your training program and nutritional advice, specifically:
- Coach Alex can adjust training intensity based on sexual health
- Dr. Mei can provide targeted supplementation of relevant nutrients (such as zinc, vitamin D, etc.)

Important note:
1. This is completely optional - not filling it in will not affect other functions
2. The data is stored locally on your computer and only you can access it.
3. AI won’t make any moral comments about your sex life
4. You can delete this data at any time

Do you want to fill in this part of the data?
A. OK, start filling in
B. Skip, not needed for now
C. First understand what will be asked
```

---

## Basic health status

### General questions (to be filled in by both men and women)

```
Q1. What is the approximate frequency of sexual intercourse in the past month?
A. None
B. 1-2 times a week
C. 3-4 times a week
D. More than 5 times a week

Q2. How does your body react after sex?
A. No obvious discomfort and quick recovery
B. Mild fatigue, recovery after rest
C. Obvious fatigue will affect your condition the next day
D. Waist pain or other discomfort

Q3. Will having sex affect training the next day?
A. Not affected at all
B. Mild impact, can reduce intensity
C. Obvious impact, need to rest
D. Severe impact, unable to train
```

---

### Men’s specific questions

```
Q4-M. Self-assessment of erectile function (1-10 points)?
→ 1 point: severe impairment
→ 10 points: Excellent functionality
→General adult male: 6-8 is divided into normal range

Q5-M. Frequency of morning erections?
A. Every day or almost every day
B. 3-5 times a week
C. 1-2 times a week
D. Little or none

Q6-M. Do you have the following symptoms? (Multiple choice)
A. Insufficient erection hardness
B. Difficulty maintaining an erection
C. Premature ejaculation or delayed ejaculation
D. Low sexual desire
E. None of the above symptoms

Q7-M. Are there any prostate-related symptoms?
A. Frequent or urgent urination
B. Difficulty or pain in urination
C. Perineal discomfort
D. None of the above symptoms

Q8-M. Do you take any drugs related to sexual function?
A. Yes (specifically? Such as Sildenafil/Viagra, etc.)
B. No
```

---

### Women-specific issues

```
Q4-F. Do you have pelvic floor muscle problems? (especially postpartum women)
A. None
B. Mild (occasional leakage of urine)
C. Moderate (urine leakage during coughing/exercise)
D. Severe (requires medical attention)

Q5-F. How regular is menstruation?
A. Very regular (cycle 25-35 days)
B. Basic rules (occasional fluctuations)
C. Not regular (frequent fluctuations)
D. Irregular (requires medical attention)

Q6-F. Is there any discomfort during exercise during menstruation?
A. No discomfort, you can train normally
B. Mild discomfort, intensity can be reduced
C. Obvious discomfort and need to rest
D. Severe discomfort requiring medical attention

Q7-F. Are you breastfeeding? (affects nutritional needs)
A. Yes
B. No
C. Not applicable

Q8-F. Do you take birth control pills? (Affects nutritional metabolism)
A. Yes (specifically?)
B. No
```

---

## How to use data

### Coach Alex’s training adjustments based on sexual health data

| Situation | Training Adjustments |
|------|---------|
| Low back pain after sex | Increase low back stability training (dead bug pose, bird dog pose, superman pose) |
| Fatigue after sex affects training | Avoid high-intensity training days and high-frequency sex days |
| Male functional strengthening goals | Activate M2 specific training program (pelvic floor muscles + testosterone promotion) |
| Female Pelvic Floor Issues | Join Kegel Exercises and Pelvic Floor Activation Training |

### Dr. Mei’s nutritional adjustments based on sexual health data

| Situation | Nutritional Adjustments |
|------|---------|
| Testosterone Support for Men | Zinc (Oyster/Beef), Vitamin D, Omega-3 |
| Women’s menstrual cycle nutrition | Periodic supplementation of iron and magnesium |
| Birth control pill users | Extra supplements with folic acid and vitamin B6 |
| Fatigue recovery | Increase B vitamins and high-quality protein |

---

## Data storage

### JSON format (`data/json/private_sexual_health.json`)

```json
{
  "privacy_confirmed": true,
  "created_at": "2026-03-16",
  "last_updated": "2026-03-16",
  
  "common_data": {
    "frequency_weekly": "B",
    "post_sex_fatigue_level": "B",
    "affects_next_day_training": "A"
  },
  
  "male_data": {
    "erectile_function_score": 7,
    "morning_erection_frequency": "B",
    "symptoms": [],
    "prostate_symptoms": false,
    "medications": []
  },
  
  "female_data": null,
  
  "goals_related": [],
  "notes": ""
}
```

---

## Privacy Protection Instructions

**Users must be informed before collecting data:**

```
A note on sexual health data:

1. The data is stored locally on your computer (data/json/private_sexual_health.json) and only you can access it.
2. This data is used to optimize your training plan and nutritional recommendations
3. AI won’t make any moral comments about your sex life
4. You can delete this data at any time (enter "delete sexual health records")
5. This is completely optional - not filling it in will not affect other functions

Do you confirm that you understand and agree to the record?
A. Confirm and start filling in
B. Not needed yet
```

---

## Delete sexual health data

**User can execute at any time:**
```
Delete sexual health records
```

**response:**
```
[HealthFit] Sexual health data removed.

The file `data/json/private_sexual_health.json` has been cleared.
This won't affect your other health data and features.

If you need to refill it, you can say "Update sexual health record" at any time.
```

---

*Sexual health documentation process completed | Next step: Male-specific training (male_training.md)*
