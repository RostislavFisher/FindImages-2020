import argparse
from findImages.findImages import parseLightShot, parseImgur

parseList = {
    '1': parseLightShot,
    '2': parseImgur,
}


class argumentScanner:
    def __init__(self, **kwargs):
        self.command = kwargs.get("command")
        self.siteToParse = self.command["siteToPars"] if self.command["siteToPars"] is not None else '1'
        self.amountOfIteration = self.command["amountOfIterations"] if self.command[
                                                                           "amountOfIterations"] is not None else 9999
        self.fileExpansion = self.command["fileExpansion"] if self.command["fileExpansion"] is not None else '.png'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-stp', '--siteToPars')
    parser.add_argument('-amofi', '--amountOfIterations')
    parser.add_argument('-fexp', '--fileExpansion')
    argScanner = argumentScanner(command=vars(parser.parse_args()))
    parseList[argScanner.siteToParse](argScanner.amountOfIteration, argScanner.fileExpansion)
