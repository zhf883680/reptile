#http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4&LineGuid=BD31B6B6-2455-4655-AD1C-EC7CDF8E6780&LineInfo=615(%E6%9C%A8%E6%B8%8E%E5%85%AC%E4%BA%A4%E6%8D%A2%E4%B9%98%E6%9E%A2%E7%BA%BD%E7%AB%99)
#http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4&LineGuid=BD31B6B6-2455-4655-AD1C-EC7CDF8E6780    615 去木渎
#http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4&LineGuid=D2788C6E-B49C-4B35-8B12-C78C920E061F			615 去胥香园		
#http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4&LineGuid=A7193AC1-74DF-4770-8208-C5C64FDECC62			668 去木渎
#DE2233A8-EC6A-4DD9-B799-62A7FD356777去石庄

import time
from pyquery import PyQuery as pq
import mysqlHelper
import requests
import json

def insertBus(LineGuid):
		#获取此guid对应的方向站台
		realurl=busUrl+LineGuid
		r = requests.get(realurl, headers=headers)
		if r.status_code == 200:
			doc = pq(r.text)
			#所有tr
			trs=doc('#MainContent_DATA').find('tr')
			#遍历tr 根据需要的td来显示
			for tr in trs.items():
					if tr.find('td')!=None and tr.find('td').eq(0)!=None and tr.find('td').eq(0).find('a')!=None and tr.find('td').eq(0).find('a').eq(0).text() in needName:
							#记录此时是否有车辆
							print(tr.find('td').eq(3).text())

global headers, connection, busUrl,needName
connection = {'host': 'localhost',
              'port': 3306,
              'user': 'root',
              'password': 'root',
              'database': 'bus',
              'charset':'utf8mb4'}
busUrl = "http://www.szjt.gov.cn/BusQuery/APTSLine.aspx?cid=175ecd8d-c39d-4116-83ff-109b946d7cb4&LineGuid="
needName={'吉祥小区东','张巷桥','木渎公交换乘枢纽站','中华园大酒店','南浜'}
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

if __name__ == '__main__':
		insertBus('BD31B6B6-2455-4655-AD1C-EC7CDF8E6780')