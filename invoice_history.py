import os
import webbrowser
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidget, QPushButton


class InvoiceHistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📄 Invoice History - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Past Invoices")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by customer, date, etc.")
        self.search_input.textChanged.connect(self.filter_invoices)
        layout.addWidget(self.search_input)

        self.invoice_list = QListWidget()
        self.invoice_list.itemDoubleClicked.connect(self.open_invoice)
        layout.addWidget(self.invoice_list)

        self.reload_btn = QPushButton("🔄 Reload Invoices")
        self.reload_btn.clicked.connect(self.load_invoices)
        layout.addWidget(self.reload_btn)

        layout.setContentsMargins(400, 50, 400, 50)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.load_invoices()
        self.showMaximized()

    def load_invoices(self):
        self.all_invoices = []
        self.invoice_list.clear()

        if os.path.exists("invoices"):
            for file in os.listdir("invoices"):
                if file.endswith(".pdf"):
                    self.all_invoices.append(file)

        self.invoice_list.addItems(self.all_invoices)

    def filter_invoices(self):
        keyword = self.search_input.text().lower()
        self.invoice_list.clear()
        for invoice in self.all_invoices:
            if keyword in invoice.lower():
                self.invoice_list.addItem(invoice)

    def open_invoice(self, item):
        filename = os.path.join("invoices", item.text())
        if os.path.exists(filename):
            webbrowser.open_new(os.path.abspath(filename))
