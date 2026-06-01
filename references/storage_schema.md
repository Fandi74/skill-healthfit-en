# HealthFit Data Storage Schema

## Storage architecture overview

```
HealthFit data storage
│
├── JSON file (structured data)
│ ├── profile.json — basic physiological data file
│ ├── profile_health_history.json — Health History
│ ├── profile_fitness_baseline.json — Physical Measurement Baseline
│ ├── private_sexual_health.json — Sexual health privacy data (independent storage, secondary confirmation gate control)
│ ├── tcm_profile.json — TCM constitution file
│ └── daily/YYYY-MM-DD.json — Daily comprehensive log
│
├── TXT file (text record)
│ ├── workout_log.txt — Exercise training log
│ ├── nutrition_log.txt — Diet record log
│ ├── glossary_western.txt — Western Medicine Glossary
│ ├── glossary_tcm.txt — Traditional Chinese Medicine Glossary
│ └── achievements.txt — achievement milestone record
│
├── SQLite database (query optimization)
│   └── healthfit.db
│ ├── workouts — exercise record sheet
│ ├── nutrition_entries — Diet record form
│ ├── metrics_daily — Daily body indicator table
│ ├── pr_records — personal best results table
│ ├── weekly_summaries — weekly statistics cache
│ └── monthly_summaries — monthly statistics cache
│
└── assets/ resource files (non-user data)
└── exercise_images/ — action illustration resources (public resources/user selfies)
└── [User selfie photos are recommended to be encrypted or stored in a private directory]
```

---

## Privacy data protection instructions

### Sensitive data classification

| Data Category | File | Protection Level | Description |
|---------|------|---------|------|
| **Highly Sensitive** | `private_sexual_health.json` | 🔴 Highest level | Independent storage, backup/export excluded by default, double confirmation required |
| **Moderately sensitive** | `profile_health_history.json` | 🟡 Advanced | Contains medication history, disease history, encryption is recommended |
| **Low sensitivity** | `profile.json`, `workout_log.txt` | 🟢 Normal level | Can be backed up/exported normally |
| **User selfies** | `assets/exercise_images/` | 🟡 Advanced | It is recommended to encrypt the storage or store it in a private directory and not distribute it with the skills |

### User selfie photo storage solution

**If the user chooses to take action photos for AI correction:**

1. **Storage location:** It is recommended to store it in the user's private directory (such as `data/private_photos/`) rather than the skills directory
2. **Encryption scheme:** You can use base64 encoding + password protection, or call the system encryption API
3. **Access Control:** Only read when explicitly authorized by the user, and clean up promptly after use
4. **Backup policy:** Excluded from backup by default, users can manually choose whether to include
5. **Current status:** ⚠️ v3.1 planned function, the current version requires manual uploading of images to the `exercise_images` directory

**Implementation example (pseudocode):**
```python
# User selfie photo storage suggestions
photo_path = Path(__file__).parent.parent / "data" / "private_photos" / f"{date}_{exercise}.jpg"
# Recommendation: Use an encryption library (such as cryptography) to encrypt and store photos.
# Or: Only save the base64 encoding of the photo to JSON, and the original photo will not be saved.
```

---

### Sexual health data encryption scheme (optional)

**Current status:** ⚠️ Plain text storage (relies on file isolation + backup exclusion)

**Encryption upgrade plan (future iteration):**

#### Solution A: Simple encryption (Base64 + XOR)
```python
# scripts/crypto_utils.py
import base64
import hashlib
import json

def encrypt_data(data: dict, password: str) -> str:
"""Simple encryption (not military grade, but enough to prevent casual viewing)"""
    json_str = json.dumps(data, ensure_ascii=False)
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = bytes([b ^ key[i % len(key)] for i, b in enumerate(json_str.encode('utf-8'))])
    return base64.b64encode(encrypted_bytes).decode('ascii')

def decrypt_data(encrypted_str: str, password: str) -> dict:
"""Decrypt data"""
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = base64.b64decode(encrypted_str.encode('ascii'))
    decrypted_bytes = bytes([b ^ key[i % len(key)] for i, b in enumerate(encrypted_bytes)])
    return json.loads(decrypted_bytes.decode('utf-8'))
```

#### Option B: AES-256 encryption (recommended)
```python
# scripts/secure_storage.py
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def generate_key(password: str, salt: bytes = None) -> tuple:
"""Generate encryption key from password"""
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt_file(data: dict, password: str, filepath: Path):
"""Encrypt and save the file"""
    key, salt = generate_key(password)
    fernet = Fernet(key)
    
    json_bytes = json.dumps(data, ensure_ascii=False).encode('utf-8')
    encrypted = fernet.encrypt(json_bytes)
    
# Save salt + encrypted data
    filepath.write_bytes(salt + encrypted)
```

