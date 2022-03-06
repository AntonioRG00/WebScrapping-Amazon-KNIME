import os
import scrapy
import pathlib
pathToFiles = '../../notebooks/WebScrappingTor/files/'

def countFiles(path):
    return len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

class WCGraphicsCardsSpider(scrapy.Spider):
    name = 'webscrapping_amazon'
    start_urls = [pathlib.Path(os.path.abspath(f'{pathToFiles}output{x}.html')).as_uri() for x in range(1,countFiles(pathToFiles))]

    def parse(self, response): 
        fullDivProduct = response.xpath("(//div[contains(@class,'s-card-container s-overflow-hidden')])")
        print("fullDivProduct: ", len(fullDivProduct))

        for divProduct in fullDivProduct:

            try:
                text = divProduct.xpath(".//h2//span/text()").get()

                price = divProduct.xpath(".//span[contains(@class,'a-price-whole')]/text()").get().replace(',','.')
            except:
                pass

            yield {
                'text': text,
                'price': price,
            }