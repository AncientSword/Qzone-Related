#encoding:UTF-8
#导入相关包
import urllib.request
url = "http://www.baidu.com"    #URL
data = urllib.request.urlopen(url).read()    #获取页面源码
data = data.decode('UTF-8')    #解码
print(data)