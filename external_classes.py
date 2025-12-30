class Link:
    def tupleToLink(arr: tuple) -> Link:
        return Link(arr[0], arr[1], arr[2])

    def __init__(self, link: str, newName: str, targetDirectoryPath: str):
        self._link: str = link
        self._fileName: str = newName
        self._targetDirectoryPath: str = targetDirectoryPath

    def __str__(self):
        return self._link
    
    def download(self):
        ...

class LinkSourceList:
    def __init__ (self, filePath: str):
        self._filePath = filePath
        self._mailList: dict =  {}

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
                    self._mailList[currentDir].append(Link(line[0], line[1], currentDir))

        self._links = []

        for arr in self.getMailList().values():
            for link in arr:
                self._links.append(link)

    def getMailList(self) -> dict:
        return self._mailList
    
    def getLinks(self) -> tuple:
        return self._links

    def printLinks(self, showDirectories: bool = False):
        if showDirectories:
            for k, arr in self.getMailList().items():
                for v in arr:
                    print(f"{k}: {v}")
        else:
            for link in self.getLinks():
                print(link)

