import scrapy
from bs4 import BeautifulSoup

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    # Handle the Command line arguments
    def __init__(self, url, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        self.url = url


    # Handle the initial page
    def parse(self, response):
        # logging.info('Scraping {0} in {1}'.format(self.sector,self.city))
        yield scrapy.http.Request(url = self.url, callback = self.parse_results)


    # Handle the individual result
    def parse_results(self, response):
        entry_soup = BeautifulSoup(response.text,'html.parser')

        try:
            name = entry_soup.find(id='title').text.strip()
        except:
            name = ''

        try:
            price = entry_soup.find(id='priceblock_ourprice').text.strip()
        except:
            price = ''

        try:
            img_tag = entry_soup.find(id='imgTagWrapperId').img
            img_url = img_tag.get('src')
        except:
            img_url = ''

        yield {'Name':name, 'Price':price, 'Image':img_url}