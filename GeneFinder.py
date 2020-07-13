from Gene import Gene
from enum import Enum
from FileHelper import FileHelper

END_OF_FILE = ""


class GeneSearchResults(Enum):
    INVALID_GENE = 1
    FOUND = 2
    NOT_FOUND = 3


class GeneFinder:
    _dnaFileName: str
    _bufferSize: int

    def __init__(self, dnaFileName: str, bufferSize: int):
        FileHelper.verifyFileExist(dnaFileName)
        self._dnaFileName = dnaFileName
        self._bufferSize = bufferSize

    def find(self, geneToFind: Gene) -> GeneSearchResults:
        if not geneToFind.isValid():
            return GeneSearchResults.INVALID_GENE

        return self.searchInFile(geneToFind)

    def searchInFile(self, geneToFind: Gene):
        with open(self._dnaFileName, 'rt') as dnaFile:
            currGeneCombination = dnaFile.read(geneToFind.size)
            findGeneString = geneToFind.asString

            while findGeneString not in currGeneCombination:
                nextBuffer = dnaFile.read(self._bufferSize)
                if nextBuffer == END_OF_FILE:
                    return GeneSearchResults.NOT_FOUND
                currGeneCombination = currGeneCombination[-geneToFind.size:] + nextBuffer

            return GeneSearchResults.FOUND
