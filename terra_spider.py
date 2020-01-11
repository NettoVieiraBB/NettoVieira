import scrapy

class TerraSpider(scrapy.Spider):
    name = 'Terra'
    start_urls = {
        'http://www.terra.com.br/'}
    def parse(Self, response):
        titulos = response.css(".main-url::text")
        print("titulos: {}".format(len(titulos)))
        for titulo in titulos:
            conteudo = titulo.extract().strip()
            if conteudo !="":
                yield {
                    'titulo': conteudo
                }