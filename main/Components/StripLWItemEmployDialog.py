"""
Author: xtrs
功能模块--功能条目列表控件--条目--条目雇用（使用）对话框
"""

from PyQt5.QtCore import Qt
from popup_dialog import PopDialog
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

ui_StripLWItemEmployDialog, _ = loadUiType('../UI/StripLWItemEmployDialog.ui')


class StripLWItemEmployDialog(PopDialog, ui_StripLWItemEmployDialog):
    """
    .
    """
    def __init__(self):
        super(StripLWItemEmployDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
