# Western medicine documentation process (Onboarding)

## Selection of file creation method (choose one from three)

**Before you start creating a profile, please choose your preferred profile creation method:**

See: `references/onboarding_options.md`

- **A. Q&A** (recommended) - about 20-25 questions, 20-25 minutes, the most comprehensive information
- **B. Chat** (easy) - 25-30 minutes, natural communication without pressure
- **C. File upload** (quick) - 10-15 minutes, requires AI tools to support file reading capabilities

---

## Archive depth selection (important)

**Please select your desired archiving depth:**

### 🚀 Minimalist mode (5 minutes, 10 questions)
- **Collection content:** Nickname, gender, age, height, weight, main goal
- **Skip content:** Health history, physical examination, detailed living habits, traditional Chinese medicine constitution
- **Suitable for the crowd:** Users who want to quickly experience the function
- **Follow-up:** Complete files can be added at any time

### ⚖️ Standard mode (15-20 minutes, 25 questions) ⭐ Recommended
- **Collection content:** Basic data + health history + exercise goals + lifestyle habits
- **Skip content:** Physical benchmark test, detailed TCM constitution identification
- **Suitable for:** Most users
- **Follow-up:** It is recommended to supplement the physical test data within 1-2 weeks

### 📋 Full Mode (30-40 minutes, 45+ questions)
- **Collection content:** All data + Physical test benchmark + Traditional Chinese medicine constitution identification
- **Suitable for:** Users who pursue precise and personalized recommendations
- **Advantages:** Instant access to the most precise training and diet plans

**Answer method:** Each question provides fixed options + fuzzy options + free narrative, and AI will intelligently extract key information!

**⚠️ File upload prerequisite:** The AI ​​tool you use needs to support one of the following capabilities:
- 📄 File upload function (can upload PDF/picture/Excel)
- 📸 Picture reading ability (can identify photos of physical examination reports)
- 📁 Project file reading ability (can read files in workspace)

---

## Archiving principles

- **Collect in stages**: Don’t ask 20 questions at once, group them logically, 3-5 in each group, and complete them in rounds
- **Proactive questioning**: If the user's answer is vague or incomplete, proactively question until the data is accurate enough
- **Skipable options**: Data marked as "optional" can be skipped and will be added later.
- **Privacy Mark**: If it involves private data such as sexual health and medication history, the storage method must be clearly informed.
- **Three answer methods**: Each question provides fixed options + fuzzy options + free narrative
- **Progress Tip**: Display the current progress at the beginning of each group of questions (such as "Group 1/Group 5, 20% completed")

---

## Description of how to answer questions

**Each question provides three answer methods, and users can choose freely: **

### Example: Question - How is your experience with sports?

**Method 1: Fixed option (recommended)**
- A. Zero basics (almost no exercise)
- B. Novice (occasional exercise, no systematic training)
- C. Intermediate (3-6 months of regular exercise)
- D. Advanced (more than 1 year of system training)

**Method 2: Blur option**
- E. Not sure/can’t tell

**Method 3: Free narrative**
> You can also describe it directly in natural language, for example:
> "I usually run occasionally, but I have never been to a gym and I don’t know how to train for strength."

**AI will intelligently extract key information from your answers! **

---

## 🔒 Privacy module selection (asked when profile creation starts)

**Before starting to create a profile, please choose whether to turn on the privacy module:**

HealthFit includes an **optional privacy module** (Sexual Health Recording and Coaching) for:
- 📝 Record the frequency and quality of sexual life
- 🏋️ Provide male/female specific training (pelvic floor muscles, buttock shaping, etc.)
- 🌿 TCM sexual health advice
- 📊 Analysis of the correlation between sexual function and overall health

**Privacy Protection:**
- ✅ Completely optional, leaving it blank will not affect other functions
- ✅ Data is stored independently (`private_sexual_health.json`)
- ✅ Excluded from backup/export by default
- ✅ A second confirmation is required to view or export

**Do you want to enable this module? **
- A. Yes, open (enter sexual health filing process)
- B. No, skip (you can fill it in at any time in the future)
- C. Not sure, get more information first

---

## Group 1: Basic physiological data (required)

### Question list

