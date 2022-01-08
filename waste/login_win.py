"""
Author: xtrs
登录窗口
"""
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main.Components.my_win import MyWin

ui, _ = loadUiType('login_dialog.ui')


class LoginWin(MyWin, ui):
    """
    登录窗口
    """

    def __init__(self):
        MyWin.__init__(self)
        # self.getConfig()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # 隐藏边框 | 置顶
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 设置阴影
        self.render_shadow()
        self.handle_ui_change()
        self.handle_btn()

    def render_shadow(self):
        """

        :return:
        """
        self.shadow.setOffset(0, 0)  # 偏移
        self.shadow.setBlurRadius(20)  # 阴影半径
        self.shadow.setColor(QColor(128, 128, 255))  # 阴影颜色
        self.widget.setGraphicsEffect(self.shadow)  # 将设置套用到widget窗口中

    def handle_ui_change(self):
        """
        处理前期页面
        :return:
        """

    def handle_btn(self):
        """
        绑定btn事件
        :return:
        """
        self.btn_close.clicked.connect(self.close)
        self.btn_min.clicked.connect(self.showMinimized)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    lt_win = LoginWin()
    lt_win.show()
    app.exec_()
