import PyPDF2

pdf_in = open("C:\\Users\\Korisnik\\Desktop\\nlp-centar\\lbdl-a5-booklet.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_in)
pdf_writer = PyPDF2.PdfWriter()

for pagenum in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[pagenum]
    if pagenum % 2:
        page.rotate(180)
    pdf_writer.add_page(page)

pdf_out = open('rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
