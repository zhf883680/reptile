# -*- coding:utf-8 -*-
import time
# import mysqlHelper
import requests
import json
import re
import codecs

def getNewBookList(typeName,url,page):
    # 获取主页新电影,必看热片
    fo = open("book.csv", "a+",encoding='utf-8')
    try:
        r = requests.get(url+ str(page), headers=headers)
       
        # 找到此界面,则继续操作
        if r.status_code == 200:
            r.encoding = 'utf8'
            html = r.text  # 页面代码
            #获取所有a标签
            pattern=re.compile(r"<a href=\"http://www.zxcs.me/post/([0-9]+)\">(.*)</a>")
            results=pattern.findall(html)
            for result in results[:15]:
                id=result[0]
                name=result[1]
                #获取分数
                scoreList=getScore(id)
                if(int(scoreList[0])>int(scoreList[4])):
                    fo.write("%s,%s,%s,%s,%s\n" % (typeName,name,scoreList[0],scoreList[4],bookInfo+id))
                    #print("小说名:%s,仙草:%s,毒草:%s" % (name,scoreList[0],scoreList[4]))
                time.sleep(0.3)
    except:
        print("%s的第%s页有问题"%(typeName,page))
    fo.close()

def getScore(id):
    r = requests.get(scoreUrl+ id, headers=headers)
    if r.status_code == 200:
        return r.text.split(',')


global headers, connection, bookUrl
# 23 都市 25 仙侠 26 玄幻 27 科幻 29 游戏
needList=[[23,"都市"],[25,"仙侠"],[26,"玄幻"],[27,"科幻"],[29,"游戏"]]
#needList=[[23,"都市"]]
bookUrl = "http://www.zxcs.me/sort/26/page/"
bookInfo="http://www.zxcs.me/post/"
scoreUrl = "http://www.zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing_action.php?action=show&id="
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
}

if __name__ == '__main__':
    for typeii in needList:
        for i in range(20,60):
            getNewBookList(typeii[1],"http://www.zxcs.me/sort/%s/page/"%(typeii[0]),i)
    