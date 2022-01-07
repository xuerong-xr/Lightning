"""
Author: xtrs
自定义 右键菜单
"""
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import PyQt5.QtCore as qtc
from PyQt5.QtWidgets import QMenu


class moduleItemRightMenu(QMenu):
    """
    模块内项目的右键菜单
    """

    def __init__(self, parent=None):
        super(moduleItemRightMenu, self).__init__(parent)
        self.isShow = False
        self.setUI()

    def setUI(self):
        self.editAct = self.addAction('编辑')
        self.deleteAct = self.addAction('删除')
        self.tagAct = self.addAction('设置标签')
        self.editAct.triggered.connect(self.editItem)
        self.deleteAct.triggered.connect(self.deleteItem)
        self.tagAct.triggered.connect(self.setTag)
        self.setStyleSheet('QMenu::item:selected{color:rgb(30,205,153)}')
        self.parent().setContextMenuPolicy(Qt.CustomContextMenu)

    def request_menu_bind(self, func):
        self.parent().customContextMenuRequested.connect(func)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.isShow = True
        print('我出现了')

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.isShow = False
        print('我关了')

    def editItem(self):
        print('编辑项目')

    def deleteItem(self):
        # 警告弹窗
        print('删除项目')

    def setTag(self):
        # TODO(直接拖动标签上来设置)
        print('设置标签')
