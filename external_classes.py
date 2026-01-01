from tqdm import tqdm # for progess bars
import requests # for downloading files with error handling capacities
import os # for files handling

class Link:
    def tupleToLink(arr: tuple) -> Link:
        return Link(arr[0], arr[1], arr[2])

    def __init__(self, link: str, newName: str, targetDirectoryPath: str):
        self._link: str = link
        self._fileName: str = newName
        self._targetDirectoryPath: str = targetDirectoryPath
        self._fullPath = os.path.join(self._targetDirectoryPath, self._fileName)

    def __str__(self):
        return self._link
    
    def download(self) -> bool: # return a status code on the success of the download process
        response = requests.get(self._link)

        if response.status_code == 200:
            with open(self._fullPath, "wb") as file:
                file.write(response.content)

            return True
        
        else:
            #FIXME: error handling
            print("error")
            return False

class LinkSourceList:
    def format(string: str, mode: int = 0) -> str:
        ...

    def __init__ (self, filePath: str, parentDirectoryPath: str, format=None):
        self._filePath = filePath
        self._mailList: dict =  {}
        self._parentDirectoryPath = os.path.abspath(parentDirectoryPath)

        with open(self._filePath) as src:
            while True:
                line = src.readline()

                if not line:
                    break
                elif line == "\n":
                    continue

                line = line.strip() # this is after the check because a blank line will be an empty string after being stripped of newline characters

                if line[0] == "@": # destination directory indicator
                    currentDir = line[1:]
                    self._mailList[currentDir] = []
                else:
                    line = line.split(" , ")
                    self._mailList[currentDir].append(Link(line[0], line[1], os.path.join(self._parentDirectoryPath, currentDir)))

        self._links = []

        for arr in self.getMailList().values():
            for link in arr:
                self._links.append(link)

    def getMailList(self) -> dict:
        return self._mailList
    
    def getLinks(self) -> tuple[Link]:
        return self._links

    def printLinks(self, verbose: bool = False):
        links = self.getLinks()

        if verbose:
            for link in links:
                print(f"({link._link}) goes to [{link._targetDirectoryPath}] as \"{link._fileName}\"")
        else:
            for link in links:
                print(link)

    def downloadAll(self) -> str: #TODO: add a way to filter files to download
        errMessage = ""

        print("Creating needed directories\n------------------------------\n")
        for subdirectoryName in tqdm(self.getMailList().keys()): # creating the required directories
            newDirectoryPath = os.path.join(self._parentDirectoryPath, subdirectoryName)

            if not os.path.isdir(newDirectoryPath):
                try:
                    os.makedirs(newDirectoryPath)
                except:
                    #FIXME: error handling
                    errMessage = f"\"{newDirectoryPath}\" could not be created"
                    return errMessage

        print("\nDownloading files\n--------------------\n")
        for link in tqdm(self.getLinks()):
            success = link.download()

            if not success:
                errMessage = f"\"{link._link}\" could not be downloaded"
                return errMessage

        return errMessage

    def cleanUp(): # removed unused directories that were created
        ...