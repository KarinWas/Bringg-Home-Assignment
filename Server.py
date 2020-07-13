from flask import Flask
from Gene import Gene
from GeneFinder import GeneFinder, GeneSearchResults

api = Flask(__name__)
_geneFinder = None
BUFFER_SIZE = 1024
DNA_FILE_NAME = "DNA.txt"


@api.route("/genes/find/<gene>", methods=['GET'])
def findGene(gene):
    searchResult = _geneFinder.find(Gene(gene))

    if searchResult == GeneSearchResults.INVALID_GENE:
        return "Bad request", 400
    elif searchResult == GeneSearchResults.FOUND:
        return "Valid Gen", 200
    return "Not Found", 404


if __name__ == '__main__':
    _geneFinder = GeneFinder(DNA_FILE_NAME, BUFFER_SIZE)
    api.run("localhost", 8080)
