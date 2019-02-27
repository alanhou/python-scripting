import PyPDF2

def main():
	file_name = 'Haltermanpythonbook.pdf'
	pdfFile = PyPDF2.PdfFileReader(open(file_name, 'rb'))
	pdf_data = pdfFile.getDocumentInfo()
	print('----Metadata of the file----')
	for md in pdf_data:
		print(md+ ':' +pdf_data[md])

if __name__ == '__main__':
	main()
