import scrapy
from Amazon.items import AmazonItem
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor


class AmazonSpider(CrawlSpider):
    # start_url = 'https://www.amazon.cn/s?k=t%E6%81%A4&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss_1'
    # start_url = start_url
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    # start_urls = [start_url]

    link = LinkExtractor(allow=r'ref=sr_pg_\d+')
    # link1 = LinkExtractor(allow=r'4kmeinv/index\.html')  # 第一页
    rules = (
        Rule(link, callback='parse_item', follow=True),
        # Rule(link1, callback='parse_item'),
    )

    def parse_item(self, response):
        div_list = response.xpath('//div[@data-component-type="s-search-result"]')
        for div in div_list:
            item = AmazonItem()
            # try:
            #     data_uuid = div.xpath('./@data-uuid')
            #     if data_uuid:
            #         pass
            #     else:
            #         continue
            # except:
            #     continue
            src = 'https://www.amazon.cn' + div.xpath('./div/span/div/div/span/a/@href').extract()[0]
            yield scrapy.Request(url=src,callback=self.parse_thing,meta={'item':item,'src':src})

    def parse_thing(self,response):
        item = response.meta['item']
        src = response.meta['src']

        title = response.xpath("//h1[@id='title']/span/text()").extract()[0]
        item['title'] = title.strip()  # 去除两端空白
        price = response.xpath("//td[@class='a-span12']/span/text()").extract()[0]
        item['price'] = price
        img_url = response.xpath("//div[@id='imgTagWrapperId']/img/@data-old-hires").extract()[0]
        item['img_url'] = img_url
        item['src'] = src
        try:
            info = response.xpath("//div[@id='productDescription']/p/text()").extract()[0]
            info = info.strip()
        except:
            info = '空'
        item['info'] = info
        yield item