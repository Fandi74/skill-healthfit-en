#!/usr/bin/env python3
"""
HealthFit data backup script
Function: back up the data/ directory to data/db/backup/

Privacy design:
  private_sexual_health.json is excluded from all backups by default.
  To include it, run with the --include-private parameter and confirm in the interactive prompt.
  This is the actual implementation of the "secondary confirmation" commitment in SKILL.md.
"""

import sys
import shutil
import json
import argparse
import logging
import time
import random
import string
from datetime import datetime
from pathlib import Path

# Configure logging
def setup_logging():
    """Set up logging"""
    log_path = Path(__file__).parent.parent / "data" / "backup.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# ─── Sensitive file list ───────────────────────────────────────────
# Files in this list are excluded from backups by default.
# The user must satisfy both of the following conditions to include them in a backup:
#   1. Add the --include-private parameter when running
#   2. Manually enter "yes" in the interactive prompt to confirm
PRIVATE_FILES = {
    "private_sexual_health.json",
}
# ───────────────────────────────────────────────────────────────────


def get_skill_dir() -> Path:
    """Get the HealthFit skill root directory (two levels above the script directory)"""
    return Path(__file__).parent.parent


def get_data_dir() -> Path:
    return get_skill_dir() / "data"


def get_backup_dir() -> Path:
    return get_skill_dir() / "data" / "db" / "backup"


def _confirm_private_inclusion() -> bool:
    """
    Perform interactive secondary confirmation before backing up sensitive files (enhanced version).
    Includes random verification-code confirmation and operation log recording.
    Returns True only when the user enters the correct verification code.
    """
    print()
    print("=" * 60)
    print("⚠️  Warning: Highly Sensitive Data Backup Confirmation  ⚠️")
    print("=" * 60)
    print("""
You requested that private sensitive files be included in this backup.

Files involved:
  - private_sexual_health.json (sexual health records)
  - Other personal health privacy information

Risks of this operation:
  ❌ Backup files may be accessed by others
  ❌ Cloud sync may upload them automatically
  ❌ Data leakage may cause privacy harm

Please confirm that you understand the above risks.
""")
    print("=" * 60)
    
    # Random verification-code confirmation
    verify_code = ''.join(random.choices(string.ascii_uppercase, k=6))
    print(f"\nPlease enter the following verification code to confirm: {verify_code}")
    
    user_input = input("Verification code: ").strip().upper()
    if user_input != verify_code:
        print("❌ Verification code incorrect, operation canceled")
        logger.warning("Private file backup verification failed")
        return False
    
    # Record operation log
    log_path = Path(__file__).parent.parent / "data" / "security_log.txt"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Private file backup operation confirmed\n")
    
    logger.info("Private file backup verification passed")
    print("✅ Verification passed, continuing backup...\n")
    return True


def check_disk_space(required_mb: int = 100) -> bool:
    """Check whether disk space is sufficient"""
    try:
        import shutil
        total, used, free = shutil.disk_usage(Path(__file__).parent)
        free_mb = free // (1024 * 1024)
        if free_mb < required_mb:
            logger.error(f"Insufficient disk space: requires {required_mb}MB, currently available {free_mb}MB")
            print(f"❌ Insufficient disk space: requires {required_mb}MB, currently available {free_mb}MB")
            return False
        return True
    except Exception as e:
        logger.error(f"Disk space check failed: {e}")
        return True  # Do not block backup if the check fails


def safe_copy(src: Path, dest: Path) -> bool:
    """Safely copy a file with error handling"""
    try:
        if not src.exists():
            logger.warning(f"Source file does not exist: {src}")
            return False
        
        if not dest.parent.exists():
            dest.parent.mkdir(parents=True)
        
        shutil.copy2(src, dest)
        logger.info(f"Successfully copied: {src} -> {dest}")
        return True
    
    except PermissionError:
        logger.error(f"Insufficient permissions, cannot copy: {src}")
        print(f"❌ Permission error: cannot access {src}")
        return False
    
    except OSError as e:
        logger.error(f"System error: {e}")
        print(f"❌ System error: {e}")
        return False


def backup_with_retry(src: Path, dest: Path, max_retries: int = 3) -> bool:
    """Backup with retry"""
    for attempt in range(max_retries):
        if safe_copy(src, dest):
            return True
        logger.warning(f"Attempt {attempt + 1} failed, retrying...")
        time.sleep(1)
    return False


