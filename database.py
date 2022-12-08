import psycopg2


# # 程序用到的sql语句
# ins = "insert into students (Sno,Sname,Semail,Scredit,Ssex) values ('{}','{}','{}',{},'{}');"
# del = "delete from students where Sno='{}'"
# sel = "select * from students"
# upd = "update students set Sname='{}',Semail='{}',Scredit={},Ssex='{}' where Sno='{}';"


# 建立连接函数：连接数据库,返回psycopg2的连接对象
def create_conn():
    conn = psycopg2.connect(database="GamingPlatform",
                            user="gaussdb",
                            password="openGauss@2022",
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


# 用户平台的数据库接口类
class Database:
    def __init__(self):
        self.__ins_user = None
        self.__ins_user_remembered = None
        # self.__upd_user = None
        self.__upd_user_forbidden = None
        self.__del_user = None
        self.__del_user_remembered = None
        self.__sel_user = None
        self.__sel_user_remembered = None
        self.sql_init()

    # sql语句初始化
    def sql_init(self):
        # 用户表sql语句初始化
        self.__ins_user = "insert into user_table (user_name,user_secret,user_forbidden) values ('{}','{}','{}');"
        self.__ins_user_remembered = "insert into user_remembered (user_name,user_secret,is_remembered) values ('{}'," \
                                     "'{}','{}'); "
        self.__upd_user_forbidden = "update user_table set user_forbidden='{}' where user_name='{}';"
        self.__del_user = "delete from user_table where user_name='{}'"
        self.__del_user_remembered = "delete from user_remembered where user_name='{}'"
        self.__sel_user = "select * from user_table"
        self.__sel_user_remembered = "select * from user_remembered"

    # 插入数据函数
    def insert(self, table_name, argv):
        """
        根据table_name选取对应的表进行数据库的插入
        :param table_name: 需要插入数据的表
        :param argv: 数据列表
        :return: 无返回值
        """
        # 用户表的插入
        if table_name == "user_table":
            user_name = argv[0]
            user_secret = argv[1]
            user_forbidden = argv[2]
            sql = self.__ins_user.format(user_name, user_secret, user_forbidden)
            ExecuSQL(sql)
        # 记住用户表的插入
        elif table_name == "user_remembered":
            user_name = argv[0]
            user_secret = argv[1]
            is_remembered = argv[2]
            sql = self.__ins_user_remembered.format(user_name, user_secret, is_remembered)
            ExecuSQL(sql)
        pass

    # 删除数据函数
    def delete(self, table_name, argv):
        """
        根据table_name选取对应的表进行数据库的删除
        :param table_name: 需要删除数据的表
        :param argv: 数据列表
        :return: 无返回值
        """
        # 用户表的删除
        if table_name == "user_table":
            user_name = argv[0]
            sql = self.__del_user.format(user_name)
            ExecuSQL(sql)
        # 记住用户表的删除
        if table_name == "user_remembered":
            user_name = argv[0]
            sql = self.__del_user_remembered.format(user_name)
            ExecuSQL(sql)
        pass

    # 更新数据函数
    def update(self, table_name, argv):
        """
        根据table_name选取对应的表进行数据库的更新
        :param table_name: 需要更新数据的表
        :param argv: 数据列表
        :return: 无返回值
        """
        # 用户表的更新
        if table_name == "user_table":
            user_name = argv[0]
            update_param = argv[1]
            # 更新禁用标志：封禁用户
            if update_param == "forbidden":
                user_forbidden = argv[2]
                sql = self.__upd_user_forbidden.format(user_forbidden, user_name)
                ExecuSQL(sql)
        pass

    # 查询数据函数
    def select(self, table_name):
        """
        根据table_name选取对应的表进行数据库的查询
        :param table_name: 需要查询数据的表
        :return: 数据元组列表
        """
        # 用户表的查询
        if table_name == "user_table":
            sql = self.__sel_user
            data = getData(sql)
            return data
        # 记住用户表的查询
        if table_name == "user_remembered":
            sql = self.__sel_user_remembered
            data = getData(sql)
            return data
        pass


if __name__ == '__main__':
    a = Database()
    # a.insert("user_table", ["aa", "aa", False])
    # a.update("user_table", ["aa", "aa", True])
    # a.delete("user_table", ["aa"])
    # a.select("user_table")
    # a.select("user_remembered")
    a.insert("user_remembered", ["aa", "aa", True])
    # create_conn()