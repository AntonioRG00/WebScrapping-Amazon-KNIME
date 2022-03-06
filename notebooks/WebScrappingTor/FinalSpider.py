# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from ConnectionManager import ConnectionManager
from time import sleep

URL_BASE = "https://www.amazon.es/s?k="
URLS_SCRAPPING = ["tarjeta+grafica","procesador","ram","placa+base","caja+pc","disipador","nvme","fuente+alimentacion"]
MAX_PAGES = 8
counter_post = 0
cm = ConnectionManager()

def saveToFile(string, index):
    print("Writing the file number:", index)
    f = open("files/output" + str(index) + ".html", "w")
    f.write(string)
    f.close()

def requestPage(finalUrl, index, numberOfTries=0):
    sleep(1)
    if numberOfTries < 20:
        try:
            req = cm.request(finalUrl)
            print(req)
            status_code = req.code if req != '' else -1
            if status_code == 200:
                return BeautifulSoup(req.read(), "html.parser")
            else:
                raise Exception
        except:
            requestPage(finalUrl, index, numberOfTries = numberOfTries + 1)

def main():
    for i in URLS_SCRAPPING:
        for j in range(1, MAX_PAGES):
            print("We are on the index number:", j, "of the page:", i)

            html = requestPage("%s%s&page=%d" % (URL_BASE, i, j), j)

            saveToFile(str(html), j+(URLS_SCRAPPING.index(i)*(len(URLS_SCRAPPING)-1)))

            if j % 5 == 0:
                cm.new_identity()

if __name__ == "__main__":
    main()