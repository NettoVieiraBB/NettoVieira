import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = 'Uol'
    start_urls = {'https://lista.mercadolivre.com.br/super-mario'}
    
    def parse(Self, response):
        produtos = response.xpath(".//ol[contains(@class,'section') and contains(@class,'search-results')]/li")

        for produto in produtos:
            print(produto.xpath(".//span[@class='main-title']/text()").extract_first())