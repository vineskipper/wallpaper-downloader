import argparse # for argument parsing
from time import sleep # for a delaying
import os # for file checking and command execution
import external_classes as ec # for Link and LinkSourceList classes

'''TODO: future additions
- add format option numbers for snakecase and camelcase, automatic file naming, and automatically adding ook extension
- add an interactive argument with image previews and editable filenames where you can manually choose which files to be downloaded
- add a silent argument where errors are ignored and not displayed
'''

def clearScreen(waitTime = 0):
    sleep(waitTime) and os.system("cls") if os.name == "nt" else os.system("clear")

parser = argparse.ArgumentParser(prog="linkDownloader.py", description="Downloads and stores files using links from a text file")
parser.add_argument("filePath", help="file to read from", metavar="file path", nargs="?", default=None)
parser.add_argument("parentDirectory", help="parent directory to store downloaded files in", metavar="parent directory", nargs="?", default=None)
parser.add_argument("-f", "--formatStyle", help="formatting style for directory names", metavar="optionNumber")
parser.add_argument("-s", "--silent", action="store_true", help="enable silent mode")
parser.add_argument("-i", "--interactive", action="store_true", help="enable interactive mode")
#TODO: future arguments go here

args = parser.parse_args()

FILEPATH = args.filePath if args.filePath else input("Enter the file's path: ")

if not os.path.isfile(FILEPATH):
    print("\nError: File not found")
    exit(1)

PARENT_DIRECTORY = args.parentDirectory if args.parentDirectory else input("Enter the parent directory: ")

if not os.path.isdir(PARENT_DIRECTORY):
    print("\nError: Directory not found")
    exit(1)

clearScreen()

srcList = ec.LinkSourceList(FILEPATH, PARENT_DIRECTORY)

srcList.printLinks(verbose=True)

# testing

input(">> ")
srcList.downloadAll()