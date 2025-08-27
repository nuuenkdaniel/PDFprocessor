python -m venv pdf-venv
pdf-venv/bin/pip install -r requirements.txt
chmod +x pdf.py
mv pdf.py ~/.local/bin/pdf
mv pdf-venv ~/.local/share
cd ..
rm -rf PDFprocessor
