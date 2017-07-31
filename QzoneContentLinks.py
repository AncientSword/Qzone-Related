# -*- coding: utf-8 -*-
#导入相关包
from selenium import webdriver
import time,random
#使用selenium+phantomjs
driver = webdriver.PhantomJS(executable_path="D:\\study information\\Interesting Programmes\\python\\Qzone-Related\\phantomjs.exe")
driver.maximize_window()
driver.implicitly_wait(30)    #设置隐式等待时长为30秒
#登录QQ空间
def get_content(file_path,qq):
    fwrite=open(file_path,'w')
    url='http://user.qzone.qq.com/'+qq+'/311'    #说说URL
    driver.get(url)
    time.sleep(random.randint(5,7))   #线程休眠指定随机时间 避免反爬虫
    try:
        driver.find_element_by_id('login_div')    #判断是否需要登录
        login = True
    except:
        login = False
    if login == True:    #若需要登录，则利用selenium模拟登录
        driver.switch_to.frame('login_frame')   #跳转至登录框架
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()#选择用户名框
        driver.find_element_by_id('u').send_keys('QQ号')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('QQ密码')
        driver.find_element_by_id('login_button').click()
        time.sleep(random.randint(5,7))   #线程休眠指定随机时间 避免反爬虫
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')  #判断是否有权限访问空间
        access = True
    except:
        access = False
    if access == True:    #有权限访问，则利用selenium获取说说信息
        driver.switch_to.frame('app_canvas_frame')    #跳转至指定框架
        detail = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')    #搜索指定标签
        for det in detail:    #将说说链接写入文件
            fwrite.write(det.get_attribute('href')+'\n')

    try:
        driver.find_element_by_link_text('下一页').click()    #判断是否存在下一页
        next = True
    except:
        next = False
    while(next == True):    #当存在下一页时，则访问下一页
        time.sleep(random.randint(5,7))    #线程休眠指定随机时间 避免反爬虫
        detail= driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')    #搜索指定标签
        for det in detail:    #将说说链接写入文件
            fwrite.write(det.get_attribute('href')+'\n')
        try:
            driver.find_element_by_link_text('下一页').click()    #判断是否存在下一页
            next = True
        except:
            next = False
    print("==========完成================")
    fwrite.close()
    driver.close()
    driver.quit()
if __name__ == '__main__':
    get_content('data/Links.txt','QQ')