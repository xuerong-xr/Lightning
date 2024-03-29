"""
Author: xtrs
功能模块--功能条目列表控件--条目--条目设置对话框
"""
from PyQt5.QtWidgets import QApplication, QColorDialog, QFontDialog
import PyQt5.QtCore as qtc
from PyQt5.QtCore import Qt
from popup_dialog import PopDialog
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

ui_StripLWItemSettingDialog, _ = loadUiType('../UI/StripLWItemSettingDialog.ui')


class StripLWItemSettingDialog(PopDialog, ui_StripLWItemSettingDialog):
    """
    .
    """

    def __init__(self):
        super(StripLWItemSettingDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.bindSlots()

    def bindSlots(self):
        self.bg_color_btn.clicked.connect(self.getColor)
        self.font_btn.clicked.connect(self.getFont)

    def getColor(self):
        color = QColorDialog().getColor()
        if color.isValid():
            self.label.setStyleSheet(f'background-color:{color.name()}')

    def getFont(self):
        font, isValid = QFontDialog().getFont()
        if isValid:
            self.label.setFont(font)


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    win = StripLWItemSettingDialog()
    win.show()
    app.exec_()
