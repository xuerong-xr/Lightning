"""
Author: xtrs
insertShapes界面管理
"""
from tool_wid import ToolWid
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

ui_InsertShapesForm, _ = loadUiType('../UI/InsertShapesForm.ui')


class InsertShapesForm(ToolWid, ui_InsertShapesForm):
    """
    插入图片
    """
    # 配置
    config_j = {}

    def __init__(self):
        super(InsertShapesForm, self).__init__()
        self.setupUi(self)
        self.init_UI()

    def init_UI(self):
        
        pass
