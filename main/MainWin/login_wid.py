"""
Author: xtrs
时间：2021/12/27
内嵌窗口_用户_登录
"""
from main.MainWin.user_wid import UserWid
from PyQt5.QtWidgets import *
import PyQt5.QtCore as qtc


class LoginWid(UserWid):
    """
    内嵌窗口_用户
    """
    signal_int = qtc.pyqtSignal(int)

    def __init__(self, parent=None):
        super(LoginWid, self).__init__(parent)

    def ui_init_slot(self):
        """
        接收主界面载入完成之后发射的信号 【槽】
        :return:
        """
        super(LoginWid, self).ui_init_slot()

    def getChildren(self):
        """
        获取子控件
        :return:
        """
        self.btnToRegisterPage = self.findChild(QPushButton, 'btnToRegisterPage')

    def update_setting(self):
        """
        从配置文件读取 用户设置数据
        :return:
        """

    def bindSlots(self):
        """
        给子控件绑定槽函数
        :return:
        """
        self.btnToRegisterPage.clicked.connect(self.to_registerPage)

    def to_registerPage(self):
        print('to_registerPage')
        self.signal_int.emit(2)
