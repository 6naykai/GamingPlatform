from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow

from UI.UI_login import Ui_MainWindow


class Login(Ui_MainWindow, QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)                  # 引入UI界面
        self.setWindowTitle("创意游戏平台")   # 设置窗口名
        self.connecter()

    # 连接按钮和对应的函数
    def connecter(self):
        self.pushButton_landing.clicked.connect(self.landing)           # 登陆
        self.pushButton_enroll.clicked.connect(self.enroll)             # 注册
        self.pushButton_quit.clicked.connect(QCoreApplication.quit)     # 退出

    # 登陆功能
    def landing(self):
        pass

    # 注册功能
    def enroll(self):
        self.switch_window.emit()


# def main():
#     app = QApplication(sys.argv)
#     login = Login()
#     login.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
