from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow

from UI.UI_verify import Ui_MainWindow


# 验证窗口类
class Verify(Ui_MainWindow, QMainWindow):

    # 窗口切换信号
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Verify, self).__init__()
        self._tracking = None
        self._startPos = None
        self._endPos = None
        self.effect_shadow_label = None
        self.setupUi(self)                  # 引入UI界面
        self.setWindowTitle("创意游戏平台")   # 设置窗口名
        self.connecter()                    # 连接按钮
        # 隐藏框
        self.setWindowFlags(Qt.FramelessWindowHint)     # 隐藏标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        # 添加阴影
        self.add_shadow()

    # 连接按钮和对应的函数
    def connecter(self):
        pass
        # self.pushButton_landing.clicked.connect(self.landing)           # 登陆页面
        # self.pushButton_enroll.clicked.connect(self.enroll)             # 注册页面
        # self.pushButton_login.clicked.connect(self.login)               # 登陆功能
        # self.pushButton_register.clicked.connect(self.register)         # 注册功能
        # self.pushButton_quit.clicked.connect(QCoreApplication.quit)     # 退出

    # 控件阴影添加
    def add_shadow(self):
        # label控件阴影添加
        self.effect_shadow_label = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow_label.setOffset(0, 0)                               # 偏移
        self.effect_shadow_label.setBlurRadius(25)                             # 阴影半径
        self.effect_shadow_label.setColor(Qt.gray)                             # 阴影颜色
        self.label.setGraphicsEffect(self.effect_shadow_label)                 # 将设置套用到label控件中

    # 重写移动事件——用控件拖重写鼠标事件
    # 重写鼠标移动事件
    def mouseMoveEvent(self, e: QMouseEvent):
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    # 重写鼠标点击事件
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    # 重写鼠标释放事件
    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

