from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from UI.UI_login import Ui_MainWindow
from database import Database


# 登陆窗口类
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
        # 登陆设置
        self.list = [{"account": ["password", 3]}]      # 账户列表
        self.timeOut = 3                                # 登陆的错误上限
        # 便捷登陆设置
        self.list.append({"a": ["a", 100]})
        # 数据库的设置
        self.database = Database()
        self.user_init()

    # 数据库用户表的接口函数：账户列表信息初始化
    def user_init(self):
        user_data = self.database.select("user_table")
        for i in range(len(user_data)):
            # 若用户被封禁,则将其登陆错误上限设置为0,否则设置为timeOut
            if user_data[i][2]:
                self.list.append({user_data[i][0]: [user_data[i][1], 0]})
            else:
                self.list.append({user_data[i][0]: [user_data[i][1], self.timeOut]})

    # 数据库用户表的接口函数：注册插入新账户信息
    def user_insert(self, user_name, user_secret):
        self.database.insert("user_table", [user_name, user_secret, False])

    # 数据库用户表的接口函数：更新用户表信息(封禁账户)
    def user_update(self, account):
        self.database.update("user_table", [account, "forbidden", True])

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
        """
        登陆确认按钮出发函数,包括一些合法性的检测,账户信息的输入与记录
        """
        account = self.lineEdit_login_account.text()
        password = self.lineEdit_login_password.text()
        if str(account) == "":
            QMessageBox.warning(self, "注意", "账号不能为空")
        elif str(password) == "":
            QMessageBox.warning(self, "注意", "密码不能为空")
        else:
            otherAccount = []         # 遍历过的账户存放在otherAccount列表中
            # 遍历整个账户列表查询该账户
            while self.list:
                temp = self.list.pop()
                # 若查到该账户
                if str(account) in temp:
                    # 若账户已被锁定
                    if temp[str(account)][1] == 0:
                        QMessageBox.warning(self, "注意", "错误3次，账户已被锁定！")
                        self.list = self.list + [temp] + otherAccount
                        return
                    # 若账户未被锁定
                    else:
                        # 若密码正确
                        if temp[str(account)][0] == str(password):
                            QMessageBox.information(self, "提示", "登陆成功")
                            # 成功登陆后跳转到验证窗口
                            self.switch_window.emit()
                            return      # 后续添加恢复账户可用输入错误机会(已实现,通过数据库进行隔离)
                        # 若密码错误
                        else:
                            temp[str(account)][1] -= 1      # 账户可用输入错误机会-1
                            # 若账户此时已无可用输入错误机会
                            if temp[str(account)][1] == 0:
                                self.user_update(str(account))      # 通过数据库将账号封禁
                                QMessageBox.warning(self, "注意", "错误3次，账户已被锁定！")
                                self.list = self.list + [temp] + otherAccount
                                return
                            # 若账户此时还有可用错误机会
                            QMessageBox.warning(self, "注意", "密码错误！您还有" + str(temp[str(account)][1]) + "次输入机会。")
                            self.list = self.list + [temp] + otherAccount
                            self.lineEdit_login_password.clear()    # 清空密码输入框
                            return
                # 若未查到该用户
                else:
                    otherAccount.append(temp)
            # 若遍历完整个账户列表仍未查到该用户
            QMessageBox.warning(self, "注意", "账户不存在！")
            self.list = otherAccount
            # 清空账户输入框和密码输入框
            self.lineEdit_login_account.clear()
            self.lineEdit_login_password.clear()

    # 实现注册功能
    def register(self):
        """
        注册确认按钮出发函数,包括一些合法性的检测,账户信息的输入与记录
        """
        temp = {}       # 存放当前账户信息
        account = self.lineEdit_register_account.text()
        password = self.lineEdit_register_password.text()
        passwordConfirm = self.lineEdit_register_passwordConfirm.text()
        if str(account) == "":
            QMessageBox.warning(self, "注意", "账号不能为空!")
        elif str(password) == "":
            QMessageBox.warning(self, "注意", "密码不能为空!")
        elif password != passwordConfirm:
            QMessageBox.warning(self, "注意", "两次输入密码不一致!")
            self.lineEdit_register_password.clear()
            self.lineEdit_register_passwordConfirm.clear()
        else:
            temp[str(account)] = [str(password), self.timeOut]
            self.list.append(temp)                             # 用户列表添加temp用户
            self.user_insert(str(account), str(password))      # 数据库用户表添加temp用户
            QMessageBox.information(self, "提示", "注册成功!")
            # 注册成功则跳转回登陆页面,并清空注册框内容
            self.landing()
            self.lineEdit_register_account.clear()
            self.lineEdit_register_password.clear()
            self.lineEdit_register_passwordConfirm.clear()

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


