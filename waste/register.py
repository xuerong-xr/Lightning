"""
Author: xtrs
注册窗口
"""
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from my_captcha import createCaptcha
from my_math import rand4words

ui, _ = loadUiType('register_dialog.ui')


class RegisterWin(QDialog, ui):
    """
    主窗口类
    """

    def __init__(self):
        QDialog.__init__(self)
        # self.getConfig()
        self.setupUi(self)
        self.handle_ui_change()
        self.handle_btn()

    def handle_ui_change(self):
        """
        处理前期页面
        :return:
        """
        self.reCaptcha()

    def handle_btn(self):
        """
        绑定btn事件
        :return:
        """
        self.lab_captcha.connect_clicked_slot(self.reCaptcha)

    def reCaptcha(self):
        """
        刷新验证码
        :return:
        """
        num = rand4words()
        print(num)
        createCaptcha(num)[0].save('../icon/captcha_register.png')
        self.lab_captcha.setPixmap(QPixmap('../icon/captcha_register.png'))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    lt_win = RegisterWin()
    lt_win.show()
    app.exec_()
