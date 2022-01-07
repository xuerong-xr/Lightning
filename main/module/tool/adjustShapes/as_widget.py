"""
Author: xtrs
adjustShapes界面管理
"""
import os.path

from PyQt5 import QtGui as qui
from PyQt5.QtWidgets import *
import PyQt5.QtCore as qtc
from PyQt5.QtWidgets import QRadioButton
import const
from tool_wid import ToolWid
from setting import Setting as se


class AdjustShapesWidget(ToolWid):
    """
    工具窗口
    """
    # 定义信号
    signal_str = qtc.pyqtSignal(str)
    signal_str_int = qtc.pyqtSignal(str, int)

    def __init__(self, parent=None):
        super(AdjustShapesWidget, self).__init__(parent)

    def ui_init_slot(self):
        """
        接收主界面载入完成之后发射的信号 【槽】
        :return:
        """
        print('as ui_init')
        super(AdjustShapesWidget, self).ui_init_slot()

    def getChildren(self):
        """
        获取子控件
        :return:
        """
        # QRadioButton
        self.rBtn_aS_doc = self.findChild(QRadioButton, 'rBtn_aS_doc')
        self.rBtn_aS_file = self.findChild(QRadioButton, 'rBtn_aS_file')
        self.list_d_f = [self.rBtn_aS_doc, self.rBtn_aS_file]

        self.rBtn_aS_all = self.findChild(QRadioButton, 'rBtn_aS_all')
        self.rBtn_aS_tab = self.findChild(QRadioButton, 'rBtn_aS_tab')
        self.rBtn_aS_chapter = self.findChild(QRadioButton, 'rBtn_aS_chapter')
        self.list_s_t = [self.rBtn_aS_all, self.rBtn_aS_tab, self.rBtn_aS_chapter]

        self.rBtn_aS_allTab = self.findChild(QRadioButton, 'rBtn_aS_allTab')
        self.rBtn_aS_partTab = self.findChild(QRadioButton, 'rBtn_aS_partTab')
        self.list_tab_s = [self.rBtn_aS_allTab, self.rBtn_aS_partTab]

        # RadioButton分组列表
        self.list_rBtn = [self.list_d_f, self.list_s_t, self.list_tab_s]

        # QLineEdit
        self.Edit_aS_docPath = self.findChild(QLineEdit, 'Edit_aS_docPath')
        self.Edit_aS_filePath = self.findChild(QLineEdit, 'Edit_aS_filePath')
        self.list_edit_dfpath = [self.Edit_aS_docPath, self.Edit_aS_filePath]

        self.Edit_aS_table = self.findChild(QLineEdit, 'Edit_aS_table')
        self.Edit_aS_chapter = self.findChild(QLineEdit, 'Edit_aS_chapter')

        # QPushButton
        self.Btn_aS_exec = self.findChild(QPushButton, 'Btn_aS_exec')
        self.Btn_aS_choosePlatform = self.findChild(QPushButton, 'Btn_aS_choosePlatform')

    def update_setting(self):
        """
        从配置文件读取 用户设置数据
        :return:
        """
        self.cfg_to_ui('$.setting.as[?(200<@.id<206)]', self, 'setChecked')
        if se.get_config('$.setting.as[?(@.name=="rBtn_aS_tab")].value')[0]:
            self.cfg_to_ui('$.setting.as[?(205<@.id<208)]', self, 'setChecked')
        self.cfg_to_ui('$.setting.as[?(@.type=="QLineEdit")]', self, 'setText')

    def bindSlots(self):
        """
        给子控件绑定槽函数
        :return:
        """
        # RadioButton
        self.rBtn_aS_doc.clicked.connect(lambda: self.handle_rBtnGrp_1(self.rBtn_aS_doc))
        self.rBtn_aS_file.clicked.connect(lambda: self.handle_rBtnGrp_1(self.rBtn_aS_file))

        self.rBtn_aS_all.clicked.connect(lambda: self.handle_rBtnGrp_2(self.rBtn_aS_all))
        self.rBtn_aS_tab.clicked.connect(lambda: self.handle_rBtnGrp_2(self.rBtn_aS_tab))
        self.rBtn_aS_chapter.clicked.connect(lambda: self.handle_rBtnGrp_2(self.rBtn_aS_chapter))

        self.rBtn_aS_allTab.clicked.connect(lambda: self.handle_rBtnGrp_3(self.rBtn_aS_allTab))
        self.rBtn_aS_partTab.clicked.connect(lambda: self.handle_rBtnGrp_3(self.rBtn_aS_partTab))

        # LineEdit
        self.Edit_aS_docPath.textChanged.connect(self.handle_editGrp_1)
        self.Edit_aS_filePath.textChanged.connect(self.handle_editGrp_1)
        # 给 页码范围输入框添加 正则验证器
        re_validator = qui.QRegExpValidator(qtc.QRegExp(const.PAGES_RANGE_REGEXP))
        self.Edit_aS_table.setValidator(re_validator)
        self.Edit_aS_chapter.setValidator(re_validator)

        # PushButton
        self.Btn_aS_exec.clicked.connect(self.exec)
        self.Btn_aS_choosePlatform.clicked.connect(self.choose_wps_word)

    def filter_rBtn_p(index: int):
        """
        过滤非点击按钮的信号 带上索引
        :return:
        """

        def filter_rBtn(func):
            """
            过滤非点击按钮的信号 【装饰器】
            :param func:
            :return:
            """

            def wrapper(self, wid: QRadioButton):
                """

                :param self:
                :param wid:
                :return:
                """
                # 控件 先状态改变 再进入此函数
                if wid.isChecked():
                    temp_li = self.list_rBtn[index]
                    other = [o for o in temp_li if o != wid]
                    # 自己写互斥 【代码会影响Qt_designer设置的自动互斥效果】
                    for other_ in other:
                        other_.setChecked(False)
                    func(self, wid)
                    # 每次执行完 都把状态记录到config中去
                    self.ui_to_cfg(temp_li, self, 'isChecked', 'as')
                else:
                    # 不能通过点击自身的方式取消选中状态
                    wid.setChecked(True)

            return wrapper

        return filter_rBtn

    @filter_rBtn_p(0)
    def handle_rBtnGrp_1(self, wid: QRadioButton):
        """
        doc _ file 选择处理文件类型的 单选按钮响应函数 只做被选中的响应 其他放到装饰器 filter_rBtn
        :param wid:
        """
        print('handle_doc_file')

    @filter_rBtn_p(1)
    def handle_rBtnGrp_2(self, wid: QRadioButton):
        """
        all _ tab _ chapter 选择处理范围类型的 单选按钮响应函数 只做被选中的响应 其他放到装饰器 filter_rBtn
        只处理按钮 ui 不处理内部数据，交由exec自个儿集中处理
        :param wid:
        """
        # TODO(优化联动算法)
        print('handle_scope_type')
        if wid.objectName() != 'rBtn_aS_tab':
            # 将 tab子项都切换成未选状态
            [te.setChecked(False) for te in self.list_tab_s]
            return
        # 判断信号来源 如果是子项来的 则不更新
        if self.rBtn_aS_allTab.isChecked() or self.rBtn_aS_partTab.isChecked():
            return
        self.cfg_to_ui('$.setting.as[?(205<@.id<208)]', self, 'setChecked')

    @filter_rBtn_p(2)
    def handle_rBtnGrp_3(self, wid: QRadioButton):
        """
        allTab _ partTab 选择处理表格范围的 单选按钮响应函数 只做被选中的响应 其他放到装饰器 filter_rBtn
        :param wid:
        """
        print('handle_tab_scope')
        # 如果是第三组选择tab范围的响应 且此时tab还没被选上，则把 tab选项勾上
        if not self.rBtn_aS_tab.isChecked():
            # setChecked()槽函数 不会发出信号 响应按钮动作，故需要使用click()
            self.rBtn_aS_tab.click()

    def dragEnterEvent(self, a0: qui.QDragEnterEvent) -> None:
        # TODO(改进)
        path = a0.mimeData().text().replace('file:///', '')
        if path.endswith('.docx') or os.path.isdir(path):
            a0.accept()

    def dropEvent(self, a0: qui.QDropEvent) -> None:
        path = a0.mimeData().text().replace('file:///', '')
        if path.endswith('.docx'):
            self.Edit_aS_docPath.setText(path)
            return
        if os.path.isdir(path):
            self.Edit_aS_filePath.setText(path)
            return

    def handle_editGrp_1(self):
        """
        docPath _ filePath
        """
        # 把状态保存到配置文件
        self.ui_to_cfg(self.list_edit_dfpath, self, 'text', 'as')

    def exec(self):
        """
        执行调整操作
        """
        # 弹出进度条提示窗口
        # 执行完给状态栏发射信号
        self.signal_str_int.emit('已完成', 3000)
        # 结束之前 禁用执行按钮

    def choose_wps_word(self):
        """
        弹出设置窗口
        """
        pass
