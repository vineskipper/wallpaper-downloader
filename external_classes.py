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
    COMMENT_TOKEN = ":-"
    CASING_STYLE = {None: 0, "snake": 1, "camel": 2, "kebab": 3, "pascal": 4}
    MODE = {"silent": 1, "interactive": 2}

    def format(string: str, casing: int = 0) -> str:
        unformatted = string.split(" ")

        match casing:
            case 1:
                return "_".join(s.lower() for s in unformatted)

            case 2:
                return "".join(s.capitalize() if unformatted.index(s) != 0 else s.lower() for s in unformatted)
            
            case 3:
                return "-".join(s.lower() for s in unformatted)
            
            case 4:
                return "".join(s.capitalize() for s in unformatted)
            
            case _:
                return string

    def __init__ (self, filePath: str, parentDirectoryPath: str, casingStyle: str = None, enableFileExtensions: bool = True):
        self._filePath = filePath
        self._mailList: dict =  {}
        self._parentDirectoryPath = os.path.abspath(parentDirectoryPath)

        self._casing = casingStyle if casingStyle in LinkSourceList.CASING_STYLE.keys() else None
        # self._enableFileExtensions = enableFileExtensions #FIXME: update when config files are added

        with open(self._filePath) as src:
            while True:
                line = src.readline()

                if not line:
                    break
                elif line == "\n": #NOTE: comments
                    continue

                line = line.strip() # this is after the check because a blank line will be an empty string after being stripped of newline characters
                
                if line[0:2] == LinkSourceList.COMMENT_TOKEN:
                    continue

                commentPosition = line.find(LinkSourceList.COMMENT_TOKEN)

                if commentPosition + 1:
                    line = line[0:commentPosition].strip() # incase there were any spaces between the comment and the other contents of the line

                if line[0] == "@": # destination directory indicator
                    currentDir = LinkSourceList.format(line[1:], casing=LinkSourceList.CASING_STYLE[self._casing])
                    self._mailList[currentDir] = []
                else:
                    line = line.split(" , ") # 0 index is the link, 1 index is the name
                    self._mailList[currentDir].append(Link(line[0], LinkSourceList.format(line[1], casing=LinkSourceList.CASING_STYLE[self._casing]), os.path.join(self._parentDirectoryPath, currentDir)))

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