import tkinter as tk
from barangay_system.database.database import init_db
from barangay_system.ui.login_window import LoginWindow
from barangay_system.ui.dashboard import Dashboard
from barangay_system.logger_config import logger

class BIMSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw() # Hide root during initialization
        
        # Initialize DB
        init_db()
        logger.info("Application started and database initialized.")
        
        self.show_login()

    def show_login(self):
        self.login_win = tk.Toplevel(self.root)
        self.login_app = LoginWindow(self.login_win, self.on_login_success)
        self.login_win.protocol("WM_DELETE_WINDOW", self.root.quit)

    def on_login_success(self, user):
        self.login_win.destroy()
        self.root.deiconify() # Show root
        self.dashboard = Dashboard(self.root, user)
        logger.info(f"User logged in: {user['username']}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BIMSApp()
    app.run()
