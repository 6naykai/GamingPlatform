import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from login import Login
from verify import Verify
from game_screen import GameScreen


# 窗口控制类——用于控制窗口切换
class Controller:
    def __init__(self):
        self.verify = None
        self.login = None
        self.gameScreen = None
        # 账户信息：用于窗口间传递

    # 显示登陆与注册窗口
    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_verify)
        self.login.show()

    # 显示验证窗口
    def show_verify(self):
        self.verify = Verify()
        self.login.close()
        self.verify.switch_window.connect(self.show_gameScreen)
        self.verify.show()

    # 显示GamingPlatform主页面
    def show_gameScreen(self):
        self.gameScreen = GameScreen()
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
