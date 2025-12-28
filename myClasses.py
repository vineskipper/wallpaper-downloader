class Link:
    def tupleToLink(arr: tuple) -> Link:
        return Link(arr[0], arr[1], arr[2])

    def __init__(self, link: str, newName: str, targetDirectoryPath: str):
        self.link: str
        self.fileName: str
        self.targetDirectoryPath: str

    def __str__(self):
        return self.link

class LinkSourceList:
    def __init__ (self, filePath: str):
        self._filePath = filePath
        self.links: list[Link] = [] #FIXME: move later
        self.mailList: dict =  {}

        with open(self.filePath) as src:
            while True:
                line = src.readline()

                if not line:
                    break

                if line[0] == "@": # destination directory indicator
                    currentDir = line[1:]
                    self.mailList[currentDir] = []
                else:
                    line = line.strip().split(" , ")
                    self.mailList[currentDir].append(line[0], line[1], currentDir)

    def printLinks(self):
        for k, v in self.mailList:
            print(f"{k}: {v}")