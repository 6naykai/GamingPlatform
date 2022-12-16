import sys
from copy import copy

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPoint, QUrl
from PyQt5.QtGui import QMouseEvent, QColor, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist, QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from UI.UI_gamescreen import Ui_MainWindow
from database.database_root import Database_root
from database.database_user import Database_user
from cpgames import CPGames
from core.games.gobang.gobang import GobangGame


# 使用界面窗口
class GameScreen_music(Ui_MainWindow):
    def __init__(self):
        super(GameScreen_music, self).__init__()
        self.setupUi(self)  # 引入UI界面


    # 连接按钮和对应的函数
    def connecter_music(self):
        self.pushButton_test1.clicked.connect(self.close1)

    def close1(self):
        sys.exit()
# 使用界面窗口
class GameScreen_music2(GameScreen_music):
    def __init__(self):
        super(GameScreen_music2, self).__init__()
        # self.setupUi(self)  # 引入UI界面
        self.connecter_music1()
    # 连接按钮和对应的函数
    def connecter_music1(self):
        self.pushButton_test.clicked.connect(self.close2)

    def close2(self):
        sys.exit()

class GameScreen_music3(GameScreen_music):
    def __init__(self):
        super(GameScreen_music3, self).__init__()
        # self.setupUi(self)  # 引入UI界面
        self.connecter_music3()
    # 连接按钮和对应的函数
    def connecter_music3(self):
        self.pushButton_test2.clicked.connect(self.close3)

    def close3(self):
        sys.exit()