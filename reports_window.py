from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QHBoxLayout, QLineEdit, QPushButton, QDateEdit
from PyQt5.QtCore import QDate
from core.logic import get_all_sales, get_all_purchases
from datetime import datetime


class ReportsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Reports - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Sales & Purchase Reports")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        # Sales Section
        sales_filter_layout = QHBoxLayout()

        self.sales_customer_input = QLineEdit()
        self.sales_customer_input.setPlaceholderText("Customer")
        sales_filter_layout.addWidget(self.sales_customer_input)

        self.sales_product_input = QLineEdit()
        self.sales_product_input.setPlaceholderText("Product")
        sales_filter_layout.addWidget(self.sales_product_input)

        self.sales_from = QDateEdit()
        self.sales_from.setCalendarPopup(True)
        self.sales_from.setDate(QDate.currentDate().addMonths(-1))
        sales_filter_layout.addWidget(self.sales_from)

        self.sales_to = QDateEdit()
        self.sales_to.setCalendarPopup(True)
        self.sales_to.setDate(QDate.currentDate())
        sales_filter_layout.addWidget(self.sales_to)

        self.sales_filter_btn = QPushButton("Apply Sales Filter")
        self.sales_filter_btn.clicked.connect(self.refresh_sales)
        sales_filter_layout.addWidget(self.sales_filter_btn)

        layout.addLayout(sales_filter_layout)

        self.sales_text = QTextEdit()
        self.sales_text.setReadOnly(True)
        layout.addWidget(self.sales_text)

        # Purchase Section
        purchase_filter_layout = QHBoxLayout()

        self.purchase_vendor_input = QLineEdit()
        self.purchase_vendor_input.setPlaceholderText("Vendor")
        purchase_filter_layout.addWidget(self.purchase_vendor_input)

        self.purchase_product_input = QLineEdit()
        self.purchase_product_input.setPlaceholderText("Product")
        purchase_filter_layout.addWidget(self.purchase_product_input)

        self.purchase_from = QDateEdit()
        self.purchase_from.setCalendarPopup(True)
        self.purchase_from.setDate(QDate.currentDate().addMonths(-1))
        purchase_filter_layout.addWidget(self.purchase_from)

        self.purchase_to = QDateEdit()
        self.purchase_to.setCalendarPopup(True)
        self.purchase_to.setDate(QDate.currentDate())
        purchase_filter_layout.addWidget(self.purchase_to)

        self.purchase_filter_btn = QPushButton("Apply Purchase Filter")
        self.purchase_filter_btn.clicked.connect(self.refresh_purchases)
        purchase_filter_layout.addWidget(self.purchase_filter_btn)

        layout.addLayout(purchase_filter_layout)

        self.purchase_text = QTextEdit()
        self.purchase_text.setReadOnly(True)
        layout.addWidget(self.purchase_text)

        layout.setContentsMargins(50, 20, 50, 20)
        layout.setSpacing(15)

        self.setLayout(layout)
        self.refresh_sales()
        self.refresh_purchases()
        self.showMaximized()

    def refresh_sales(self):
        sales = get_all_sales()
        customer_filter = self.sales_customer_input.text().lower()
        product_filter = self.sales_product_input.text().lower()
        from_date = self.sales_from.date().toPyDate()
        to_date = self.sales_to.date().toPyDate()

        filtered = []
        for sale in sales:
            parts = sale.split(",")
            if len(parts) < 8:
                continue
            customer, item, _, _, _, _, total_str, date_str = parts
            sale_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if (customer_filter in customer.lower() and
                product_filter in item.lower() and
                from_date <= sale_date <= to_date):
                filtered.append(sale)

        self.sales_text.setText("\n".join(filtered))

    def refresh_purchases(self):
        purchases = get_all_purchases()
        vendor_filter = self.purchase_vendor_input.text().lower()
        product_filter = self.purchase_product_input.text().lower()
        from_date = self.purchase_from.date().toPyDate()
        to_date = self.purchase_to.date().toPyDate()

        filtered = []
        for purchase in purchases:
            parts = purchase.split(",")
            if len(parts) < 8:
                continue
            vendor, item, _, _, _, _, total_str, date_str = parts
            purchase_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if (vendor_filter in vendor.lower() and
                product_filter in item.lower() and
                from_date <= purchase_date <= to_date):
                filtered.append(purchase)

        self.purchase_text.setText("\n".join(filtered))
