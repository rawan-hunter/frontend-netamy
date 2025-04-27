from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from core.logic import register_user, get_all_users, delete_user


class UserManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("👥 Manage Users - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Manage Users (Admin Only)")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full Name")
        layout.addWidget(self.name_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        layout.addWidget(self.password_input)

        self.role_input = QLineEdit()
        self.role_input.setPlaceholderText("Role (admin/staff)")
        layout.addWidget(self.role_input)

        self.add_user_btn = QPushButton("➕ Add User")
        self.add_user_btn.clicked.connect(self.create_user)
        layout.addWidget(self.add_user_btn)

        layout.addWidget(QLabel("📄 All Users:"))
        self.user_list = QTextEdit()
        self.user_list.setReadOnly(True)
        layout.addWidget(self.user_list)

        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("Email to delete")
        layout.addWidget(self.delete_input)

        self.delete_btn = QPushButton("🗑 Delete User")
        self.delete_btn.clicked.connect(self.delete_user_record)
        layout.addWidget(self.delete_btn)

        self.refresh_btn = QPushButton("🔄 Refresh Users")
        self.refresh_btn.clicked.connect(self.load_users)
        layout.addWidget(self.refresh_btn)

        layout.setContentsMargins(400, 50, 400, 50)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.load_users()
        self.showMaximized()

    def create_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        role = self.role_input.text()

        if not name or not email or not password or role not in ["admin", "staff"]:
            QMessageBox.warning(self, "Missing Fields", "Fill all fields correctly.")
            return

        try:
            register_user(name, email, password, role)
            QMessageBox.information(self, "Success", "User created successfully.")
            self.load_users()
            self.name_input.clear()
            self.email_input.clear()
            self.password_input.clear()
            self.role_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_user_record(self):
        email = self.delete_input.text()
        if not email:
            QMessageBox.warning(self, "Missing Field", "Please enter email.")
            return

        delete_user(email)
        QMessageBox.information(self, "Deleted", f"User {email} deleted.")
        self.load_users()
        self.delete_input.clear()

    def load_users(self):
        users = get_all_users()
        self.user_list.setText("\n".join(users))
