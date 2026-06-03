import tkinter as tk
from tkinter import ttk, messagebox
from ..services.official_service import OfficialService

class OfficialsModule:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        ttk.Label(self.parent, text="Barangay Officials", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        action_bar = ttk.Frame(self.parent)
        action_bar.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(action_bar, text="Add Official", style="Accent.TButton", command=self.show_add_dialog).pack(side=tk.RIGHT)
        
        columns = ("ID", "Name", "Position", "Term Start", "Term End", "Contact")
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<Double-1>", lambda e: self.show_edit_dialog())

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for o in OfficialService.get_all_officials():
            self.tree.insert("", tk.END, values=(o['id'], o['name'], o['position'], o['term_start'], o['term_end'], o['contact_number']))

    def show_add_dialog(self, edit_data=None):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Official Details")
        dialog.geometry("400x500")
        
        container = ttk.Frame(dialog, padding=20)
        container.pack(fill=tk.BOTH, expand=True)
        
        fields = [("Name", "name"), ("Position", "position"), ("Term Start", "term_start"), ("Term End", "term_end"), ("Contact", "contact_number")]
        self.entries = {}
        for i, (label, key) in enumerate(fields):
            ttk.Label(container, text=label).pack(anchor=tk.W, pady=(5, 0))
            entry = ttk.Entry(container)
            entry.pack(fill=tk.X, pady=(0, 5))
            self.entries[key] = entry
            if edit_data:
                entry.insert(0, str(edit_data[key]))

        ttk.Button(container, text="Save", style="Accent.TButton", 
                   command=lambda: self.save_official(dialog, edit_data['id'] if edit_data else None)).pack(pady=20)

    def save_official(self, dialog, edit_id=None):
        data = {k: v.get() for k, v in self.entries.items()}
        if not data['name'] or not data['position']:
            messagebox.showerror("Error", "Name and Position required.")
            return
            
        if edit_id:
            success = OfficialService.update_official(edit_id, data)
        else:
            success = OfficialService.add_official(data)
            
        if success:
            dialog.destroy()
            self.load_data()
            messagebox.showinfo("Success", "Official saved.")

    def show_edit_dialog(self):
        selected = self.tree.selection()
        if not selected: return
        o_id = self.tree.item(selected[0])['values'][0]
        # In a real app we'd fetch by ID, for now we filter all
        officials = OfficialService.get_all_officials()
        for o in officials:
            if o['id'] == o_id:
                self.show_add_dialog(edit_data=o)
                break
