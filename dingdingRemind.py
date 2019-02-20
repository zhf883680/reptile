import datetime
import time
import requests
import json
import io
import sys

if __name__ == '__main__':
    try:
        # 获取access_token凭证
    
         # 获取心跳包发送情况
        fo = open("D:/ServerWeb/postinfo.json", "r+")
        content = fo.read()
        fo.close()
        dingdingUsers = json.loads(content)
        res = requests.get(
                    "https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s" % (corpid, corpSecret))
        access_token = res.json()['access_token']
        for data in dingdingUsers:
            # 获取时间
            postTime = datetime.datetime.strptime(
                data['GetPostTime'], '%Y-%m-%d %H:%M:%S')
            checkTime = datetime.datetime.now()
            delta = checkTime - postTime
            # 超过5分钟 发送请求
            if delta.seconds > 300:
                # 获取打卡情况
                msg = {"userId": data['UserId'], 'workDateFrom': checkTime.strftime(
                    '%Y-%m-%d 0:0:0'), 'workDateTo': checkTime.strftime('%Y-%m-%d 23:0:0'), 'userIdList': [data['UserId']]}
                res = requests.post(
                    "https://oapi.dingtalk.com/attendance/list?access_token=%s" % (access_token), json=msg)
                workStatus = res.json()
                # 若今日只打卡了一次,且此次打卡为有效打卡  则进行提示  
                if len(workStatus['recordresult']) == 1:
                    if workStatus['recordresult'][0]['timeResult'] != "NotSigned":
                        # 发送下i奥西
                        nowTime=workStatus['recordresult'][0]['userCheckTime']/1000
                        print(time.localtime(nowTime))
                        print("\n")
                        # msg = {"msgtype": "text", "text": {"content": "您该打卡拉"},
                        #     "at": {"atMobiles": [data['Phone']], "isAtAll": "false"}}
                        # rss = requests.post(
                        #     "https://oapi.dingtalk.com/robot/send?access_token=d81a9b3ccd8c49ca9cfa8ae5c0504243cbe8c0468840e948bc60f857381d6e6d", json=msg)
    except OSError as err:
        fp = open("D:/ServerWeb/error.txt",'a')
        fp.writelines(format(err)+"\n")
        fp.close()
        sys.exit()
    else:
        sys.exit()
