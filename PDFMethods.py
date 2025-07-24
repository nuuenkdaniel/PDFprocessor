from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from fpdf import FPDF
from PIL import Image
import sys
import os
import argparse

def convertPDF(file):
    file_name, file_ext = os.path.splitext(file)
    if file_ext == ".png" or file_ext == ".jpg":
        with Image.open(file) as image:
           image_rgb = image.convert('RGB')
           image_rgb.save(f"{file_name}.pdf", "PDF")        
    elif file_ext == ".txt":
        with open(file,"r") as txt_file:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial",size=16)
            for line in txt_file:
                pdf.cell(200,10,txt=line,ln=1,align="L")
            pdf.output(f"{file_name}.pdf")
    return f"{file_name}.pdf"

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
        merger.write(new_file_name)
    merger.close()

def splitPDF(file):
    with open(file,"rb") as originalPDF:
        reader = PdfReader(originalPDF)
        pages = len(reader.pages)
        title = os.path.splitext(file)[0]
        for i in range(pages):
            writer = PdfWriter()
            writer.append(fileobj=originalPDF,pages=(i,i+1))
            writer.write(f"{title}_{i+1}.pdf")
            writer.close()

def main():
    parser = argparse.ArgumentParser(
        description="Tool that can convert, merge, or split files (exactly one action)."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-c", "--convert",
        nargs=1,
        metavar="FILE",
        help="Convert a single FILE"
    )
    group.add_argument(
        "-m", "--merge",
        nargs="+",
        metavar="FILE",
        help="Merge two or more FILEs"
    )
    group.add_argument(
        "-s", "--split",
        nargs=1,
        metavar="FILE",
        help="Split a single FILE"
    )

    args = parser.parse_args()

    if args.convert:
        infile = args.convert[0]
        print(f"Converting {infile} to pdf...")
    elif args.merge:
        files = args.merge
        if len(files) < 2:
            parser.error("--merge requires at least two files")
        print(f"Merging {len(files)} files: {', '.join(files)}")
    elif args.split:
        infile = args.split[0]
        print(f"Splitting {infile}...")
    else:
        parser.error("No action specified")

if __name__ == "__main__":
    print("Testing")
    main()
