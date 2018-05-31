from scrapy import Spider,Request
# from yunyinyue.items import YunyinyueItem
from urllib.parse import quote
from lxml import etree


import scrapy


class YunyinyueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    song = scrapy.Field()


class YunyinyueSpider(Spider):

    name = 'yunyinyue'

    def start_requests(self):
        singer = '周杰伦'
        raw_url = 'http://www.xiami.com/search/song/page/{}?spm=a1z1s.3521869.0.0.Nv2jr2&key={}&category=-1'

        for i in range(44):
            url = raw_url.format(str(i+1), quote(singer))
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = etree.HTML(response.text)
        hrefs = selector.xpath('//td[@class="song_name"]/a[1]/@href')
        titles = selector.xpath('//td[@class="song_name"]/a[1]/@title')
        for href,title in zip(hrefs, titles):
            yield Request(url=href, callback=self.parse_content, meta={'title': title})

    def parse_content(self,response):
        selector = etree.HTML(response.text)

        song_list = selector.xpath('//div[@class="lrc_main"]/text()')
        song = []
        for line in song_list:
            song.append(line.strip())
        result = '，'.join(song)
        item = YunyinyueItem()
        item['title'] = response.meta['title']
        item['song'] = result
        yield item

spider = YunyinyueSpider()
songs_generator = spider.start_requests()
for i in songs_generator:
    print(i.title,i.song)
