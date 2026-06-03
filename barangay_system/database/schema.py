CREATE_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS residents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resident_id TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    gender TEXT,
    birthdate TEXT,
    age INTEGER,
    civil_status TEXT,
    occupation TEXT,
    address TEXT,
    contact_number TEXT,
    voter_status TEXT,
    photo BLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS households (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    household_id TEXT UNIQUE NOT NULL,
    head_name TEXT NOT NULL,
    address TEXT,
    members TEXT
);

CREATE TABLE IF NOT EXISTS officials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    term_start TEXT,
    term_end TEXT,
    contact_number TEXT
);

CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    certificate_number TEXT UNIQUE NOT NULL,
    resident_id TEXT NOT NULL,
    certificate_type TEXT NOT NULL,
    issued_date TEXT NOT NULL,
    FOREIGN KEY (resident_id) REFERENCES residents(resident_id)
);
"""
