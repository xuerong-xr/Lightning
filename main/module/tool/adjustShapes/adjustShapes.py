"""
Author: xtrs
封装 批量调整docx文件中图片大小 的接口
"""
import re
from docx import Document
from docx.shared import Cm
import const
from setting import AdjShaSet
import win32com.client as w32


class DocUnit:
    """
    用来实例化存储文档信息的实例
    """

    def __init__(self, path: str):
        self.path = path
        self.docx = None
        self.dispatch = None


def getDocUnit(path: str):
    """

    :param path: 路径
    :return:
    """
    temp_bool = path.split('.')[-1] == 'docx'
    if temp_bool:
        doc_unit = DocUnit(path)
        doc_unit.docx = Document(path)
        return doc_unit
    else:
        print('不是Word文档')


class AdjustShapes:
    """
    调整图片
    """

    @staticmethod
    def __handle_single(text):
        # 遍历单个数字数组,转换成数字类型，去掉区间范围内的、去重、去零、去空值，返回一个新的数组，并加入到区间数组中，组合成最终不连续区间数组
        # 拿到拆分得到的列表
        singles = re.split(r'[,，.]', text)
        # 第一次循环，去重，去掉空值、零值
        new_singles = []
        for single in singles:
            if single not in new_singles and single not in ('', '0'):
                new_singles.append(single)
        # print(new_singles)
        # 第二次循环 转换成数字类型
        new_singles = [int(i) for i in new_singles]
        return new_singles

    @staticmethod
    def __handle_secs(text):
        # 拿到区间迭代器
        temp_sections = re.finditer(r'(\d+)-(\d+)', text)
        # 将获得的区间（迭代器）转换成 区间（可用interval）组成的数组 判断是否重叠，将重叠部抠除
        new_secs = []
        for sec in temp_sections:
            num1 = min(int(sec.group(1)), int(sec.group(2)))
            num2 = max(int(sec.group(1)), int(sec.group(2)))
            new_secs.append([num1, num2])
        # 排序,合并重叠部分
        new_secs.sort()
        ran_s = []
        for new_sec in new_secs:
            if len(ran_s) == 0 or ran_s[-1][0] > new_sec[1]:
                ran_s.append(new_sec)
            else:
                ran_s[-1][1] = max(ran_s[-1][1], new_sec[1])
        # 将区间（假）转换成range
        # 效率测试(花费时间) map<推导式<for循环≈list_d_f(map)
        new_ranges = [range(x[0], x[1] + 1) for x in ran_s]
        return new_ranges

    @classmethod
    def pagesTextToRanges(cls, text: str):
        """
        页码范围 转区间数组‘[range1，range2，..]’
        :param text:页码范围
        :return: 区间数组
        """
        if not re.search(const.PAGES_RANGE_REGEXP, text):
            print('页码描述不符合规范!')
            return
        # 如果是空字符串 返回
        if not text:
            print('空字符串')
            return
        # 搜索是否有单个数字
        hasSgl = re.search(r'[,，.]', text)
        # 搜索是否有区间
        hasSecs = re.search(r'(\d+)-(\d+)', text)
        # 申明返回的range
        pagesRanges = []
        # 如果只有单个数字
        if not hasSecs:
            pagesRanges.append(cls.__handle_single(text))
            # 如果只有区间
        elif hasSecs and not hasSgl:
            pagesRanges = cls.__handle_secs(text)
        # 如果两个都有（不会出现两个都没有的情况）
        else:
            # 替换掉原字符串中的区间，获取单个数字组成的数组
            temp = re.sub(r'\d+-\d+', '', text)
            sglNums = cls.__handle_single(temp)
            secs = cls.__handle_secs(text)
            new_sglNums = []
            # 去掉存在于区间内的数字
            for sglNum in sglNums:
                for new_sec in secs:
                    if sglNum not in new_sec:
                        new_sglNums.append(sglNum)
            # 如果最后还剩下一些数字，把他们组成的数组加到区间数组里 返回最终的区间数组
            if len(new_sglNums) > 0:
                secs.append(new_sglNums)
            pagesRanges = secs
        print(pagesRanges)
        return pagesRanges

    @staticmethod
    def adjust_shapes_all(doc_unit: DocUnit, shapes_h: float = 6.0, shapes_w: float = 8.0):
        """

        :param doc_unit:
        :param shapes_h:
        :param shapes_w:
        """
        doc = doc_unit.docx
        shapes = doc.inline_shapes
        shapes_num = len(shapes)
        for shape in shapes:
            shape.height = Cm(shapes_h)
            shape.width = Cm(shapes_w)
        try:
            doc.save(doc_unit.path)
        except PermissionError:
            print('权限异常,关闭Word文档后重试！')
        else:
            print('恭喜你！已调整{}个图片。高{}cm，宽{}cm'.format(shapes_num, shapes_h, shapes_w))
        pass

    def __startApp(func):
        def wrapper(doc_unit: DocUnit, **kwargs):
            """
            装饰器
            :param doc_unit:
            :param kwargs:
            :return:
            """
            # 启动程序(判断WPS 还是 office)
            app = w32.DispatchEx(AdjShaSet.platform)
            # 打开文档
            doc_unit.dispatch = app.Documents.Open(doc_unit.path)
            temp_args = {}
            if 'scope' in kwargs.keys():
                temp_args['scope'] = kwargs['scope']
            if 'shapes_h' in kwargs.keys():
                temp_args['shapes_h'] = kwargs['shapes_h'] * const.CM_POUND_UNIT
            else:
                temp_args['shapes_h'] = 6 * const.CM_POUND_UNIT
            if 'shapes_w' in kwargs.keys():
                temp_args['shapes_w'] = kwargs['shapes_w'] * const.CM_POUND_UNIT
            else:
                temp_args['shapes_w'] = 8 * const.CM_POUND_UNIT
            print('已包装')
            try:
                func(doc_unit, **temp_args)
                doc_unit.dispatch.Save()
                doc_unit.dispatch.Close()
            except Exception as e:
                print(e)
            finally:
                app.Quit()
                print('已退出应用')

        return wrapper

    @staticmethod
    @__startApp
    def adjust_shapes_chapter(doc_unit: DocUnit, *, scope: list = (), shapes_h, shapes_w):
        """

        :param doc_unit:
        :param scope:
        :param shapes_h:
        :param shapes_w:
        """
        if len(scope) == 0:
            print('章节范围不可为空')
            return
        doc = doc_unit.dispatch
        sections = doc.sections
        # 要调整的 section 集合
        for i, secs in enumerate(sections):
            for scope_ in scope:
                if i + 1 in scope_:
                    temp_shapes = secs.Range.InlineShapes
                    for temp_shape in temp_shapes:
                        temp_shape.LockAspectRatio = False
                        temp_shape.Height = shapes_h
                        temp_shape.Width = shapes_w

    @staticmethod
    @__startApp
    def adjust_shapes_tab(doc_unit: DocUnit, *, scope: list = (), shapes_h, shapes_w):
        """
        调整表格中的图片大小
        :param doc_unit:
        :param scope:为空时，调整所有tab
        :param shapes_h:
        :param shapes_w:
        """
        doc = doc_unit.dispatch
        tables = doc.tables
        if len(scope) == 0:
            for table in tables:
                temp_shapes = table.Range.InlineShapes
                for temp_shape in temp_shapes:
                    temp_shape.LockAspectRatio = False
                    temp_shape.Height = shapes_h
                    temp_shape.Width = shapes_w
            return
        # 要调整的 tab 集合
        for i, table in enumerate(tables):
            for scope_ in scope:
                if i + 1 in scope_:
                    temp_shapes = table.Range.InlineShapes
                    for temp_shape in temp_shapes:
                        temp_shape.LockAspectRatio = False
                        temp_shape.Height = shapes_h
                        temp_shape.Width = shapes_w


if __name__ == '__main__':
    ran = AdjustShapes.pagesTextToRanges('1,2,4-10')
    # doc1 = getDocUnit(r'C:\Users\学容xr\Desktop\测试文件夹\新建DOCX文档1.docx')
    # AdjustShapes.adjust_shapes_all(doc1)
    # AdjustShapes.adjust_shapes_tab(doc1, scope=ran, shapes_h=5.2)
    # AdjustShapes.adjust_shapes_chapter(doc1, scope=ran, shapes_h=5.6)