**Implementation suggestions:**
- Current version: plain text storage + file isolation + backup exclusion (safe enough)
- Future versions: Optional encryption upgrade (enabled after user sets password)
- Password management: Passwords only exist in the user's memory and are not saved by the system (cannot be recovered if lost)

---

## JSON Schema definition

### 1. profile.json (basic physiological data)

```json
{
  "created_at": "2026-03-16",
  "updated_at": "2026-03-16",
"nickname": "User Nickname",
  "gender": "male",
  "age": 28,
  "height_cm": 175,
  "weight_kg": 70.5,
  "body_fat_pct": 18.5,
  "waist_cm": 82,
  "hip_cm": 96,
  "bmi": 23.0,
  "bmr": 1780,
  "tdee": 2490,
  "activity_level": "moderate",
  "primary_goal": "fat_loss",
  "secondary_goals": ["glute_shape", "cardio"],
  "target_weight_kg": 65,
  "goal_deadline": "2026-09-16",
  "has_gym": true,
  "equipment": ["dumbbells", "resistance_bands"],
  "weekly_workout_days": 4,
  "session_duration_min": 60,
  "preferred_time": "evening",
  "diet_type": "omnivore",
  "food_allergies": [],
  "alcohol_weekly": "occasional",
  "work_type": "sedentary",
  "stress_level": 6,
  "sleep_target_hours": 7.5
}
```

### 2. profile_health_history.json (health history)

```json
{
  "medications": [
    {
"name": "X medicine",
"category": "antihypertensive drugs",
      "start_date": "2024-06",
      "status": "ongoing",
"purpose": "hypertension",
"notes": "Affects the upper limit of exercise intensity"
    }
  ],
  "diseases": [
    {
"name": "Mild lumbar disc herniation",
      "diagnosed_date": "2024-03",
      "status": "managed",
"impact_on_training": "Avoid high-load spinal compression movements"
    }
  ],
  "surgeries": [],
  "chronic_conditions": ["hypertension"],
  "allergies": {
"food": ["nuts"],
    "medication": []
  }
}
```

### 3. profile_fitness_baseline.json (physical measurement baseline)

```json
{
  "test_date": "2026-03-16",
  "cardio": {
    "run_1500m_sec": null,
    "run_2km_sec": 720,
    "step_test_recovery_hr": 95
  },
  "upper_body": {
    "pushup_max": 22,
    "pushup_type": "standard",
    "pullup_max": 5,
    "dumbbell_curl_max_kg": 14
  },
  "core": {
    "plank_sec": 85,
    "situp_1min": 28,
    "side_plank_left_sec": 60,
    "side_plank_right_sec": 55
  },
  "lower_body": {
    "squat_bodyweight_max": 30,
    "lunge_max": 20,
    "single_leg_squat_can_do": false
  },
  "flexibility": {
    "seated_reach_cm": -3,
    "shoulder_clasp_can_do": false
  }
}
```

### 4. private_sexual_health.json (sexual health privacy data)

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

### 5. tcm_profile.json (TCM constitution file)

```json
{
  "created_at": "2026-03-16",
  "last_assessed": "2026-03-16",
  "primary_constitution": "yang_xu",
  "secondary_constitutions": ["qi_xu"],
  "constitution_scores": {
    "ping_he": 45,
    "qi_xu": 62,
    "yang_xu": 78,
    "yin_xu": 30,
    "tan_shi": 40,
    "shi_re": 25,
    "xue_yu": 35,
    "qi_yu": 50,
    "te_bing": 20
  },
  "questionnaire": {
    "q1": "A",
    "q2": "A",
    "q3": "A"
  },
  "tongue_records": [
    {
      "date": "2026-03-16",
"body_color": "Light white",
"body_shape": "Fat and tooth-marked",
"coating": "white greasy moss",
"moisture": "water slippery",
"notes": "There are slight tooth marks on the edges",
"dr_chen_assessment": "Typical Yang deficiency + Qi deficiency tongue symptoms"
    }
  ],
  "current_plan": {
"exercise_restrictions": ["Avoid sweating", "Reduce outdoor use in winter"],
"recommended_exercises": ["Ba Duan Jin", "Tai Chi"],
    "food_therapy": {
"beneficial": ["yam", "red dates", "mutton"],
"avoid": ["cold drink", "bitter melon"],
"daily_tea": "Astragalus, red dates and wolfberry tea"
    },
"acupoints": ["Guanyuan point", "Zusanli"],
"seasonal_notes": "Before and after the winter solstice is the golden period for recuperation"
  }
}
```

### 6. daily/YYYY-MM-DD.json (daily comprehensive log)

