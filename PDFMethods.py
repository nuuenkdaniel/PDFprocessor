from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from fpdf import FPDF
from PIL import Image
import os

def convertPDF(file):
    file_name, file_ext = os.path.splitext(file)
    if file_ext == ".png" or file_ext == ".jpg":
        with Image.open(file) as image:
           image_rgb = image.convert('RGB')
           image_rgb.save(f"{file_name}.pdf", "PDF")
        return f"{file_name}.pdf"    
    elif file_ext == ".txt":
        with open(file,"r") as txt_file:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial",size=16)
            for line in txt_file:
                pdf.cell(200,10,txt=line,ln=1,align="L")
            pdf.output(f"{file_name}.pdf")

def mergePDF(files,new_file_name):
    merger = PdfWriter()
    for file in files:
        file_ext = os.path.splitext(file)[1]
        if file_ext != ".pdf":
            file = convertPDF(file)
        merger.append(file)
    if new_file_name == None:
        merger.write("merged.pdf")
    else:
        merger.write(f"{new_file_name}.pdf")
    merger.close()


def splitPDF(file):
    with open(file,"rb") as originalPDF:
        reader = PdfReader(originalPDF)
        pages = len(reader.pages)
        title = os.path.basename(file)
        for i in range(pages):
            writer = PdfWriter()
            writer.append(fileobj=originalPDF,pages=(i,i+1))
            writer.write(f"{title[0:-4]}_{i+1}.pdf")
            writer.close()