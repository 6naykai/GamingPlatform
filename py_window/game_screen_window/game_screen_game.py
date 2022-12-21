import os

from PyQt5.QtGui import QIcon

from core import GobangGame
from cpgames import CPGames
from database.database_root import Database_root
from .game_screen_init import GameScreen_init
from ProjectPath import projectPath


# 使用界面窗口：游戏界面类
class GameScreen_game(GameScreen_init):
    def __init__(self):
        super(GameScreen_game, self).__init__()
        # 数据库的设置
        self.database_game = Database_root()
        # 设置平台内置游戏列表
        self.game_in_platform = ["五子棋", "2048", "飞腾的小鸟", "飞机大作战", "乒乓球",
                                 "推箱子", "走迷宫", "俄罗斯方块", "消消乐", "贪吃蛇"]
        self.game_path = []     # 游戏路径列表
        # 游戏界面显示初始化
        self.gameWidget_init()
        # 游戏服务设置
        self.gobang = GobangGame()
        self.games_client = CPGames()
        self.all_supports = self.games_client.getallsupported()
        self.game_list = list(self.all_supports.values())
        self.connecter_game()

    # 根据数据库中是否添加游戏入库信息来显示游戏widget
    def gameWidget_init(self):
        self.widget_wuziqi.hide()
        self.widget_niao.hide()
        self.widget_eluosi.hide()
        self.widget_zoumigong.hide()
        self.widget_xiaoxiaole.hide()
        self.widget_tuixiangzi.hide()
        self.widget_pingpang.hide()
        self.widget_feiji.hide()
        self.widget_tanchishe.hide()
        self.widget_2048.hide()
        # 批量化隐藏新增游戏的widget
        for i in range(11):
            exec('self.widget_game_{}.hide()'.format(i))
        # game_num是游戏标签
        game_num = 0
        # 获取列表数据
        data = self.database_game.select("game_table")
        for i in range(len(data)):
            if data[i][2]:
                if data[i][0] == "五子棋":
                    self.widget_wuziqi.show()
                if data[i][0] == "2048":
                    self.widget_2048.show()
                if data[i][0] == "飞腾的小鸟":
                    self.widget_niao.show()
                if data[i][0] == "飞机大作战":
                    self.widget_feiji.show()
                if data[i][0] == "乒乓球":
                    self.widget_pingpang.show()
                if data[i][0] == "推箱子":
                    self.widget_tuixiangzi.show()
                if data[i][0] == "走迷宫":
                    self.widget_zoumigong.show()
                if data[i][0] == "俄罗斯方块":
                    self.widget_eluosi.show()
                if data[i][0] == "消消乐":
                    self.widget_xiaoxiaole.show()
                if data[i][0] == "贪吃蛇":
                    self.widget_tanchishe.show()
                if data[i][0] not in self.game_in_platform:
                    exec('self.widget_game_{}.show()'.format(game_num))
                    exec('self.label_game_{}.setText(data[i][0])'.format(game_num))
                    self.game_path.append(projectPath + '/' + data[i][1])
                    game_num += 1
                    pass
        pass

    # 通过路径连接游戏exe程序的函数
    def gameForEXE0(self):
        # os.startfile(self.game_path[0])
        os.system(self.game_path[0])
        pass

    def gameForEXE1(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[1])
        pass

    def gameForEXE2(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[2])
        pass

    def gameForEXE3(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[3])
        pass

    def gameForEXE4(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[4])
        pass

    def gameForEXE5(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[5])
        pass

    def gameForEXE6(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[6])
        pass

    def gameForEXE7(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[7])
        pass

    def gameForEXE8(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[8])
        pass

    def gameForEXE9(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[9])
        pass

    def gameForEXE10(self):
        # os.startfile(self.game_path[1])
        os.system(self.game_path[10])
        pass

    # 连接按钮和对应的函数
    def connecter_game(self):
        self.pushButton_game_zoumigong.clicked.connect(self.get0)
        self.pushButton_game_wuziqi.clicked.connect(self.get1)
        self.pushButton_game_eluosi.clicked.connect(self.get2)
        self.pushButton_game_xiaoxiaole.clicked.connect(self.get3)
        self.pushButton_game_tuixiangzi.clicked.connect(self.get4)
        self.pushButton_game_pingpang.clicked.connect(self.get5)
        self.pushButton_game_niao.clicked.connect(self.get6)
        self.pushButton_game_feiji.clicked.connect(self.get7)
        self.pushButton_game_tanchishe.clicked.connect(self.get8)
        self.pushButton_game_2048.clicked.connect(self.get9)
        for i in range(11):
            exec('self.pushButton_game_{}.clicked.connect(self.gameForEXE{})'.format(i, i))

    def get0(self):
        self.games_client.execute(self.game_list[0])

    def get1(self):
        # self.gobang = GobangGame()
        # aa = self.games_client.execute(self.game_list[1])
        self.gobang.show()

    def get2(self):
        self.games_client.execute(self.game_list[2])

    def get3(self):
        self.games_client.execute(self.game_list[3])

    def get4(self):
        self.games_client.execute(self.game_list[4])

    def get5(self):
        self.games_client.execute(self.game_list[5])

    def get6(self):
        self.games_client.execute(self.game_list[6])

    def get7(self):
        self.games_client.execute(self.game_list[7])

    def get8(self):
        self.games_client.execute(self.game_list[8])

    def get9(self):
        self.games_client.execute(self.game_list[9])
