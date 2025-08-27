#!/bin/sh

python -m venv pdf-venv
pdf-venv/bin/pip install -r requirements.txt
sed -i "1s|^#!.*|#!$HOME/.local/share/pdf-venv/bin/python|" pdf.py
chmod +x pdf.py
mv pdf.py ~/.local/bin/pdf
rm -rf ~/.local/share/pdf-venv
mv pdf-venv ~/.local/share
cd ..
rm -rf PDFprocessor
