from tkinter import ttk

def apply_styles():
    style = ttk.Style()
    style.theme_use('clam')
    
    # Colors
    bg_color = "#ffffff"
    panel_color = "#f5f5f5"
    accent_color = "#0056b3"
    text_color = "#333333"
    
    style.configure("TFrame", background=bg_color)
    style.configure("Panel.TFrame", background=panel_color)
    
    style.configure("TLabel", background=bg_color, foreground=text_color, font=("Helvetica", 10))
    style.configure("Header.TLabel", font=("Helvetica", 18, "bold"), foreground=accent_color)
    style.configure("Subheader.TLabel", font=("Helvetica", 14, "bold"))
    
    style.configure("TButton", font=("Helvetica", 10), padding=5)
    style.configure("Accent.TButton", font=("Helvetica", 10, "bold"), foreground="white", background=accent_color)
    style.map("Accent.TButton", background=[('active', '#004494')])
    
    style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
    
    style.configure("Card.TFrame", background="white", relief="raised", borderwidth=1)
    style.configure("Stat.TLabel", font=("Helvetica", 24, "bold"), foreground=accent_color)
