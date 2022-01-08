"""
Author: xtrs
自定义 Dialog
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegExpValidator
import const
from IconListWid import IconListWid
from popup_dialog import PopDialog


class AddTagDialog(PopDialog):
    """
    添加标签
    """
    signal_object_str = pyqtSignal(object, object)

    def __init__(self, parent=None):
        super(AddTagDialog, self).__init__(parent)
        self.setUI()

    def setUI(self):
        self.setFixedSize(200, 140)
        self.setWindowTitle('新增标签')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # 竖向装上 lineEdit 和 btn
        self.layout = QVBoxLayout()
        self.edit = QLineEdit()
        self.listWid = IconListWid()
        self.btn = QPushButton('确定')

        self.edit.setPlaceholderText('如需添加多个标签，以分号分隔')
        self.edit.setFixedSize(180, 26)
        self.listWid.setFixedSize(180, 48)
        self.btn.setFixedSize(80, 24)

        # 输入验证，限制4位
        re_validator = QRegExpValidator(QRegExp(const.TAG_INPUT_REGEXP))
        self.edit.setValidator(re_validator)

        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.listWid)
        self.layout.addWidget(self.btn)

        self.layout.setAlignment(self.edit, Qt.AlignCenter)
        self.layout.setAlignment(self.btn, Qt.AlignCenter)

        self.setLayout(self.layout)

        self.btn.clicked.connect(self.__confirmed)

        self.ui_init_slot()

    def ui_init_slot(self):
        # TODO(初始化)
        self.listWid.item(0).setSelected(True)
        pass

    def __confirmed(self):
        # 去重
        text = self.edit.text()
        icon = self.listWid.selectedItems()[0].icon()
        if text:
            text_set = set(text.replace('；', ';').split(';'))
            self.signal_object_str.emit(text_set, icon)
        self.close()

    def confirmed_bind(self, func):
        self.signal_object_str.connect(func)
