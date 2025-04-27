from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.logic import save_sale, get_all_products


class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("➕ Record New Sale - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Record New Sale")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.customer_input = QLineEdit()
        self.customer_input.setPlaceholderText("Customer Name")
        layout.addWidget(self.customer_input)

        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("Product Name")
        layout.addWidget(self.item_input)

        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("Unit (e.g., pcs, kg)")
        layout.addWidget(self.unit_input)

        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Quantity")
        layout.addWidget(self.qty_input)

        self.rate_input = QLineEdit()
        self.rate_input.setPlaceholderText("Rate per Unit")
        layout.addWidget(self.rate_input)

        self.tax_input = QLineEdit()
        self.tax_input.setPlaceholderText("Tax (%)")
        layout.addWidget(self.tax_input)

        self.total_input = QLineEdit()
        self.total_input.setPlaceholderText("Total Amount")
        layout.addWidget(self.total_input)

        self.save_btn = QPushButton("Save Sale")
        self.save_btn.clicked.connect(self.save_sale_record)
        layout.addWidget(self.save_btn)

        layout.setContentsMargins(400, 100, 400, 100)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.showMaximized()

    def save_sale_record(self):
        customer = self.customer_input.text()
        item = self.item_input.text()
        unit = self.unit_input.text()
        qty = self.qty_input.text()
        rate = self.rate_input.text()
        tax = self.tax_input.text()
        total = self.total_input.text()

        if not customer or not item or not unit or not qty or not rate or not tax or not total:
            QMessageBox.warning(self, "Missing Fields", "Please fill all fields.")
            return

        save_sale(customer, item, unit, float(qty), float(rate), float(tax), float(total))
        QMessageBox.information(self, "Success", f"Sale recorded for {customer}.")

        self.customer_input.clear()
        self.item_input.clear()
        self.unit_input.clear()
        self.qty_input.clear()
        self.rate_input.clear()
        self.tax_input.clear()
        self.total_input.clear()
