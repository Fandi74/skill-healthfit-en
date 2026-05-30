#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HealthFit data export script
Supports exporting to JSON, CSV, and Markdown formats
"""

import json
import csv
import sqlite3
from pathlib import Path
from datetime import datetime
import argparse
import shutil


BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "db" / "healthfit.db"


def export_json_files(output_dir: Path, include_private: bool = False):
    """Export all JSON files"""
    json_dir = DATA_DIR / "json"
    
    if not json_dir.exists():
        print("⚠️ JSON directory does not exist, skipping")
        return
    
    exported_count = 0
    skipped_count = 0
    
    for json_file in json_dir.glob("*.json"):
        # Skip private files unless explicitly requested
        if json_file.name == "private_sexual_health.json" and not include_private:
            print(f"⏭️ Skipping private file: {json_file.name}")
            skipped_count += 1
            continue
        
        # Copy file
        dest = output_dir / json_file.name
        shutil.copy2(json_file, dest)
        print(f"✅ Exported: {json_file.name}")
        exported_count += 1
    
    print(f"\n📊 JSON file export complete: {exported_count} files, skipped {skipped_count} private files")


def export_database_to_csv(output_dir: Path):
    """Export database tables to CSV"""
    if not DB_PATH.exists():
        print("⚠️ Database does not exist, skipping")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    exported_count = 0
    
    for (table_name,) in tables:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        
        # Write CSV
        csv_path = output_dir / f"{table_name}.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)
        
        print(f"✅ Exported table: {table_name}.csv ({len(rows)} records)")
        exported_count += 1
    
    conn.close()
    print(f"\n📊 Database export complete: {exported_count} tables")


def generate_markdown_report(output_dir: Path):
    """Generate a readable Markdown report"""
    report_lines = [
        "# HealthFit Data Export Report",
        f"\nExport time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "---\n"
    ]
    
    # Read user profile
    profile_path = DATA_DIR / "json" / "profile.json"
    if profile_path.exists():
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
        report_lines.append("## User Profile\n")
        report_lines.append(f"- Nickname: {profile.get('nickname', 'Not set')}")
        report_lines.append(f"- Height: {profile.get('height_cm', 'Not set')} cm")
        report_lines.append(f"- Weight: {profile.get('weight_kg', 'Not set')} kg")
        report_lines.append(f"- Primary goal: {profile.get('primary_goal', 'Not set')}")
        report_lines.append(f"- Created at: {profile.get('created_at', 'Unknown')}")
        report_lines.append(f"- Last updated: {profile.get('updated_at', 'Unknown')}\n")
    
    # Count database records
    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        report_lines.append("## Data Statistics\n")
        
        cursor.execute("SELECT COUNT(*) FROM workouts")
        report_lines.append(f"- Exercise records: {cursor.fetchone()[0]} records")
        
        cursor.execute("SELECT COUNT(*) FROM nutrition_entries")
        report_lines.append(f"- Nutrition records: {cursor.fetchone()[0]} records")
        
        cursor.execute("SELECT COUNT(*) FROM metrics_daily")
        report_lines.append(f"- Daily metrics: {cursor.fetchone()[0]} records")
        
        cursor.execute("SELECT COUNT(*) FROM pr_records")
        report_lines.append(f"- PR records: {cursor.fetchone()[0]} records")
        
        cursor.execute("SELECT COUNT(*) FROM weekly_summaries")
        report_lines.append(f"- Weekly statistics: {cursor.fetchone()[0]} records")
        
        cursor.execute("SELECT COUNT(*) FROM monthly_summaries")
        report_lines.append(f"- Monthly statistics: {cursor.fetchone()[0]} records\n")
        
        conn.close()
    
    # Write TXT log statistics
    txt_dir = DATA_DIR / "txt"
    if txt_dir.exists():
        report_lines.append("## Text Logs\n")
        
        workout_log = txt_dir / "workout_log.txt"
        if workout_log.exists():
            lines = workout_log.read_text(encoding="utf-8").strip().split('\n')
            report_lines.append(f"- Exercise log: {len(lines)} records")
        
        nutrition_log = txt_dir / "nutrition_log.txt"
        if nutrition_log.exists():
            lines = nutrition_log.read_text(encoding="utf-8").strip().split('\n')
            report_lines.append(f"- Nutrition log: {len(lines)} records")
        
        achievements = txt_dir / "achievements.txt"
        if achievements.exists():
            lines = achievements.read_text(encoding="utf-8").strip().split('\n')
            report_lines.append(f"- Achievement records: {len(lines)} records")
        
        report_lines.append("")
    
    # Write report
    report_path = output_dir / "export_report.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"✅ Generated report: export_report.md")


def main():
    parser = argparse.ArgumentParser(description="HealthFit data export")
    parser.add_argument("--output", "-o", default="./healthfit_export", help="Export directory")
    parser.add_argument("--include-private", action="store_true", help="Include private data (requires secondary confirmation)")
    parser.add_argument("--format", choices=["all", "json", "csv", "markdown"], default="all",
                       help="Export format")
    
    args = parser.parse_args()
    
    # Secondary confirmation for private data
    if args.include_private:
        print("\n" + "="*60)
        print("⚠️  Warning: Highly Sensitive Data Export Confirmation  ⚠️")
        print("="*60)
        print("""
You chose to export private data, including:
  - Sexual health records (private_sexual_health.json)
  - All personal health privacy information

Risks of this operation:
  ❌ Export files may be accessed by others
  ❌ Cloud sync may upload them automatically
  ❌ Data leakage may cause privacy harm

Please confirm that you understand the above risks.
""")
        print("="*60)
        
        # Random verification-code confirmation
        import random
        import string
        verify_code = ''.join(random.choices(string.ascii_uppercase, k=6))
        print(f"\nPlease enter the following verification code to confirm: {verify_code}")
        
        user_input = input("Verification code: ").strip().upper()
        if user_input != verify_code:
            print("❌ Verification code incorrect, operation canceled")
            return
        
        # Record operation log
        log_path = DATA_DIR / "security_log.txt"
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] Private data export operation executed\n")
        
        print("✅ Verification passed, continuing export...\n")
    
    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_dir = output_dir / f"export_{timestamp}"
    export_dir.mkdir()
    
    print(f"📁 Export directory: {export_dir}\n")
    
    # Execute export
    if args.format in ["all", "json"]:
        print("📄 Exporting JSON files...")
        export_json_files(export_dir, args.include_private)
        print()
    
    if args.format in ["all", "csv"]:
        print("📊 Exporting database to CSV...")
        export_database_to_csv(export_dir)
        print()
    
    if args.format in ["all", "markdown"]:
        print("📝 Generating Markdown report...")
        generate_markdown_report(export_dir)
        print()
    
    print(f"\n✅ Export complete! Directory: {export_dir}")
    print(f"💡 Tip: you can manually compress the backup or upload it to cloud storage")


if __name__ == "__main__":
    main()
