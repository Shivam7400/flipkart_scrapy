import scrapy
from ..items import FlipkartScraperItem

class FlipkartScraper(scrapy.Spider):
    name = "flipkart_scraper"
    allowed_domains = ["flipkart.com"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    Search_Product_Name = 'laptop'
    no_of_pages = 2

    def start_requests(self):
        urls = f"https://www.flipkart.com/search?q={FlipkartScraper.Search_Product_Name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
        yield scrapy.Request(url=urls, callback=self.parse, headers=self.headers)

    def parse(self, response):
        list_i = response.xpath("//*[@id='container']/div/div[3]/div[1]/div[2]/div/div/div/div/a")
        for item in list_i:
            product = FlipkartScraperItem()
            product['title'] = " ".join(item.xpath(".//div[2 or 3]/div[1]/div[1]/text()").getall())
            product['price'] = " ".join(item.xpath(".//div/div/div[1]/div[1]/div[1]/text()").getall())
            product['original_price'] = " ".join(item.xpath(".//div/div[2]/div[1]/div[1]/div[2]/text()").getall())
            product['price_off_percentages'] = " ".join(item.xpath(".//div/div[2]/div[1]/div[1]/div[3]/span/text()").getall())
            product['image_url'] = item.xpath(".//div/div[1]/div/div/img/@src").get()
            yield product


        next_page = f"https://www.flipkart.com/search?q={FlipkartScraper.Search_Product_Name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={FlipkartScraper.no_of_pages}"
        if FlipkartScraper.no_of_pages <= 2:
            FlipkartScraper.no_of_pages += 1
            yield scrapy.Request(url=next_page, callback=self.parse, headers=self.headers)