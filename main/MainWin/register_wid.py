"""
Author: xtrs
时间：2021/12/27
内嵌窗口_用户_注册
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main.MainWin.user_wid import UserWid
from my_captcha import createCaptcha
from my_math import rand4words


class RegisterWid(UserWid):
    """
    内嵌窗口_用户
    """

    def __init__(self, parent=None):
        super(RegisterWid, self).__init__(parent)

    def ui_init_slot(self):
        """
        接收主界面载入完成之后发射的信号 【槽】
        :return:
        """
        super(RegisterWid, self).ui_init_slot()
        self.reCaptcha()

    def getChildren(self):
        """
        获取子控件
        :return:
        """
        self.lab_captcha = self.findChild(QLabel, 'lab_captcha')

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
