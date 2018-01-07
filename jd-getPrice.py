import jd
import mysqlHelper
import time
import requests

if __name__ == '__main__':
    shopInfo = mysqlHelper.GetDb(
        'select id from shop where 1=1', 0, None, jd.connection)
    if shopInfo != None:
        ids = []
        # 获取商品Id合集
        for s in shopInfo:
            ids.append(str(s[0]))
            # 判断该物品的记录是否存在,不存在则增加
            shop = mysqlHelper.GetDb(
                'select name from shop where id=%s', 1, s[0], jd.connection)
            if shop == None:
                mysqlHelper.ExecuteSql('insert into shop (id,name,isSelf,businessman) values("%s","%s","%s","%s")' % (
                    id, jd.getName(id), 1, ''), jd.connection)
    # 获取价格
    prices = jd.getPrice(ids)
    # 时间(datetime类型)
    dt = time.strptime(time.strftime("%Y-%m-%d %H:%M:%S",
                                     time.localtime()), "%Y-%m-%d %H:%M:%S")
    # 多条插入时,使用的值
    pars = []
    for price in prices:
        par = (int(price['id'][2:]), float(price['p']), dt)
        pars.append(par)
    # 插入数据库
    mysqlHelper.ExecuteManySql(
        'insert into price (shopId,price,addtime) values("%s","%s",%s)', pars, jd.connection)
    # 遍历价格与通知表
    for price in prices:
        # 获取此物品的通知人
        users = mysqlHelper.GetDb(
            'select userlist.*,shop.Name from userlist left join shop on userlist.shopId=shop.Id where shopid=%s', 0, price['id'][2:], jd.connection)
        if users != None:
            for s in users:
                if float(s[3]) >= float(price['p']):
                    lastTime = time.strptime(str(s[4]), "%Y-%m-%d %H:%M:%S")
                    localtime = time.localtime(time.time())
                    if (lastTime[0] != localtime[0] or lastTime[1] != localtime[1] or lastTime[2] != localtime[2]) or (lastTime[0] == localtime[0] and lastTime[1] == localtime[1] and lastTime[2] == localtime[2] and lastTime[3]!=localtime[3]):
                        msg = {
                            "msgtype": "text",
                            "text": {
                                "content": "您关注的商品%s现在已经降低到%s元了" % (str(s[5]), str(price['p']))
                            },
                            "at": {
                                "atMobiles": [
                                    str(s[1])
                                ],
                                "isAtAll": "false"
                            }
                        }
                        rss = requests.post(
                            "https://oapi.dingtalk.com/robot/send?access_token=", json=msg)
                        # 增加发送时间
                        # dtTime = time.strftime("%H:%M:%S", time.localtime())
                        dtDay = time.strftime(
                            "%Y-%m-%d %H:%M:%S", time.localtime())
                        mysqlHelper.ExecuteSql(
                            "update userlist set addTime='%s' where id=%s" % (dtDay, s[0]), jd.connection)
                        # print(rss)
