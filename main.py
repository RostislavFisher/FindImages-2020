import argparse
from findImages.findImages import parseLightShot, parseImgur
import os

baseImageDir = "images"

parseList = {
    '1': parseImgur,
    '2': parseLightShot,
}


class argumentScanner:
    """
    argumentScanner - класс, использованый для удобнейшого способа хранить информацию из аргументов.

    - self.command хранит полный список(если быть точнее - словарь) аргументов

    - self.siteToParse - атрибут, хранящий ID сайта, которого мы будем парсить (переадрессация стоит в parseList) (хранится в int)

    - self.amountOfIterations - атрибут, хранящий количество фотографий, сколько мы будем сохранять (хранится в int)

    - self.fileExpansion - атрибут, хранящий расширение файла, которое будем искать

    - self.imageDir - атрибут, хранящий путь к папке с файлами

    Запуск программы из cmd:

    - Типичный запуск:
        $ python main.py
    - Запуск парсинга конкретного сервиса:
        $ python main.py --siteToParse 2
    - Запуск парсинга с фиксированным количеством файла:
        $ python main.py --amountOfIterations
    - Запуск парсинга с фикированным расширеним:
        $ python main.py --fileExpansion .png

    - Запуск парсинга и сохранения файлов в конкретную папку:
        $ python main.py --imageDir images

    """
    def __init__(self, **kwargs):
        self.command = kwargs.get("command")
        self.siteToParse = self.command["siteToPars"] if self.command["siteToPars"] is not None else '1'
        self.amountOfIteration = int(self.command["amountOfIterations"]) if self.command[
                                                                           "amountOfIterations"] is not None else 9999
        self.fileExpansion = self.command["fileExpansion"] if self.command["fileExpansion"] is not None else '.png'
        self.imageDir = self.command["baseDir"] if self.command["baseDir"] is not None else baseImageDir

        if not os.path.exists(self.imageDir):
            os.makedirs(self.imageDir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-stp', '--siteToPars')
    parser.add_argument('-amofi', '--amountOfIterations')
    parser.add_argument('-fexp', '--fileExpansion')
    parser.add_argument('-bd', '--baseDir')
    argScanner = argumentScanner(command=vars(parser.parse_args()))
    parseList[argScanner.siteToParse](argScanner)
