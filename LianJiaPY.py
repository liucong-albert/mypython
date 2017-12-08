#encoding:UTF-8

import re
import xlwt
import SpiderData
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


class LianJiaPy(object):
    page = 1
    def __init__(self):
        pass
    def __findHouseName__(self,data):
        a = re.compile('h2>[^<]+<[^>]+"xinfang">([^<]+)')
        data1 = a.findall(data)
        return data1

    def __findHousePrice__(self,data):
        b = re.compile('<span.*?class="num">(.*?)</span>')
        data2 = b.findall(data)
        return data2

    def __saveHouseDataInExcel__(self,data):
        names = self.__findHouseName__(data)
        prices = self.__findHousePrice__(data)
        if int(self.page)==1:
            wbk = xlwt.Workbook()
            sheet1 = wbk.add_sheet('sheet 1')
            for i, x in enumerate(names):
                sheet1.write(i + 1, 0, x)
            for j, y in enumerate(prices):
                if not y.strip():
                    sheet1.write(j + 1, 1, '暂无价格')
                else:
                    sheet1.write(j + 1, 1, y)
            wbk.save('链家数据.xls')
        else:
            rexcel = open_workbook("链家数据.xls")  # 用wlrd提供的方法读取一个excel文件
            rows1 = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
            excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
            table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
            for i, x in enumerate(names):
                table.write(i + 1+rows1, 0, x)
            for j, y in enumerate(prices):
                if not y.strip():
                    table.write(j + 1+rows1, 1, '暂无价格')
                else:
                    table.write(j + 1+rows1, 1, y)
            excel.save("链家数据.xls")

    def __getDataLen(self,data):
        c = re.compile('<div[^>]*class="page-box.*?house-lst-page-box"[^>]*?page-data=(.*?)>')
        pageData = c.findall(data)
        if len(pageData)<1:
            return
        d = re.compile('".*?":(\d)')
        pageCount = d.findall(pageData[0])
        totalPage = pageCount[0]
        if int(totalPage) <= int(self.page):
            print('抓取完成！')
            return
        else:
            print('继续抓去：'+ str(self.page))
            self.page += 1
            self.startGetData()

    def startGetData(self):
        url = 'https://cq.fang.lianjia.com/loupan/jiangbei/pg'+str(self.page)
        spiderData = SpiderData.SpiderData()
        data = spiderData.getList(url)
        self.__saveHouseDataInExcel__(data)
        self.__getDataLen(data)
