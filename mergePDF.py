#!/home/Danuu/Documents/Coding_Projects/Personal_Projects/PDFprocessor/pdfvenv/bin/python3.11

from PDFMethods import mergePDF
import sys

def help():
    print("Usage: {} [OPTIONS]".format(sys.argv[0]))
    print("     -f <file1> <file2> ...\
                -p 'new file name'")

if(len(sys.argv) < 2 or sys.argv[1] == "-h"):
    help()
else:
    files = []
    fileName = "merged.pdf"
    mode = None
    saveLocation = None
    for i in range(len(sys.argv)):
        if(i != 0):
            if(sys.argv[i] == "-f" or sys.argv[i] == "-p"): 
                mode = sys.argv[i]
            else:
                if(mode == "-f"):
                    files.append(sys.argv[i])
                elif(mode == "-p"):
                    fileName = sys.argv[i]
                elif(mode == "-s"):
                    saveLocation = sys.argv[i]
                else:
                    print("{} is not an option".format(sys.argv[i]))
                    help()
                    sys.exit()
    if(len(files) == 0):
        print("no files to merge")
        print("exiting...")
        sys.exit()
    try:
        mergePDF(files, fileName)
        print("merged file created")
    except:
        print("error")
