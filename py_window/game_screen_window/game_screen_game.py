from core import GobangGame
from cpgames import CPGames
from .game_screen_init import GameScreen_init


# 使用界面窗口：游戏界面类
class GameScreen_game(GameScreen_init):
    def __init__(self):
        super(GameScreen_game, self).__init__()
        # 游戏服务设置
        self.games_client = CPGames()
        self.all_supports = self.games_client.getallsupported()
        self.game_list = list(self.all_supports.values())
        self.connecter_game()

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

    def get0(self):
        self.games_client.execute(self.game_list[0])

    def get1(self):
        self.aa = GobangGame()
        # aa = self.games_client.execute(self.game_list[1])
        self.aa.show()

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
