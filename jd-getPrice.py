import jd
import mysqlHelper
import time

if __name__ == '__main__':
	shopInfo = mysqlHelper.GetDb(
		'select id from shop where 1=1', 1, None, jd.connection)
	if shopInfo!=None:
		ids=[]
		#获取商品Id合集
		for s in shopInfo:
			ids.append(str(s))
	#获取价格
	prices=jd.getPrice(ids)
	#时间(datetime类型)
	dt = time.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"%Y-%m-%d %H:%M:%S")
	#多条插入时,使用的值
	pars=[]
	for price in prices:
		par=(int(price['id'][2:]),float(price['p']),dt)
		pars.append(par)
	#插入数据库
	mysqlHelper.ExecuteManySql('insert into price (shopId,price,addtime) values("%s","%s",%s)',pars, jd.connection)