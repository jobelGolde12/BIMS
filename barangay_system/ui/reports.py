import tkinter as tk
from tkinter import ttk, messagebox
from ..services.report_service import ReportService
import os

class ReportsModule:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.parent, text="System Reports", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        container = ttk.Frame(self.parent, padding=20)
        container.pack(fill=tk.BOTH, expand=True)
        
        report_types = [
            ("Resident List (CSV)", ReportService.export_residents_csv),
            ("Household List (CSV)", ReportService.export_households_csv),
            ("Official List (CSV)", ReportService.export_officials_csv),
            ("Certificate Logs (CSV)", ReportService.export_certificates_csv)
        ]
        
        for title, command in report_types:
            frame = ttk.Frame(container, style="Panel.TFrame", padding=10)
            frame.pack(fill=tk.X, pady=5)
            ttk.Label(frame, text=title, background="#f5f5f5").pack(side=tk.LEFT)
            ttk.Button(frame, text="Generate", command=lambda cmd=command: self.run_report(cmd)).pack(side=tk.RIGHT)

    def run_report(self, command):
        path = command()
        if path:
            messagebox.showinfo("Success", f"Report generated at:\n{path}")
        else:
            messagebox.showerror("Error", "Failed to generate report.")
