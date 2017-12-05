#encoding:UTF-8

"""
需求：
重庆各区域近半年房价对比
每个区域5-8个标的
"""

"""
分析：
参考数据链家
参考安居客数据
"""

"""
设计思路：
抓去数据存入Excel中
"""

import urllib
from urllib import request
import re
import xlwt
import json

url = 'https://cq.fang.lianjia.com/loupan/jiangbei/'
request = urllib.request.urlopen(url)
data = request.read()
data = data.decode('UTF-8')
print(data)
# a = re.compile('<a.*?data-el="xinfang">(.*?)</a>')
a = re.compile('h2>[^<]+<[^>]+"xinfang">([^<]+)')
data1 = a.findall(data)
b = re.compile('<span.*?class="num">(.*?)</span>')
data2 = b.findall(data)
wbk = xlwt.Workbook()
sheet1 = wbk.add_sheet('sheet 1')
for i,x in enumerate(data1):
    sheet1.write(i+1,0, x)

for j,y in enumerate(data2):
    sheet1.write(j+1,1,y)

wbk.save('test.xls')

c = re.compile('<div[^>]*class="page-box.*?house-lst-page-box"[^>]*?page-data=(.*?)>')
data3 = c.findall(data)
if len(data3)>0:
    d = re.compile('".*?":(\d)')
    s = data3[0]
    data4 = d.findall(s)
    print(data4[0])
    print(type(data4))




