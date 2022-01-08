"""
Author: xtrs
自定义Label
"""
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QApplication


class MyLabel(QLabel):
    """
    发送点击信号的 Label
    """
    # 自定义信号, 注意信号必须为类属性,为啥
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        """

        :param QMouseEvent:
        """
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_clicked_slot(self, func):
        """

        :param func:
        """
        self.button_clicked_signal.connect(func)


class StarLab(QLabel):
    """
    星标 Lab
    """
    signal_bool = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super(StarLab, self).__init__(parent)
        self.setScaledContents(True)
        self.setPixmap(QtGui.QPixmap())
        self.isChecked = False
        self.isEnter = False

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.isChecked:
            self.setPixmap(QtGui.QPixmap())
        else:
            self.setPixmap(QtGui.QPixmap('../icon/blue_octopus.ico'))
        self.isChecked = not self.isChecked
        self.signal_bool.emit(self.isChecked)

    def connect_clicked_slot(self, func):
        self.signal_bool.connect(func)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.isEnter = True

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.isEnter = False


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    win = StarLab()
    win.show()
    app.exec_()
