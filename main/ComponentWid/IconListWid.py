"""
Author: xtrs
自定义 ListWidget
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5.QtCore as qtc
from PyQt5.QtGui import QIcon


class IconListWid(QListWidget):
    """
    2行 8列 固定大小
    """

    def __init__(self, parent=None):
        super(IconListWid, self).__init__(parent)
        self.setUI()

    def setUI(self):
        self.setViewMode(QListWidget.IconMode)
        self.setIconSize(QSize(20, 20))
        # 提供4个默认 TODO(使默认的不可更改)
        for i in range(4):
            item = QListWidgetItem()
            icon = QIcon('../icon/blue_octopus.ico')
            item.setIcon(icon)
            item.setSizeHint(QSize(20, 20))
            self.addItem(item)

        item2 = QListWidgetItem('+')
        item2.setSizeHint(QSize(20, 20))
        self.addItem(item2)
        self.setMovement(QListWidget.Static)
        self.itemClicked.connect(self.to_addItemDialog)

    def to_addItemDialog(self):
        item = self.selectedItems()[0]
        if item.text():
            print('打开目录')
            return


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    win = IconListWid()
    win.show()
    app.exec_()
