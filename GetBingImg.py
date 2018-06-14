import requests
import urllib  
from bs4 import BeautifulSoup
import os
import time
import logging

url = "https://bing.ioliu.cn/?p="
downUrl="https://bing.ioliu.cn"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                    filename='d:\\bingImgs\\log.txt', 
                    filemode='a', 
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s') 

    pageIndex=2
    i=1
    isFirst=1
    while i!=pageIndex:
        r = requests.get(url+str(i), headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            divs=soup.find_all('div',class_="card")
            # if isFirst==1:
            #     pageStr=soup.find_all('div',class_="page")[0].span.string
            #     pageIndex=int(pageStr[pageStr.find('/')+2:len(pageStr)])#页数
            #     isFirst=isFirst+1
            #print(imgs)
            for div in divs:
                #图片与描述的div
                #if div.get('class')[0]=='card':
                    #print(downUrl+div.div['options'].find_all('a')[1].get('href'))#图片下载链接
                    #print(div.div.h3)#图片描述
                    #print(div.div.p.em)#图片时间
                savePath="d:\\bingImgs\\"+div.div.p.em.string+'.jpg'
                if os.path.exists(savePath)==False:
                    logging.info('开始下载图片'+div.div.p.em.string+'.jpg')
                    r = requests.get(downUrl+div.find_all('div')[1].find_all('a')[1].get('href')) 
                    with open(savePath, "wb") as code:
                        code.write(r.content)
                    logging.info('图片'+div.div.p.em.string+'.jpg 下载完成')                    
        time.sleep(4)
        i=i+1
        logging.info('开始第'+str(i)+'页图片下载')    
                

         