from copy import copy
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow
from database.database_root import Database_root
from .game_screen_init import GameScreen_init


# 使用界面窗口：权限管理类
class GameScreen_quanxian(GameScreen_init, QMainWindow):
    def __init__(self):
        super(GameScreen_quanxian, self).__init__()
        # 数据库的设置
        self.database_quanxian = Database_root()
        # 管理员表设置
        self.header_quanxian = [""]  # 列表头,用于显示数据对应的行序号
        self.saveList_quanxian = []  # 数据存储列表(数据库中内容)
        self.displayList_quanxian = []  # 数据显示列表(表格中内容)
        self.tableHeader_init_quanxian()  # 初始化表头
        self.data_init_quanxian()  # 初始化数据
        # 连接信号
        self.connecter_quanxian()

    # 连接按钮和对应的函数
    def connecter_quanxian(self):
        self.tablequanxian.itemChanged.connect(self._dataChanged_quanxian)
        self.pushButton_save1.clicked.connect(self.save_quanxian)
        self.pushButton_delete1.clicked.connect(self.delete_quanxian)
        self.pushButton_refresh1.clicked.connect(self.refresh_quanxian)
        self.pushButton_add1.clicked.connect(self.add_quanxian)

    # 初始化表头和行列数
    def tableHeader_init_quanxian(self):
        self.header_quanxian = [""]  # 初始化列表头
        # 设置表格有1行5列
        self.tablequanxian.setColumnCount(3)  # 设置列数
        self.tablequanxian.setRowCount(1)  # 设置行数
        self.tablequanxian.setItem(0, 0, QTableWidgetItem("用户名"))
        self.tablequanxian.setItem(0, 1, QTableWidgetItem("密码"))
        self.tablequanxian.setItem(0, 2, QTableWidgetItem("管理类型"))

    # 初始化操作：即从数据库加载数据
    def data_init_quanxian(self):
        # 获取sel语句的数据列表
        data = self.database_quanxian.select("administrator_table")
        # 遍历data列表
        # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
        for index, item in enumerate(data):
            self.newLine_quanxian(index + 1, item=item)  # 表格新增1行
            self.displayList_quanxian.append(item)  # 显示列表添加数据元组
        self.saveList_quanxian = copy(self.displayList_quanxian)
        self.update()

    # 表格新增一行函数
    def newLine_quanxian(self, num, item=None):
        """
        :param num: 在对应序号处的序号画空白行
        :param item: 输入为对应数据
        """
        if self.lineEdit_num1.text() == "" and item is None:
            QMessageBox.warning(self, "注意", "输入用户名不能为空!")
            return
        self.tablequanxian.insertRow(num)
        _0 = QTableWidgetItem("")
        _0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        _1 = QTableWidgetItem("")
        _2 = QTableWidgetItem("")
        if item is not None:
            _0.setText(str(item[0]))
            _1.setText(str(item[1]))
            _2.setText(str(item[2]))
        else:
            _0.setText(self.lineEdit_num1.text())
        self.tablequanxian.setItem(num, 0, _0)
        self.tablequanxian.setItem(num, 1, _1)
        self.tablequanxian.setItem(num, 2, _2)
        self.header_quanxian.append(str(num))
        self.table.setVerticalHeaderLabels(self.header_quanxian)
        self.update()

    # 表格数据更改的函数
    def _dataChanged_quanxian(self):
        """
        一旦检测到数据改变,则进行检查,
        选择添加新数据还是对原数据进行修改
        :return:
        """
        row_select = self.tablequanxian.selectedItems()
        if len(row_select) == 0:
            return
        row = row_select[0].row()
        content = (self.tablequanxian.item(row, 0).text(), self.tablequanxian.item(row, 1).text(),
                   self.tablequanxian.item(row, 2).text())

        if row <= len(self.displayList_quanxian):
            print("修改行", content)
            self.displayList_quanxian[row - 1] = content
        else:
            print("最新行", content)
            self.displayList_quanxian.append(content)

    # 刷新表格函数
    def refresh_quanxian(self):
        self.tableHeader_init_quanxian()  # 初始化表头
        self.data_init_quanxian()  # 初始化数据

    # 表格删除一行函数
    def delete_quanxian(self):
        """
        若有选中行,点击删除后即可删除
        :return:
        """
        row_select = self.tablequanxian.selectedItems()
        # 若没有选中行
        if len(row_select) == 0:
            return
        Id = row_select[0].row()
        if int(Id) <= len(self.displayList_quanxian):
            print("删除一条数据")
            self.displayList_quanxian.pop()
        self.header_quanxian.pop()
        self.tablequanxian.removeRow(row_select[0].row())
        self.tablequanxian.setVerticalHeaderLabels(self.header_quanxian)
        self.update()

    # 保存表格函数
    def save_quanxian(self):
        """
        点击保存需要筛选出
        需要更新的数据
        需要删除的数据
        需要添加的数据
        """
        idList = [str(k[0]) for k in self.saveList_quanxian]
        _idList = [str(k[0]) for k in self.displayList_quanxian]
        print("点击保存")
        for item in self.displayList_quanxian:
            if item not in self.saveList_quanxian:
                print("存在修改数据")
                if item[0] not in idList:
                    self.database_quanxian.insert("user_table1", [item[0], item[1], item[2]])
                    print("insert")
                else:
                    self.database_quanxian.update("user_table1", [item[0], item[1], item[2]])
                    print("update")
        for item in self.saveList_quanxian:
            if item[0] not in _idList:
                self.database_quanxian.delete("user_table1", [item[0]])
                print("delete", item)
        self.saveList_quanxian = copy(self.displayList_quanxian)

    # 表格新增一行函数
    def add_quanxian(self):
        self.newLine_quanxian(len(self.displayList_quanxian) + 1)
