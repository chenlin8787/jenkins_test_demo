# 导包
from appium import webdriver


def get_driver():
    """获取驱动对象方法"""

    # 实例化驱动对象
    capabilities = {
        "platformName": "Android",  # 设备类型(Android / iOS)
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "模拟器",  # 设备名称
        "appPackage": "com.android.settings",  # 待测应用的包名
        "appActivity": ".Settings",  # 待测应用的启动名
        # 解决中文无法输入问题
        'resetKeyboard': True,
        'unicodeKeyboard': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver  # 为提供给外界调用, 需要添加返回值
