"""
搜索测试用例
"""
import time
import pytest

from read_data.read_yaml import build_data_func
from page.page_factory import PageFactory
from utils import get_driver


class TestSearch(object):
    """搜索测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = get_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 实例化统一入口类
        yield  # 结束操作
        time.sleep(3)
        self.driver.quit()  # 退出驱动对象

    # def test_func(self):
    #     """搜索测试方法"""
    #
    #     self.page_factory.index_page().click_search_btn()  # 点击搜索按钮跳转搜索页面
    #     self.page_factory.search_page().input_search_bar('黑马程序员')  # 输入内容搜索结果

    @pytest.mark.parametrize('text', build_data_func())  # 1.调用参数化方法, 传入测试数据
    def test_func(self, text):  # 2.声明参数
        """搜索测试方法"""

        self.page_factory.index_page().click_search_btn()  # 点击搜索按钮跳转搜索页面
        self.page_factory.search_page().input_search_bar(text)  # 输入内容搜索结果 # 3. 调用参数
