from copy import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow

from database.database_root import Database_root
from .game_screen_init import GameScreen_init


# 使用界面窗口：用户管理类
class GameScreen_user(GameScreen_init, QMainWindow):
    def __init__(self):
        super(GameScreen_user, self).__init__()
        # 数据库设置
        self.User_database = Database_root()
        # 用户表设置
        self.header_user = [""]  # 列表头,用于显示数据对应的行序号
        self.saveList_user = []  # 数据存储列表(数据库中内容)
        self.displayList_user = []  # 数据显示列表(表格中内容)
        self.UsertableHeader_init()  # 初始化表头
        self.Userdata_init()  # 初始化数据
        # 连接信号
        self.connecter_user()

    # 连接按钮和对应的函数
    def connecter_user(self):
        self.pushButton_save.clicked.connect(self.save_user)
        self.pushButton_delete.clicked.connect(self.delete_user)
        self.pushButton_refresh.clicked.connect(self.refresh_user)
        self.pushButton_add.clicked.connect(self.add_user)
        self.table.itemChanged.connect(self._dataChanged_user)

    # 初始化表头和行列数
    def UsertableHeader_init(self):
        self.header_user = [""]  # 初始化列表头
        self.saveList_user = []  # 数据存储列表(数据库中内容)
        self.displayList_user = []  # 数据显示列表(表格中内容)
        # 设置表格有1行5列
        self.table.setColumnCount(3)  # 设置列数
        self.table.setRowCount(1)  # 设置行数
        self.table.setItem(0, 0, QTableWidgetItem("用户名"))
        self.table.setItem(0, 1, QTableWidgetItem("密码"))
        self.table.setItem(0, 2, QTableWidgetItem("封禁标志"))

    # 初始化操作：即从数据库加载数据
    def Userdata_init(self):
        # 获取sel语句的数据列表
        data = self.User_database.select("user_table")
        # 遍历data列表
        # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
        for index, item in enumerate(data):
            self.User_newLine(index + 1, item=item)  # 表格新增1行
            self.displayList_user.append(item)  # 显示列表添加数据元组
        self.saveList_user = copy(self.displayList_user)
        self.update()

    # 表格新增一行函数
    def User_newLine(self, num, item=None):
        """
        :param num: 在对应序号处的序号画空白行
        :param item: 输入为对应数据
        """
        if self.lineEdit_num.text() == "" and item is None:
            QMessageBox.warning(self, "注意", "输入用户名不能为空!")
            return
        self.table.insertRow(num)
        _0 = QTableWidgetItem("")
        _0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        _1 = QTableWidgetItem("")
        _2 = QTableWidgetItem("")
        if item is not None:
            _0.setText(str(item[0]))
            _1.setText(str(item[1]))
            _2.setText(str(item[2]))
        else:
            _0.setText(self.lineEdit_num.text())
            content = (self.lineEdit_num.text(), None, None)
            self.displayList_user.append(content)
        self.table.setItem(num, 0, _0)
        self.table.setItem(num, 1, _1)
        self.table.setItem(num, 2, _2)
        self.header_user.append(str(num))
        self.table.setVerticalHeaderLabels(self.header_user)
        self.update()

    # 表格数据更改的函数
    def _dataChanged_user(self):
        """
        一旦检测到数据改变,则进行检查,
        选择添加新数据还是对原数据进行修改
        :return:
        """
        row_select = self.table.selectedItems()
        if len(row_select) == 0:
            return
        row = row_select[0].row()
        content = (self.table.item(row, 0).text(), self.table.item(row, 1).text(),
                   self.table.item(row, 2).text())

        if row <= len(self.displayList_user):
            print("修改行", content)
            self.displayList_user[row - 1] = content
        else:
            print("最新行", content)
            self.displayList_user[row - 1] = content

    # 刷新表格函数
    def refresh_user(self):
        self.UsertableHeader_init()  # 初始化表头
        self.Userdata_init()  # 初始化数据

    # 表格删除一行函数
    def delete_user(self):
        """
        若有选中行,点击删除后即可删除
        :return:
        """
        row_select = self.table.selectedItems()
        # 若没有选中行
        if len(row_select) == 0:
            return
        Id = row_select[0].row()
        if int(Id) <= len(self.displayList_user):
            print("删除一条数据")
            self.displayList_user.pop(Id - 1)
        self.header_user.pop()
        self.table.removeRow(row_select[0].row())
        self.table.setVerticalHeaderLabels(self.header_user)
        self.update()

    # 保存表格函数
    def save_user(self):
        """
        点击保存需要筛选出
        需要更新的数据
        需要删除的数据
        需要添加的数据
        """
        idList = [str(k[0]) for k in self.saveList_user]
        _idList = [str(k[0]) for k in self.displayList_user]
        print("点击保存")
        for item in self.displayList_user:
            if item not in self.saveList_user:
                print("存在修改数据")
                if item[0] not in idList:
                    self.User_database.insert("user_table1", [item[0], item[1], item[2]])
                    print("insert")
                else:
                    self.User_database.update("user_table1", [item[0], item[1], item[2]])
                    print("update")
        for item in self.saveList_user:
            if item[0] not in _idList:
                self.User_database.delete("user_table1", [item[0]])
                print("delete", item)
        self.saveList_user = copy(self.displayList_user)

    # 表格新增一行函数
    def add_user(self):
        self.User_newLine(len(self.displayList_user) + 1)
