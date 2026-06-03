import tkinter as tk
from tkinter import ttk, messagebox
from ..services.household_service import HouseholdService

class HouseholdModule:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        ttk.Label(self.parent, text="Household Management", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        action_bar = ttk.Frame(self.parent)
        action_bar.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(action_bar, text="Search: ").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.handle_search())
        ttk.Entry(action_bar, textvariable=self.search_var, width=30).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(action_bar, text="Add New Household", style="Accent.TButton", command=self.show_add_dialog).pack(side=tk.RIGHT)
        
        columns = ("ID", "Household Head", "Address", "Members")
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<Double-1>", lambda e: self.show_edit_dialog())

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for h in HouseholdService.get_all_households():
            self.tree.insert("", tk.END, values=(h['household_id'], h['head_name'], h['address'], h['members']))

    def handle_search(self):
        query = self.search_var.get()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for h in HouseholdService.search_households(query):
            self.tree.insert("", tk.END, values=(h['household_id'], h['head_name'], h['address'], h['members']))

    def show_add_dialog(self, edit_data=None):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Household Details")
        dialog.geometry("400x400")
        
        container = ttk.Frame(dialog, padding=20)
        container.pack(fill=tk.BOTH, expand=True)
        
        fields = [("Household ID", "household_id"), ("Head Name", "head_name"), ("Address", "address"), ("Members Count", "members")]
        self.entries = {}
        for i, (label, key) in enumerate(fields):
            ttk.Label(container, text=label).pack(anchor=tk.W, pady=(5, 0))
            entry = ttk.Entry(container)
            entry.pack(fill=tk.X, pady=(0, 5))
            self.entries[key] = entry
            if edit_data:
                entry.insert(0, str(edit_data[key]))

        ttk.Button(container, text="Save", style="Accent.TButton", 
                   command=lambda: self.save_household(dialog, edit_data['household_id'] if edit_data else None)).pack(pady=20)

    def save_household(self, dialog, edit_id=None):
        data = {k: v.get() for k, v in self.entries.items()}
        if not data['household_id'] or not data['head_name']:
            messagebox.showerror("Error", "Required fields missing.")
            return
            
        if edit_id:
            success = HouseholdService.update_household(edit_id, data)
        else:
            success = HouseholdService.add_household(data)
            
        if success:
            dialog.destroy()
            self.load_data()
            messagebox.showinfo("Success", "Household saved.")

    def show_edit_dialog(self):
        selected = self.tree.selection()
        if not selected: return
        h_id = self.tree.item(selected[0])['values'][0]
        households = HouseholdService.search_households(h_id)
        if households:
            self.show_add_dialog(edit_data=households[0])
