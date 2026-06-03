import tkinter as tk
from tkinter import ttk
import datetime
from .residents import ResidentsModule
from .households import HouseholdModule
from .officials import OfficialsModule
from .certificates import CertificateModule
from .settings import SettingsModule
from ..services.report_service import ReportService

class Dashboard:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("BIMS - Dashboard")
        self.root.geometry("1200x800")
        
        self.setup_ui()
        self.show_home()

    def setup_ui(self):
        # Sidebar
        self.sidebar = ttk.Frame(self.root, style="Panel.TFrame", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        ttk.Label(self.sidebar, text="BIMS", style="Header.TLabel", background="#f5f5f5").pack(pady=20)
        ttk.Label(self.sidebar, text=f"Welcome, {self.user['username']}", background="#f5f5f5").pack(pady=(0, 5))
        ttk.Label(self.sidebar, text=f"Role: {self.user['role']}", background="#f5f5f5", font=("Helvetica", 8, "italic")).pack(pady=(0, 20))
        
        if self.user['role'] == 'Administrator':
            nav_items = [
                ("Home", self.show_home),
                ("Residents", self.show_residents),
                ("Households", self.show_households),
                ("Officials", self.show_officials),
                ("Certificates", self.show_certificates),
                ("Settings", self.show_settings),
                ("Logout", self.logout)
            ]
        else: # Resident Role
            nav_items = [
                ("View Residents", self.show_residents),
                ("Logout", self.logout)
            ]
        
        for text, command in nav_items:
            btn = ttk.Button(self.sidebar, text=text, command=command)
            btn.pack(fill=tk.X, padx=10, pady=5)
            
        # Main Content Area
        self.content_area = ttk.Frame(self.root, padding="20")
        self.content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    def show_home(self):
        if self.user['role'] != 'Administrator':
            self.show_residents()
            return
        
        self.clear_content()
        ttk.Label(self.content_area, text="Dashboard Overview", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Stats Cards
        stats_frame = ttk.Frame(self.content_area)
        stats_frame.pack(fill=tk.X, pady=10)
        
        stats = ReportService.get_system_stats()
        
        card_data = [
            ("Total Residents", stats["total_residents"]),
            ("Total Households", stats["total_households"]),
            ("Total Officials", stats["total_officials"]),
            ("Certificates Issued", stats["total_certificates"])
        ]
        
        for i, (title, value) in enumerate(card_data):
            card = ttk.Frame(stats_frame, style="Card.TFrame", padding=15)
            card.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
            ttk.Label(card, text=title, background="white").pack()
            ttk.Label(card, text=str(value), style="Stat.TLabel", background="white").pack()

        # Date and Time
        now = datetime.datetime.now().strftime("%A, %B %d, %Y - %I:%M %p")
        ttk.Label(self.content_area, text=f"Current Date & Time: {now}", font=("Helvetica", 10, "italic")).pack(anchor=tk.W, pady=20)

        # Recent Activity
        ttk.Label(self.content_area, text="Recent Activities", style="Subheader.TLabel").pack(anchor=tk.W, pady=(20, 10))
        activity_frame = ttk.Frame(self.content_area, style="Panel.TFrame", padding=10)
        activity_frame.pack(fill=tk.BOTH, expand=True)
        
        # Placeholder for recent logs
        try:
            with open("barangay_system/logs/app.log", "r") as f:
                logs = f.readlines()[-10:] # Get last 10 logs
                for log in reversed(logs):
                    ttk.Label(activity_frame, text=log.strip(), background="#f5f5f5").pack(anchor=tk.W)
        except:
            ttk.Label(activity_frame, text="No recent activities found.", background="#f5f5f5").pack(anchor=tk.W)

    def show_residents(self):
        self.clear_content()
        ResidentsModule(self.content_area, self.user['role'])

    def show_households(self):
        self.clear_content()
        HouseholdModule(self.content_area)

    def show_officials(self):
        self.clear_content()
        OfficialsModule(self.content_area)

    def show_certificates(self):
        self.clear_content()
        CertificateModule(self.content_area)

    def show_settings(self):
        self.clear_content()
        SettingsModule(self.content_area)

    def logout(self):
        self.root.quit()
