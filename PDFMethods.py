from pypdf import PdfWriter
def mergePDF(file1,file2):
    merger = PdfWriter()
    for file in [file1,file2]:
        merger.append(file)
    merger.write("merged.pdf")
    merger.close()

def splitPDF(fileNames):
    print("PDF Splitter")

def createPDF():
    print("PDF Creater")