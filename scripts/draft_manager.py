#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HealthFit profile-creation draft management tool
Function: save, recover, and clear profile-creation progress
"""

import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent.parent / "data" / "draft_manager.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('draft_manager')


BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
JSON_DIR = DATA_DIR / "json"
DRAFT_FILE = JSON_DIR / "onboarding_draft.json"
PROFILE_FILE = JSON_DIR / "profile.json"


def save_draft(data: dict, section: int, question: str):
    """Save profile-creation progress to the draft file"""
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    
    draft = {
        "started_at": data.get("started_at", datetime.now().isoformat()),
        "last_updated": datetime.now().isoformat(),
        "current_section": section,
        "current_question": question,
        "completed_sections": data.get("completed_sections", []),
        "partial_data": data.get("partial_data", {})
    }
    
    with open(DRAFT_FILE, "w", encoding="utf-8") as f:
        json.dump(draft, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Draft saved: {DRAFT_FILE}")
    print(f"   Progress: question group {section} - {question}")
    return draft


def load_draft() -> dict | None:
    """Load the draft file"""
    if not DRAFT_FILE.exists():
        return None
    
    try:
        with open(DRAFT_FILE, "r", encoding="utf-8") as f:
            draft = json.load(f)
        return draft
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️ Failed to read draft: {e}")
        return None


def recover_draft() -> bool:
    """
    Recover the draft to the formal profile
    Copy draft data to profile.json
    """
    draft = load_draft()
    if not draft:
        print("❌ No draft available to recover")
        return False
    
    # Convert draft data to profile format
    partial = draft.get("partial_data", {})
    
    profile = {
        "created_at": draft.get("started_at", datetime.now().isoformat()),
        "updated_at": datetime.now().isoformat(),
        "nickname": partial.get("nickname", "User"),
        "gender": partial.get("gender", "unknown"),
        "age": partial.get("age", 0),
        "height_cm": partial.get("height_cm", 0),
        "weight_kg": partial.get("weight_kg", 0),
        # Other fields to be completed later
    }
    
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Draft recovered to formal profile: {PROFILE_FILE}")
    return True


def clear_draft():
    """Delete the draft file"""
    if DRAFT_FILE.exists():
        DRAFT_FILE.unlink()
        print("✅ Draft cleared")
    else:
        print("ℹ️ No draft file")


def get_draft_status() -> dict:
    """Get draft status information"""
    draft = load_draft()
    if not draft:
        return {"exists": False}
    
    # Calculate saved-file age
    last_updated = datetime.fromisoformat(draft["last_updated"])
    age_hours = (datetime.now() - last_updated).total_seconds() / 3600
    
    return {
        "exists": True,
        "started_at": draft["started_at"],
        "last_updated": draft["last_updated"],
        "age_hours": round(age_hours, 1),
        "current_section": draft["current_section"],
        "current_question": draft["current_question"],
        "completed_sections": draft["completed_sections"],
        "has_partial_data": bool(draft.get("partial_data"))
    }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="HealthFit profile-creation draft management")
    parser.add_argument("action", choices=["save", "load", "recover", "clear", "status"],
                       help="Operation type")
    parser.add_argument("--section", type=int, default=0, help="Current question group number")
    parser.add_argument("--question", type=str, default="", help="Current question identifier")
    parser.add_argument("--data", type=str, default="", help="partial_data in JSON format")
    
    args = parser.parse_args()
    
    if args.action == "save":
        data = {
            "started_at": datetime.now().isoformat(),
            "completed_sections": [],
            "partial_data": json.loads(args.data) if args.data else {}
        }
        save_draft(data, args.section, args.question)
    
    elif args.action == "load":
        draft = load_draft()
        if draft:
            print(json.dumps(draft, ensure_ascii=False, indent=2))
        else:
            print("No draft")
    
    elif args.action == "recover":
        recover_draft()
    
    elif args.action == "clear":
        clear_draft()
    
    elif args.action == "status":
        status = get_draft_status()
        print(json.dumps(status, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
