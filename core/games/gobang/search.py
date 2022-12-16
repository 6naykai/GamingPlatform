from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from copy import copy
import sys
from database_interface import ExecuSQL, getData

sel = "select * from game_table"


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        hhbox = QHBoxLayout()  # 横向布局
        hhbox_1 = QHBoxLayout()
        vbox = QVBoxLayout()
        self.addItem = QPushButton("游戏记录")
        hhbox_1.addWidget(self.addItem)

        self.displayList = []
        self.saveList = []
        self.table = QTableWidget()

        self.table_sitting()
        hhbox.addWidget(self.table)  # 把表格加入布局

        vbox.addLayout(hhbox)
        vbox.addLayout(hhbox_1)
        self.setLayout(vbox)  # 创建布局
        self.setWindowTitle("五子棋游戏记录")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(680, 600)
        self.show()

    def newLine(self, num, item=None):
        """
        :param num: 在对应序号处的序号画空白行
        :param item: 输入为对应数据
        """
        # num=self.table.rowCount()
        self.table.insertRow(num)
        _0 = QTableWidgetItem("")
        _0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        _1 = QTableWidgetItem("")
        _2 = QTableWidgetItem("")

        # item=studentInfo()
        if item != None:
            _0.setText(str(item[0]))
            _1.setText(str(item[1]))
            _2.setText(str(item[2]))

        else:
            _0.setText(str(num))

        self.table.setItem(num, 0, _0)
        self.table.setItem(num, 1, _1)
        self.table.setItem(num, 2, _2)

        self.header.append(str(num))
        self.table.setVerticalHeaderLabels(self.header)
        self.update()

    def init(self):
        """
        初始化操作
        即从数据库加载数据
        """
        argv = "select * from game_table"
        data = getData(argv)
        print("初始化")
        for index, item in enumerate(data):
            self.newLine(index + 1, item=item)
            self.displayList.append(item)
        self.saveList = copy(self.displayList)
        self.update()

    def _redraw(self):
        """
        repaint即刷新数据,
        用保存的数据覆盖未保存的数据
        """
        self.table.setRowCount(0)
        self.table.clearContents()
        self.table_sitting(flag=0)
        for index, item in enumerate(self.saveList):
            self.newLine(index + 1, item)
        self.update()


    def table_sitting(self, flag=1):
        """
        :param flag: 初始化表头和行列数
        """
        self.header = [""]
        self.table.setColumnCount(3)
        self.table.setRowCount(2)  # 设置表格有两行五列
        self.table.setItem(0, 0, QTableWidgetItem("      start_time"))
        self.table.setItem(0, 1, QTableWidgetItem("     game_type"))
        self.table.setItem(0, 2, QTableWidgetItem("        winner"))
        if flag:
            self.init()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Example()
    sys.exit(app.exec_())
