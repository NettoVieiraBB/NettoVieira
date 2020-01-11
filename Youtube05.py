import scrapy
from scrapy.shell import inspect_response
import re

class YotubeSpider(scrapy.Spider):
    name = "Youtube"

    canal = 'videosimprovaveis'
    # canal = 'portadosfundos'

    start_urls = {
        'https://www.youtube.com/user/{}/videos'.format(canal)
    }

    def parse(self, response):

        #inspect_response(response, self)
        
        divs = response.xpath('.//div[contains(@class, "yt-lockup-video")]')

        for div in divs:
            duracao = div.xpath('.//span[@class="video-time"]/span/text()').extract_first()
            tempo = duracao.split(':')
            if len(tempo) == 2:
                duracao = tempo[0].rjust(2, "0")+":"+tempo[1]
            else:
                duracao = tempo[0]+":"+tempo[1].rjust(2, "0")+":"+tempo[2]
            imagem = div.xpath('.//span[@class="yt-thumb-clip"]/img/@src').extract_first()
            div_content = div.xpath('.//div[contains(@class, "yt-lockup-content")]')
            titulo = div_content.xpath('.//a/text()').extract_first()
            link = div_content.xpath('.//a/@href').extract_first()
            metainfo = div_content.xpath('.//ul[@class="yt-lockup-meta-info"]')
            views = metainfo.xpath('./li[1]/text()').extract_first()
            views = views.split()[0]
            views = re.sub(",", "", views)
            dias = metainfo.xpath('./li[2]/text()').extract_first()
            yield {
                "titulo": titulo,
                "duracao": duracao,
                "views": views,
                "dias": dias,
                "link": "https://www.youtube.com"+link,
                "image": imagem
            }