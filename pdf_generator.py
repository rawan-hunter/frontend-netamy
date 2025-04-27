import os
from fpdf import FPDF
from datetime import date

def generate_invoice(customer, items, total_amount):
    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Netamy Accounting - Invoice", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Customer: {customer}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {date.today()}", ln=True)

    pdf.ln(10)

    for item in items:
        pdf.cell(200, 10, txt=f"{item}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Amount: NPR {total_amount:.2f}", ln=True)

    filename = f"invoices/invoice_{customer}_{date.today()}.pdf"
    pdf.output(filename)
