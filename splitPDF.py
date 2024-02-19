#!/home/Danuu/Documents/Coding_Projects/Personal_Projects/PDFprocessor/pdfvenv/bin/python3.11

from PDFMethods import splitPDF
import sys

def help():
    print("Usage: {} [OPTIONS]".format(sys.argv[0]))
    print("     -f <file>")

if(len(sys.argv) < 3 or sys.argv[1] == "-h"):
    help()
    sys.exit()
else:
    file = None
    mode = None
    for i in range(len(sys.argv)):
        if(i != 0):
            if(sys.argv[i] == "-f"):
                mode = "-f"
            else:
                if(mode == "-f"):
                    file = sys.argv[i]
                else:
                    print("{} is not an option".format(sys.argv[i]))
                    help()
                    sys.exit()
    if(file == None):
        print("no files given")
        print("exiting")
    splitPDF(file)
    print("done")
