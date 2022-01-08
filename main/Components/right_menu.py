"""
Author: xtrs
自定义 右键菜单
"""
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu


class StripLWItemRightMenu(QMenu):
    """
    模块内项目的右键菜单
    """

    def __init__(self, parent=None):
        super(StripLWItemRightMenu, self).__init__(parent)
        self.isShow = False
        self.setUI()

    def setUI(self):
        self.editAct = self.addAction('编辑')
        self.deleteAct = self.addAction('删除')
        self.tagAct = self.addAction('置顶')
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


class TagListWidRightMenu(QMenu):
    def __init__(self, parent=None):
        super(TagListWidRightMenu, self).__init__(parent)
        self.setUI()

    def setUI(self):
        self.addTagAct = self.addAction('添加标签')
        self.refreshAct = self.addAction('刷新')
        self.setStyleSheet('QMenu::item:selected{color:rgb(30,205,153)}')
        self.parent().setContextMenuPolicy(Qt.CustomContextMenu)

    def request_menu_bind(self, func):
        self.parent().customContextMenuRequested.connect(func)
