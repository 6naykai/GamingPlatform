import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from py_window import Login, Verify, GameScreen
from database.database_root import Database_root


# 窗口控制类——用于控制窗口切换
class Controller:
    def __init__(self):
        self.verify = None
        self.login = None
        self.gameScreen = None
        # 账户信息
        self.account = ""
        self.database = Database_root()

    # 显示登陆与注册窗口
    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.identify_Administrator_User)
        self.login.show()

    # 区分管理员与用户：若为管理员直接进入主页面，若为用户则进行验证
    def identify_Administrator_User(self):
        self.account = self.database.select("user_remembered")[0][0]
        print(self.account)
        if self.account == "root":
            self.show_gameScreen()
        else:
            administrator_data = self.database.select("administrator_table")
            for i in range(len(administrator_data)):
                if administrator_data[i][0] == self.account:
                    self.show_gameScreen()
                    return
            self.show_verify()

    # 显示验证窗口
    def show_verify(self):
        self.verify = Verify()
        self.login.close()
        self.verify.switch_window.connect(self.show_gameScreen)
        self.verify.show()

    # 显示GamingPlatform主页面
    def show_gameScreen(self):
        self.gameScreen = GameScreen()
        if self.login:
            self.login.close()
        if self.verify:
            self.verify.close()
        self.gameScreen.show()
        pass


def main():
    # 创建应用
    app = QApplication(sys.argv)
    # 设置窗口icon
    app.setWindowIcon(QIcon('pic/favicon.ico'))
    # 控制窗口切换
    controller = Controller()
    controller.show_login()
    # 退出应用
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
