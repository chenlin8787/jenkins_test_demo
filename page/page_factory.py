"""
统一入口类(集中封装页面对象的实例化操作)
"""
from page.index_page import IndexPage
from page.search_page import SearchPage


class PageFactory(object):  # 1. 对照文件名定义类名
    def __init__(self, driver):  # 封装代码过程中, 如果需要驱动对象, 直接编写此方法
        self.driver = driver

    def index_page(self):  # 2. 对应页面的文件名定义方法名
        """设置首页"""
        return IndexPage(self.driver)  # 3. 直接返回页面实例化的对象

    def search_page(self):
        """搜索页面"""
        return SearchPage(self.driver)
