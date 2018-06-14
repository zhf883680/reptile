# reptile
python 爬虫
### jd.py
爬取京东的相关数据的一些方法  
后续分类增加 以jd-开头
#### jd-getPrice.py
根据数据库中数据获取价格,保存  ,并且若低于设定价格,则自动通过钉钉群组机器人发送消息 请自行获取机器人accesstokend
### mysqlHelper.py
处理mysql数据库的一些方法
### busTime.py  
公交站点到达时间的记录  
### wechat.py
微信公众号的一些调用
### GetBookList.py
获取书本表面信息,深一层未获取   
P.S. 需要自行登录readfree.me  
p.s. 数据库连接字符串未更改
### GetBookListByThread.py
通过多线程获取书本表面信息,深一层未获取  
P.S. 需要自行登录readfree.me
### dytt8
电影天堂爬虫,目前只爬了首页的新片和热片,爬取了对应的下载地址,名称,url 
当有重复的则会退出该列,转到另一列
后续会增加对所有的经典电影的爬虫
### 后续补充
