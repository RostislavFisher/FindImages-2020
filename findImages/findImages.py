import requests
import bs4
import random


def parseImgur(amountOfIterations=9999, fileExpansion='.png'):
    Key = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    url = 'https://i.imgur.com/'
    removedURL = "https://i.imgur.com/removed.png"
    RemovedReq = requests.get(removedURL, allow_redirects=True).content
    numOfIteration = len(open("List.txt", 'r').readlines())
    while amountOfIterations < numOfIteration:
        Adr = url + ''.join([random.choice(list(Key)) for x in range(7)]) + fileExpansion
        RequestedImage = requests.get(Adr, allow_redirects=True).content
        if RequestedImage != RemovedReq:
            ListWrite = open("List.txt", 'a')
            print(Adr)
            open(str(numOfIteration) + fileExpansion, 'wb').write(RequestedImage)
            ListWrite.write(Adr + "\n")
            numOfIteration += 1
            ListWrite.close()


def parseLightShot(amountOfIterations=9999, fileExpansion='.png'):
    import bs4
    Key = '123456789qwertyuiopasdfghjklzxcvbnm'
    url = 'https://prnt.sc/'
    FileLen = len(open("List.txt", 'r').readlines())
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
            numOfIteration += 1
            ListWrite.close()
            RequestedImage = requests.get(RequestedImage, allow_redirects=True).content
            open(str(FileLen) + fileExpansion, 'wb').write(RequestedImage)
            FileLen = FileLen + 1
