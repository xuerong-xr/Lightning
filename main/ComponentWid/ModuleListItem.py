"""
Author: xtrs
自定义 Frame
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import PyQt5.QtCore as qtc
from LabBtnVerFrame import LabBtnVerFrame
from my_label import StarLab
from my_widget import MyWidget
from right_menu import moduleItemRightMenu


class ModuleListItem(QFrame, MyWidget):
    """
    存放四大主要功能模块 ListWidget 的 item，形式为Frame
    内部结构为：layout_out - QFrame - layout_main - layout_top(QLabel+MyLabel)+layout_bottom(LabBtnVerFrame*3)
    """

    def __init__(self, parent=None):
        super(ModuleListItem, self).__init__(parent)
        self.__setUI()

    def __setUI(self):
        # TODO(设置样式)
        # 外层 layout
        self.layout_out = QGridLayout()
        self.layout_out.setSpacing(0)
        # 外层 QFrame
        self.frame_out = QFrame()
        # 把上面两者依次添加上
        self.layout_out.addWidget(self.frame_out)
        self.setLayout(self.layout_out)

        # 第二层 垂直布局 套 两个水平布局
        self.layout_main = QVBoxLayout()
        self.layout_top = QHBoxLayout()
        self.layout_bottom = QHBoxLayout()
        # 依次添加上
        self.layout_main.addLayout(self.layout_top)
        self.layout_main.addLayout(self.layout_bottom)
        self.frame_out.setLayout(self.layout_main)
        # 设置外边距
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(6)
        self.layout_top.setContentsMargins(6, 6, 6, 6)
        self.layout_top.setSpacing(6)
        self.layout_bottom.setContentsMargins(0, 0, 0, 0)
        self.layout_bottom.setSpacing(6)

        # 第一个布局top 加入lab
        self.lab = QLabel('我是item的name')
        self.layout_top.addWidget(self.lab, Qt.AlignCenter)

        # 加入toolBtn
        self.starLab = StarLab('星')
        self.starLab.setFixedSize(26, 26)
        self.layout_top.addWidget(self.starLab, Qt.AlignCenter)
        self.starLab.connect_clicked_slot(lambda: print(self.starLab.isChecked))

        # 第二个布局bottom 加入三个LabBtnVerFrame
        self.verFrameLabBtn_s = [LabBtnVerFrame(), LabBtnVerFrame(), LabBtnVerFrame()]
        [self.layout_bottom.addWidget(x) for x in self.verFrameLabBtn_s]

        # 添加右键菜单
        self.contextMenu = moduleItemRightMenu(self)
        self.contextMenu.request_menu_bind(self.exec_menu)

        # 设置整体样式
        self.setStyleSheet('*{font-family:"华文新魏"}')
        self.render_smaller()

    def exec_menu(self):
        # TODO(优化算法，1。过滤子控件内的点击，2.不强制做一次变小)
        temp_bool = sum([btn.isEnter for btn in self.findChildren(QPushButton)]) + self.starLab.isEnter
        if temp_bool:
            return
        self.contextMenu.exec_(QCursor.pos())
        self.render_smaller()

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
        self.layout_out.setContentsMargins(4, 4, 4, 4)

    def render_smaller(self):
        self.render_shadow_child(self, radius=15, color=(222, 222, 222))
        self.layout_out.setContentsMargins(6, 6, 6, 6)


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    win = ModuleListItem()
    win.show()
    app.exec_()
