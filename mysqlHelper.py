import pymysql

# escape_string


def ExecuteSql(sql,connection):
    db = pymysql.connect(**connection)
    cursor = db.cursor()
    # SQL 插入语句
        # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('success')
    # 关闭数据库连接
    db.close()

#执行多条操作
def ExecuteManySql(sql, values,connection):
    db = pymysql.connect(**connection)
    cursor = db.cursor()
    # SQL 插入语句
    # try:
    # 执行sql语句
    cursor.executemany(sql, values)
    # 提交到数据库执行
    db.commit()
    print('success')
    db.close()


#selectType==1 查询单条
def GetDb(sql,selectType,pars,connection):
    db = pymysql.connect(**connection)
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

if __name__ == '__main__':
    connection={'host':'localhost',
          'port':3306,
          'user':'root',
          'password':'root',
          'database':'jd'}
    shopInfo = GetDb(
        'select * from shop where id=%s', 1, '123', connection)
    print(shopInfo)