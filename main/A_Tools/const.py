"""
Author: xtrs
常量模块
"""
# import sys
#
#
# class _Const:
#     # 自定义异常处理
#     class ConstError(PermissionError):
#         pass
#
#     class ConstCaseError(ConstError):
#         pass
#
#     # 重写 __setattr__() 方法
#     def __setattr__(self, name, value):
#         if name in self.__dict__:  # 已包含该常量，不能二次赋值
#             raise self.ConstError("Can't change const {0}".format(name))
#         if not name.isupper():  # 所有的字母需要大写
#             raise self.ConstCaseError("const name {0} is not all uppercase".format(name))
#         self.__dict__[name] = value
#
#
# # 将系统加载的模块列表中的 constant 替换为 _Const() 实例
# sys.modules[__name__] = _Const()


# 页码范围正则表达式常量
PAGES_RANGE_REGEXP = r'^((\d{1,4}|(\d{1,4}-\d{1,4}))[,，.])*(\d{1,4}|(\d{1,4}-\d{1,4}))?$'
TAG_INPUT_REGEXP = r'^(([^\s;；]{1,6}[;；])*[^\s;；]{1,6})?$'
# 1cm = 28.346磅
CM_POUND_UNIT = 28.346
# PLATFORM
PLATFORM_WPS_WENZI = 'kwps.Application'
PLATFORM_OFFICE_WORD = 'word.Application'

# + + + + + + + + + + + + + + + + + + + + + + + + + ++ + + + + + + + + + + + + + + + + + + + + + + + + + +

SET_DEFAULT = {
    'setting': {
        'main': [
            {
                'id': 101,
                'name': 'rBtn_aS_doc',
                'type': 'QRadioButton',
                'value': True
            },
            {
                'id': 102,
                'name': 'rBtn_aS_file',
                'type': 'QRadioButton',
                'value': False
            },
            {
                'id': 103,
                'name': 'rBtn_aS_doc',
                'type': 'QRadioButton',
                'value': False
            }
        ],
        'as': [
            {
                'id': 201,
                'name': 'rBtn_aS_doc',
                'type': 'QRadioButton',
                'value': True
            },
            {
                'id': 202,
                'name': 'rBtn_aS_file',
                'type': 'QRadioButton',
                'value': False
            },
            {
                'id': 203,
                'name': 'rBtn_aS_all',
                'type': 'QRadioButton',
                'value': True
            },
            {
                'id': 204,
                'name': 'rBtn_aS_tab',
                'type': 'QRadioButton',
                'value': False
            },
            {
                'id': 205,
                'name': 'rBtn_aS_chapter',
                'type': 'QRadioButton',
                'value': False
            },
            {
                'id': 206,
                'name': 'rBtn_aS_allTab',
                'type': 'QRadioButton',
                'value': True
            },
            {
                'id': 207,
                'name': 'rBtn_aS_partTab',
                'type': 'QRadioButton',
                'value': False
            },
            {
                'id': 208,
                'name': 'Edit_aS_docPath',
                'type': 'QLineEdit',
                'value': ''
            },
            {
                'id': 209,
                'name': 'Edit_aS_filePath',
                'type': 'QLineEdit',
                'value': ''
            }

        ],
        'template': [

        ],
        'data': [

        ],
        'photo': [

        ],
        'tool': [

        ]},
    'other': {
    }
}