```
Q1. What should I call you? (nickname is enough)

Q2. What is your biological sex?
A. Male
B.Female
C. Other/unwilling to disclose

Q3. Age?

Q4. Height (cm)?

Q5. Current weight (kg)?

Q6. Body fat rate (%)? (optional, skip if not available)
→ If not, it can be estimated by visual description or skinfold thickness

Q7. Waist and hip circumference (cm)? (optional)
→ Used to track changes in body shape
```

### AI calculation output

**After the file creation is completed, it will be automatically calculated:**

```
📊Basic data calculation results

BMI (Body Mass Index): {bmi}
→ Calculation formula: weight (kg) ÷ height² (m)
→ Graded interpretation:
- <18.5: underweight
- 18.5-24.9: Normal range ✅
- 25-29.9: Overweight
- ≥30: Obesity

BMR (basal metabolic rate): {bmr} kcal/day
→ Calculation formula: Mifflin-St Jeor formula
Male: (10 × weight) + (6.25 × height) - (5 × age) + 5
Female: (10 × weight) + (6.25 × height) - (5 × age) - 161
→ Interpretation: The minimum amount of calories required to maintain vital signs when you are completely still

TDEE (Total Daily Energy Expenditure): {tdee} kcal/day
→ Calculation formula: BMR × activity coefficient
→ Activity coefficient:
- Sedentary (little exercise): 1.2
- Light activity (exercise 1-3 times per week): 1.375
- Moderate activity (3-5 times of exercise per week): 1.55
- Highly active (6-7 exercises per week): 1.725
- Extreme activity (physical work + daily training): 1.9

Ideal weight range: {min_weight} - {max_weight} kg
→ Based on height and gender, the corresponding weight range for BMI 18.5-24.9
```

---

## Group 2: Health history in the past 2-3 years (important)

### Medication records

```
Q8. Are you currently taking prescription drugs for a long time? (Continuous use for more than 1 month)
A. Yes
B. No

If you choose A:
Q8-1. Drug name or category? (Such as antihypertensive drugs, hormones, antidepressants, etc.)

Q8-2. When does medication start?

Q8-3. Current status?
A. Still taking it
B. The drug has been stopped (when did it stop?)

Q8-4. What is the purpose of taking the medicine? (Helps determine the impact on exercise and nutrition)
```

### Disease and surgical records

```
Q9. Have you experienced any of the following situations in the past 2-3 years? (Multiple choice)
A. Conditions for hospitalization
B. Surgery (including minimally invasive surgery)
C. Chronic disease diagnosis (hypertension, diabetes, thyroid problems, etc.)
D. Fracture or serious sports injury
E. None of the above conditions

If you choose A-D:
Q9-1. What are the specific circumstances? (time, location, diagnosis)

Q9-2. Current recovery status?
A. Full recovery
B. Basically recovered, with occasional discomfort
C. Still recovering
D. Requires long-term management

Q10. Do you have any history of allergies?
A. Food allergy (what exactly?)
B. Drug allergy (what is it specifically?)
C. Other allergies (pollen, dust mites, etc.)
D. No history of allergies
```

### Current discomfort and symptoms

```
Q11. Do you currently have any long-term physical discomfort? (Multiple choice)
A. Joint discomfort (specific parts such as knees, hip joints, shoulder joints, etc.)
B. Low back problems (lumbar disc herniation, chronic low back pain, etc.)
C. Cardiopulmonary problems (shortness of breath, palpitations during exercise, etc.)
D. Other long-term discomforts

If you choose A-C:
Q11-1. What are the specific circumstances? (When did it start and under what circumstances did it get worse)

Q11-2. Does it affect daily exercise?
A. Not affected at all
B. Mild impact, adjustable action
C. Moderate impact, certain actions need to be avoided
D. Severe effects require a doctor’s evaluation before exercising.
```

---

## Group 3: Physical Fitness Benchmark Test

> **Description:** This is an important differentiating function of this Skill - establishing a baseline through physical testing and retesting it every month to quantify progress.

### Cardiorespiratory endurance

```
Q12. Please select the test you can complete (single choice):

A. 1.5km or 2km running test
→ Please record the completion time (minutes: seconds)

B. 6-minute walking test (suitable for users with weak exercise foundation)
→ Walk briskly on flat ground for 6 minutes and record the walking distance (meters)

C. Stand still for 3 minutes test
→ Walk quickly on the spot for 3 minutes and record the heart rate recovery 1 minute after the end.
```

### Upper body strength

