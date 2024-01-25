def mergePDF(files,newFileName):
    from PyPDF2 import PdfWriter
    merger = PdfWriter()
    for file in files:
        merger.append(file)
    if newFileName == None:
        merger.write("merged.pdf")
    else:
        merger.write(f"{newFileName}.pdf")
    merger.close()

def splitPDF(file):
    from PyPDF2 import PdfReader
    from PyPDF2 import PdfWriter
    import os
    with open(file,"rb") as originalPDF:
        reader = PdfReader(originalPDF)
        pages = len(reader.pages)
        title = os.path.basename("merged.pdf")
        for i in range(pages):
            writer = PdfWriter()
            writer.append(fileobj=originalPDF,pages=(i,i+1))
            writer.write(f"{title[0:-4]}_{i+1}.pdf")
            writer.close()
            
def createPDF(file):
    from PyPDF2 import PdfWriter
    from pillow import Image
    with Image.open(file) as image:
        pdf_writer = PdfWriter()
        pdf_writer.addPage(image.convert('RGB'))
        with open(pdf_path, 'wb') as pdf_file:
            pdf_writer.write(pdf_file)