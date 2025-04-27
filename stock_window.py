from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from core.logic import get_all_products


class StockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📦 Stock Overview - Netamy ERP")

        layout = QVBoxLayout()

        title = QLabel("Stock Overview")
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 30px;")
        layout.addWidget(title)

        self.stock_text = QTextEdit()
        self.stock_text.setReadOnly(True)
        layout.addWidget(self.stock_text)

        self.refresh_btn = QPushButton("🔄 Refresh Stock")
        self.refresh_btn.clicked.connect(self.load_stock)
        layout.addWidget(self.refresh_btn)

        layout.setContentsMargins(400, 100, 400, 100)
        layout.setSpacing(20)

        self.setLayout(layout)
        self.load_stock()
        self.showMaximized()

    def load_stock(self):
        products = get_all_products()
        self.stock_text.setText("\n".join(products))
