GENE_PREFIX = "AAAAAAAAAAA"


class Gene:
    __gene: str
    __size: int

    def __init__(self, gene: str):
        self.__gene = str.upper(gene)
        self.__size = len(self.__gene)

    @property
    def size(self) -> int:
        return self.__size

    @property
    def string(self) -> str:
        return self.__gene

    def isValid(self) -> bool:
        return self.__gene.startswith(GENE_PREFIX)
