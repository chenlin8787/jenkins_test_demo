"""
搜索页面
"""

import page
from base.base_page import BasePage


class SearchPage(BasePage):
    # 注意: By.xxx 才能反向导包
    # 1. 使用 By方式将目标元素的定位信息封装成属性
    # search_bar = (By.ID, 'android:id/search_src_text')  # 搜索框

    search_bar = page.search_bar  # 搜索框

    # 2.根据目标元素的操作类型 + 元素名称得出封装方法名
    def input_search_bar(self, text):
        """输入搜索框方法"""
        # 3. 通过基类继承, 调用基类的元素定位方法, 并实现元素操作
        # 注意: 方法封装过程中, 不能写固定值, 元素输入方法最好传参
        # self.find_element_func(self.search_bar).send_keys(text)
        # 调用基类封装的输入方法(传入元素对象, 要输入的内容)
        # self.input_func(self.find_element_func(self.search_bar), text)
        # 传入写在__init__.py文件中的元素定位属性值
        self.input_func(self.find_element_func(self.search_bar), text)
