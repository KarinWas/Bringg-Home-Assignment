from Gene import Gene
from enum import Enum
from FileHelper import FileHelper


class GeneSearchResults(Enum):
    INVALID_GENE = 1
    FOUND = 2
    NOT_FOUND = 3


END_OF_FILE = ""


class GeneFinder:
    __dnaFileName: str
    __bufferSize: int

    def __init__(self, dnaFileName: str, bufferSize: int):
        FileHelper.verifyFileExist(dnaFileName)
        self.__dnaFileName = dnaFileName
        self.__bufferSize = bufferSize

    def find(self, geneToFind: Gene) -> GeneSearchResults:
        if not geneToFind.isValid():
            return GeneSearchResults.INVALID_GENE

        return self.__searchInDNA(geneToFind)

    def __searchInDNA(self, geneToFind: Gene):
        with open(self.__dnaFileName, 'rt') as dnaFile:
            currGeneCombination = dnaFile.read(geneToFind.size)
            wantedGene = geneToFind.string
            geneSize = geneToFind.size

            while wantedGene not in currGeneCombination:
                nextBuffer = dnaFile.read(self.__bufferSize)
                if nextBuffer == END_OF_FILE:
                    return GeneSearchResults.NOT_FOUND
                currGeneCombination = self.__calculateNextCombination(currGeneCombination, geneSize, nextBuffer)

            return GeneSearchResults.FOUND

    def __calculateNextCombination(self, currGeneCombination, geneSize, nextBuffer) -> str:
        lastCombinationSuffix = currGeneCombination[-geneSize:]
        return f"{lastCombinationSuffix}{nextBuffer}"
