from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
name = 'abhiram'
acc = 1234
amount = 2500
pdf.set_font('Arial', '', 14)  # use Arial font instead of DejaVu
pdf.cell(200, 10, 'withdrawal form', border=True, ln=5)
pdf.cell(200, 10, 'account number\n'+str(acc), border=True, ln=5)
pdf.cell(200, 10, 'account name\n'+name, border=True, ln=5)
pdf.cell(200, 10, 'amount\n'+str(amount), border=True, ln=5)
pdf.output('w'+str(acc)+'hello_worl.pdf', 'F')