def _copy_json_dir(json_dir: Path, dest: Path, include_private: bool) -> dict:
    """
    Copy the json/ directory to the target path and filter private files.

    Returns a summary dictionary: {copied: [...], skipped: [...]}
    """
    dest.mkdir(parents=True, exist_ok=True)
    summary = {"copied": [], "skipped": []}

    # Copy top-level JSON files (filter by list, use safe copy)
    for src_file in json_dir.glob("*.json"):
        if src_file.name in PRIVATE_FILES:
            if include_private:
                if backup_with_retry(src_file, dest / src_file.name):
                    summary["copied"].append(src_file.name)
                else:
                    summary["skipped"].append(src_file.name + " (copy failed)")
            else:
                summary["skipped"].append(src_file.name)
        else:
            if backup_with_retry(src_file, dest / src_file.name):
                summary["copied"].append(src_file.name)
            else:
                summary["skipped"].append(src_file.name + " (copy failed)")

    # Copy the complete daily/ subdirectory (there are no private files in this directory)
    daily_src = json_dir / "daily"
    if daily_src.exists():
        shutil.copytree(daily_src, dest / "daily")
        daily_count = len(list((dest / "daily").glob("*.json")))
        summary["copied"].append(f"daily/ ({daily_count} files)")

    return summary


def create_backup(include_private: bool = False) -> Path:
    """
    Create a timestamped backup under data/db/backup/.

    Args:
        include_private: If True (and the user has confirmed), also back up private files.
                         If False (default), private files are silently excluded.
    """
    data_dir = get_data_dir()
    backup_dir = get_backup_dir()
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"backup_{timestamp}"
    backup_path.mkdir(parents=True, exist_ok=True)

    print(f"Starting backup → {backup_path}")
    print(f"Private file handling: {'Include (user confirmed)' if include_private else 'Exclude (default safe value)'}")
    print()

    json_summary = {"copied": [], "skipped": []}
    txt_count = 0
    db_count = 0

    # ── JSON directory ─────────────────────────────────────────────
    json_dir = data_dir / "json"
    if json_dir.exists():
        json_summary = _copy_json_dir(json_dir, backup_path / "json", include_private)
        print(f"✓ Backed up JSON files: {len(json_summary['copied'])}")
        if json_summary["skipped"]:
            print(f"  ⚠ Excluded (private): {', '.join(json_summary['skipped'])}")

    # ── TXT directory ──────────────────────────────────────────────
    txt_dir = data_dir / "txt"
    if txt_dir.exists():
        dest_txt = backup_path / "txt"
        dest_txt.mkdir(exist_ok=True)
        for f in txt_dir.glob("*.txt"):
            shutil.copy2(f, dest_txt / f.name)
        txt_count = len(list(dest_txt.glob("*.txt")))
        print(f"✓ Backed up TXT logs: {txt_count}")

    # ── SQLite database ────────────────────────────────────────────
    db_dir = data_dir / "db"
    if db_dir.exists():
        dest_db = backup_path / "db"
        dest_db.mkdir(exist_ok=True)
        for db_file in db_dir.glob("*.db"):
            shutil.copy2(db_file, dest_db / db_file.name)
            db_count += 1
        print(f"✓ Backed up SQLite databases: {db_count}")

    # ── Backup manifest ────────────────────────────────────────────
    manifest = {
        "backup_time": timestamp,
        "backup_path": str(backup_path),
        "include_private": include_private,
        "private_files_excluded": json_summary["skipped"],
        "files": {
            "json_copied": len(json_summary["copied"]),
            "json_skipped": len(json_summary["skipped"]),
            "txt": txt_count,
            "db": db_count,
        },
    }
    with open(backup_path / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print()
    print(f"✓ Backup manifest written → {backup_path / 'manifest.json'}")
    return backup_path


def cleanup_old_backups(keep_count: int = 4) -> None:
    """Delete the oldest backup directories and keep only the most recent `keep_count`."""
    backup_dir = get_backup_dir()
    if not backup_dir.exists():
        return
    backups = sorted([d for d in backup_dir.iterdir() if d.is_dir()], reverse=True)
    for old_backup in backups[keep_count:]:
        print(f"  Deleting old backup: {old_backup.name}")
        shutil.rmtree(old_backup)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="HealthFit data backup tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Privacy note:\n"
            "  Sensitive files (such as private_sexual_health.json) are excluded from backups by default.\n"
            "  Use the --include-private parameter to include them in the backup, but interactive secondary confirmation is required."
        ),
    )
    parser.add_argument(
        "--include-private",
        action="store_true",
        default=False,
        help="Include private/sensitive files in the backup (requires interactive secondary confirmation).",
    )
    parser.add_argument(
        "--keep",
        type=int,
        default=4,
        metavar="N",
        help="Number of recent backups to keep (default: 4).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    print("🔵 HealthFit Data Backup Tool")
    print("=" * 50)

    args = parse_args()

    # Secondary-confirmation gate for private files
    include_private = False
    if args.include_private:
        include_private = _confirm_private_inclusion()

    try:
        backup_path = create_backup(include_private=include_private)
        cleanup_old_backups(keep_count=args.keep)
        print("=" * 50)
        print("✅ Backup complete!")
        if not include_private and PRIVATE_FILES:
            print()
            print("ℹ️  Private files were excluded from this backup (safe default value).")
            print("   To back up private files, rerun with the --include-private parameter.")
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        raise
