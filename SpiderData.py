#encoding:UTF-8

import urllib
from urllib import request
import xlwt

class SpiderData(object):
    def __init__(self):
        pass

    def getList(self,url):
        request = urllib.request.urlopen(url)
        data = request.read()
        data = data.decode('UTF-8')
        return data
