# HealthFit shortcut command description

> **Version:** v3.0.1
> **Last update:** 2026-03-17

---

## 📋 Command list

### Recording commands

| Commands | Aliases | Functions | Examples | Response Roles |
|------|------|------|------|---------|
| `/log` | `/log` | Quick log of exercise | `/log Run 5km 32 minutes` | Coach Alex |
| `/eat` | `/eat` | Quick food record | `/eat Lunch Chicken Breast Salad` | Dr. Mei |
| `/weight` | `/weight` | Record today’s weight | `/weight 70.2` | Analyst Ray |
| `/pr` | `/record PR` | record personal best | `/pr squat 80kg` | Coach Alex |

### Query commands

| Commands | Aliases | Functions | Examples | Response Roles |
|------|------|------|------|---------|
| `/plan` | `/plan` | View today’s training plan | `/plan` | Coach Alex |
| `/week` | `/weekly report` | View this week's summary | `/week` | Analyst Ray |
| `/month` | `/monthly report` | View this month's summary | `/month` | Analyst Ray |
| `/tcm` | `/ Constitution ` | View TCM constitution | `/tcm` | Dr. Chen |
| `/solar` | `/solar` | View solar term health care | `/solar` | Dr. Chen |

### Set class command

| Command | Alias ​​| Function | Example |
|------|------|------|------|
| `/goal` | `/goal` | Modify fitness goals | `/goal gain muscle` |
| `/menu` | `/menu` | Show full menu | `/menu` |
| `/healthfit-help` | `/hf-help` | Display help information | `/healthfit-help` |

---

## 🔧 Command implementation logic

### Command parsing process

```
1. Check whether the message starts with "/"
2. Extract the command name (the part before the space)
3. Extract command parameters (the part after the space)
4. Route to the corresponding role based on the command name
5. The role processes the command and returns the result
```

### Command routing rules

| Command prefix | Routing role | Processing logic |
|---------|---------|---------|
| `/log`, `/pr` | Coach Alex | Analyze exercise type, duration, intensity, and record to workout_log.txt |
| `/eat` | Dr. Mei | Parse food names, estimate calories, record to nutrition_log.txt |
| `/weight` | Analyst Ray | Record weight to metrics_daily, update trend chart |
| `/plan`, `/week`, `/month` | Analyst Ray | Query database/log files and generate reports |
| `/tcm`, `/solar` | Dr. Chen | Read physical fitness files/solar terms data and provide suggestions |
| `/goal` | Multiple roles | Update profile.json to notify related role adjustment plans |
| `/menu`, `/help` | System | Display static menu/help information |

---

## 📝 Command usage example

### 1. Record exercise

**enter:**
```
/log run 5km 32 minutes
```

**Analysis:**
- Command: `/log`
- Type of exercise: running
- Distance: 5 km
- Duration: 32 minutes

**Response (Coach Alex):**
```
[Coach Alex] ✅ Today’s exercise has been recorded!

🏃 5km run | 32 minutes
📊 Pace: 6'24"/km
🔥 Estimated consumption: about 320 kcal
💪 Strength: Moderate (RPE 6/10)

This is your 3rd cardio session of the week, keep it up!
```

### 2. Record your diet

**enter:**
```
/eat lunch chicken breast 200g broccoli 150g brown rice 1 bowl
```

**Analysis:**
- Command: `/eat`
- Meal: Lunch
- Food: 200g chicken breast, 150g broccoli, 1 bowl of brown rice

**Response (Dr. Mei):**
```
[Dr. Mei] ✅ Lunch has been recorded!

🍗 Chicken breast 200g → about 330 kcal, protein 62g
🥦 Broccoli 150g → about 50 kcal, fiber 5g
🍚 1 bowl of brown rice → about 215 kcal, carbohydrate 45g

Total: approx. 595 kcal
Protein: 62g ✅ | Carbohydrate: 45g | Fat: 5g

Nutritionally balanced, keep it up!
```

### 3. Record weight

**enter:**
```
/weight 70.2
```

**Analysis:**
- Command: `/weight`
- Weight: 70.2 kg

**Response (Analyst Ray):**
```
[Analyst Ray] ✅ Weight has been recorded!

⚖️ Today’s weight: 70.2 kg
📈 Compared with yesterday: -0.3 kg ⬇️
📊 Average this week: 70.5 kg
🎯 On target: -5.8 kg (12 weeks to go)

The trend is good, keep it up!
```

---

## ⚠️ Notes

1. **Command format:** Use spaces to separate commands and parameters.
2. **Optional parameters:** Some commands can have no parameters (such as `/plan`)
3. **Natural language compatibility:** Natural language will be recognized even if no command is used (such as "Record a 5km run today")
4. **Command conflict:** `/help` is changed to `/healthfit-help` to avoid conflicts with system commands

---

## 🔮 Future Plans (v3.1)

- [ ] `/photo` - Upload body comparison photos
- [ ] `/period` - record menstrual cycle (female users)
- [ ] `/share` - Share achievements to social media
- [ ] `/compare` - Compare body data changes

---

*HealthFit v3.0.1 | 2026-03-17*
