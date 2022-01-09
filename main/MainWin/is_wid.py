"""
Author: xtrs
插入图片
"""
from PyQt5.QtWidgets import *

from tool_wid import ToolWid


class InsertShapesWidget(ToolWid):
    """
    插入图片
    """

    def __init__(self, parent=None):
        super(InsertShapesWidget, self).__init__(parent)

    def ui_init_slot(self):
        """
        接收界面载入信号 【槽】
        :return:
        """
        super(InsertShapesWidget, self).ui_init_slot()

    def getChildren(self):
        """
        .
        """
        pass

    def update_setting(self):
        """
        .
        """
        pass

    def bindSlots(self):
        """
        .
        """
        pass
