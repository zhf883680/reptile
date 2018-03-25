import requests
import json
import mysqlHelper
import time
import re
import sys
from pyquery import PyQuery as pq


def getPrice(skuIds):
    # 需要获取的Id集合
    skuIdString = ''
    for x in skuIds:
        skuIdString += ("J_" + x + ",")
    skuIdString = skuIdString[:-1]
    realurl = priceUrl + skuIdString
    r = requests.get(realurl, headers=headers)
    jd = json.loads(r.text)
    # 获取价格列表
    return jd


def getName(skuId):
    realurl = shopUrl + skuId
    r = requests.get(realurl, headers=headers)
    if r.text == "{}":
        # 非自营产品name
        r = requests.get(shopChinaUrl + skuId + '.html', headers=headers)
        if r.status_code == 200:
            doc = pq(r.text)
            return doc('.sku-name').text()
        else:
            return "获取失败"
    else:
        jd = json.loads(r.text)
        try:
            return jd['accessories']['data']['wName']
        except:
            r = requests.get(shopChinaUrl + skuId + '.html', headers=headers)
            if r.status_code == 200:
                doc = pq(r.text)
                return doc('.sku-name').text()
            else:
                return "获取失败"


# 全局变量
global priceUrl, shopUrl, headers, shopChinaUrl, connection
connection = {'host': 'localhost',
              'port': 3306,
              'user': 'root',
              'password': 'root',
              'database': 'jd',
              'charset':'utf8mb4'}
shopChinaUrl = "https://item.jd.com/"
priceUrl = "https://p.3.cn/prices/mgets?skuIds="
# cat 随意3个值 无影响
shopUrl = "https://c.3.cn/recommend?cat=9987%2C653%2C655&methods=accessories&sku="
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

if __name__ == '__main__':
    
    print("链接格式:https://item.jd.com/15806736305.html")
    str = input("请输入京东商品链接：")
    while str!="exit":
    #str="https://item.jd.com/15806736305.html"
        id = re.findall('([1-9]\d*)',str)
        if len(id)<=0:
            print("请输入正确的带数字的链接地址")
            str = input("请输入京东商品链接：")
        else:
            id=id[0]
            dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            shopInfo = mysqlHelper.GetDb(
                'select * from shop where id=%s', 1, id, connection)
            if shopInfo == None:
                mysqlHelper.ExecuteSql('insert into shop (id,name,isSelf,businessman) values("%s","%s","%s","%s")' % (
                    id, getName(id), 1, ''), connection)
                mysqlHelper.ExecuteSql('insert into price (shopId,price,addtime) values("%s","%s","%s")' % (
                    id, getPrice([id])[0]['p'], dt), connection)
            else:
                print('商品已经存在了')
            print("商品名:%s,价格%s" % (getName(id), getPrice([id])[0]['p']))
        #是否需要加入此商品至通知列表
        phone = input("是否加入此商品到通知列表,若需要, 请输入手机号,若不需要,请输入no:")
        if phone!="no":
            #加入到通知列表
            str = input("请输入通知价格,当低于此价格时,会进行通知:")
            mysqlHelper.ExecuteSql('insert into userlist (shopId,minprice,phone,addtime) values("%s","%s","%s","%s")' % (
                    id, str, phone,"2017-12-31"), connection)
            str = input("请输入京东商品链接：")
        else:
            str = input("请输入京东商品链接：")
        

# 获取id
# 写入数据库
# 定期查询价格
# 发送到微信公众号
