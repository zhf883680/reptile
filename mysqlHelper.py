import pymysql

# escape_string


def ExecuteSql(sql):
    db = pymysql.connect("localhost", "root", "root",
                         "readfree", charset='utf8')
    cursor = db.cursor()
    # SQL 插入语句
        # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('success')
    # 关闭数据库连接
    db.close()

#selectType==1 查询单条
def GetDb(sql,selectType,pars):
    db = pymysql.connect("localhost", "root", "root",
                         "readfree", charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql,pars)
    # 查询数据
    if selectType==1:
        result=cursor.fetchone()
    else:
        result = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return result


def ExecuteManySql(sql, values):
    db = pymysql.connect("localhost", "root", "root",
                         "readfree", charset='utf8')
    cursor = db.cursor()
    # SQL 插入语句
    # try:
    # 执行sql语句
    cursor.executemany(sql, values)
    # 提交到数据库执行
    db.commit()
    print('success')
    db.close()

# sql = """INSERT INTO bookinfo(bookName,
#             bookimg, downurl, writer)
#             VALUES ('Ma3333c', 'Mohan', '321', 'M')"""


# insertIntoBookInfo(sql)
#sql = "select * from getpage order by id desc limit 0,1"
#valued = GetDb(sql,1)
#print(valued)
