from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from database.database_root import Database_root
from database.database_user import Database_user
from .game_screen_window import GameScreen_game, GameScreen_music, GameScreen_user, GameScreen_quanxian


# 使用界面窗口
class GameScreen(GameScreen_music, GameScreen_game, GameScreen_user, GameScreen_quanxian):

    # 窗口切换信号
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(GameScreen, self).__init__()
        self._startPos = None
        self._tracking = None
        self._endPos = None
        self.setWindowTitle("创意游戏平台")  # 设置窗口名
        # 界面初始化
        self.ui_init()
        # 连接按钮
        self.connecter()
        # 用户名及身份设置
        self.user_name = ""
        self.user_permission = ""
        # 数据库的设置：显示用户名和身份
        self.database = Database_root()
        self.account_init()
        # 权限管控
        self.account_permission()

    # 权限管控：根据用户身份显示不同页面
    def account_permission(self):
        self.listWidget.clear()
        user_list = ["音乐", "游戏"]
        useradmin_list = ["音乐", "游戏", "用户管理"]
        root_list = ["音乐", "游戏", "用户管理", "权限管理"]
        if self.user_permission == "普通用户":
            self.listWidget.addItems(user_list)
        elif self.user_permission == "用户管理员":
            self.listWidget.addItems(useradmin_list)
        else:
            self.listWidget.addItems(root_list)

    # 账户信息初始化：设置用户名和身份
    def account_init(self):
        # 设置用户名
        data = self.database.select("user_remembered")
        self.label_username.setText(data[0][0])
        self.user_name = data[0][0]
        # 设置身份
        dataadm = self.database.select("administrator_table")
        flag = 1    # 管理员标志：若管理员表中查不到该用户,则设置为0
        for i in range(len(dataadm)):
            if dataadm[i][0] == data[0][0]:
                self.label_usershuxing.setText(dataadm[i][2])
                self.user_permission = dataadm[i][2]
                flag = 0
        if flag:
            self.label_usershuxing.setText("普通用户")
            self.user_permission = "普通用户"

    # 界面初始化
    def ui_init(self):
        # 隐藏框
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        # 初始化游戏初始界面
        self.widget_musics.hide()
        self.widget_users.hide()
        self.widget_quanxians.hide()

    # 连接按钮和对应的函数
    def connecter(self):
        self.listWidget.itemClicked.connect(self.onClickedListWidget)
        pass

    # 列表切换按钮：用于切换主界面的不同widget
    def onClickedListWidget(self, item):
        text = item.text()
        if text == "音乐":
            self.widget_games.hide()
            self.widget_users.hide()
            self.widget_quanxians.hide()
            self.widget_musics.show()
        if text == "游戏":
            self.widget_musics.hide()
            self.widget_users.hide()
            self.widget_quanxians.hide()
            self.widget_games.show()
        if text == "用户管理":
            self.widget_musics.hide()
            self.widget_quanxians.hide()
            self.widget_games.hide()
            self.widget_users.show()
        if text == "权限管理":
            self.widget_musics.hide()
            self.widget_users.hide()
            self.widget_games.hide()
            self.widget_quanxians.show()
        print(text)
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