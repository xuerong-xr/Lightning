"""
Author: xtrs
module 里面的两个提升listWidget
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from AddTagDialog import AddTagDialog
from ModuleListItem import ModuleListItem


class MyListWidTag(QListWidget):

    def __init__(self, parent=None):
        super(MyListWidTag, self).__init__(parent)
        # TODO(头三个item独特标识，不可以移动)
        self.setRightMenue()

    def setRightMenue(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu = QMenu(self)
        self.contextMenu.setStyleSheet('QMenu::item:selected{color:rgb(30,205,153)}')
        self.addTag = self.contextMenu.addAction('添加标签')
        self.refresh = self.contextMenu.addAction('刷新')
        self.addTag.triggered.connect(self.toNewTagDialog)
        self.customContextMenuRequested.connect(lambda: self.contextMenu.exec_(QCursor.pos()))

    def toNewTagDialog(self):
        # 定义一个对话框
        self.dialog = AddTagDialog()
        self.dialog.confirmed_bind(self.newTag)
        # 执行
        self.dialog.exec_()

    def newTag(self, text_set, icon):
        """
        添加标签
        :param text_set:
        :param icon:
        :return:
        """
        # TODO(去重复)
        if text_set:
            text_array = [self.item(i).text() for i in range(self.count())]
            for text_ in text_set:
                if text_ in text_array:
                    continue
                item = QListWidgetItem()
                item.setSizeHint(QSize(80, 22))
                item.setText(text_)
                item.setIcon(icon)
                self.addItem(item)

    def addCustomItem(self, item_wid, item_size=(80, 22)):
        item = QListWidgetItem()
        item.setSizeHint(QSize(item_size[0], item_size[1]))
        self.addItem(item)
        self.setItemWidget(item, item_wid)

    def addCustomItems(self, wid_iterable, item_size=(80, 22)):
        for wid_ in wid_iterable:
            self.addCustomItem(wid_, item_size)


class MyListWidStrip(QListWidget):
    """
    .
    """

    def __init__(self, parent=None):
        super(MyListWidStrip, self).__init__(parent)
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 120))
        self.addItem(item)
        self.setItemWidget(item, ModuleListItem())

    def addItem(self, *__args):
        super(MyListWidStrip, self).addItem(*__args)

    def addItems(self, Iterable, p_str=None):
        super(MyListWidStrip, self).addItems(Iterable)

    def clear(self):
        super(MyListWidStrip, self).clear()
