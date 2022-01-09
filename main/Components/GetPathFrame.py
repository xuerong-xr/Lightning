"""
Author: xtrs
获取路径的Frame
"""
from enum import Enum

from PyQt5.QtWidgets import QFrame, QPushButton, QLineEdit, QFileDialog


class FileType(Enum):
    """
    文件类型
    """
    DOC = 0
    DOCX = 1
    EXCEL = 2
    DIRECTORY = 3


class GetPathFrame(QFrame):
    def __init__(self, parent=None):
        super(GetPathFrame, self).__init__(parent)
        self.fileType = FileType.DIRECTORY.value

    def ui_init_slot(self):
        self.btn = self.findChild(QPushButton)
        self.edit = self.findChild(QLineEdit)
        self.bindSlots()

    def bindSlots(self):
        self.btn.clicked.connect(lambda: self.get_path(self.fileType))

    def get_path(self, file_ype):
        """

        :param file_ype:
        """
        # 打开系统目录界面
        print('获取路径')
        temp = ['Word files(.doc .docx)', 'Word07 files(*.docx)', 'Excel files(.xls .xlsx)']
        if file_ype < 3:
            path = QFileDialog.getOpenFileName(self, '选择文件', '/', filter=temp[file_ype])[0]
        elif file_ype == FileType.DIRECTORY.value:
            path = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')
        else:
            path = ''
        if path:
            self.edit.setText(path)
