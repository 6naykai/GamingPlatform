from database.database_permissionControl import ExecuSQL1, getData1


# User = "AdministratorUser"
# Password = "AdministratorUser@2022"


# 用户平台的数据库接口类(gaussdb系统管理员权限)
class Database_user:
    def __init__(self):
        self.__sel_user = None
        # self.User = "gaussdb"
        # self.Password = "openGauss@2022"
        self.User = "AdministratorUser"
        self.Password = "AdministratorUser@2022"
        # 设置会话路径
        search_path = """
        --设置当前会话的搜索路径为gaussdb模式、Public模式，
        --随后创建的基本表就会自动创建gaussdb模式下。
        SET SEARCH_PATH TO gaussdb, Public;"""
        ExecuSQL1(search_path, self.User, self.Password)
        self.sql_init()

    # sql语句初始化
    def sql_init(self):
        # 用户表sql语句初始化
        self.__sel_user = "select * from user_table;"
        pass

    # 插入数据函数
    def insert(self, table_name, argv):
        """
        根据table_name选取对应的表进行数据库的插入
        :param table_name: 需要插入数据的表
        :param argv: 数据列表
        :return: 无返回值
        """
        pass

    # 删除数据函数
    def delete(self, table_name, argv):
        """
        根据table_name选取对应的表进行数据库的删除
        :param table_name: 需要删除数据的表
        :param argv: 数据列表
        :return: 无返回值
        """
        pass

    # 更新数据函数
    def update(self, table_name, argv):
        """
        根据table_name选取对应的表进行数据库的更新
        :param table_name: 需要更新数据的表
        :param argv: 数据列表
        :return: 无返回值
        """
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
            data = getData1(sql, self.User, self.Password)
            print(data)
            return data
        pass


if __name__ == '__main__':
    a = Database_user()
    # a.insert("user_table", ["aa", "aa", False])
    # a.update("user_table", ["aa", "aa", True])
    # a.delete("user_table", ["aa"])
    # a.select("user_table")
    # a.select("user_remembered")
    a.select("user_table")
    # create_conn()
