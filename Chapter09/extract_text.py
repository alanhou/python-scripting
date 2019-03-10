import PyPDF2

with open('Haltermanpythonbook.pdf', 'rb') as pdf:
	read_pdf = PyPDF2.PdfFileReader(pdf)
	pdf_page = read_pdf.getPage(2)
	pdf_content = pdf_page.extractText()
	print(pdf_content)
