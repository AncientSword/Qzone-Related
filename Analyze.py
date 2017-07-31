# -*- coding: utf-8 -*-
#导入相关包
import csv
from collections import Counter
#统计互动情况
def interactionCount(str,myname,interaction):
    myname=myname
    begin=str.find(' 回复 ')  #查找‘ 回复 ’
    if(begin!=-1):  #若存在‘ 回复 ’ 寻找‘  ： ’
        end=str.find(' : ')
        if(end!=-1):    #若存在‘  ： ’ 则满足要求，计数
            interaction[(str[0:begin],str[begin+4:end])] += 1
    else:   #若不存在‘ 回复 ’ 寻找‘  ： ’
        begin=str.find(' : ')
        if(begin!=-1):  #若存在‘  ： ’ 则满足要求，计数
            interaction[(str[0:begin],myname)] += 1
#保存在文件中
def writeToFile(file_path,interaction):
    csvfile = open(file_path,'w',newline='')    #打开csv文件
    writer = csv.writer(csvfile)
    temp=["Source","Target","Weight"]   #稍后利用gephi进行分析，故在第一行加入列名
    writer.writerow(temp)
    for (a,b), count in interaction.items():    #将计数器中元素写入文件
        if(a!=b):   #不考虑自互动
            temp=[]
            temp.append(a)
            temp.append(b)
            temp.append(count)
            writer.writerow(temp)
    csvfile.close()    #关闭文件
#主函数
def main():
    fread=open('data/Comments.txt','r')    #读取文件
    interaction = Counter()    #互动情况计数器
    for line in fread:
        interactionCount(line,'姓名',interaction)    #统计互动情况
    writeToFile('result/relationship.csv',interaction)    #保存在文件中

if __name__=="__main__":
    main()