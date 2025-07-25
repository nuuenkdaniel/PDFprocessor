#!/home/{changeme}/.local/share/pdf-venv/bin/python

from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from fpdf import FPDF
from PIL import Image
from pathlib import Path
import sys
import os
import argparse

def convert2PDF(file, out_path):
    file_name, file_ext = os.path.splitext(file)
    if file_ext == ".png" or file_ext == ".jpg":
        with Image.open(file) as image:
            image_rgb = image.convert('RGB')
            image_rgb.save(out_path, "PDF")        
    elif file_ext == ".txt":
        with open(file,"r") as txt_file:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial",size=16)
            for line in txt_file:
                pdf.cell(200,10,txt=line,ln=1,align="L")
            pdf.output(out_path)
    else:
        raise ValueError(f"Unsupported extension: {file_ext}")

def mergePDF(files, out_path):
    merger = PdfWriter()
    for file in files:
        file_ext = os.path.splitext(file)[1]
        if file_ext != ".pdf":
            temp_out = Path.cwd() / "temporary_conversion_pdf.pdf"
            convert2PDF(file, temp_out)
            merger.append(temp_out)
            os.remove(temp_out)
        else:
            merger.append(file)
    merger.write(out_path)
    merger.close()

def splitPDF(file, out_path):
    with open(file,"rb") as originalPDF:
        reader = PdfReader(originalPDF)
        pages = len(reader.pages)
        title = os.path.splitext(file)[0]
        for i in range(pages):
            writer = PdfWriter()
            writer.append(fileobj=originalPDF,pages=(i,i+1))
            writer.write(f"{out_path}/{title}_{i+1}.pdf")
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
        help="Merge two or more FILES"
    )
    group.add_argument(
        "-s", "--split",
        nargs=1,
        metavar="FILE",
        help="Split a single FILE"
    )

    args = parser.parse_args()

    if args.convert:
        file = args.convert[0]
        print(f"Converting {file} to pdf...")
        stem = Path(file).stem
        out_path = Path.cwd() / f"{stem}.pdf"
        convert2PDF(file, out_path)
        print(f"Saved to {out_path}")
    elif args.merge:
        files = args.merge
        if len(files) < 3:
            parser.error("--merge requires at least two files and a new file name")
        print(f"Merging {len(files)-1} files: {', '.join(files[:-1])}")
        out_path = Path.cwd() / f"{files[-1]}.pdf"
        mergePDF(files[:-1], out_path)
        print(f"Saved to {out_path}")
    elif args.split:
        file = args.split[0]
        print(f"Splitting {file}...")
        out_path = Path.cwd()
        splitPDF(file, out_path)
        print(f"Saved to directory {out_path}/")
    else:
        parser.error("No action specified")

if __name__ == "__main__":
    main()
