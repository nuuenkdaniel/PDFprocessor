# PDFprocessor
## Installation ##
```
git clone https://github.com/nuuenkdaniel/PDFprocessor
cd PDFprocessor
./install.sh
```

## Usage ##
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
Will give you output.pdf

### Splitting files ###
```
# Split will only take files of the pdf format
pdf.py -s merged_pdf.pdf
```
Will give merged_pdf1.pdf merged_pdf2.pdf merged_pdf3.pdf ...
