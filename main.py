import sys

from PyQt5.QtGui import QWindow, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from login import Login
from register import Register


class Controller:
    def __init__(self):
        self.register = None
        self.login = None

    # 显示登陆窗口
    def show_login(self):
        self.login = Login()
        if self.register is not None:
            self.register.close()
        self.login.switch_window.connect(self.show_register)
        self.login.show()

    # 显示注册窗口
    def show_register(self):
        self.register = Register()
        self.login.close()
        self.register.switch_window.connect(self.show_login)
        self.register.show()


def main():
    # 创建应用
    app = QApplication(sys.argv)
    # 设置窗口icon
    app.setWindowIcon(QIcon('pic/favicon.ico'))
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()