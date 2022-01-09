"""
Author: xtrs
InsertShapes
"""
from PyQt5.QtWidgets import *
import PyQt5.QtCore as qtc


class TargetTabListView(QListView):
    def __init__(self, parent=None):
        super(TargetTabListView, self).__init__(parent)
        # model = qtc.QAbstractListModel()
        model = qtc.QStringListModel()
        # list = [QLabel(), QLineEdit, QPushButton()]
        list = ['QLabel()', 'QLineEdit()', 'QPushButton()']
        model.setStringList(list)
        self.setModel(model)


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    win = TargetTabListView()
    win.show()
    app.exec_()
