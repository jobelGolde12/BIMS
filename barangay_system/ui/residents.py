import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ..services.resident_service import ResidentService
from PIL import Image, ImageTk
import io

class ResidentsModule:
    def __init__(self, parent, user_role='Administrator'):
        self.parent = parent
        self.user_role = user_role
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        ttk.Label(self.parent, text="Resident List", style="Subheader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Search and Action Bar
        action_bar = ttk.Frame(self.parent)
        action_bar.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(action_bar, text="Search: ").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.handle_search())
        ttk.Entry(action_bar, textvariable=self.search_var, width=30).pack(side=tk.LEFT, padx=10)
        
        if self.user_role == 'Administrator':
            ttk.Button(action_bar, text="Add New Resident", style="Accent.TButton", command=self.show_add_dialog).pack(side=tk.RIGHT)
            ttk.Button(action_bar, text="Delete Resident", command=self.handle_delete).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(action_bar, text="Refresh", command=self.load_data).pack(side=tk.RIGHT, padx=5)
        
        # Treeview
        columns = ("ID", "Name", "Gender", "Birthdate", "Civil Status", "Voter Status")
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
            
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Context Menu - Only for Admin
        if self.user_role == 'Administrator':
            self.tree.bind("<Double-1>", lambda e: self.show_edit_dialog())
            self.menu = tk.Menu(self.parent, tearoff=0)
            self.menu.add_command(label="Edit", command=self.show_edit_dialog)
            self.menu.add_command(label="Delete", command=self.handle_delete)
            self.tree.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.menu.post(event.x_root, event.y_root)

    def handle_delete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a resident to delete.")
            return
            
        resident_id = self.tree.item(selected[0])['values'][0]
        name = self.tree.item(selected[0])['values'][1]
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete resident {name} ({resident_id})?"):
            if ResidentService.delete_resident(resident_id):
                messagebox.showinfo("Success", "Resident deleted successfully.")
                self.load_data()
            else:
                messagebox.showerror("Error", "Could not delete resident.")

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        residents = ResidentService.get_all_residents()
        for r in residents:
            name = f"{r['last_name']}, {r['first_name']}"
            self.tree.insert("", tk.END, values=(r['resident_id'], name, r['gender'], r['birthdate'], r['civil_status'], r['voter_status']))

    def handle_search(self):
        query = self.search_var.get()
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        residents = ResidentService.search_residents(query)
        for r in residents:
            name = f"{r['last_name']}, {r['first_name']}"
            self.tree.insert("", tk.END, values=(r['resident_id'], name, r['gender'], r['birthdate'], r['civil_status'], r['voter_status']))

    def show_add_dialog(self, edit_data=None):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Add/Edit Resident")
        dialog.geometry("600x700")
        
        container = ttk.Frame(dialog, padding=20)
        container.pack(fill=tk.BOTH, expand=True)
        
        fields = [
            ("Resident ID", "resident_id"),
            ("First Name", "first_name"),
            ("Middle Name", "middle_name"),
            ("Last Name", "last_name"),
            ("Gender", "gender"),
            ("Birthdate (YYYY-MM-DD)", "birthdate"),
            ("Age", "age"),
            ("Civil Status", "civil_status"),
            ("Occupation", "occupation"),
            ("Address", "address"),
            ("Contact Number", "contact_number"),
            ("Voter Status", "voter_status")
        ]
        
        self.entries = {}
        for i, (label, key) in enumerate(fields):
            ttk.Label(container, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(container, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[key] = entry
            
            if edit_data:
                entry.insert(0, str(edit_data[key] or ""))

        # Photo selection
        self.photo_data = edit_data['photo'] if edit_data else None
        ttk.Label(container, text="Photo").grid(row=len(fields), column=0, sticky=tk.W, pady=5)
        ttk.Button(container, text="Select Photo", command=self.select_photo).grid(row=len(fields), column=1, sticky=tk.W, padx=10, pady=5)

        # Buttons
        btn_frame = ttk.Frame(container)
        btn_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)
        
        action_text = "Update" if edit_data else "Save"
        ttk.Button(btn_frame, text=action_text, style="Accent.TButton", 
                   command=lambda: self.save_resident(dialog, edit_data['resident_id'] if edit_data else None)).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy).pack(side=tk.LEFT)

    def select_photo(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if path:
            with open(path, "rb") as f:
                self.photo_data = f.read()
            messagebox.showinfo("Success", "Photo selected.")

    def save_resident(self, dialog, edit_id=None):
        data = {key: entry.get() for key, entry in self.entries.items()}
        data['photo'] = self.photo_data
        
        if not data['resident_id'] or not data['first_name'] or not data['last_name']:
            messagebox.showerror("Error", "ID, First Name, and Last Name are required.")
            return
            
        success = False
        if edit_id:
            success = ResidentService.update_resident(edit_id, data)
        else:
            success = ResidentService.add_resident(data)
            
        if success:
            messagebox.showinfo("Success", "Resident saved successfully.")
            dialog.destroy()
            self.load_data()
        else:
            messagebox.showerror("Error", "Could not save resident. Check logs for details.")

    def show_edit_dialog(self):
        selected = self.tree.selection()
        if not selected:
            return
            
        resident_id = self.tree.item(selected[0])['values'][0]
        residents = ResidentService.search_residents(resident_id)
        if residents:
            self.show_add_dialog(edit_data=residents[0])
