import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from login import Login
from verify import Verify


# 窗口控制类——用于控制窗口切换
class Controller:
    def __init__(self):
        self.verify = None
        # self.register = None
        self.login = None

    # 显示登陆窗口
    def show_login(self):
        self.login = Login()
        # if self.register is not None:
        #     self.register.close()
        self.login.switch_window.connect(self.show_verify)
        self.login.show()

    # 显示验证窗口
    def show_verify(self):
        self.verify = Verify()
        self.login.close()
        self.verify.show()
        pass

    # # 显示注册窗口
    # def show_register(self):
    #     self.register = Register()
    #     self.login.close()
    #     self.register.switch_window.connect(self.show_login)
    #     self.register.show()


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
