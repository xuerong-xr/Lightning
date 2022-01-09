"""
Author: xtrs
adjustShapes界面管理
"""
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType
import os.path
from PyQt5 import QtGui as qui
import PyQt5.QtCore as qtc
from PyQt5.QtWidgets import QRadioButton
import const
from GetPathFrame import FileType
# from main.DefaultConfigure.GenerateDefaultConfig import generateDCfg
from SizeAdjustFrame import SizeAdjustFrame
from tool_wid import ToolWid
import adjustShapes as AS
import setting as se

ui_AdjustShapesForm, _ = loadUiType('../UI/AdjustShapesForm.ui')


class AdjustShapesForm(ToolWid, ui_AdjustShapesForm):
    """
    工具窗口
    """
    # 定义信号
    init_signal = qtc.pyqtSignal()
    signal_str = qtc.pyqtSignal(str)
    signal_str_int = qtc.pyqtSignal(str, int)
    # 配置
    config_j = {}

    def __init__(self, parent=None):
        super(AdjustShapesForm, self).__init__(parent)
        self.setupUi(self)
        self.init_signal.emit()
        self.init_UI()

    def init_UI(self):
        """
        初始化
        """
        # 单选按钮
        self.fd_rbtn_list = [self.rBtn_aS_file, self.rBtn_aS_dir]
        self.range_rBtn_list = [self.rBtn_aS_all, self.rBtn_aS_tab, self.rBtn_aS_chapter]
        self.tab_rbtn_list = [self.rBtn_aS_allTab, self.rBtn_aS_partTab]
        # 上面list的list
        self.rBtn_list = [self.fd_rbtn_list, self.range_rBtn_list, self.tab_rbtn_list]
        # 路径edit list
        self.path_edit_list = [self.Edit_aS_filePath, self.Edit_aS_dirPath]
        # 添加尺寸调整Frame
        self.sizeAdjustFrame = SizeAdjustFrame()
        self.size_frame.layout().addWidget(self.sizeAdjustFrame)
        # 设置路径edit的类型
        self.path_frame_1.fileType = FileType.DOCX.value

        # generateDCfg(self)
        se.loadConfig_local(self, 'as_config.json')
        self.update_config()
        self.bindSlots()

    def update_config(self):
        """
        从配置文件读取 用户设置数据
        :return:
        """
        se.cfg_to_ui(self, '$.setting[?(@.type_=="QRadioButton")]', 'setChecked')
        # TODO(tab没点亮时，不点亮子 rBtn)
        if se.get_config(self, '$.setting[?(@.name=="rBtn_aS_tab")].value')[0]:
            se.cfg_to_ui(self, '$.setting[?(19<@.id<22)]', 'setChecked')
        else:
            self.rBtn_aS_allTab.setChecked(False)
            self.rBtn_aS_partTab.setChecked(False)
        se.cfg_to_ui(self, '$.setting[?(@.type_=="QLineEdit")]', 'setText')

    def bindSlots(self):
        """
        给子控件绑定槽函数
        :return:
        """
        # RadioButton
        self.rBtn_aS_file.clicked.connect(lambda: self.handle_rBtnGrp_1(self.rBtn_aS_file))
        self.rBtn_aS_dir.clicked.connect(lambda: self.handle_rBtnGrp_1(self.rBtn_aS_dir))

        self.rBtn_aS_all.clicked.connect(lambda: self.handle_rBtnGrp_2(self.rBtn_aS_all))
        self.rBtn_aS_tab.clicked.connect(lambda: self.handle_rBtnGrp_2(self.rBtn_aS_tab))
        self.rBtn_aS_chapter.clicked.connect(lambda: self.handle_rBtnGrp_2(self.rBtn_aS_chapter))

        self.rBtn_aS_allTab.clicked.connect(lambda: self.handle_rBtnGrp_3(self.rBtn_aS_allTab))
        self.rBtn_aS_partTab.clicked.connect(lambda: self.handle_rBtnGrp_3(self.rBtn_aS_partTab))

        # LineEdit
        self.Edit_aS_filePath.textChanged.connect(lambda: self.handle_editGrp_1(self.Edit_aS_filePath))
        self.Edit_aS_dirPath.textChanged.connect(lambda: self.handle_editGrp_1(self.Edit_aS_dirPath))
        # 给 页码范围输入框添加 正则验证器
        re_validator = qui.QRegExpValidator(qtc.QRegExp(const.PAGES_RANGE_REGEXP))
        self.as_scope_edit.setValidator(re_validator)

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
                # 控件 先状态改变 再进入此函数 * * * * * * * * * * * * * *
                if wid.isChecked():
                    temp_li = self.rBtn_list[index]
                    other = [o for o in temp_li if o != wid]
                    # 自己写互斥 【代码会影响Qt_designer设置的自动互斥效果】
                    for other_ in other:
                        other_.setChecked(False)
                    func(self, wid)
                    # 每次执行完 都把状态记录到config中去
                    se.ui_to_cfg(self, temp_li, 'isChecked')
                else:
                    # 不能通过点击自身的方式取消选中状态
                    wid.setChecked(True)

            return wrapper

        return filter_rBtn

    @filter_rBtn_p(0)
    def handle_rBtnGrp_1(self, wid: QRadioButton):
        """
        *只做状态转变为选中的响应*，原是选中状态，重复点击事件已过滤
        file _ dir 选择处理文件类型的 单选按钮响应函数 其他放到装饰器 filter_rBtn
        :param wid:
        """
        print('handle_doc_file')

    @filter_rBtn_p(1)
    def handle_rBtnGrp_2(self, wid: QRadioButton):
        """
        *只做状态转变为选中的响应*，原是选中状态，重复点击事件已过滤
        all _ tab _ chapter 选择处理范围类型的 单选按钮响应函数 其他放到装饰器 filter_rBtn
        只处理按钮 ui 不处理内部数据，交由exec自个儿集中处理
        :param wid:
        """
        # TODO(优化联动算法)
        print('handle_scope_type')
        if wid.objectName() != 'rBtn_aS_tab':
            # 将 tab子项都切换成未选状态
            [te.setChecked(False) for te in self.tab_rbtn_list]
            return
        # 判断信号来源 如果是子项来的 则不更新
        if self.rBtn_aS_allTab.isChecked() or self.rBtn_aS_partTab.isChecked():
            return
        se.cfg_to_ui(self, '$.setting[?(19<@.id<22)]', 'setChecked')

    @filter_rBtn_p(2)
    def handle_rBtnGrp_3(self, wid: QRadioButton):
        """
        *只做状态转变为选中的响应*，原是选中状态，重复点击事件已过滤
        allTab _ partTab 选择处理表格范围的 单选按钮响应函数 其他放到装饰器 filter_rBtn
        :param wid:
        """
        print('handle_tab_scope')
        # 如果是第三组选择tab范围的响应 且此时tab还没被选上，则把 tab选项勾上
        if not self.rBtn_aS_tab.isChecked():
            # setChecked()槽函数 不会发出信号 响应按钮动作，故需要使用click()
            self.rBtn_aS_tab.click()

    def dragEnterEvent(self, a0: qui.QDragEnterEvent) -> None:
        """
        拖入
        :param a0:
        """
        # TODO(改进)
        path = a0.mimeData().text().replace('file:///', '')
        if path.endswith('.docx') or os.path.isdir(path):
            a0.accept()

    def dropEvent(self, a0: qui.QDropEvent) -> None:
        """
        接收
        :param a0:
        :return:
        """
        path = a0.mimeData().text().replace('file:///', '')
        if path.endswith('.docx'):
            self.Edit_aS_filePath.setText(path)
            return
        if os.path.isdir(path):
            self.Edit_aS_dirPath.setText(path)
            return

    def handle_editGrp_1(self, wid):
        """
        docPath _ filePath
        """
        # 把状态保存到配置文件
        se.ui_to_cfg(self, [wid], 'text')

    def exec(self):
        """
        执行调整操作
        """
        # 弹出进度条提示窗口
        # 如果 range 不为 0 则传入scope
        print('执行')
        # TODO(优化算法)
        path = [edit.text() for edit in self.path_edit_list if
                self.fd_rbtn_list[self.path_edit_list.index(edit)].isChecked()][0]
        print(f'path:{path}')
        if path:
            range_ = [i for i, rBtn in enumerate(self.range_rBtn_list) if rBtn.isChecked()][0]
            print(f'range_:{range_}')
            shapes_size = self.sizeAdjustFrame.shapes_size
            print(shapes_size)
            if range_:
                scope = self.as_scope_edit.text()
                AS.adjust(path, range_, scope=scope, shapes_size=shapes_size)
            else:
                AS.adjust(path, range_, shapes_size=shapes_size)
        # 执行完给状态栏发射信号
        self.signal_str_int.emit('已完成', 3000)
        # 结束之前 禁用执行按钮

    def choose_wps_word(self):
        """
        弹出设置窗口
        """
        pass
