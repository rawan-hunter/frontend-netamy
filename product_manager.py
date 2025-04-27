from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
from core.logic import add_product, get_all_products


class ProductManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📦 Manage Products - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Manage Products")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Product Name")
        layout.addWidget(self.name_input)

        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("Unit (e.g., pcs, kg)")
        layout.addWidget(self.unit_input)

        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Initial Quantity")
        layout.addWidget(self.qty_input)

        self.rate_input = QLineEdit()
        self.rate_input.setPlaceholderText("Rate per Unit")
        layout.addWidget(self.rate_input)

        self.add_btn = QPushButton("Add Product")
        self.add_btn.clicked.connect(self.add_new_product)
        layout.addWidget(self.add_btn)

        layout.addWidget(QLabel("📄 Current Products:"))

        self.product_list = QTextEdit()
        self.product_list.setReadOnly(True)
        layout.addWidget(self.product_list)

        self.refresh_btn = QPushButton("🔄 Refresh Products")
        self.refresh_btn.clicked.connect(self.load_products)
        layout.addWidget(self.refresh_btn)

        layout.setContentsMargins(400, 50, 400, 50)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.load_products()
        self.showMaximized()

    def add_new_product(self):
        name = self.name_input.text()
        unit = self.unit_input.text()
        qty = self.qty_input.text()
        rate = self.rate_input.text()

        if not name or not unit or not qty or not rate:
            QMessageBox.warning(self, "Missing Fields", "Please fill all fields.")
            return

        add_product(name, unit, float(qty), float(rate))
        QMessageBox.information(self, "Success", f"Product {name} added.")

        self.name_input.clear()
        self.unit_input.clear()
        self.qty_input.clear()
        self.rate_input.clear()
        self.load_products()

    def load_products(self):
        products = get_all_products()
        self.product_list.setText("\n".join(products))
