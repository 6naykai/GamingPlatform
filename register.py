import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.UI_enroll import Ui_MainWindow


class Register(Ui_MainWindow, QMainWindow):

    # 窗口切换信号
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)           # 引入UI界面
        self.setWindowTitle("注册")   # 设置窗口名
        self.connecter()

    # 连接按钮和对应的函数
    def connecter(self):
        self.pushButton_enroll.clicked.connect(self.enroll)
        self.pushButton_MyReturn.clicked.connect(self.MyReturn)

    # 注册响应
    def enroll(self):
        pass

    # 返回响应
    def MyReturn(self):
        self.switch_window.emit()
