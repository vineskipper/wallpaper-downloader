import argparse
from time import sleep
import os

def clearScreen(waitTime = 0):
    sleep(waitTime) and os.system("cls") if os.name == "nt" else os.system("clear")

parser = argparse.ArgumentParser(prog="linkDownloader.py", description="Downloads and stores files using links from a text file")
parser.add_argument("filePath", help="file to read from", metavar="linkFile.txt", nargs="?", default=None)

#TODO: future arguments go here

args = parser.parse_args()

FILEPATH = args.filePath if args.filePath else input("Enter the file's path: ")

if not os.path.isfile(FILEPATH):
    print("Error: File not found")
    exit(1)

clearScreen()
