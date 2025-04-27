from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from ui.company_form import CompanyForm
from ui.sales_form import SalesForm
from ui.purchase_form import PurchaseForm
from ui.product_manager import ProductManager
from ui.reports_window import ReportsWindow
from ui.stock_window import StockWindow
from ui.invoice_history import InvoiceHistoryWindow
from ui.user_manager import UserManager


class DashboardWindow(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle(f"Dashboard - {user['name']} ({user['role']})")

        layout = QVBoxLayout()

        title = QLabel("Netamy Accounting Dashboard")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.sales_label = QLabel("✔ Total Sales: NPR 0.00")
        self.purchase_label = QLabel("✔ Total Purchase: NPR 0.00")
        self.profit_label = QLabel("✔ Profit/Loss: NPR 0.00")

        layout.addWidget(self.sales_label)
        layout.addWidget(self.purchase_label)
        layout.addWidget(self.profit_label)

        self.new_company_btn = QPushButton("➕ Create New Company")
        self.new_company_btn.clicked.connect(self.open_company_form)

        self.sales_btn = QPushButton("➕ Record New Sale")
        self.sales_btn.clicked.connect(self.open_sales_form)

        self.purchase_btn = QPushButton("➕ Record New Purchase")
        self.purchase_btn.clicked.connect(self.open_purchase_form)

        self.product_btn = QPushButton("📦 Manage Products")
        self.product_btn.clicked.connect(self.open_product_manager)

        self.reports_btn = QPushButton("📊 View Reports")
        self.reports_btn.clicked.connect(self.open_reports)

        self.stock_btn = QPushButton("📦 View Stock Overview")
        self.stock_btn.clicked.connect(self.open_stock_window)

        self.invoice_history_btn = QPushButton("📄 View Invoice History")
        self.invoice_history_btn.clicked.connect(self.open_invoice_history)

        layout.addWidget(self.new_company_btn)
        layout.addWidget(self.sales_btn)
        layout.addWidget(self.purchase_btn)
        layout.addWidget(self.product_btn)
        layout.addWidget(self.reports_btn)
        layout.addWidget(self.stock_btn)
        layout.addWidget(self.invoice_history_btn)

        if self.user['role'] == "admin":
            self.user_mgmt_btn = QPushButton("👥 Manage Users")
            self.user_mgmt_btn.clicked.connect(self.open_user_manager)
            layout.addWidget(self.user_mgmt_btn)
        else:
            self.new_company_btn.setDisabled(True)

        layout.setContentsMargins(400, 100, 400, 100)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.showMaximized()

    def open_company_form(self):
        self.company_form = CompanyForm()
        self.company_form.showMaximized()

    def open_sales_form(self):
        self.sales_form = SalesForm()
        self.sales_form.showMaximized()

    def open_purchase_form(self):
        self.purchase_form = PurchaseForm()
        self.purchase_form.showMaximized()

    def open_product_manager(self):
        self.product_manager = ProductManager()
        self.product_manager.showMaximized()

    def open_reports(self):
        self.reports_window = ReportsWindow()
        self.reports_window.showMaximized()

    def open_stock_window(self):
        self.stock_window = StockWindow()
        self.stock_window.showMaximized()

    def open_invoice_history(self):
        self.invoice_history = InvoiceHistoryWindow()
        self.invoice_history.showMaximized()

    def open_user_manager(self):
        self.user_manager = UserManager()
        self.user_manager.showMaximized()
