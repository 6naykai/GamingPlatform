from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from UI.UI_gamescreen import Ui_MainWindow


# 使用界面窗口
class GameScreen(Ui_MainWindow, QMainWindow):

    # 窗口切换信号
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(GameScreen, self).__init__()
        self._startPos = None
        self._tracking = None
        self._endPos = None
        self.setupUi(self)  # 引入UI界面
        self.setWindowTitle("创意游戏平台")  # 设置窗口名
        self.connecter()  # 连接按钮
        # 隐藏框
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        # 设置阴影
        self.effect_shadow_style(self.widget_3)
        self.effect_shadow_style(self.widget_7)
        self.effect_shadow_style(self.widget_11)
        self.effect_shadow_style(self.widget_15)

    # 连接按钮和对应的函数
    def connecter(self):
        pass

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

    # 设置阴影样式
    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(5, 5)       # 偏移
        effect_shadow.setBlurRadius(48)     # 阴影半径
        effect_shadow.setColor(QColor(155, 230, 237, 150))
        widget.setGraphicsEffect(effect_shadow)


