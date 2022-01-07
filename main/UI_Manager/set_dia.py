"""
Author: xtrs
设置窗口
"""
from PyQt5.QtWidgets import *
from main import UI


class SettingWin(QDialog, UI.ui_set):
    """
    设置窗口
    """
    def __init__(self):
        super(SettingWin, self).__init__()
        self.setupUi(self)
