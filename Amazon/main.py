#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.03.30
# Filename:主程序入口

from word_url import Conversion

from scrapy.crawler import CrawlerProcess
from Amazon.spiders import amazon
from scrapy.utils.project import get_project_settings
import os

#选择执行方式（特用于指定类型的商品）
def SelectWay():
    print('\n'
          '选择输入url请输入‘1’\n'
          '选择输入商品关键字请输入‘2’')
    w = input('请输入选择：')
    if w == '1':
        print('\n'
              '请输入url')
        url = input('url为：')
        return url
    elif w == '2':
        print('\n'
              '请输入关键字')
        word = input('关键字为：')
        url = Conversion(word)
        return url
    else:
        print('  请确认后重新输入')
        SelectWay()

#爬虫项目启动端口
def StartSpider(url):
    """
    传入起始url来开始爬虫
    :param url:
    :return:
    """
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'Amazon.settings'
    scrapy_settings = get_project_settings()
    scrapy_settings.set(
        'ITEM_PIPELINES',
        {'Amazon.pipelines.AmazonJsonPipeline': 300,
       'Amazon.pipelines.AmazonExcelPipeline': 400,},
    )

    process = CrawlerProcess(scrapy_settings)
    start_urls = [url]
    process.crawl(amazon.AmazonSpider,start_urls=start_urls)  #开启指定爬虫
    process.start()

#主程序
def main():
    url = SelectWay()
    StartSpider(url)

if __name__ == '__main__':
    main()