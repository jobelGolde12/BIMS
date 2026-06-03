import tkinter as tk
from tkinter import ttk, messagebox
from ..services.resident_service import ResidentService
from ..services.certificate_service import CertificateService
import os

class CertificateModule:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.parent, text="Certificate Issuance", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        container = ttk.Frame(self.parent, padding=20, style="Panel.TFrame")
        container.pack(fill=tk.BOTH, expand=True)
        
        # Resident Selection
        ttk.Label(container, text="Select Resident", background="#f5f5f5").pack(anchor=tk.W)
        self.resident_var = tk.StringVar()
        self.resident_combo = ttk.Combobox(container, textvariable=self.resident_var, width=50)
        self.resident_combo.pack(fill=tk.X, pady=(0, 20))
        self.load_residents()
        
        # Certificate Type
        ttk.Label(container, text="Certificate Type", background="#f5f5f5").pack(anchor=tk.W)
        self.cert_type_var = tk.StringVar()
        cert_types = ["Barangay Clearance", "Certificate of Residency", "Certificate of Indigency"]
        self.cert_combo = ttk.Combobox(container, textvariable=self.cert_type_var, values=cert_types, width=50)
        self.cert_combo.pack(fill=tk.X, pady=(0, 20))
        
        # Certificate Number
        ttk.Label(container, text="Certificate Number", background="#f5f5f5").pack(anchor=tk.W)
        self.cert_num_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.cert_num_var, width=50).pack(fill=tk.X, pady=(0, 30))
        
        ttk.Button(container, text="Generate Certificate", style="Accent.TButton", command=self.handle_generate).pack(pady=10)
        
        # List of issued certificates
        ttk.Label(self.parent, text="Recent Issuances", style="Subheader.TLabel").pack(anchor=tk.W, pady=(20, 10))
        columns = ("Number", "Resident ID", "Type", "Date")
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.load_issuances()

    def load_residents(self):
        residents = ResidentService.get_all_residents()
        values = [f"{r['resident_id']} - {r['last_name']}, {r['first_name']}" for r in residents]
        self.resident_combo['values'] = values

    def load_issuances(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for c in CertificateService.get_all_certificates():
            self.tree.insert("", tk.END, values=(c['certificate_number'], c['resident_id'], c['certificate_type'], c['issued_date']))

    def handle_generate(self):
        res_val = self.resident_var.get()
        cert_type = self.cert_type_var.get()
        cert_num = self.cert_num_var.get()
        
        if not res_val or not cert_type or not cert_num:
            messagebox.showerror("Error", "All fields are required.")
            return
            
        resident_id = res_val.split(" - ")[0]
        path = CertificateService.generate_certificate(resident_id, cert_type, cert_num)
        
        if path:
            messagebox.showinfo("Success", f"Certificate generated at:\n{path}")
            self.load_issuances()
        else:
            messagebox.showerror("Error", "Generation failed.")
            
