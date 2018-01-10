import time
from pyquery import PyQuery as pq
import mysqlHelper
import requests
import json
import re
import sys


def GetLineInfo(lineId):
    r = requests.get(busUrl, headers=headers)
    if r.status_code == 200:
        doc = pq(r.text)
        data = {
            '__VIEWSTATE': doc('#__VIEWSTATE').val(),
            '__VIEWSTATEGENERATOR': doc('#__VIEWSTATEGENERATOR').val(),
            '__EVENTVALIDATION': doc('#__EVENTVALIDATION').val(),
            'ctl00$MainContent$LineName': lineId,
            'ctl00$MainContent$SearchLine': '搜索'
        }
        rx = requests.post(busUrl, data=data)
        if rx.status_code == 200:
            doc = pq(rx.text)
            trs = doc('#MainContent_DATA').find('tr')
            results = []
            if len(trs) > 1:
                # 有查到结果
                for tr in trs.items():
                    if len(tr.find('td')) > 0:
                        # 遍历查到的结果,去除标题
                        busId = tr.find('a').eq(0).attr('href')
                        busId = re.findall('LineGuid=(.*)&', busId)[0]
                        busLine = tr.find('a').eq(0).text()
                        overPlace = tr.find('td').eq(1).text()
                        results.append((busId, busLine, overPlace))
                return results


def GetLineStop(lineId):
    r = requests.get(busUrl + "&LineGuid=" + lineId, headers=headers)
    if r.status_code == 200:
        doc = pq(r.text)
        trs = doc('#MainContent_DATA').find('tr')
        results = []
        if len(trs) > 1:
            # 有查到结果
            for tr in trs.items():
                if len(tr.find('td')) > 0:
                    # 遍历查到的结果,去除标题
                    stopName = tr.find('a').eq(0).text()
                    results.append(stopName)
            return results


global headers, connection, busUrl
connection = {'host': 'localhost',
              'port': 3306,
              'user': 'root',
              'password': 'root',
              'database': 'bus',
              'charset': 'utf8mb4'}
busUrl = "http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
# #控制台程序
if __name__ == '__main__':
	line = input("请输入线路号:")
	while line!='exit':
		result=GetLineInfo(line)
		i=1
		for item in result:#[0][0]=>id
			print('%d. 线路:%s  终点站:%s' % (i,item[1],item[2]))
			i=i+1
		line= input("请选择需要记录的序列号:")
		#判断是否输入的是数字 不是数字则提示

		#记录值
		busId=str(result[int(line)-1][0])
		busLine=result[int(line)-1][1]
		overPlace=result[int(line)-1][2]
		#显示站点
		stops=GetLineStop(busId)
		i=1
		for stop in stops:
			 print('%d. 站点:%s' % (i,stop))
			 i=i+1
		stopPlace=[]
		line=input("请输入要记录的站点的序号,按-1取消输入:")
		while line!='-1':
			#判断是否输入的是数字
			stopPlace.append(stops[int(line)])
			print('已经记录%s' % (stops[int(line)]))
			line=input("请输入要记录的站点的序号,按-1取消输入:")
		#查询该车辆是否有记录 无则添加
		busInfo=mysqlHelper.GetDb('select * from businfo where guid="%s"' % (busId),1,None,connection)
		if busInfo==None:
			mysqlHelper.ExecuteSql('insert into busInfo (guid,name,arriveplace) values ("%s","%s","%s")' % (busId,busLine,overPlace),connection)
		#查询该车辆是否有记录位置  有则修改后保存
		busarriverecord=mysqlHelper.GetDb('select * from recordPlace where guid="%s"' % (busId),1,None,connection)
		if busarriverecord==None:
			mysqlHelper.ExecuteSql('insert into recordPlace (needrecordplace,guid) values ("%s","%s")' % (','.join(stopPlace),busId),connection)
		else:
			#判断是否已经记录过此站点,若记录过,则不再记录
			stopPlace=busarriverecord[1]+','+','.join(stopPlace)
			mysqlHelper.ExecuteSql('update recordPlace set needrecordplace="%s" where guid="%s"' % (stopPlace,busId),connection)
		line= input("请输入线路号,输入exit退出")

# 控制台程序
# if __name__ == '__main__':
#     paras = sys.argv[1].split('&')  # 用&分隔参数
#     if paras[0] == "GetLine":
#         result = GetLineInfo(paras[1])
#         i = 1
#         for item in result:  # [0][0]=>id
#             print('%d. 线路:%s  终点站:%s' % (i, item[1], item[2]))
#             i = i + 1
#     elif paras[0] == "GetArrive":
#         # 记录值
#         busId = paras[1]  # guid
#         busLine = paras[2]  # 线路号
#         overPlace = paras[3]  # 终点站
#         # 显示站点
#         stops = GetLineStop(busId)
#         i = 1
#         for stop in stops:
#             print('%d. 站点:%s' % (i, stop))
#             i = i + 1
#     elif paras[0] == "GetPlace":
#         busId = paras[1]  # guid
#         busLine = paras[2]  # 线路号
#         overPlace = paras[3]  # 终点站
#         stopPlace = paras[4]  # 需要记录的站点
#         busInfo = mysqlHelper.GetDb(
#             'select * from businfo where guid="%s"' % (busId), 1, None, connection)
#         if busInfo == None:
#             mysqlHelper.ExecuteSql('insert into busInfo (guid,name,arriveplace) values ("%s","%s","%s")' % (
#                 busId, busLine, overPlace), connection)
#         # 查询该车辆是否有记录位置  有则修改后保存
#         busarriverecord = mysqlHelper.GetDb(
#             'select * from recordPlace where guid="%s"' % (busId), 1, None, connection)
#         if busarriverecord == None:
#             mysqlHelper.ExecuteSql('insert into recordPlace (needrecordplace,guid) values ("%s","%s")' % (
#                 stopPlace, busId), connection)
#         else:
#             # 判断是否已经记录过此站点,若记录过,则不再记录
#             stopPlace = busarriverecord[1] + ',' + stopPlace
#             mysqlHelper.ExecuteSql('update recordPlace set needrecordplace="%s" where guid="%s"' % (
#                 stopPlace, busId), connection)
