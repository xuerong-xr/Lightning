"""
Author: xtrs
功能模块--功能条目列表控件--条目
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
import PyQt5.QtCore as qtc

from StripLWItemSettingDialog import StripLWItemSettingDialog
from my_widget import MyWidget
from right_menu import StripLWItemRightMenu
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

ui_moduleListItem, _ = loadUiType('../UI/StripListWidItem.ui')


class StripListWidItem(MyWidget, ui_moduleListItem):
    """
    存放四大主要功能模块 ListWidget 的 item，形式为Frame
    内部结构为：layout_out - QFrame - layout_main - layout_first(QLabel+MyLabel)+layout_third(LabBtnVerFrame*3)
    """

    def __init__(self, parent=None):
        super(StripListWidItem, self).__init__(parent)
        self.setupUi(self)
        self.ui_init_slot()
        self.render_smaller()

    def ui_init_slot(self):
        self.contextMenu = StripLWItemRightMenu(self)
        self.contextMenu.request_menu_bind(self.exec_menu)
        self.nameLabel = self.findChild(QLabel)
        self.nameLabel.setToolTip(self.nameLabel.text())

    def exec_menu(self):
        # TODO(优化算法，1。过滤子控件内的点击，2.不强制做一次变小)
        temp_bool = sum([btn.isEnter for btn in self.findChildren(QPushButton)])
        if temp_bool:
            return
        self.contextMenu.exec_(QCursor.pos())
        self.render_smaller()

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.setDialog = StripLWItemSettingDialog()
        self.setDialog.exec_()
        print('双击了')

    def enterEvent(self, *args, **kwargs):
        # TODO(优化进出效果，考虑协程，是leaveEvent等待 contextMenu执行完再执行)
        print('进入')
        if self.contextMenu.isShow:
            return
        self.render_larger()
        print('变大')

    def leaveEvent(self, *args, **kwargs):
        print('离开')
        if self.contextMenu.isShow:
            return
        self.render_smaller()
        print('变小')

    def render_larger(self):
        self.render_shadow_child(self)
        self.setContentsMargins(4, 4, 4, 4)

    def render_smaller(self):
        self.render_shadow_child(self, radius=15, color=(222, 222, 222))
        self.setContentsMargins(6, 6, 6, 6)


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    win = StripListWidItem()
    win.show()
    app.exec_()
