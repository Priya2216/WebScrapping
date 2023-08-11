# import scrapy
# from ..items import TreeScraperItem

# class TreeScrapy(scrapy.Spider):
#     name='quotes'
#     start_urls =[
#         'https://quotes.toscrape.com/'
#     ]

#     # def parse(self, response):
#     #     title=response.css('title::text').extract()
#     #     yield {'titletext':title}

#     def parse(self, response):
#         # all_div_quotes=response.css('div.quote')[0]
#         items = TreeScraperItem()
#         all_div_quotes = response.css('div.quote')
        
#         for quotes in all_div_quotes:

#             title= quotes.css('span.text::text').extract()
#             author= quotes.css('.author::text').extract()
#             tag= quotes.css('.tag::text').extract()

#             items['title']=title
#             items['author']=author
#             items['tag']=tag
            
#             # yield {
#             #     'title': title,
#             #     'author' : author,
#             #     'tag' : tag
#             # }

#             yield items

#         next_page =response.css('li.next a::attr(href)').get()
#         print(next_page)
#         if next_page is not None:
#             yield response.follow(next_page, callback= self.parse)


import scrapy
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse


class ImageDownloaderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'images/{image_guid}.jpg'

    def item_completed(self, results, item, info):
        item['image_paths'] = [x['path'] for ok, x in results if ok]
        return item

