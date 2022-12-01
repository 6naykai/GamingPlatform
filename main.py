import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from login import Ui_MainWindow


class Login(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.connecter()

    # 连接按钮和对应的函数
    def connecter(self):
        self.pushButton_landing.clicked.connect(self.landing)
        self.pushButton_enroll.clicked.connect(self.enroll)
        self.pushButton_quit.clicked.connect(self.quit)

    # 登陆功能
    def landing(self):
        pass

    # 注册功能
    def enroll(self):
        pass

    # 退出功能
    def quit(self):
        pass


def main():
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()