```json
{
  "date": "2026-03-16",
  "metrics": {
    "weight_kg": 70.2,
    "energy_level": 7,
    "sleep_hours": 7.0,
    "sleep_quality": 6,
    "stress_level": 5,
    "sore_muscles": ["quadriceps", "glutes"]
  },
  "workout_ids": ["workout:2026-03-16:1"],
  "nutrition_logged": true,
"daily_note": "I'm in good condition today, but I feel a little sleepy in the afternoon",
  "sexual_health_note": null
}
```

---

## TXT log format

### workout_log.txt

```
[2026-03-16 19:30] Upper body strength training | 55 minutes
- Dumbbell bench press: 4 sets (12/10/8/8) × 20-22kg
- Single-arm rowing: 3 sets × 12 times/side × 14kg
- Face pull: 3 sets × 15 times × tension rope
RPE: 7/10 | Completion: 100% | Notes: In good condition, bench press PR 22kg

[2026-03-15 07:00] Morning run | 32 minutes
- Distance: 5.0km
- Pace: 6'24''/km
- Average heart rate: 145bpm
RPE: 6/10 | Completion: 100% | Remarks: Morning run in good condition
```

### nutrition_log.txt

```
[2026-03-16] Training Day | Target: 2740 kcal
Breakfast: oats + milk + eggs + banana = 550 kcal (P30g/C65g/F12g)
Lunch: chicken breast + brown rice + broccoli = 750 kcal (P45g/C85g/F18g)
Dinner: salmon + sweet potato + asparagus = 700 kcal (P35g/C60g/F25g)
Snack: protein powder + apple + almond = 400 kcal (P28g/C25g/F15g)
  ────────────────────────────────────────────────────
Total: 2400 kcal (P138g/C235g/F70g)
Compliance rate: Calories 88% | Protein 99% | Carbohydrates 61% | Fat 100%
Note: Carbs are on the low side, please make sure to replenish them tomorrow
```

### achievements.txt

```
[2026-03-16 19:45] Achievement Unlocked: Iron Will
Description: Training for 30 consecutive days
Difficulty: 🔴 Hard
Statistics:
- Start date: 2026-02-15
- End date: 2026-03-16
- Total training times: 26 times
- Total training time: 1,480 minutes
- Total consumption: approx. 11,200 kcal
Progress during this period:
- Weight: -2.0kg
- Squat: +14%
- 5km pace: -25 seconds
```

---

## SQLite Database Schema

```sql
-- Exercise record sheet
CREATE TABLE workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    type TEXT NOT NULL,
    subtype TEXT,
    duration_min INTEGER,
    calories INTEGER,
    exercises TEXT,
    rpe INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Diet record sheet
CREATE TABLE nutrition_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    meal_type TEXT NOT NULL,
    items TEXT,
    total_calories INTEGER,
    protein_g REAL,
    carbs_g REAL,
    fat_g REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

--Daily indicator table
CREATE TABLE metrics_daily (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL UNIQUE,
    weight_kg REAL,
    sleep_hours REAL,
    sleep_quality INTEGER,
    energy_level INTEGER,
    stress_level INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

--PR record table
CREATE TABLE pr_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_name TEXT NOT NULL,
    best_value REAL NOT NULL,
    unit TEXT NOT NULL,
    achieved_date TEXT NOT NULL,
    history TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Weekly statistics cache table
CREATE TABLE weekly_summaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    week TEXT NOT NULL UNIQUE,
    period_start TEXT,
    period_end TEXT,
    training_days INTEGER,
    total_duration_min INTEGER,
    total_calories INTEGER,
    avg_weight_kg REAL,
    weight_change_kg REAL,
    achievements TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

--Monthly statistics cache table
CREATE TABLE monthly_summaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT NOT NULL UNIQUE,
    period_start TEXT,
    period_end TEXT,
    training_days INTEGER,
    total_workouts INTEGER,
    avg_weight_kg REAL,
    weight_change_kg REAL,
    pr_count INTEGER,
    achievements TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Index optimization
CREATE INDEX idx_workouts_date ON workouts(date);
CREATE INDEX idx_nutrition_date ON nutrition_entries(date);
CREATE INDEX idx_metrics_date ON metrics_daily(date);
CREATE INDEX idx_weekly_week ON weekly_summaries(week);
CREATE INDEX idx_monthly_month ON monthly_summaries(month);
```

---

## Data backup strategy

### Automatic backup
- **Frequency**: Every Sunday at 2:00 AM
- **Content**: All JSON files + SQLite database
- **Location**: `data/db/backup/`
- **KEEP**: Last 4 backups

### Manual export
**User Command**: `Export my data`

**Output**:
- All JSON files packaged
- SQLite database export to CSV
- Generate readable Markdown reports

### Data clearing
**User Command**: `Clear Health Data`

**operate**:
1. Clear all JSON file contents
2. Delete SQLite database
3. Keep TXT log (optional)
4. Reset all counters

---

*Storage Schema completed | Next step: reply templates (response_templates.md)*
