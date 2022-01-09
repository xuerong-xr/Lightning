"""
Author: xtrs
设置窗口
"""
from PyQt5.QtWidgets import *
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

ui_set, _ = loadUiType('../UI/setting.ui')


class SettingWin(QDialog, ui_set):
    """
    设置窗口
    """

    def __init__(self):
        super(SettingWin, self).__init__()
        self.setupUi(self)
