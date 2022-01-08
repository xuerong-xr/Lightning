"""
Author: xtrs
module 里面的两个提升listWidget
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from StripListWidItem import StripListWidItem


class StripListWid(QListWidget):
    """
    .
    """

    def __init__(self, parent=None):
        super(StripListWid, self).__init__(parent)

        item = QListWidgetItem()
        item.setSizeHint(QSize(240, 140))
        self.addItem(item)
        self.setItemWidget(item, StripListWidItem())

        item2 = QListWidgetItem()
        item2.setSizeHint(QSize(240, 140))
        self.addItem(item2)
        self.setItemWidget(item2, StripListWidItem())

        item3 = QListWidgetItem()
        item3.setSizeHint(QSize(240, 140))
        self.addItem(item3)
        self.setItemWidget(item3, StripListWidItem())

    def addItem(self, *__args):
        super(StripListWid, self).addItem(*__args)

    def addItems(self, Iterable, p_str=None):
        super(StripListWid, self).addItems(Iterable)

    def clear(self):
        super(StripListWid, self).clear()
