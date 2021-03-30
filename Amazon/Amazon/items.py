# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # 商品名
    title = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # # 品牌
    # brand = scrapy.Field()
    # 图片链接
    img_url = scrapy.Field()
    # 商品链接
    src = scrapy.Field()
    # 商品信息
    info = scrapy.Field()
    pass
