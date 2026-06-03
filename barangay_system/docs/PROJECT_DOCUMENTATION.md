# Project Documentation

## Architecture
BIMS follows a modular N-Tier architecture:
1. **UI Layer (Tkinter)**: Handles user interaction.
2. **Service Layer**: Contains business logic and orchestrates data flow.
3. **Database Layer (SQLite)**: Persistence layer.

## Design Decisions
- **Tkinter/ttk**: Chosen for native desktop look and feel without external heavy dependencies.
- **SQLite**: Local file-based database for easy portability.
- **ReportLab**: Professional PDF generation library.

## Security Notes
- Password storage is currently plaintext as per basic requirements. For production, hashing (e.g., bcrypt) is recommended.
- Database backups are stored locally in `exports/backups/`.
