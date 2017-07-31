# -*- coding: utf-8 -*-
#导入相关包
import requests
import json
url = 'http://www.toutiao.com/api/pc/focus/'    #今日头条URL
webdata = requests.get(url).text    #获取页面源文件
data = json.loads(webdata)   #js加载数据
news = data['data']['pc_feed_focus']    
for n in news:    # 提取出标题和链接信息并输出
  title = n['title']    
  img_url = n['image_url']    
  url = n['media_url']    
  print(url,title,img_url)
  