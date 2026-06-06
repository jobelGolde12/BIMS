# Barangay Information and Management System (BIMS)

## Project Overview
BIMS is a comprehensive desktop application designed to streamline the management of resident information, household data, barangay officials, and the issuance of various certificates. Built with Python and Tkinter, it provides a reliable and portable solution for local government units.

---

## Features
- **User Authentication**: Role-based access (Administrator and Resident) with secure login.
- **Resident Management**: Full CRUD (Create, Read, Update, Delete) operations, search functionality, and photo upload support.
- **Household Management**: Track households, their members, and addresses.
- **Barangay Officials Tracking**: Manage records of officials, their positions, and terms of service.
- **Automated Certificate Generation**: Generate professional PDF certificates (Barangay Clearance, Residency, Indigency) using ReportLab.
- **System Reports**: Export data to CSV and PDF formats for Residents, Households, Officials, and Certificates.
- **Database Backup & Restore**: Built-in utility to backup the SQLite database to `exports/backups/`.
- **Activity Logging**: Automated logging of system activities in `logs/app.log`.

---

## Requirements
### System Requirements
- **Operating System**: Windows, Linux, or macOS.
- **Python**: version 3.12 or higher.

### Dependencies
The following libraries are required:
- `Pillow>=10.0.0`: For image processing and resident photos.
- `reportlab>=4.0.0`: For professional PDF certificate generation.
- `tkinter`: Standard GUI library (included with most Python installations).
- `sqlite3`: Standard database engine (included with Python).

---

## Architecture
BIMS follows a modular **N-Tier Architecture** to ensure maintainability and scalability:

1.  **UI Layer (Tkinter/ttk)**: Handles all user interactions and data presentation.
2.  **Service Layer**: Contains the core business logic, data validation, and orchestrates the flow between the UI and the database.
3.  **Database Layer (SQLite)**: Manages persistent data storage using a local file-based database for portability.
4.  **Utilities/Service Mixins**: Handles cross-cutting concerns like PDF generation, CSV exports, and logging.

---

## Installation Instructions

### Linux (Ubuntu/Debian)
1.  **Update System & Install Python**:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv python3-tk
    ```
2.  **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    ```
3.  **Activate Environment & Install Dependencies**:
    ```bash
    source venv/bin/activate
    pip install -r barangay_system/requirements.txt
    ```
4.  **Run the Application**:
    ```bash
    python3 -m barangay_system.main
    ```

### Windows
1.  **Install Python**: Download and install Python 3.12+ from [python.org](https://www.python.org/). Ensure **"Add Python to PATH"** is checked.
2.  **Create a Virtual Environment**:
    ```powershell
    python -m venv venv
    ```
3.  **Activate Environment & Install Dependencies**:
    ```powershell
    .\venv\Scripts\Activate.ps1
    pip install -r barangay_system/requirements.txt
    ```
4.  **Run the Application**:
    ```powershell
    python -m barangay_system.main
    ```

---

## User Guide

### Initial Login
- **Administrator**:
    - **Username**: `admin`
    - **Password**: `admin123`
    - *Full access to all modules.*
- **Resident**:
    - **Username**: `resident`
    - **Password**: `res123`
    - *View-only access to resident lists.*

### Dashboard
The Dashboard provides a quick overview of system statistics:
- Total Residents, Households, Officials, and Certificates Issued.
- Current Date/Time and Recent Activity logs.

### Resident Management
- **Adding Residents**: Navigate to the Residents tab and click "Add New Resident". Fill in the details and optionally upload a photo.
- **Editing/Deleting**: Double-click any entry in the list to open the update/delete dialog.
- **Searching**: Use the real-time search bar to filter residents by name or ID.

### Certificate Issuance
1. Go to the **Certificates** module.
2. Select a resident from the list.
3. Select the certificate type (Clearance, Residency, or Indigency).
4. Enter a serial number and click **Generate**.
5. The PDF will be saved in `barangay_system/exports/pdf/`.

---

## Folder Structure
- `barangay_system/`: Core application package.
  - `database/`: SQLite database and schema definitions.
  - `ui/`: GUI modules and styling.
  - `services/`: Business logic and backend services.
  - `assets/`: Icons and static assets.
  - `exports/`: Destination for generated PDFs, CSVs, and Backups.
  - `docs/`: Technical documentation and user guides.
  - `charts/`: System architecture diagrams (ASCII).
  - `logs/`: Application execution logs.

PROJECT STRUCTURE

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