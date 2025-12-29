class Link:
    def tupleToLink(arr: tuple) -> Link:
        return Link(arr[0], arr[1], arr[2])

    def __init__(self, link: str, newName: str, targetDirectoryPath: str):
        self.link: str = link
        self.fileName: str = newName
        self.targetDirectoryPath: str = targetDirectoryPath

    def __str__(self):
        return self.link

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

    def getMailList(self) -> dict:
        return self._mailList

    def printLinks(self):
        for k, arr in self.getMailList().items():
            for v in arr:
                print(f"{k}: {v}")
