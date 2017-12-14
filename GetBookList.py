# from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as pq
import requests
import mysqlHelper


def GetbookInfo(pageIndex):
    # 获取页面
    url = 'http://readfree.me/?page=' + pageIndex
    r = requests.get(url, headers=header)
    d = pq(r.text)
    # sql语句
    #sql = "INSERT INTO bookinfo(bookName,bookimg, downurl, writer,mark) values(%s,%s,%s,%s,%s)"
    sql = "INSERT INTO bookinfo(bookName,bookimg, downurl, writer,mark) values(%s,%s,%s,%s,%s)"
    books = d('.book-item')
    bookInfos = []
    fo = open("result.txt", "a",encoding='utf8')
    # 遍历页面中的内容
    for book in books.items():
        # 判断当前页的数据是否已经存在,若存在,则跳过此项 并直接前一页
        img = book.find('img').attr('src')
        getdata = mysqlHelper.GetDb(
            "select * from bookinfo where bookimg=%s", 1, img)
        if getdata == None:
            linka = book.find('.pjax').eq(1)
            name = linka.text()
            fo.write("成功找到书籍%s\n" %(name))
            writer = book.find('.z-link-search').text()
            mark = book.find('.badge-success').text()
            bookurl = url + linka.attr('href')
            bookInfo = (name, img, bookurl, writer, mark)
            bookInfos.append(bookInfo)
        else:
            fo.write("书籍%s已经存在了\n" %(getdata[1]))
            continue
    
    fo.close()
    mysqlHelper.ExecuteManySql(sql, bookInfos)
# 插入页数记录


def InsertPage(begin, end):
    pageSql = "insert into getpage(pageAll,pageIndex) values (" + \
        end + "," + begin + ")"
    mysqlHelper.ExecuteSql(pageSql)


# requests获取界面
url = 'http://readfree.me'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': '',#自行注册账号登陆后获取cookie
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
r = requests.get(url, headers=header)
d = pq(r.text)
# 获取总页数
pageAll = d('.hidden-phone:last').children().eq(0).text()
#InsertPage('0', pageAll)
pageAllInt = int(pageAll)
# 获取上次访问的页数 判断页数差  根据现在的末页 减去页数差 +n 从此页开始
result = mysqlHelper.GetDb(
    "select * from getpage order by id desc limit 0,1", 1, None)
pageBegin = result[2]
pageEnd = result[1]
pageBegin = pageBegin + pageAllInt - pageEnd
# 从最后一页开始遍历
for i in range(pageBegin, pageBegin - 20, -1):
    GetbookInfo(str(i))
    InsertPage(str(i), str(pageAll))
# 获取书籍信息
