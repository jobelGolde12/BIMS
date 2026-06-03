import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import shutil
import datetime
from pathlib import Path

class SettingsModule:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.parent, text="System Settings", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        container = ttk.Frame(self.parent, padding=20)
        container.pack(fill=tk.BOTH, expand=True)
        
        # Backup section
        backup_frame = ttk.LabelFrame(container, text="Database Backup & Restore", padding=20)
        backup_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(backup_frame, text="Create Database Backup", command=self.create_backup).pack(fill=tk.X, pady=5)
        ttk.Button(backup_frame, text="Restore from Backup", command=self.restore_backup).pack(fill=tk.X, pady=5)
        
        # Info section
        info_frame = ttk.LabelFrame(container, text="About BIMS", padding=20)
        info_frame.pack(fill=tk.X, pady=20)
        ttk.Label(info_frame, text="Barangay Information and Management System").pack()
        ttk.Label(info_frame, text="Version 1.0.0").pack()
        ttk.Label(info_frame, text="Developed with Python and Tkinter").pack()

    def create_backup(self):
        try:
            db_path = Path("barangay_system/database/barangay.db")
            if not db_path.exists():
                messagebox.showerror("Error", "Database file not found.")
                return
                
            backup_dir = Path("barangay_system/exports/backups")
            backup_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = backup_dir / f"barangay_backup_{timestamp}.db"
            
            shutil.copy2(db_path, backup_path)
            messagebox.showinfo("Success", f"Backup created successfully at:\n{backup_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Backup failed: {e}")

    def restore_backup(self):
        try:
            backup_file = filedialog.askopenfilename(
                title="Select Backup File",
                filetypes=[("Database files", "*.db")],
                initialdir="barangay_system/exports/backups"
            )
            
            if not backup_file:
                return
                
            if messagebox.askyesno("Confirm Restore", "Restoring will overwrite the current database. Continue?"):
                db_path = Path("barangay_system/database/barangay.db")
                shutil.copy2(backup_file, db_path)
                messagebox.showinfo("Success", "Database restored successfully. Please restart the application.")
        except Exception as e:
            messagebox.showerror("Error", f"Restore failed: {e}")
