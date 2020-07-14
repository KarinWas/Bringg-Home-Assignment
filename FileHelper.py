from os import path


class FileHelper:
    @staticmethod
    def verifyFileExist(filename: str):
        if not path.exists(filename):
            raise FileNotFoundError
