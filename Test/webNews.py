# -*- coding: utf-8 -*-
#导入相关包
import requests
from bs4 import BeautifulSoup
url = "http://news.qq.com/"    #腾讯新闻URL
webdata = requests.get(url).text    #获取页面源文件
soup = BeautifulSoup(webdata,'lxml')    #解析文件
news_titles = soup.select("div.text > em.f14 > a.linkto")    # 从解析文件中通过select选择器定位指定的元素，返回一个列表
for news in news_titles:    # 提取出标题和链接信息并输出
    title = news.get_text()
    link = news.get("href")
    print (title,link)