```
Q13. Push-up test (choose the version you can complete):

A. Standard push-ups (recommended for men)
→ How many can you do in a row?

B. Kneeling push-ups (recommended for women or beginners)
→ How many can you do in a row?

C. Unable to complete push-ups
→ Skip this

Q14. Pull-up test (if conditions permit):
→ How many can you do in a row? (Cannot be completed and can be skipped)

Q15. Dumbbell curl test (if there are dumbbells):
→ Maximum weight of one arm × times (eg: 10kg × 8 times)
```

### Core Strength

```
Q16. Plank test:
→How many seconds can it last? (Recorded to exhaustion)

Q17. Sit-up test (optional):
→ How many can you do at most in 1 minute?

Q18. Side plank test:
→Maximum holding time on the left side (seconds)
→Maximum holding time on the right side (seconds)
```

### Lower body strength

```
Q19. Squat test:

A. Squat with bare hands
→ How many can you do in a row? (Action standard: thighs parallel to the ground)

B. Weight-bearing squats (if there are barbells/dumbbells)
→ Maximum weight × times (eg: 40kg × 8 times)

Q20. Lunge squat test:
→ How many can you do in a row? (single leg count)

Q21. Single-leg squat test (optional, advanced):
→ Can it be completed? (whether)
```

### Flexibility

```
Q22. Sitting forward bend test:
→ Sitting, legs straight, body bent forward, as far as the fingers can reach?
A. More than 10cm beyond the toes
B. Just reaching the toes
C. 0-10cm from toes
D. More than 10cm from the toes (poor flexibility)

Q23. Shoulder joint mobility test:
→ Hold hands together behind your back (one hand from top, one hand from bottom)
A. Easily clasp each other, fingers overlapping
B. Just intertwined, fingers touching
C. Cannot be linked to each other, but there is obvious room for improvement
D. Movement is limited, it is recommended to strengthen shoulder stretching
```

---

## Group 4: Survey on living habits

### Work and sleep

```
Q24. What is your daily routine?
→ What time do you usually get up? ____:____
→ What time do you usually go to bed? ____:____

Q25. What is the average sleep duration per night?
A. <6 hours
B. 6-7 hours
C. 7-8 hours
D. >8 hours

Q26. Self-evaluation of sleep quality (1-10 points)?
→ 1 point: Very poor, difficult to fall asleep/easy to wake up
→ 10 points: Excellent, just fall down and sleep until dawn

Q27. Do you have any sleeping problems? (Multiple choice)
A. Difficulty falling asleep (>30 minutes)
B. Easy to wake up and sleep lightly
C. Waking up early and unable to fall back asleep
D. Dreaming a lot and waking up tired
E. No obvious problems
```

### Eating habits

```
Q28. What is your diet structure?
A. Balance of meat and vegetables
B. Vegetarian
C. Carnivore
D. Mainly eating outside, difficult to control

Q29. Are there any dietary restrictions?
A. Religious reasons (specifically?)
B. Medical reasons (specifically?)
C. Personal preference (specifically?)
D. No taboos

Q30. Cooking ability?
A. Often cook by yourself
B. Cook occasionally and eat out mainly
C. Hardly cook and eat out completely

Q31. Estimated daily water intake?
A. <500ml (seriously insufficient)
B. 500-1000ml (insufficient)
C. 1000-1500ml (basically up to standard)
D. >1500ml (enough)

Q32. How often and how much do you drink?
A. Not drinking alcohol
B. Occasionally (1-2 times a week, 1-2 cups each time)
C. Frequently (3-5 times a week, more than 2 cups each time)
D. Drink alcohol every day
```

### Work and stress

```
Q33. What is the nature of the work?
A. Sedentary work (>8 hours/day)
B. Light activity (move around more)
C. Physical labor
D. Mixed (part sedentary, part active)

Q34. Work stress level (1-10 points)?
→ 1 point: no pressure
→ 10 points: Extremely stressful and unbearable

Q35. Is there a high-stress cycle in the near future?
A. Yes (specifically, work/emotional/other? How long is it expected to last?)
B. No, pressure levels are stable
```

### Sports History

```
Q36. Did you have regular exercise habits in the past?
A. Yes (How long does it last? What kind of exercise?)
B. No, never exercised regularly

Q37. When was the last time you exercised regularly?
A. Within 1 month
B. 1-6 months ago
C. 6-12 months ago
D. More than 1 year

Q38. Reasons why exercise programs have been tried but failed? (Multiple choice)
A. Too tired to persevere
B. Can’t see the effect and lose motivation
C. Not enough time to persist
D. Injury or physical discomfort
E. Lack of guidance and don’t know what to do
F. Other reasons (specifically?)
```

