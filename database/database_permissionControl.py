import psycopg2

from database.database_root import Database_root


# 系统管理员数据库连接接口
Database = "GamingPlatform"
# # Database_root = "nbuuser"
# User = "gaussdb"
# Password = "openGauss@2022"
# # 管理员权限控制
# database_gaussdb = Database_root()
# user_remembered_data = database_gaussdb.select("user_remembered")
# user_name = user_remembered_data[0][0]
# is_logged = user_remembered_data[0][3]
# if is_logged:
#     administrator_data = database_gaussdb.select("administrator_table")
#     for i in range(len(administrator_data)):
#         if user_name == administrator_data[i][0]:
#             if administrator_data[i][2] == "root":
#                 break
#             if administrator_data[i][2] == "music":
#                 User = "AdministratorMusic"
#                 Password = "AdministratorMusic@2022"
#                 break
#             if administrator_data[i][2] == "game":
#                 User = "AdministratorGame"
#                 Password = "AdministratorGame@2022"
#                 break
#             if administrator_data[i][2] == "user":
#                 User = "AdministratorUser"
#                 Password = "AdministratorUser@2022"
#                 break


# 建立连接函数：连接数据库,返回psycopg2的连接对象
def create_conn1(User, Password):
    conn = psycopg2.connect(database=Database,
                            user=User,
                            password=Password,
                            host="127.0.0.1",
                            port="5432")
    return conn


# sql语句执行函数(无返回值),argv:需要执行的sql语句
def ExecuSQL1(argv, User, Password):
    conn = create_conn1(User, Password)
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


# sql语句执行函数(有返回值),argv:需要执行的sql语句
def getData1(argv, User, Password):
    conn = create_conn1(User, Password)
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return data  # 返回数据列表
