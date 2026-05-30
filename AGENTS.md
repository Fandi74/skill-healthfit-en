# AGENTS.md — HealthFit Skill Multi-AI Tool Adaptation Configuration

> This file defines how HealthFit Skill is configured in different AI tools, ensuring a consistent cross-tool experience.

---

## Overview

HealthFit Skill's core logic is defined in `SKILL.md`. Different AI tools load Skills differently; this file provides specific configuration guidance for each tool.

---

## Claude Code (Recommended, Full Functionality)

**Installation Method:**
```bash
# Method 1: Clone directly to the skills directory
git clone https://github.com/ChenChen913/healthfit ~/.claude/skills/healthfit

# Method 2: Use skills.sh (if already installed)
skills install healthfit
```

**Configuration File (`~/.claude/CLAUDE.md` or project `CLAUDE.md`):**
```markdown
## Active Skills
- healthfit: personal health management; activate when the user mentions exercise, diet, or TCM constitution topics
```

**Feature Support:**
- ✅ Complete file read/write (`profile.json`, `workout_log.txt`, etc.)
- ✅ Python script execution (`backup.py`, `export.py`, etc.)
- ✅ SQLite database read/write (weekly/monthly report features)
- ✅ Complete routing for all 13 expert roles

---

## Cursor (Use in Code Editor)

**Installation Method:**
Place the `healthfit/` folder in the project root directory or the `~/.cursor/skills/` directory.

**`.cursorrules` Configuration Snippet:**
```
You have access to the HealthFit skill located in ./healthfit/.
When the user mentions fitness, nutrition, TCM constitution, exercise logging,
or health management, load SKILL.md and follow its routing table.

Key behaviors:
- Route sports questions to the correct coach agent in ./healthfit/agents/
- Content moderation layer applies at all times (see SKILL.md)
- Data storage path: ./healthfit/data/
```

**Feature Support:**
- ✅ File read/write (requires in-project paths)
- ✅ Expert role routing
- ⚠️ Python scripts need manual execution
- ❌ SQLite query functionality is limited

---

## Windsurf / Trae

**Configuration Method:** Similar to Cursor, add the following content to global rules or project rules:

```
HealthFit Skill is available at ./healthfit/SKILL.md.
Load it when health, fitness, nutrition, or TCM topics arise.
Follow the expert matrix routing defined in SKILL.md.
Enforce content moderation layer at all times.
Data path: ./healthfit/data/
```

---

## OpenHands (OpenDevin)

**Configuration File (`.openhands/config.toml`):**
```toml
[agent]
system_prompt_suffix = """
You have access to HealthFit health management skill.
Skill location: ./healthfit/SKILL.md
Activate when: exercise, diet, nutrition, TCM, health tracking topics
Follow expert routing table in SKILL.md.
Content moderation applies to sexual health discussions.
"""
```

---

## Gemini CLI

**Configuration Method (`~/.gemini/config.yaml`):**
```yaml
system_instructions:
  - |
    HealthFit skill is available at ./healthfit/SKILL.md.
    Trigger on: fitness, nutrition, exercise, TCM, health management requests.
    Load the appropriate agent file from ./healthfit/agents/ based on the routing table.
    Enforce content moderation layer (no explicit sexual content, maintain civility).
```

---

## OpenAI Codex / ChatGPT (Custom GPT)

**System Prompt Snippet:**
```
You are HealthFit, a personal health management system with a matrix of expert advisors.
Core configuration is in [SKILL.md content pasted here].

Expert routing:
- Athletics/Running → Coach Lin
- Swimming → Coach Shui  
- Strength/General → Coach Alex
- Ball Sports → Coach Qiu
- Martial Arts → Coach Wu
- Flexibility → Coach Rou
- Endurance → Coach Che
- Western Nutrition → Dr. Mei
- TCM Constitution → Dr. Chen
- Qigong/Exercises → Dr. Gong
- TCM Gynecology → Dr. Fang
- TCM Internal → Dr. Nei
- Data Analysis → Analyst Ray

Content Moderation: Sexual health discussions are limited to health optimization only.
No explicit content. Maintain civility in all interactions.
```

---

## Claude.ai (Web / App)

**Skill Usage Method:**
At the start of the conversation, send:
```
Please load HealthFit Skill. Profile path: [your data path]
```

Or trigger directly:
```
Help me create a health profile
Today I ran 5 kilometers
What is my TCM constitution?
```

**Feature Support:**
- ✅ Conversation features for all expert roles
- ⚠️ File persistence depends on claude.ai's Storage API or Projects feature
- ❌ Python scripts require Claude Code to execute

---

## General Configuration Principles

No matter which tool is used, the following configurations always apply:

1. **Content rules have highest priority** — sexual health topics are limited to health optimization, with a civility warning mechanism
2. **Expert routing must be followed** — different sports route to corresponding coaches, with no boundary crossing
3. **Medical disclaimer** — all advice does not constitute medical diagnosis
4. **Privacy data isolation** — sexual health data is stored separately and excluded from backups by default

---

## Version Compatibility

| Tool | Minimum Version Requirement | Full Feature Support |
|------|------------|------------|
| Claude Code | Any version | ✅ Full support |
| Cursor | 0.40+ | ⚠️ Partial support (no script execution) |
| Windsurf / Trae | Latest version | ⚠️ Partial support |
| Gemini CLI | 1.0+ | ⚠️ Partial support |
| OpenHands | 0.9+ | ✅ Relatively complete support |

---

*AGENTS.md — HealthFit v4.0 | Cross-platform health management, available everywhere*
