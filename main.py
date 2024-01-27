from PDFMethods import convertPDF
from PDFMethods import splitPDF
from PDFMethods import mergePDF

splitPDF("merged.pdf")
mergePDF(["merged_1.pdf","merged_2.pdf"],"merged2.pdf")