"""
Author: xtrs
时间：2021/12/27
内嵌窗口_用户
"""
from embedded_wid import EmbWid
from PyQt5.QtWidgets import *


class UserWid(EmbWid):
    """
    内嵌窗口_用户
    """

    def __init__(self, parent=None):
        super(UserWid, self).__init__(parent)

    def ui_init_slot(self):
        """
        接收主界面载入完成之后发射的信号 【槽】
        :return:
        """
        super(UserWid, self).ui_init_slot()

    def getChildren(self):
        """
        获取子控件
        :return:
        """
        # QStackedWidget
        self.staWid_user = self.findChild(QStackedWidget, 'staWid_user')

        # QPushButton 左侧
        self.btn_user_main = self.findChild(QPushButton, 'btn_user_main')
        self.btn_user_mine = self.findChild(QPushButton, 'btn_user_mine')
        self.btn_user_style = self.findChild(QPushButton, 'btn_user_style')
        self.btn_user_about = self.findChild(QPushButton, 'btn_user_about')

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
        # QStackWidget
        self.btn_user_main.clicked.connect(lambda: self.set_staWid_user_index(0))
        self.btn_user_mine.clicked.connect(lambda: self.set_staWid_user_index(1))

    def set_staWid_user_index(self, index):
        self.staWid_user.setCurrentIndex(index)
