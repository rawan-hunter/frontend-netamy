from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.logic import login_user
from ui.dashboard_window import DashboardWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Welcome to Netamy ERP")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)

        layout.setContentsMargins(400, 150, 400, 150)  # Wide centered
        layout.setSpacing(20)

        self.setLayout(layout)
        self.showMaximized()

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, "Missing Input", "Please enter both email and password.")
            return

        user = login_user(email, password)
        if user:
            QMessageBox.information(self, "Login Success", f"Welcome, {user['name']} ({user['role']})")
            self.dashboard = DashboardWindow(user=user)
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid credentials.")
