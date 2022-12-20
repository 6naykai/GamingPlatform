'''
Function:
    五子棋小游戏-支持人机和局域网对战
'''
import os
import sys
from .modules import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .database_interface import ExecuSQL, getData
import datetime,time
from copy import copy


ins = "insert into gobang_game_table(start_time, game_type, winner) values ('{}','{}','{}');"
upd = "update gobang_game_table set winner='{}' where start_time='{}';"
sel = "select * from gobang_game_table"


# 系统管理员数据库连接接口
Database = "GamingPlatform"
#Database = "nbuuser"
User = "gaussdb"
Password = "openGauss@2022"


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        hhbox = QHBoxLayout()  # 横向布局
        hhbox_1 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.displayList = []
        self.saveList = []
        self.table = QTableWidget()

        self.table_sitting()
        hhbox.addWidget(self.table)  # 把表格加入布局

        vbox.addLayout(hhbox)
        vbox.addLayout(hhbox_1)
        self.setLayout(vbox)  # 创建布局
        self.setWindowTitle("五子棋游戏记录")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(680, 600)
        self.show()

    def newLine(self, num, item=None):
        """
        :param num: 在对应序号处的序号画空白行
        :param item: 输入为对应数据
        """
        # num=self.table.rowCount()
        self.table.insertRow(num)
        _0 = QTableWidgetItem("")
        _0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        _1 = QTableWidgetItem("")
        _2 = QTableWidgetItem("")

        # item=studentInfo()
        if item != None:
            _0.setText(str(item[0]))
            _1.setText(str(item[1]))
            _2.setText(str(item[2]))

        else:
            _0.setText(str(num))

        self.table.setItem(num, 0, _0)
        self.table.setItem(num, 1, _1)
        self.table.setItem(num, 2, _2)

        self.header.append(str(num))
        self.table.setVerticalHeaderLabels(self.header)
        self.update()

    def init(self):
        """
        初始化操作
        即从数据库加载数据
        """
        argv = "select * from gobang_game_table"
        data = getData(argv)
        print("初始化")
        for index, item in enumerate(data):
            self.newLine(index + 1, item=item)
            self.displayList.append(item)
        self.saveList = copy(self.displayList)
        self.update()

    def _redraw(self):
        """
        repaint即刷新数据,
        用保存的数据覆盖未保存的数据
        """
        self.table.setRowCount(0)
        self.table.clearContents()
        self.table_sitting(flag=0)
        for index, item in enumerate(self.saveList):
            self.newLine(index + 1, item)
        self.update()

    def table_sitting(self, flag=1):
        """
        :param flag: 初始化表头和行列数
        """
        self.header = [""]
        self.table.setColumnCount(3)
        self.table.setRowCount(2)  # 设置表格有两行五列
        self.table.setItem(0, 0, QTableWidgetItem("      start_time"))
        self.table.setItem(0, 1, QTableWidgetItem("     game_type"))
        self.table.setItem(0, 2, QTableWidgetItem("        winner"))
        if flag:
            self.init()

