from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow

from UI.UI_login import Ui_MainWindow


class Login(Ui_MainWindow, QMainWindow):

    # 窗口切换信号
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Login, self).__init__()
        self._tracking = None
        self._startPos = None
        self._endPos = None
        self.effect_shadow_pushButton_register = None
        self.effect_shadow_pushButton_login = None
        self.effect_shadow_label_2 = None
        self.effect_shadow_label = None
        self.setupUi(self)                  # 引入UI界面
        self.setWindowTitle("创意游戏平台")   # 设置窗口名
        self.connecter()                    # 连接按钮
        # 隐藏框
        self.setWindowFlags(Qt.FramelessWindowHint)     # 隐藏标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        self.widget_enroll.hide()                       # 隐藏注册页面
        # 添加阴影
        self.add_shadow()

    # 连接按钮和对应的函数
    def connecter(self):
        self.pushButton_landing.clicked.connect(self.landing)           # 登陆页面
        self.pushButton_enroll.clicked.connect(self.enroll)             # 注册页面
        self.pushButton_login.clicked.connect(self.login)               # 登陆功能
        self.pushButton_register.clicked.connect(self.register)         # 注册功能
        # self.pushButton_quit.clicked.connect(QCoreApplication.quit)     # 退出

    # 显示登陆页面
    def landing(self):
        self.widget_enroll.hide()   # 隐藏注册页面
        # 注册页面切换按钮变灰
        self.pushButton_enroll.setStyleSheet(
            "border:none;"
            "color:rgb(186,186,186);"
        )
        # 登陆页面切换按钮变黑
        self.pushButton_landing.setStyleSheet(
            "border:none;"
            "color:black;"
        )
        self.widget_landing.show()  # 显示登陆页面

    # 显示注册页面
    def enroll(self):
        self.widget_landing.hide()  # 隐藏登陆页面
        # 登陆页面切换按钮变灰
        self.pushButton_landing.setStyleSheet(
            "border:none;"
            "color:rgb(186,186,186);"
        )
        # 注册页面切换按钮变黑
        self.pushButton_enroll.setStyleSheet(
            "border:none;"
            "color:black;"
        )
        self.widget_enroll.show()   # 显示注册页面
        # self.switch_window.emit()

    # 实现登陆功能
    def login(self):
        pass

    # 实现注册功能
    def register(self):
        pass

    # 控件阴影添加
    def add_shadow(self):
        # label控件阴影添加
        self.effect_shadow_label = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow_label.setOffset(0, 0)                               # 偏移
        self.effect_shadow_label.setBlurRadius(25)                             # 阴影半径
        self.effect_shadow_label.setColor(Qt.gray)                             # 阴影颜色
        self.label.setGraphicsEffect(self.effect_shadow_label)                 # 将设置套用到label控件中
        # label_2控件阴影添加
        self.effect_shadow_label_2 = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow_label_2.setOffset(0, 0)
        self.effect_shadow_label_2.setBlurRadius(25)
        self.effect_shadow_label_2.setColor(Qt.gray)
        self.label_2.setGraphicsEffect(self.effect_shadow_label_2)
        # pushButton_login控件阴影添加
        self.effect_shadow_pushButton_login = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow_pushButton_login.setOffset(3, 3)                               # 偏移
        self.effect_shadow_pushButton_login.setBlurRadius(25)                             # 阴影半径
        self.effect_shadow_pushButton_login.setColor(Qt.gray)                             # 阴影颜色
        self.pushButton_login.setGraphicsEffect(self.effect_shadow_pushButton_login)      # 将设置套用到pushButton控件中
        # pushButton_register控件阴影添加
        self.effect_shadow_pushButton_register = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow_pushButton_register.setOffset(3, 3)
        self.effect_shadow_pushButton_register.setBlurRadius(25)
        self.effect_shadow_pushButton_register.setColor(Qt.gray)
        self.pushButton_register.setGraphicsEffect(self.effect_shadow_pushButton_register)

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


