<div align="center">

# HealthFit.skill

> *"Your personal health advisor matrix — East meets West, anytime, anywhere"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-4.0.0-brightgreen)](SKILL.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)
[![TCM+Western](https://img.shields.io/badge/TCM%2BWestern-Integrated-red)](SKILL.md)

<br>

**HealthFit builds a matrix of 13 specialized advisors for your health journey —**
**sports coaches by discipline, nutrition experts bridging Western and Traditional Chinese Medicine, and focused TCM advisors by specialty.**

<br>

The sports coach matrix covers 100+ disciplines: running, swimming, strength training, ball sports, martial arts, yoga, cycling, and more.<br>
The TCM advisor matrix covers constitution assessment, health exercises such as Baduanjin/Wuqinxi/Liuzijue, gynecology, internal medicine, and more.<br>
One skill, your complete companion for long-term health management.

[Quick Start](#quick-start) · [Expert Matrix](#expert-matrix) · [Features](#features) · [Installation](#installation) · [Content Policy](#content-policy)

<br>

**Original project:**
[ChenChen913/healthfit](https://github.com/ChenChen913/healthfit)

</div>

---

## 📖 What Is HealthFit

HealthFit is a health management Skill designed for Claude and other AI tools. Through an **Expert Matrix** architecture, it upgrades personal health management from a single assistant into a **collaborative system of 13 specialized advisors**:

- 🏃 **Sports Coach Matrix** (7 coaches): a dedicated specialist for each type of sport
- 🥗 **Nutrition Advisor Matrix** (5 advisors): Western nutrition + TCM constitution assessment + health exercises + gynecology + internal medicine
- 📊 **Data Analyst** (1 analyst): weekly/monthly reports, trend tracking, and achievement milestones

---

## 🎯 Expert Matrix

### 🏃 Sports Coach Matrix (7 Coaches)

| Coach | Specialty | Disciplines Covered |
|-------|-----------|---------------------|
| Coach Lin | Athletics / Running | Marathon, 5K/10K, trail running, track sprints, middle-distance and long-distance running |
| Coach Shui | Swimming | All four strokes, fitness swimming, open-water swimming, triathlon swim segment |
| Coach Alex | Strength / General Fitness | Squat, deadlift, bench press, bodybuilding, CrossFit, general fitness |
| Coach Qiu | Ball Sports | Basketball, soccer, tennis, badminton, table tennis, and more |
| Coach Wu | Martial Arts / Combat | Boxing, Muay Thai, MMA, traditional martial arts for competition |
| Coach Rou | Flexibility / Mind-Body | Yoga, Pilates, stretching, recovery, myofascial release |
| Coach Che | Endurance Sports | Cycling, triathlon, kayaking, rowing |

> 📌 Full routing for 100+ sports is available in `references/sport_routing.md`.

### 🥗 Nutrition Advisor Matrix (5 Advisors)

| Advisor | Specialty | Core Functions |
|---------|-----------|----------------|
| Dr. Mei | Western Sports Nutrition | Calorie targets, macronutrients, sports supplements, weight management |
| Dr. Chen | TCM Constitution | Nine-constitution assessment, food therapy plans, tongue examination, seasonal wellness |
| Dr. Gong | Health Exercises | Baduanjin, Wuqinxi, Liuzijue, Yijinjing, Taiji wellness exercises |
| Dr. Fang | TCM Gynecology | Menstrual cycle support, postpartum recovery, dysmenorrhea, PCOS intervention |
| Dr. Nei | TCM Internal Medicine | Sleep support, digestion, chronic fatigue, sub-health concerns |

### 📊 Data Analysis (1 Analyst)

| Analyst | Core Functions |
|---------|----------------|
| Analyst Ray | Weekly/monthly reports, body-composition trends, personal records, achievement milestones |

---

## ✨ Features

### 🔑 Core Features

- **Smart routing**: assigns the right specialist based on the sport or health topic you describe
- **Dual-track profiling**: combines Western health metrics with TCM constitution assessment
- **Long-term tracking**: persists local data and supports weekly reports, monthly reports, and trend analysis
- **Quick commands**: `/run`, `/swim`, `/eat`, `/weight`, `/pr`, and other commands for fast logging

### 🌿 TCM-Specific Features

- **Nine-constitution assessment**: complete TCM body-type assessment with personalized care suggestions
- **Health exercise library**: complete guidance for Baduanjin, Wuqinxi, Liuzijue, and Yijinjing
- **24 solar terms**: seasonal wellness recommendations aligned with traditional Chinese seasonal theory
- **Exercise × constitution matrix**: recommends the most suitable health exercises for your constitution
- **Menstrual-cycle exercise plans**: differentiated training suggestions across four cycle phases

### 🔒 Privacy Protection

- All data is stored locally, with no cloud upload
- Sexual health data is isolated in a separate file and excluded from backups by default
- Users can export or fully delete their data at any time

---

## 🚀 Quick Start

### ⚡ Fastest: npx One-Line Install

```bash
npx skills add Fandi74/skill-healthfit-en
```

### After Manual Installation, Say:

```text
Help me create my health profile
```

### Option 2: Direct Conversation Triggers

Any of the following can activate HealthFit:

```text
I ran 5 km today. Please log it for me.
I want to create a swimming training plan.
What is my TCM body constitution?
Help me prepare for a marathon.
I want to practice Baduanjin today.
Give me this week's training summary.
```

### Option 3: Quick Commands

```text
/run 10K 52min          # Log a run
/swim freestyle 1000m   # Log a swim
/weight 68.5            # Log body weight
/pr squat 90kg          # Log a personal record
/week                   # Weekly summary
/tcm                    # View TCM constitution
/solar                  # Solar-term wellness
/menu                   # Full feature menu
```

---

## 📦 Installation

### ⚡ Option 1: npx One-Line Install (Recommended)

```bash
# Recommended
npx skills add Fandi74/skill-healthfit-en

# Install specifically for Claude Code
npx skills add Fandi74/skill-healthfit-en -a claude-code

# Global install
npx skills add Fandi74/skill-healthfit-en -g
```

After installation, the Skill is configured for your Claude Code environment and ready to use.

> Requires [Node.js](https://nodejs.org/) v18 or later. `npx` fetches the latest version automatically, so manual updates are not required.

### 🔧 Option 2: Manual Claude Code Install

```bash
git clone https://github.com/Fandi74/skill-healthfit-en ~/.claude/skills/healthfit
```

### 🛠 Option 3: Cursor / Windsurf / Trae

Place the `healthfit/` folder in your project root and refer to [AGENTS.md](AGENTS.md) for configuration.

### 📖 Other AI Tools

See [AGENTS.md](AGENTS.md), which covers Cursor, Gemini CLI, OpenHands, OpenAI Codex, and other tools.

---

## 🚨 Content Policy

HealthFit includes a built-in **Content Moderation Layer** that applies to all roles:

- **Sexual health topics**: limited to health management and training optimization; explicit content is not supported
- **Civil language**: mild inappropriate language receives one friendly reminder; serious violations end the conversation
- **Medical disclaimer**: all suggestions are not medical diagnoses; cardiovascular conditions, post-surgical recovery, and similar situations should be handled with professional medical care

---

## 📁 Project Structure

```text
healthfit/
├── SKILL.md                 # Core Skill configuration
├── README.md                # English documentation
├── README_EN.md             # English documentation mirror from upstream
├── AGENTS.md                # Multi-AI tool adaptation guide
├── agents/                  # 13 expert roles: 7 coaches + 5 nutrition/TCM advisors + 1 analyst
├── references/              # Core reference documents
│   ├── sport_routing.md     # Routing table for 100+ sports
│   ├── tcm_qigong_library.md# Complete health exercise library
│   └── ...
├── assets/                  # Fitness baseline test, tongue exam guide, achievement milestones
├── data/                    # Local data storage
└── scripts/                 # Utility scripts for backup, export, and database setup
```

---

## 🤝 Contributing and Feedback

Issues and pull requests are welcome:

- Add new sport routing entries
- Improve TCM health exercise guidance
- Add new nutrition advisor specialties, such as sports medicine or oncology nutrition
- Improve multilingual support

---

## 📄 License

[MIT License](LICENSE) — free to use and extend.

---

<div align="center">

*HealthFit v4.0 — Expert Matrix, East-West Integration*<br>
*Your dedicated companion for a healthier journey*

[⭐ Star this repo](https://github.com/Fandi74/skill-healthfit-en) · [Original Chinese project](https://github.com/ChenChen913/healthfit)

</div>
