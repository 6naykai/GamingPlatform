import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI_enroll import Ui_MainWindow


class Register(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)           # 引入UI界面
        self.setWindowTitle("注册")   # 设置窗口名
        self.connecter()

    # 连接按钮和对应的函数
    def connecter(self):
        self.pushButton_enroll.clicked.connect(self.enroll)

    # 注册响应
    def enroll(self):
        pass

    # 返回响应
    def MyReturn(self):
        pass


def main():
    app = QApplication(sys.argv)
    register = Register()
    register.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()