import requests
import json
import time
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
        return jd['accessories']['data']['wName']


# 全局变量
global priceUrl, shopUrl, headers, shopChinaUrl
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
    id = ""
    print("商品名:%s,价格%s" % (getName(id), getPrice([id])[0]['p']))

#获取id
#写入数据库
# 定期查询价格
# 发送到微信公众号

# r = requests.get(url, headers=headers)
# print(r.text)
# 获取必要的一些参数
# J-follow-shop 多个相同  data-vid="1000015003" 商户id
#
# https://c0.3.cn/stock?skuId=1004610&area=1_72_2799_0&venderId=1000004349&cat=670,686,689&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=1510707152965956130682&pdpin=&detailedAdd=null&callback=jQuery4726459
# https://c0.3.cn/stock?skuId=3378484&area=1_72_4137_0&venderId=1000015269&cat=670,686,689&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=1510707152965956130682&pdpin=&detailedAdd=null&callback=jQuery3720438
# https://c0.3.cn/stock?skuId=5712532&area=1_72_4137_0&venderId=1000000326&cat=670,671,2694&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=1510707152965956130682&pdpin=&detailedAdd=null&callback=jQuery346735
# 获取价格
# skuId='1981018569'#商品号
# #J_1,J_2  可一次查询多个
# realurl=priceUrl+'J_'+skuId
# r = requests.get(realurl, headers=headers)
# jd = json.loads(r.text)
# print(jd[0]['p'])#输出价格
# #获取物品名 好像只能京东自营商品
# realurl=shopUrl+skuId
# r = requests.get(realurl, headers=headers)
# jd = json.loads(r.text)
# {
# "accessories": {
# "status": 200,
# "data": {
# "wName": "罗技（Logitech）G610 Cherry轴全尺寸背光机械游戏键盘 机械键盘 红轴 吃鸡键盘 绝地求生",
# "wid": 3378484,
# "imageUrl": "jfs/t3268/132/227094941/162137/a1ffa50f/57abe0a0Ne962f9b2.jpg",
# "chBrand": "罗技",
# "model": "G610 ORION RED 背光机械游戏键盘",
# "list": [],
# "wMeprice": 900,
# "wMaprice": 499
# }
# }
# }
# print(jd['accessories']['data']['wName'])#输出物品名
