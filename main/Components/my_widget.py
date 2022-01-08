"""
Author: xtrs
自定义 widget
"""
from PyQt5.QtWidgets import QWidget
from secondary_win import SecWin


class MyWidget(SecWin, QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
