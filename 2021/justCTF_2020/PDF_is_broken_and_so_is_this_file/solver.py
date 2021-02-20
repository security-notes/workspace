import PyPDF2
import os

inputPath = f"{os.path.dirname(__file__)}/challenge.pdf"
outputPath = f"{os.path.dirname(__file__)}/out.pdf"
pdfWriter = PyPDF2.PdfFileWriter()
# rb for read binary
f = open(inputPath, 'rb')
pdfReader = PyPDF2.PdfFileReader(f)
print(pdfReader.documentInfo)
# Opening each page of the PDF
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
pdfWriter.addPage(pageObj)
# save PDF to file, wb for write binary
pdfOutput = open(outputPath, 'wb')
# Outputting the PDF
pdfWriter.write(pdfOutput)
# Closing the PDF writer
pdfOutput.close()