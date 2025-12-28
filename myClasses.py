class Link:
    def tupleToLink():
        ...

    def __init__(self, link: str, newName: str, targetDirectoryPath: str):
        self.link: str
        self.fileName: str
        self.targetDirectoryPath: str

class LinkSourceList:
    def __init__ (self, filePath: str):
        self._filePath = filePath
        self.links: list[Link] = []