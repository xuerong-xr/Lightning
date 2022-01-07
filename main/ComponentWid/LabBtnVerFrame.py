"""
Author: xtrs
自定义 Frame
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from my_button import LeaveEnterBtn


class LabBtnVerFrame(QFrame):
    """
    竖向排版Frame，包含第一个子控件label,第二个子控件button
    """

    def __init__(self, parent=None):
        super(LabBtnVerFrame, self).__init__(parent)
        # TODO(改进)
        # frame自适应大小 父控件有大小 则不需要给大小
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # 加入布局 垂直
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # 加入lab
        self.lab = QLabel('lab')
        self.layout.addWidget(self.lab, 1, Qt.AlignCenter)
        # 加入btn
        self.btn = LeaveEnterBtn('btn')
        self.layout.addWidget(self.btn, 1, Qt.AlignCenter)
