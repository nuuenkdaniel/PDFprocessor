#!/home/Danuu/Documents/Coding_Projects/Personal_Projects/PDFprocessor/pdfvenv/bin/python3.11

from PDFMethods import convertPDF
import sys

def help():
    print("Usage: {} [OPTIONS]".format(sys.argv[0]))
    print("     -f <file1> <file2> ...")

if(len(sys.argv) < 3):
    help()
    sys.exit()

files = []
mode = None
for i in range(len(sys.argv)):
    if(i != 0):
        if(sys.arg[i] == "-f"):
            mode = "-f"
        elif(mode == "-f"):
            files.append(sys.argv[i])
        else:
            print("{} is not an option".format(sys.argv[i]))
            help()
            sys.exit()

if(len(files) <= 0):
    print("no files given")
    print("exiting...")
    sys.exit()
else:
    try:
        for file in files:
            convertPDF(file)
    except:
        print("Something went wrong")
    print("All files converted")
