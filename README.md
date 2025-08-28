# PDFprocessor
A command-line tool to convert, merge, and split files with ease.
Supports PDF, text, latex, and image formats.
## Installation ##
```
git clone https://github.com/nuuenkdaniel/PDFprocessor
cd PDFprocessor
./install.sh
```

## Usage ##
```
pdf.py (-c FILE | -m FILE [FILE ...] OUTPUT | -s FILE)
```
### Convert a file ###
```
# Convert can accept files of the pdf, txt, jpg, png formats
pdf.py -c input.txt
```
Will give you input.pdf

### Merge file(s) ###
```
# Merge can accept files of the pdf, txt, jpg, png formats
pdf.py -m input1.txt input2.pdf input3.tex output_name
```
Will give you output_name.pdf

### Splitting files ###
```
# Split will only take files of the pdf format
pdf.py -s merged_pdf.pdf
```
Will give merged_pdf1.pdf merged_pdf2.pdf merged_pdf3.pdf ...
