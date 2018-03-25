import time
#from pyquery import PyQuery as pq
import mysqlHelper
import requests
import json
import re


class movie:
    def __init__(self, url, name, downUrl,desc):
        self.url = url
        self.name = name
        self.downUrl = downUrl
        self.desc = desc

def setValue(strs,begin,end):
    for i in range(begin,end):
        pattern = re.compile(r"《(.*)》")
        name = pattern.findall(strs[i])[0]
        try:
            if nameList.index(name)>-1:
                break
        except ValueError:
            # 正则匹配获取页面地址
            pattern = re.compile(r"href='(.*)'")   # 查找href链接地址
            url = pattern.findall(strs[i])[0]
            one = getMovieNameAndDownUrl(url)
            mysqlHelper.ExecuteSql('insert into movie (url,`name`,`desc`,downurl) values ("%s","%s","%s","%s")' % (
                            one.url,one.name,one.desc,one.downUrl), connection)
        
def getMovieNameAndDownUrl(url):
    r = requests.get(movieUrl + url, headers=headers)
    if r.status_code == 200:
        r.encoding = 'gb2312'
        html = r.text  # 页面代码
        thisOne=movie(url,'','','') #初始化对象
        # 正则匹配获取页面地址
        pattern = re.compile(r"《(.*)》")   # 查找片名
        thisOne.name = pattern.findall(html)[0]
        #pattern = re.compile("片(\s)*名\s(.*)</p>")   # 查找描述
        #thisOne.desc = pattern.findall(html)[0]
        pattern = re.compile(r"bgcolor=\"#fdfddf\"><a href=\"(.*)\"")   # 查找下载地址
        downUrls = pattern.findall(html)
        for downUrl in downUrls:
            thisOne.downUrl+=('zhfdownurl'+downUrl)
        return thisOne
def getNewMovie():
    # 获取主页新电影,必看热片
    r = requests.get(movieUrl, headers=headers)
    # 找到此界面,则继续操作
    if r.status_code == 200:
        r.encoding = 'gb2312'
        html = r.text  # 页面代码
        #获取所有a标签
        pattern=re.compile(r"<a href='.*' title=\".*\">")
        results=pattern.findall(html)
        #若有存在的,则调出该循环,进入下一个循环
        setValue(results,0,15)
        setValue(results,15,30)
def getNameList():
    nameDb=mysqlHelper.GetDb("select name from movie",2,None,connection)
    for n in nameDb:
        nameList.append(n[0])
global headers, connection, movieUrl,nameList
connection = {'host': 'localhost',
              'port': 3306,
              'user': 'root',
              'password': 'root',
              'database': 'movie',
              'charset': 'utf8mb4'}
movieUrl = "https://www.dy2018.com"
nameList=[]
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

if __name__ == '__main__':
    getNameList()
    getNewMovie()