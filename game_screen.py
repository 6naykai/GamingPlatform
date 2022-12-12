from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from UI.UI_gamescreen import Ui_MainWindow
from database import Database


# 使用界面窗口
class GameScreen(Ui_MainWindow, QMainWindow):

    # 窗口切换信号
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(GameScreen, self).__init__()
        self.setupUi(self)  # 引入UI界面
        self.setWindowTitle("创意游戏平台")  # 设置窗口名
        self.connecter()  # 连接按钮

    # 连接按钮和对应的函数
    def connecter(self):
        pass