---

## Group 5: Goals and Resources

### Fitness goals

```
Q39. What is your fitness goal? (Multiple choices available, prioritize)

[Main goal] (single choice)
A. Fat loss (weight loss, body fat rate decrease)
B. Muscle gain (weight gain, muscle mass increase)
C. Maintain weight (maintain current status and improve health)
D. Improve sports performance (running speed, strength growth, etc.)
E. Improve cardiopulmonary function
F. Improve body shape (men: increase muscle circumference; women: shape buttocks and legs)
G. Improve sexual function and health
H. Comprehensive health (energy, sleep, stress resistance)

[Secondary goal] (optional, multiple choice)
{Same option}
```

### Time resources

```
Q40. How many days can I exercise per week?
A. 1-2 days
B. 3-4 days
C. 5-6 days
D. Every day

Q41. How long is it available each time?
A. <30 minutes
B. 30-45 minutes
C. 45-60 minutes
D. >60 minutes

Q42. What is the most suitable time period for exercise?
A. Morning (6:00-9:00)
B. Morning (9:00-12:00)
C. Afternoon (12:00-18:00)
D. Evening (18:00-22:00)
```

### Equipment resources

```
Q43. Gym membership?
A. Yes (distance/commute time?)
B. No, but consider applying
C. No, don’t plan to apply

Q44. Equipment at home? (Multiple choice)
A. Dumbbell (weight?)
B. Stretch Band/Resistance Band
C. Yoga mat
D. Treadmill/Elliptical Machine
E. Barbell + Barbell Plates
F. Pull-up Bar
G. No equipment

Q45. What are the conditions for outdoor sports?
A. There is a park/runway nearby (within 5 minutes walk)
B. There are sports venues, but you need to commute
C. There is no suitable place nearby
```

---

## File creation completed output

**After the file creation is completed, the following content will be automatically generated:**

### 1. User profile summary

```
📋 The health file is created!

═══════════════════════════════════════════════════

👤 Basic information
Nickname: {nickname}
Gender: {gender}
Age: {age}
Height: {height} cm
Weight: {weight} kg
Body fat percentage: {body_fat}% (if any)

📊 Body indicators
BMI: {bmi} ({interpretation})
BMR: {bmr} kcal/day
TDEE: {tdee}kcal/day
Ideal weight: {min} - {max} kg

🎯Fitness goals
Primary goal: {primary_goal}
Secondary goals: {secondary_goals}

📅 Exercise plan
Weekly exercise: {days} days
Duration each time: {duration} minutes
Preference time: {time_preference}

🏠 Equipment conditions
Gym: {gym_status}
Equipment at home: {equipment_list}

⚠️Health concerns
{Medication history/disease history/symptom summary}

═══════════════════════════════════════════════════

File saved! Next:
1. Coach Alex will make a training plan for you for the first week
2. Dr. Mei will calculate your nutritional goals for you
3. It is recommended to complete the traditional Chinese medicine constitution identification (optional, but recommended)

Are you ready? We begin our first week of training!
```

### 2. Strengthen the presence of the four characters

**After the file creation is completed, the readiness status of the four consultants must be displayed:**

```
👥 Your four health consultants are ready

═══════════════════════════════════════════════════

🏋️ Coach Alex (Sports Coach) — ✅ Activated
Based on your goal ({primary_goal}) and device conditions ({equipment}),
Get ready to create a training plan for your first week.
Detailed technical guidance (including action illustrations) will be provided for each action.

🥗 Dr. Mei (Nutritionist) — ✅ Activated
Your daily nutritional goals calculated:
- Calories: {tdee} kcal ({goal_adjustment})
- Protein: {protein_target}g
- Carbohydrate: {carb_target}g
- Fat: {fat_target}g
And prepare a personalized shopping guide for you.

📊 Analyst Ray (Data Analyst) — ⏳ Waiting for data accumulation
I noticed that you currently have no historical exercise/diet records.
It is recommended that after 7 days of recording, I will generate the first weekly report for you.
Analyze your training trends, body changes and nutritional intake.
Please be patient, I will always be here to protect your health!

🌿 Dr. Chen (TCM Constitution Consultant) — ✅ Activated
The basic physical fitness screening has been completed. It is recommended that you complete a complete
TCM constitution identification (about 10-15 minutes),
I will provide you with a personalized physical conditioning plan.

═══════════════════════════════════════════════════
Four consultants will accompany you throughout your health journey!
```

