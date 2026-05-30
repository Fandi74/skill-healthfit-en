#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HealthFit database initialization script

Purpose: create SQLite database table structures
Run: python scripts/init_db.py
"""

import sqlite3
from pathlib import Path


def init_database(db_path: Path):
    """Initialize the HealthFit database and create all required tables"""
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Exercise record table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            exercise_name TEXT NOT NULL,
            sets INTEGER,
            reps INTEGER,
            weight_kg REAL,
            duration_min INTEGER,
            distance_km REAL,
            rpe INTEGER,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 2. Nutrition record table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nutrition_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            meal_type TEXT NOT NULL,
            food_name TEXT NOT NULL,
            calories INTEGER,
            protein_g REAL,
            carbs_g REAL,
            fat_g REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 3. Daily body metrics table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics_daily (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL UNIQUE,
            weight_kg REAL,
            body_fat_pct REAL,
            waist_cm REAL,
            hip_cm REAL,
            resting_hr INTEGER,
            sleep_hours REAL,
            stress_level INTEGER,
            energy_level INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 4. Personal record table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pr_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_name TEXT NOT NULL,
            pr_type TEXT NOT NULL,
            value REAL NOT NULL,
            date_achieved TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 5. Weekly statistics cache table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weekly_summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_start TEXT NOT NULL UNIQUE,
            week_end TEXT NOT NULL,
            total_workouts INTEGER,
            total_duration_min INTEGER,
            avg_calories INTEGER,
            avg_protein_g REAL,
            avg_sleep_hours REAL,
            weight_change_kg REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 6. Monthly statistics cache table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS monthly_summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month TEXT NOT NULL UNIQUE,
            total_workouts INTEGER,
            total_duration_min INTEGER,
            avg_weight_kg REAL,
            weight_change_kg REAL,
            pr_count INTEGER,
            workout_adherence_pct REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create indexes to optimize queries
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_workouts_date ON workouts(date)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_nutrition_date ON nutrition_entries(date)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_metrics_date ON metrics_daily(date)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_pr_exercise ON pr_records(exercise_name)')
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database initialization complete: {db_path}")
    print("📊 Created data tables:")
    print("   - workouts (exercise records)")
    print("   - nutrition_entries (nutrition records)")
    print("   - metrics_daily (daily body metrics)")
    print("   - pr_records (personal records)")
    print("   - weekly_summaries (weekly statistics cache)")
    print("   - monthly_summaries (monthly statistics cache)")


if __name__ == "__main__":
    # Database path: healthfit/data/db/healthfit.db
    db_path = Path(__file__).parent.parent / "data" / "db" / "healthfit.db"
    
    # Ensure the directory exists
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Check whether the database already exists
    if db_path.exists():
        response = input(f"⚠️  Database already exists: {db_path}\nReinitialize? (y/N): ")
        if response.lower() != 'y':
            print("❌ Initialization canceled")
            exit(0)
        # Back up the old database
        backup_path = db_path.with_suffix('.db.bak')
        import shutil
        shutil.copy2(db_path, backup_path)
        print(f"💾 Old database backed up: {backup_path}")
    
    init_database(db_path)
