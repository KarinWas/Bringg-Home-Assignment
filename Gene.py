GENE_PREFIX = "AAAAAAAAAAA"


class Gene:
    _gene: str
    _size: int

    def __init__(self, gene: str):
        self._gene = str.upper(gene)
        self._size = len(self._gene)

    @property
    def size(self) -> int:
        return self._size

    @property
    def string(self) -> str:
        return self._gene

    def isValid(self) -> bool:
        return self._gene.startswith(GENE_PREFIX)
