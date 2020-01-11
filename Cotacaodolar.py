import scrapy

class UolSpider(scrapy.Spider):
    name = 'Uol'
    start_urls = {'https://www.uol.com.br/'}
    
    def parse(Self, response):
        cotacao = response.css(".HU_currency__quote.HU_currency__quote-up::text").extract_first()
        print("cotacao: ", cotacao)
     

                