'''配置类'''
class Config():
    # 根目录
    rootdir = os.path.split(os.path.abspath(__file__))[0]
    # 图标路径
    ICON_FILEPATH = os.path.join(rootdir, 'resources/images/icon/icon.ico')
    # 背景图片路径
    BACKGROUND_IMAGEPATHS = {
        'bg_game': os.path.join(rootdir, 'resources/images/bg/bg_game.png'),
        'bg_start': os.path.join(rootdir, 'resources/images/bg/bg_start.png')
    }
    # 按钮图片路径
    BUTTON_IMAGEPATHS = {
        'online': [
            os.path.join(rootdir, 'resources/images/buttons/online_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/online_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/online_2.png')
        ],
        'ai': [
            os.path.join(rootdir, 'resources/images/buttons/ai_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/ai_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/ai_2.png')
        ],
        'home': [
            os.path.join(rootdir, 'resources/images/buttons/home_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/home_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/home_2.png')
        ],
        'givein': [
            os.path.join(rootdir, 'resources/images/buttons/givein_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/givein_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/givein_2.png')
        ],
        'regret': [
            os.path.join(rootdir, 'resources/images/buttons/regret_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/regret_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/regret_2.png')
        ],
        'startgame': [
            os.path.join(rootdir, 'resources/images/buttons/startgame_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/startgame_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/startgame_2.png')
        ],
        'urge': [
            os.path.join(rootdir, 'resources/images/buttons/urge_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/urge_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/urge_2.png')
        ],
        'search': [
            os.path.join(rootdir, 'resources/images/buttons/search_0.png'),
            os.path.join(rootdir, 'resources/images/buttons/search_1.png'),
            os.path.join(rootdir, 'resources/images/buttons/search_2.png')
        ]
    }
    # 显示胜利图片路径
    WIN_IMAGEPATHS = {
        'black': os.path.join(rootdir, 'resources/images/win/black_win.png'),
        'white': os.path.join(rootdir, 'resources/images/win/white_win.png'),
        'draw': os.path.join(rootdir, 'resources/images/win/draw.png')
    }
    # 棋子图片路径
    CHESSMAN_IMAGEPATHS = {
        'black': os.path.join(rootdir, 'resources/images/chessman/black.png'),
        'white': os.path.join(rootdir, 'resources/images/chessman/white.png'),
        'sign': os.path.join(rootdir, 'resources/images/chessman/sign.png'),
    }
    # 音效
    SOUNDS_PATHS = {
        'drop': os.path.join(rootdir, 'resources/audios/drop.wav'),
        'urge': os.path.join(rootdir, 'resources/audios/urge.wav')
    }
    # 端口号(联机对战时使用)
    PORT = 3333


'''游戏开始界面'''
class GobangGame(QWidget):
    game_type = 'gobang'
    def __init__(self, parent=None, **kwargs):
        super(GobangGame, self).__init__(parent)
        self.cfg = Config
        self.setFixedSize(760, 650)
        self.setWindowTitle('五子棋小游戏')
        self.setWindowIcon(QIcon(self.cfg.ICON_FILEPATH))

        self.addItem = PushButton(self.cfg.BUTTON_IMAGEPATHS.get('search'), self)
        self.addItem.move(300, 500)
        # hhbox_1.addWidget(self.addItem)
        self.addItem.show()
        self.addItem.click_signal.connect(self.PP)

        # 背景图片
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap(self.cfg.BACKGROUND_IMAGEPATHS.get('bg_start'))))
        self.setPalette(palette)
        # 按钮
        # --人机对战
        self.ai_button = PushButton(self.cfg.BUTTON_IMAGEPATHS.get('ai'), self)
        self.ai_button.move(250, 200)
        self.ai_button.show()
        self.ai_button.click_signal.connect(self.playWithAI)
        # --联机对战
        self.online_button = PushButton(self.cfg.BUTTON_IMAGEPATHS.get('online'), self)
        self.online_button.move(250, 350)
        self.online_button.show()
        self.online_button.click_signal.connect(self.playOnline)

    def PP(self):
        self.close()
        # app1 = QApplication(sys.argv)
        self.gul = Example()
        self.gul.show()
        # sys.exit(app1.exec_())

    '''人机对战'''
    def playWithAI(self):
        self.close()

        self.now_time = datetime.datetime.now()
        self.st_t = self.now_time.strftime("%Y-%m-%d %H:%M:%S")
        self.sql = ins.format(self.st_t, '人机对战', 'NULL')
        ExecuSQL(self.sql)

        self.gaming_ui = PlayWithAIUI(self.cfg)
        self.gaming_ui.exit_signal.connect(lambda: sys.exit())
        # self.gaming_ui.exit_signal.connect(self.close)
        self.gaming_ui.back_signal.connect(self.show)
        self.gaming_ui.show()

        self.sql = upd.format(self.gaming_ui.wincol, self.st_t)
        ExecuSQL(self.sql)
    '''联机对战'''
    def playOnline(self):
        self.close()

        self.now_time = datetime.datetime.now()
        self.st_t = self.now_time.strftime("%Y-%m-%d %H:%M:%S")
        self.sql = ins.format(self.st_t, '联机对战', 'NULL')
        ExecuSQL(self.sql)

        self.gaming_ui = PlayOnlineUI(self.cfg, self)
        self.gaming_ui.show()

        self.sql = upd.format(self.gaming_ui.player_color, self.st_t)
        ExecuSQL(self.sql)