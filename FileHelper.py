from os import path


class FileHelper:
    @staticmethod
    def verifyFileExist(dnaFileName):
        if not path.exists(dnaFileName):
            raise FileNotFoundError
