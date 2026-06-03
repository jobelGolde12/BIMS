# Detailed Installation Guide

This guide provides step-by-step instructions for setting up and running the Barangay Information and Management System (BIMS) on Linux and Windows.

---

## Prerequisites
- **Python 3.12 or higher**
- **Pip** (Python package manager)
- **Git** (optional, for cloning the repository)

---

## 🐧 Linux Installation

### 1. Update System & Install Python
Ensure Python and the venv module are installed. On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk
```

### 2. Create a Virtual Environment
Navigate to the project directory and create an isolated environment:
```bash
python3 -m venv venv
```

### 3. Activate Environment & Install Dependencies
```bash
source venv/bin/activate
pip install -r barangay_system/requirements.txt
```

### 4. Run the Application
```bash
python3 -m barangay_system.main
```
*(Alternatively, run directly without activation: `./venv/bin/python3 -m barangay_system.main`)*

pag run:
./venv/bin/python -m barangay_system.main
---

## 🪟 Windows Installation

### 1. Install Python
1. Download the latest Python installer from [python.org](https://www.python.org/downloads/windows/).
2. **IMPORTANT:** During installation, check the box that says **"Add Python to PATH"**.

### 2. Open Command Prompt or PowerShell
Navigate to the folder where you extracted BIMS:
```powershell
cd path\to\DesktopApp
```

### 3. Create a Virtual Environment
```powershell
python -m venv venv
```

### 4. Activate Environment & Install Dependencies
**In Command Prompt (cmd):**
```cmd
venv\Scripts\activate
pip install -r barangay_system/requirements.txt
```
**In PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r barangay_system/requirements.txt
```

### 5. Run the Application
```powershell
python -m barangay_system.main
```

---

## 🛠️ Troubleshooting

### "Externally Managed Environment" (Linux)
If you see this error, it means your OS prevents global pip installs. Always use the **Virtual Environment** steps above to avoid this.

### "Tkinter not found" (Linux)
Some Linux distributions don't include Tkinter by default. Install it using:
`sudo apt install python3-tk`

### "Python is not recognized" (Windows)
Ensure Python is added to your System PATH. You may need to reinstall Python and check the "Add to PATH" box.

---

## 🔑 Initial Login
- **Username:** `admin`
- **Password:** `admin123`
