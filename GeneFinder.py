from Gene import Gene
from enum import Enum
from FileHelper import FileHelper


class GeneSearchResults(Enum):
    INVALID_GENE = 1
    FOUND = 2
    NOT_FOUND = 3


END_OF_FILE = ""


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

        return self.searchInDNA(geneToFind)

    def searchInDNA(self, geneToFind: Gene):
        with open(self._dnaFileName, 'rt') as dnaFile:
            currGeneCombination = dnaFile.read(geneToFind.size)
            wantedGene = geneToFind.string
            geneSize = geneToFind.size

            while wantedGene not in currGeneCombination:
                nextBuffer = dnaFile.read(self._bufferSize)
                if nextBuffer == END_OF_FILE:
                    return GeneSearchResults.NOT_FOUND
                currGeneCombination = self.calculateNextCombination(currGeneCombination, geneSize, nextBuffer)

            return GeneSearchResults.FOUND

    def calculateNextCombination(self, currGeneCombination, geneSize, nextBuffer):
        lastCombinationSuffix = currGeneCombination[-geneSize:]
        return f"{lastCombinationSuffix}{nextBuffer}"
