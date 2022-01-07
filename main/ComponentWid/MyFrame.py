"""
Author: xtrs
自定义 Frame
"""
from PyQt5 import QtGui as qui
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import *


class MyFrame(QFrame):
    """
    自定义 Frame 提供鼠标悬停、点击效果，发射点击信号、提供将信号连接槽函数的连接函数
    """
    signal_clicked = qtc.pyqtSignal()

    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent)
        self.isChecked = False
        self.color_parent_bg = self.parent().palette().window().color()
        self.color_enter_bg = 'rgb(231, 231, 231)'
        self.color_checked_bg = 'rgb(30,205,153)'
        self.color_checked_text = 'rgb(255,255,255)'

    def connect_clicked(self, func):
        """
        将信号（此处信号在点击时发射） 连接槽函数
        :param func: 槽函数
        """
        self.signal_clicked.connect(func)

    def setChecked(self, a0: bool):
        self.isChecked = a0
        if a0:
            self.setStyleSheet(f'background-color: {self.color_checked_bg};color: {self.color_checked_text};')
        else:
            self.setStyleSheet(f'background-color: {self.color_parent_bg}')

    def enterEvent(self, *args, **kwargs):
        if self.isChecked:
            return
        self.setStyleSheet(f'background-color: {self.color_enter_bg}')

    def leaveEvent(self, *args, **kwargs):
        if self.isChecked:
            return
        # TODO(改进颜色方案自由调节，或者随父控件)
        self.setStyleSheet(f'background-color: {self.color_parent_bg}')

    def mouseReleaseEvent(self, e: qui.QMouseEvent) -> None:
        # 重复点击无效
        if self.isChecked:
            return
        print(self.objectName())
        # 获取父容器内相同的子控件——MyFrame
        tempList = self.parent().findChildren(MyFrame)
        for tempList_ in tempList:
            if tempList_ == self:
                self.setChecked(True)
            else:
                tempList_.setChecked(False)
        # 先调整自己的UI变化，再向外部发射被点击的信号
        self.signal_clicked.emit()


class TagListItem(QFrame):
    pass

