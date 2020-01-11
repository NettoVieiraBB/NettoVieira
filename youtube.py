import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response

class YoutubeSpider(scrapy.Spider):
    name = "Youtube"

    canal = 'inventonahoratv'
    # canal = 'Lucas Lira'

    start_urls = {
        'https://www.youtube.com/user/inventonahoratv/videos'.format(canal)
    }

    def parse(self, response):
        #open_in_browser(response)
         resultado = response.css ('..yt-lockup-meta-info li , .yt-ui-ellipsis-2')
         print(resultado)

         inspect_response(response, self)
          for teste in resultado:
              titulo = teste.css("::text").extract_first()
              link = teste.css('::attr("href")').extract_first()
              yield {'titulo': titulo,
                        'link': link}
          
          
        #   #  print('Titulo:' + str(teste.css("::text").extract_first()))
        #   # print("Link:" + str(teste.css('::attr("href")').extract_first()))