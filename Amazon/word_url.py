#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.03.28
# Filename:根据关键字返回url

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#关键字变为url
def Conversion(word):
    """
    使用selenium模拟，输入关键字来获取url
    :param word:
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    url = 'https://www.amazon.cn/?_encoding=UTF8&ref_=nav_logo'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=url)
    driver.implicitly_wait(10)

    #还可使用xpath来定位标签
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(word)      #搜索输入框
    driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()     #确认搜索

    url = driver.current_url    #得到当前页面的url

    driver.quit()
    print('url为：{}'.format(url))
    return url

if __name__ == '__main__':
    word = 't恤'
    url = Conversion(word)
    # print(url)