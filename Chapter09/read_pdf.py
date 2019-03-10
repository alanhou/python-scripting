import PyPDF2

with open('Haltermanpythonbook.pdf', 'rb') as pdf:
	read_pdf = PyPDF2.PdfFileReader(pdf)
	print("Number of pages in pdf : ", read_pdf.numPages)
