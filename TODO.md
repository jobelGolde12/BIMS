You are a Senior Python Software Engineer and System Architect.

Create a COMPLETE, FULLY FUNCTIONAL desktop application called:

Barangay Information and Management System (BIMS)

using ONLY Python.

The application must use:

Python 3.12+
Tkinter (GUI)
ttk widgets
SQLite3 database
pathlib
datetime
json
csv
logging
reportlab (PDF reports)
Pillow (Image handling)

Do NOT use:

Web technologies
Flask
Django
React
Vue
Electron

The system must run locally as a desktop application.

PROJECT STRUCTURE

Use the current project folder and create the following structure:

barangay_system/

│
├── main.py
│
├── database/
│   ├── database.py
│   ├── schema.py
│   └── barangay.db
│
├── ui/
│   ├── login_window.py
│   ├── dashboard.py
│   ├── residents.py
│   ├── households.py
│   ├── certificates.py
│   ├── officials.py
│   ├── reports.py
│   └── settings.py
│
├── services/
│   ├── resident_service.py
│   ├── household_service.py
│   ├── certificate_service.py
│   └── report_service.py
│
├── assets/
│   ├── logo.png
│   └── icons/
│
├── exports/
│   ├── pdf/
│   ├── csv/
│   └── backups/
│
├── docs/
│   ├── README.md
│   ├── USER_GUIDE.md
│   ├── INSTALLATION.md
│   ├── DATABASE_DOCUMENTATION.md
│   └── PROJECT_DOCUMENTATION.md
│
├── charts/
│   ├── SYSTEM_FLOWCHART.txt
│   ├── DATABASE_ERD.txt
│   ├── USE_CASE_DIAGRAM.txt
│   └── CLASS_DIAGRAM.txt
│
├── logs/
│   └── app.log
│
└── requirements.txt
DESIGN REQUIREMENTS

Create a simple professional design.

Theme:

White background
Light gray panels
Dark text
Blue accent color
Modern font
Clean layout
Easy navigation

Do NOT create flashy designs.

The application should look similar to:

Government systems
School management systems
Municipal office software

Use:

ttk.Style()

for styling.

LOGIN SYSTEM

Create login page.

Default account:

Username:

admin

Password:

admin123

Features:

Username field
Password field
Show password checkbox
Login button
Exit button
DASHBOARD

After login show dashboard.

Dashboard must display:

Total Residents
Total Households
Total Officials
Total Certificates Issued

Display statistics cards.

Display current date and time.

Display recent activities.

RESIDENT MANAGEMENT

Create complete resident module.

Fields:

Resident ID
First Name
Middle Name
Last Name
Gender
Birthdate
Age
Civil Status
Occupation
Address
Contact Number
Voter Status
Photo

Functions:

Add Resident
Update Resident
Delete Resident
Search Resident
View Resident
Upload Photo
Export Resident List

Use Treeview for data display.

HOUSEHOLD MANAGEMENT

Fields:

Household ID
Household Head
Address
Number of Members

Functions:

Add
Edit
Delete
Search
BARANGAY OFFICIALS

Fields:

Name
Position
Term Start
Term End
Contact Number

Functions:

Add
Edit
Delete
View
CERTIFICATE MANAGEMENT

Generate:

Barangay Clearance
Certificate of Residency
Certificate of Indigency

Functions:

Generate Certificate
Print Preview
Export PDF

PDF should automatically include:

Barangay Name
Certificate Number
Date
Resident Information
Signature Area

Use reportlab.

REPORTS MODULE

Create reports:

Resident Report
Household Report
Officials Report
Certificates Report

Export:

PDF
CSV
DATABASE

Use SQLite.

Create tables:

Residents

id
resident_id
first_name
middle_name
last_name
gender
birthdate
age
civil_status
occupation
address
contact_number
voter_status
photo
created_at

Households

id
household_id
head_name
address
members

Officials

id
name
position
term_start
term_end
contact_number

Certificates

id
certificate_number
resident_id
certificate_type
issued_date

Users

id
username
password
role

Automatically create tables during first run.

SEARCH FEATURES

Create global search functionality.

User should search by:

Resident Name
Resident ID
Household ID
Official Name

Results should update instantly.

BACKUP SYSTEM

Create database backup feature.

Save backups to:

exports/backups/

Include:

Backup Database
Restore Database
LOGGING

Create logging system.

Store logs inside:

logs/app.log

Log:

Login
Logout
Resident Added
Resident Updated
Resident Deleted
Certificate Generated
VALIDATION

Implement validations:

Required fields
Contact number format
Duplicate resident IDs
Empty forms
Invalid dates

Show proper error messages.

DOCUMENTATION FILES

Automatically generate:

docs/README.md

Contains:

Project Overview
Features
Folder Structure
Screenshots Section
Installation

docs/USER_GUIDE.md

Contains:

Login
Dashboard
Residents
Certificates
Reports

docs/INSTALLATION.md

Contains:

Python Installation
Dependencies
Running Application

docs/DATABASE_DOCUMENTATION.md

Contains:

Database Tables
Relationships
SQL Schema

docs/PROJECT_DOCUMENTATION.md

Contains:

Architecture
Design Decisions
Security Notes
CHARTS FOLDER

Generate text-only diagrams.

charts/SYSTEM_FLOWCHART.txt

Example:

START
 |
Login
 |
Dashboard
 |
+------------------+
| Residents Module |
+------------------+
 |
Reports
 |
END

charts/DATABASE_ERD.txt

Create ASCII ER Diagram.

charts/USE_CASE_DIAGRAM.txt

Create ASCII Use Case Diagram.

charts/CLASS_DIAGRAM.txt

Create ASCII Class Diagram.

REQUIREMENTS FILE

Generate requirements.txt

Include:

Pillow
reportlab
CODE QUALITY

Requirements:

OOP architecture
Modular design
Comments
Type hints
Error handling
PEP8 compliance
Maintainable code
FINAL OUTPUT

Generate ALL source code files.

Generate ALL documentation files.

Generate ALL chart files.

Generate ALL folders automatically.

The application must run successfully after:

pip install -r requirements.txt
python main.py

No placeholders.

No pseudo-code.

No incomplete functions.

Every feature must be fully implemented and working.

Required Libraries to Install
pip install pillow reportlab

Optional packaging for distribution:

pip install pyinstaller

Create executable:

pyinstaller --onefile --windowed main.py

This prompt is structured to maximize the chance that an AI coding assistant generates a complete, organized, and maintainable Tkinter-based Barangay Information and Management System.