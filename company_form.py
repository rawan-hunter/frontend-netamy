from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.logic import create_company


class CompanyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("➕ Create New Company - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Register New Company")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Company Name")
        layout.addWidget(self.name_input)

        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Address")
        layout.addWidget(self.address_input)

        self.pan_input = QLineEdit()
        self.pan_input.setPlaceholderText("PAN/VAT Number")
        layout.addWidget(self.pan_input)

        self.contact_input = QLineEdit()
        self.contact_input.setPlaceholderText("Contact Number")
        layout.addWidget(self.contact_input)

        self.fiscal_input = QLineEdit()
        self.fiscal_input.setPlaceholderText("Fiscal Year (e.g. 2080/81)")
        layout.addWidget(self.fiscal_input)

        self.create_btn = QPushButton("Create Company")
        self.create_btn.clicked.connect(self.save_company)
        layout.addWidget(self.create_btn)

        layout.setContentsMargins(400, 100, 400, 100)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.showMaximized()

    def save_company(self):
        name = self.name_input.text()
        address = self.address_input.text()
        pan = self.pan_input.text()
        contact = self.contact_input.text()
        fiscal_year = self.fiscal_input.text()

        if not name or not address or not pan or not contact or not fiscal_year:
            QMessageBox.warning(self, "Missing Fields", "Please fill all fields.")
            return

        create_company(name, address, pan, contact, fiscal_year)
        QMessageBox.information(self, "Success", f"Company {name} created successfully!")

        self.name_input.clear()
        self.address_input.clear()
        self.pan_input.clear()
        self.contact_input.clear()
        self.fiscal_input.clear()
