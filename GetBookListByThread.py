# from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as pq
import requests
import mysqlHelper
import threading
import time


class mythread(threading.Thread):
    def __init__(self, threadIndex, pageIndex, pageAll):
        threading.Thread.__init__(self)
        self.pageIndex = pageIndex
        self.pageAll = pageAll
        self.threadIndex = threadIndex

    def run(self):
        for i in range(self.pageIndex, self.pageIndex - pageCount, -1):
            if i > -1:
                GetbookInfo(str(i))
                InsertPage(str(i), str(self.pageAll))
                print(self.threadIndex)
        # lock.acquire()      #上锁，acquire()和release()之间的语句一次只能有一个线程进入，其余线程在acquire()处等待
        # GetbookInfo(str(pageIndex))
        # InsertPage(str(pageIndex), str(pageAll))
        # lock.release()      #解锁


lock = threading.RLock()  # 创建 可重入锁


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
    #fo = open("result.txt", "a",encoding='utf8')
    # 遍历页面中的内容
    for book in books.items():
        # 判断当前页的数据是否已经存在,若存在,则跳过此项 并直接前一页
        img = book.find('img').attr('src')
        lock.acquire()
        getdata = mysqlHelper.GetDb(
            "select * from bookinfo where bookimg=%s", 1, img)
        lock.release()
        if getdata == None:
            linka = book.find('.pjax').eq(1)
            name = linka.text()
        # fo.write("成功找到书籍%s\n" %(name))
            writer = book.find('.z-link-search').text()
            mark = book.find('.badge-success').text()
            bookurl = url + linka.attr('href')
            bookInfo = (name, img, bookurl, writer, mark)
            bookInfos.append(bookInfo)
        else:
                #fo.write("书籍%s已经存在了\n" %(getdata[1]))
            continue

    # fo.close()
    lock.acquire()
    mysqlHelper.ExecuteManySql(sql, bookInfos)
    lock.release()
# 插入页数记录


def InsertPage(begin, end):
    pageSql = "insert into getpage(pageAll,pageIndex) values (" + \
        end + "," + begin + ")"
    lock.acquire()
    mysqlHelper.ExecuteSql(pageSql)
    lock.release()


# requests获取界面
global header
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
global pageAll
pageAll = d('.hidden-phone:last').children().eq(0).text()
pageAllInt = int(pageAll)#总页数
# 获取上次访问的页数 判断页数差  根据现在的末页 减去页数差 +n 从此页开始
result = mysqlHelper.GetDb(
    "select min(pageindex) from getpage", 1, None)
#"select * from getpage order by pageindex limit 0,1", 1, None)
if result == None:
    pageBegin = pageAllInt
   # pageEnd = pageAllInt
else:
    pageBegin = result[2]
    pageEnd = result[1]
    pageBegin = pageBegin + pageAllInt - pageEnd
global pageCount
pageCount = int(pageBegin / 10 + 1)
# l=mythread(pageBegin-200,pageAllInt)
# l.start()
# l.join()
l = []
for i in range(10):
    # 创建 10 个线程，并把他们放到一个列表中
    l.append(mythread(i, pageBegin - i * pageCount, pageAllInt))
for i in l:
    i.start()
for i in l:
    i.join()
# 删除重复数据
# select * from getpage where pageindex in (select  pageindex  from  getpage  group  by  pageindex  having  count(pageindex) > 1)
# delete from bookinfo where bookimg  in (select  bookimg  from bookinfo  group  by  bookimg   having  count(bookimg) > 1) and id not in (select min(id) from  bookinfo  group by bookimg  having count(bookimg )>1)
# select distinct bookimg from bookinfo
# select  *  from getpage  group  by  pageindex   having  count(pageindex) = 1;
