# -*- coding: utf-8 -*-
#导入相关包
import requests,re
from bs4 import BeautifulSoup
#设置headers信息 避免反爬虫
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer':'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=Python&sm=0&p=1&source=0'
        }
def get_message(page):
    #招聘信息搜索URL
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=Python&sm=0&p={0}&source=0'.format(page)
    webdata = requests.get(url,headers=headers).content    #获取页面源文件内容
    soup = BeautifulSoup(webdata,'lxml')    #解析页面
    names = soup.select("td.zwmc")    #获取职位名称
    salaries = soup.select("td.zwyx")    #获取工作薪水
    locations = soup.select("td.gzdd")    #获取工作地点
    times = soup.select("td.gxsj")    #获取发布时间
    for name, salary, location, time in zip(names, salaries, locations, times):
        print ('职位名称:',name.get_text().strip(),'工作薪水:',salary.get_text())
        print ('工作地点:',location.get_text(),'发布时间:',time.get_text())
    print("第{0}页".format(page))
if __name__ == '__main__':
    #智联招聘URL
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=Python&sm=0&p=1&source=0'
    webdata = requests.get(url,headers=headers).content    #获取页面源文件内容
    soup = BeautifulSoup(webdata,'lxml')    #解析页面
    #计算搜索总页码数
    job_count = re.findall(r"共<em>(.*?)</em>个职位满足条件", str(soup))[0]
    pages = (int(job_count)/60) + 1
    if(pages>=50):    #若页码数大于50，则只考虑前50页
        pages=50
    for i in range(1,pages+1):
        get_message(i)
