import sqlite3
import os
from pathlib import Path
from .schema import CREATE_TABLES_SQL

DB_PATH = Path("barangay_system/database/barangay.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    # Ensure directory exists
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # Execute schema
    cursor.executescript(CREATE_TABLES_SQL)
    
    # Check if admin user exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ('admin', 'admin123', 'Administrator')
        )
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
