import sys
from PyQt5.QtWidgets import QApplication
from ui.login_window import LoginWindow
from core.db import init_db
from core.logic import login_user, register_user
import os

def create_default_admin():
    """Create default admin if not exists."""
    admin_email = "admin@netamy.com"
    admin_password = "admin123"

    # Try to login as admin
    user = login_user(admin_email, admin_password)

    if not user:
        # If admin not found, create it
        register_user("Admin", admin_email, admin_password, "admin")
        print("✅ Default Admin created: admin@netamy.com / admin123")
    else:
        print("ℹ️ Admin user already exists.")

if __name__ == "__main__":
    init_db()

    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    app = QApplication(sys.argv)

    # Apply global stylesheet
    with open("app_style.qss", "r") as f:
        app.setStyleSheet(f.read())

    # Create default admin if not found
    create_default_admin()

    window = LoginWindow()
    window.showMaximized()

    sys.exit(app.exec_())
