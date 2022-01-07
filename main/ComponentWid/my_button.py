"""
Author: xtrs
自定义Button
"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qui

sizePolicyPre = QSizePolicy.Preferred


class ASButton(QPushButton):
    """
    adjustShapes 打开目录的btn
    """
    signal_str = qtc.pyqtSignal(str)

    def __init__(self, parent=None):
        super(ASButton, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        # 打开系统目录界面
        name = self.objectName()
        print(name)
        if name.endswith('_docPath'):
            path = QFileDialog.getOpenFileName(self, '选择文件', '/', filter='Word07 files(*.docx)')[0]
        elif name.endswith('_excelPath'):
            path = ''
        elif name.endswith('_filePath'):
            path = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')
        else:
            path = ''
        if path:
            # 拿到路径后 把信号发射出去
            self.signal_str.emit(path)


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

class BtnTwoActions(QPushButton):
    """
    Btn 带两个action
    """

    def __init__(self, parent=None):
        super(BtnTwoActions, self).__init__(parent)
        self.__setUI()

    def __setUI(self):
        # 默认icon
        self.ICON_OCTOPUS = qui.QIcon('../icon/blue_octopus.ico')
        # 添加动作
        self.menu = QMenu()
        self.action1 = QAction(self.ICON_OCTOPUS, '测试1')
        self.menu.addAction(self.action1)
        self.action2 = QAction(self.ICON_OCTOPUS, '测试2')
        self.menu.addAction(self.action2)

        self.setText('☰')
        self.setMenu(self.menu)

        # 去掉设置menu时带上的向下箭头 设置整体样式
        self.setStyleSheet('BtnTwoActions:menu-indicator{image:None}')
        self.setSizePolicy(sizePolicyPre, sizePolicyPre)

    def bindSlots(self, func):
        self.action1.triggered.connect(func)
        self.action2.triggered.connect(func)


class LeaveEnterBtn(QPushButton):

    def __init__(self, parent=None):
        super(LeaveEnterBtn, self).__init__(parent)
        self.isEnter = False

    def connect_enter_leave_slot(self, func):
        self.signal_bool.connect(func)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.isEnter = True

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.isEnter = False


if __name__ == '__main__':
    app = QApplication([])
    win = BtnTwoActions()
    win.show()
    app.exec_()
