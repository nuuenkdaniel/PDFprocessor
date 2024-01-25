def mergePDF(files):
    from PyPDF2 import PdfWriter
    merger = PdfWriter()
    for file in files:
        merger.append(file)
    merger.write("merged.pdf")
    merger.close()

def splitPDF(file):
    from PyPDF2 import PdfReader
    from PyPDF2 import PdfWriter
    with open(file,"rb") as originalPDF:
        reader = PdfReader(originalPDF)
        pages = len(reader.pages)
        for i in range(pages):
            writer = PdfWriter()
            writer.append(fileobj=originalPDF,pages=(i,i+1))
            writer.write(f"split{i+1}.pdf")
            writer.close()
            

def createPDF():
    print("PDF Creater")