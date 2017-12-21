import time
from pyquery import PyQuery as pq
import mysqlHelper
import requests
import json


def getLineInfo(lineId):
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
		rx = response = requests.post(busUrl, data=data)
		print(rx.text)


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


if __name__ == '__main__':
	line = input("请输入线路号:")
    while line!='exit':
	# http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4	
		print('当前站点的终点为')
		line= input("请选择线路终点:")
		if line==1:
			# 记录值
			print("当前记录的站点为:")
		else:
			print("当前记录的站点为:")
		line=("请输入要记录的站点的序号:")

		line= input("请输入线路号:")