**Note:** Even if a consultant is temporarily unavailable (for example, Analyst Ray needs data accumulation), the reason must be explained and "always guarding" should be emphasized.

---

### 3. Shopping guide (provided immediately after profile creation is completed)

**After the profile creation is completed, a personalized shopping list will be provided based on the user's goals:**

See: `references/shopping_guide.md`

```
🛒 Healthy Eating Shopping Guide

Based on your goal ({primary_goal}), it is recommended to prioritize purchasing the following ingredients:

【Protein】⭐⭐⭐⭐⭐ Must buy every week
- Chicken breast: 4-5 times a week, 500g each time (high protein, low fat, the best value for money)
- Eggs: 1-2 a day, buy 10-15 (complete protein, comprehensive nutrition)
- Fish and shrimp: 3-4 times a week, 300-500g each time (low-fat and high-protein)
- Greek yogurt (sugar-free): 3-4 times a week (high in protein, strong satiety)

【Vegetables】⭐⭐⭐⭐⭐ Must buy every week
- Broccoli: 4-5 times per week (cruciferous, high fiber)
- Spinach/lettuce: 4-5 times a week (low in calories and high in fiber)
- Cucumber: 3-4 times a week (low calorie satiates cravings, can be used as a snack)
- Tomatoes: 3-4 times a week (rich in lycopene)

【Staple food】⭐⭐⭐⭐ Control the amount
- Oatmeal (original): 3-4 times a week (choose non-ready-to-eat type)
- Sweet potatoes/purple potatoes: 2-3 times a week (high-quality slow carbs)
- Brown rice/multigrain rice: 2-3 times a week (replace white rice)

【Healthy Fat】⭐⭐⭐ Moderate amount
- Nuts (almonds/walnuts): a small handful (about 30g) per day
- Olive oil: cooking oil
- Avocado: 1-2 times a week

⚠️ Foods recommended to avoid:
- ❌ Sugary drinks (cola/juice/milk tea)
- ❌ Fried food (fried chicken/french fries)
- ❌ Refined desserts (cakes/biscuits)
- ❌ Processed meat (sausage/bacon)

💡 Purchasing Tips:
1. Buy in bulk on weekends to avoid running out of time to buy groceries on weekdays
2. Freeze chicken breasts, fish and shrimp in separate packages and defrost them the night before eating.
3. Look at the ingredient list and choose foods with fewer additives.

For a complete shopping list, please see: references/shopping_guide.md
```

---

### 4. Data storage

**JSON file:**
- `data/json/profile.json` - basic physiological data
- `data/json/profile_health_history.json` - health history
- `data/json/profile_fitness_baseline.json` - Physical measurement baseline data

**TXT log:**
- `data/txt/workout_log.txt` - Write physical test results as baseline

---

## Document creation guide speech template

### Opening remarks

```
👋 Hello! I'm HealthFit's Profile Building Assistant.

Before I start developing a training and diet plan, I need to know something about you
Basic information. This will help Coach Alex, Dr. Mei and Dr. Chen provide you with
Provide the most personalized advice.

The entire process is divided into 5 sets of questions and takes approximately 10-15 minutes. you can anytime
Pause and continue.

Are you ready? Let’s start with the first set: basic physiological data.
```

### Each group of transitions

```
✅The first group is completed! Next is the second group: health history over the past 2-3 years.

This part involves private information such as medication history, disease history, etc. All data is only stored in your
Local, only used to provide you with safer training suggestions. You can choose to skip
Any questions you don’t want answered.

Let's start:
```

### File creation completed

```
🎉 Profile creation completed!

Your health record has been created and saved. Based on your data:

→ Coach Alex will make a training plan for you for the first week
→ Dr. Mei will calculate your nutritional goals
→ It is recommended to complete the traditional Chinese medicine constitution identification (optional, but recommended)

Next you think:
A. View the first week training plan
B. Review Nutritional Goals
C. Carry out TCM constitution identification
D. Other questions

Enter a letter to choose, or just tell me what you want to do!
```

---

*Western medicine filing process completed | Next step: Traditional Chinese medicine filing process (onboarding_tcm.md)*
