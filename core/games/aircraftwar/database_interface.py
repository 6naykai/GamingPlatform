import psycopg2

# 系统管理员数据库连接接口
Database = "GamingPlatform"
# Database_root = "nbuuser"
User = "gaussdb"
Password = "openGauss@2022"


# 建立连接函数：连接数据库,返回psycopg2的连接对象
def create_conn():
    conn = psycopg2.connect(database=Database,
                            user=User,
                            password=Password,
                            host="127.0.0.1",
                            port="5432")
    return conn


# sql语句执行函数(无返回值),argv:需要执行的sql语句
def ExecuSQL(argv):
    conn = create_conn()
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


# sql语句执行函数(有返回值),argv:需要执行的sql语句
def getData(argv):
    conn = create_conn()
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return data  # 返回数据列表
