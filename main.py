import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from login import Login
from register import Register


def main():
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()