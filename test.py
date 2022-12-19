# import sys
# from copy import copy
#
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtCore import QCoreApplication, Qt, QPoint, QUrl
# from PyQt5.QtGui import QMouseEvent, QColor, QIcon
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist, QMediaPlayer
# from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
#
# from UI.UI_gamescreen import Ui_MainWindow
# from database.database_root import Database_root
# from database.database_user import Database_user
# from cpgames import CPGames
# from core.games.gobang.gobang import GobangGame
#
#
# # 使用界面窗口
# class GameScreen_music(Ui_MainWindow):
#     def __init__(self):
#         super(GameScreen_music, self).__init__()
#         self.setupUi(self)  # 引入UI界面
#
#
#     # 连接按钮和对应的函数
#     def connecter_music(self):
#         self.pushButton_test1.clicked.connect(self.close1)
#
#     def close1(self):
#         sys.exit()
# # 使用界面窗口
# class GameScreen_music2(GameScreen_music):
#     def __init__(self):
#         super(GameScreen_music2, self).__init__()
#         # self.setupUi(self)  # 引入UI界面
#         self.connecter_music1()
#     # 连接按钮和对应的函数
#     def connecter_music1(self):
#         self.pushButton_test.clicked.connect(self.close2)
#
#     def close2(self):
#         sys.exit()
#
# class GameScreen_music3(GameScreen_music):
#     def __init__(self):
#         super(GameScreen_music3, self).__init__()
#         # self.setupUi(self)  # 引入UI界面
#         self.connecter_music3()
#     # 连接按钮和对应的函数
#     def connecter_music3(self):
#         self.pushButton_test2.clicked.connect(self.close3)
#
#     def close3(self):
#         sys.exit()




# class GameScreen_music:
#     def __init__(self):
#         self.aa("ss")
#         self.aa("ww")
#
#     def aa(self, x):
#         exec('self.{} = 1'.format(x))
#         print(self.ss)
#
#
# a = GameScreen_music()

# coding:utf-8
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(900, 600)
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("click")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        # directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")   #起始路径
        # print(directory1)

        # fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
        #                                                   "All Files (*);;Excel Files (*.mp3)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName1, filetype)

        # files, ok1 = QFileDialog.getOpenFileNames(self,"多文件选择", "./", "All Files (*);;Text Files (*.txt)")
        # print(files)
        files = QFileDialog.getOpenFileName(self, "请选择要添加的文件", "musics", "All Files (*)")
        print(files)
        music_name = re.findall(r'(.+?)\.mp3', re.findall(r'[^\\/:*?"<>|\r\n]+$',files[0])[0])[0]
        print(music_name)
        music_path = files[0]
        # end_pos = music_path.rfind('/') - 1  # 倒数第一个"/"的位置再左移一位
        # start_pos = music_path.rfind('/', 0, end_pos)  # 网址从开始截至到end_pos的位置，从右往左出现的第一个"/"也就是我们要找的倒数第二个"/"
        # filename = music_path[start_pos + 1:]  # 截取网址的倒数第二个 "/" 后面的内容
        filename = music_path[music_path.rfind('/', 0, music_path.rfind('/') - 1) + 1:]
        print(filename)
        # fileName2, ok2 = QFileDialog.getSaveFileName(self,"文件保存", "./","All Files (*);;Text Files (*.txt)")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
