import requests
import bs4
import random


def parseImgur(argScanner):
    amountOfIterations = argScanner.amountOfIteration
    fileExpansion = argScanner.fileExpansion
    numberInFileName = len(open("List.txt", 'r').readlines())

    Key = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    url = 'https://i.imgur.com/'
    removedURL = "https://i.imgur.com/removed.png"
    RemovedReq = requests.get(removedURL, allow_redirects=True).content
    numOfIteration = 0

    while amountOfIterations > numOfIteration:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + fileExpansion
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open("{0}/{1}{2}".format(argScanner.imageDir, str(numberInFileName), fileExpansion), 'wb').write(
                RequestedImage)
            ListWrite.write(Adr + "\n")
            numOfIteration += 1
            numberInFileName += 1
            ListWrite.close()


def parseLightShot(argScanner):
    amountOfIterations = argScanner.amountOfIteration
    fileExpansion = argScanner.fileExpansion

    Key = '123456789qwertyuiopasdfghjklzxcvbnm'
    url = 'https://prnt.sc/'
    numberInFileName = len(open("List.txt", 'r').readlines())
    removedURL = "https://prnt.sc/18jgksdgh"
    RemovedReq = requests.get(removedURL, headers={'User-Agent': 'Mozilla/5.0'})
    RemovedReq = bs4.BeautifulSoup(RemovedReq.text, "html.parser")
    RemovedReq = RemovedReq.find('img', id='screenshot-image')['src']

    numOfIteration = 0
    while amountOfIterations > numOfIteration:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(6)])
        RequestedImage = requests.get(Adr, headers={'User-Agent': 'Mozilla/5.0'})
        RequestedImage = bs4.BeautifulSoup(RequestedImage.text, "html.parser")
        RequestedImage = RequestedImage.find('img', id='screenshot-image')['src']

        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            ListWrite.write(Adr + "\n")
            ListWrite.close()
            RequestedImage = requests.get(RequestedImage, allow_redirects=True).content
            open("{0}/{1}{2}".format(argScanner.imageDir, str(numberInFileName), fileExpansion), 'wb').write(RequestedImage)
            numberInFileName += 1
            numOfIteration += 1
