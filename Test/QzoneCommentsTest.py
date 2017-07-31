# -*- coding: utf-8 -*-
#导入相关包
from selenium import webdriver
import time,random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
#设置headers
dcap = dict(DesiredCapabilities.PHANTOMJS) 
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" ) 
#使用selenium+phantomjs
driver = webdriver.PhantomJS(executable_path="D:\\study information\\Interesting Programmes\\python\\Qzone-Related\\phantomjs.exe",desired_capabilities=dcap)
driver.maximize_window()
driver.implicitly_wait(90)    #设置隐式等待时长为90秒
#登录QQ空间
def connectQzone(qq):
    url='http://user.qzone.qq.com/'+qq+'/311'    #说说URL
    driver.get(url) 
    try:
        driver.find_element_by_id('login_div')  #判断是否需要登录
        login = True
    except:
        login = False
    if login == True:   #若需要登录，则利用selenium模拟登录
        driver.switch_to.frame('login_frame')   #跳转至登录框架
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()#选择用户名框
        driver.find_element_by_id('u').send_keys('QQ号')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('QQ密码')
        driver.find_element_by_id('login_button').click()   #模拟登录
        time.sleep(random.randint(80,100))    #线程休眠指定随机时间 避免反爬虫
#获取评论
def getComments(url):
    driver.get(url)
    time.sleep(random.randint(80,100))    #线程休眠指定随机时间 避免反爬虫
    try:
        driver.switch_to.frame('app_canvas_frame')    #跳转至指定框架
        content = driver.find_elements_by_css_selector('.comments_list')    #搜索指定标签
        judge=True
    except:
        judge=False
    if(judge==True):    #如果存在评论，则写入文件
        for n in content:
            fwrite.write(n.text+'\n')
fwrite=open('CommentsTest.txt','w')
connectQzone('QQ号')
getComments('http://user.qzone.qq.com/QQ号/mood/35363e8574a27858a0840a00.1')
print("==========完成================")
fwrite.close()
driver.close()
driver.quit()