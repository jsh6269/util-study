from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# pdf 읽고 쓰기
pdfReader = PdfReader("sample/input.pdf", "rb")
pdfWriter = PdfWriter()
pdfWriter.add_page(pdfReader.pages[3])
pdfWriter.add_page(pdfReader.pages[1])
pdfWriter.add_blank_page()
pdfWriter.add_page(pdfReader.pages[0])
pdfWriter.add_page(pdfReader.pages[0].rotate(90))
pdfWriter.write(open('sample/output.pdf', 'wb'))

# pdf 병합하기
pdfMerger = PdfMerger()
pdf1 = PdfReader(open('sample/input.pdf', 'rb'))
pdf2 = PdfReader(open('sample/sample.pdf', 'rb'))
pdfMerger.append(pdf1)
pdfMerger.append(pdf2)
pdfMerger.write('sample/output2.pdf')