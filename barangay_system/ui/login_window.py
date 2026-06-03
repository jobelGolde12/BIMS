import tkinter as tk
from tkinter import ttk, messagebox
from .styles import apply_styles
from ..database.database import get_connection

class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.root.title("BIMS - Login")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        apply_styles()
        self.setup_ui()

    def setup_ui(self):
        container = ttk.Frame(self.root, padding="30")
        container.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(container, text="BIMS", style="Header.TLabel").pack(pady=(20, 10))
        ttk.Label(container, text="Barangay Information and Management System").pack(pady=(0, 30))
        
        # Username
        ttk.Label(container, text="Username").pack(fill=tk.X, pady=(10, 5))
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(container, textvariable=self.username_var)
        self.username_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Password
        ttk.Label(container, text="Password").pack(fill=tk.X, pady=(10, 5))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(container, textvariable=self.password_var, show="*")
        self.password_entry.pack(fill=tk.X, pady=(0, 5))
        
        # Show Password
        self.show_pass_var = tk.BooleanVar()
        ttk.Checkbutton(container, text="Show Password", variable=self.show_pass_var, command=self.toggle_password).pack(anchor=tk.W, pady=(0, 20))
        
        # Buttons
        self.login_btn = ttk.Button(container, text="Login", style="Accent.TButton", command=self.handle_login)
        self.login_btn.pack(fill=tk.X, pady=(10, 5))
        
        ttk.Button(container, text="Exit", command=self.root.quit).pack(fill=tk.X, pady=5)

    def toggle_password(self):
        if self.show_pass_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def handle_login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return
            
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                self.on_login_success(user)
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")
