from .database_interface import ExecuSQL, getData


# 用户平台的数据库接口类(gaussdb系统管理员权限)
class Database_root:
    def __init__(self):
        self.__ins_user = None
        self.__ins_user_remembered = None
        self.__ins_administrator = None
        self.__ins_music = None
        self.__ins_game = None
        self.__upd_user_forbidden = None
        self.__upd_user_all = None
        self.__upd_administrator = None
        self.__upd_music = None
        self.__upd_game = None
        self.__del_user = None
        self.__del_user_remembered = None
        self.__del_administrator = None
        self.__del_music = None
        self.__del_game = None
        self.__sel_user = None
        self.__sel_user_remembered = None
        self.__sel_administrator = None
        self.__sel_music = None
        self.__sel_game = None
        self.sql_init()

    # sql语句初始化
    def sql_init(self):
        # 用户表sql语句初始化
        self.__ins_user = "insert into user_table (user_name,user_secret,user_forbidden) values ('{}','{}','{}');"
        self.__upd_user_forbidden = "update user_table set user_forbidden='{}' where user_name='{}';"
        self.__upd_user_all = "update user_table set user_secret='{}',user_forbidden='{}' where user_name='{}';"
        self.__del_user = "delete from user_table where user_name='{}';"
        self.__sel_user = "select * from user_table;"
        # 记住用户表sql语句的初始化
        self.__ins_user_remembered = "insert into user_remembered (user_name,user_secret,is_remembered) values ('{}'," \
                                     "'{}','{}'); "
        self.__del_user_remembered = "delete from user_remembered where user_name='{}';"
        self.__sel_user_remembered = "select * from user_remembered;"
        # 管理员账户表sql语句的初始化
        self.__ins_administrator = "insert into administrator_table(administrator_name, administrator_secret, " \
                                   "administrator_type) values ('{}','{}','{}');"
        self.__sel_administrator = "select * from administrator_table;"
        self.__upd_administrator = "update administrator_table set administrator_secret='{}',administrator_type='{}' " \
                                   "where administrator_name='{}';"
        self.__del_administrator = "delete from administrator_table where administrator_name='{}';"
        # 音乐库表sql语言的初始化
        self.__ins_music = "insert into music_table(music_name, music_path) VALUES ('{}','{}');"
        self.__del_music = "delete from music_table where music_name='{}';"
        self.__upd_music = "update music_table set music_path='{}',is_accretion='{}' where music_name='{}';"
        self.__sel_music = "select * from music_table;"
        # 游戏库表sql语言的初始化
        self.__ins_game = "insert into game_table(game_name, game_path) VALUES ('{}','{}');"
        self.__del_game = "delete from game_table where game_name='{}';"
        self.__upd_game = "update game_table set game_path='{}',is_added='{}' where game_name='{}';"
        self.__sel_game = "select * from game_table;"

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
        if table_name == "user_remembered":
            user_name = argv[0]
            user_secret = argv[1]
            is_remembered = argv[2]
            sql = self.__ins_user_remembered.format(user_name, user_secret, is_remembered)
            ExecuSQL(sql)
        # 管理员账户表的插入
        if table_name == "administrator_table":
            account_name = argv[0]
            account_secret = argv[1]
            account_type = argv[2]
            sql = self.__ins_administrator.format(account_name, account_secret, account_type)
            ExecuSQL(sql)
        # 音乐库表的插入
        if table_name == "music_table":
            music_name = argv[0]
            music_path = argv[1]
            sql = self.__ins_music.format(music_name, music_path)
            ExecuSQL(sql)
        # 游戏库表的插入
        if table_name == "game_table":
            game_name = argv[0]
            game_path = argv[1]
            sql = self.__ins_game.format(game_name, game_path)
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
        # 用户表的删除：根据用户名删除对应用户
        if table_name == "user_table":
            user_name = argv[0]
            sql = self.__del_user.format(user_name)
            ExecuSQL(sql)
        # 记住用户表的删除：删除记住用户表中记录内容
        if table_name == "user_remembered":
            user_name = argv[0]
            sql = self.__del_user_remembered.format(user_name)
            ExecuSQL(sql)
        # 管理员账户表的删除：根据管理员账户名删除对应账户
        if table_name == "administrator_table":
            account_name = argv[0]
            sql = self.__del_administrator.format(account_name)
            ExecuSQL(sql)
        # 音乐库表的删除
        if table_name == "music_table":
            music_name = argv[0]
            sql = self.__del_music.format(music_name)
            ExecuSQL(sql)
        # 游戏库表的删除
        if table_name == "game_table":
            game_name = argv[0]
            sql = self.__del_game.format(game_name)
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
            # 更新用户全部信息
            elif update_param == "all":
                user_secret = argv[2]
                user_forbidden = argv[3]
                sql = self.__upd_user_all.format(user_secret, user_forbidden, user_name)
                ExecuSQL(sql)
        # 管理员账户表的更新
        if table_name == "administrator_table":
            account_name = argv[0]
            account_secret = argv[1]
            account_type = argv[2]
            sql = self.__upd_administrator.format(account_secret, account_type, account_name)
            ExecuSQL(sql)
        # 音乐库表的更新
        if table_name == "music_table":
            music_name = argv[0]
            music_path = argv[1]
            is_accretion = argv[2]
            sql = self.__upd_music.format(music_path, is_accretion, music_name)
            ExecuSQL(sql)
        # 游戏库表的更新
        if table_name == "game_table":
            game_name = argv[0]
            game_path = argv[1]
            is_added = argv[2]
            sql = self.__upd_game.format(game_path, is_added, game_name)
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
        # 管理员账户表的查询
        if table_name == "administrator_table":
            sql = self.__sel_administrator
            data = getData(sql)
            return data
        # 音乐库表的查询
        if table_name == "music_table":
            sql = self.__sel_music
            data = getData(sql)
            return data
        # 游戏库表的查询
        if table_name == "game_table":
            sql = self.__sel_game
            data = getData(sql)
            return data
        pass


if __name__ == '__main__':
    a = Database_root()
    # a.insert("user_table", ["aa", "aa", False])
    # a.update("user_table", ["aa", "aa", True])
    # a.delete("user_table", ["aa"])
    # a.select("user_table")
    # a.select("user_remembered")
    # a.insert("user_remembered", ["aa", "aa", True])
    print(a.select("music_table"))
    # create_conn()
