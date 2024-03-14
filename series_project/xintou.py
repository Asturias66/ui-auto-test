# 确保已安装必要的第三方库
import time

from selenium.webdriver.common.by import By
import pandas as pd

# 导入元素选择填充工具函数
import element_tool

# 导入父类
from series_project.series import Series

class XinTou(Series):
    def __init__(self, order, driver):
        super().__init__(order, driver)
        self.order = order
        self.driver = driver
        # 获取页面空白处元素,方面之后操作进行点击
        self.element_blank = driver.find_element(By.XPATH, "//body")

    def fill_order(self):
        # 调用父类方法填写交易要素
        super().fill_transaction_elements()
        time.sleep(2)

        # 填写对客价
        self.fill_client_price()
        self.element_blank.click()

        super().fill_client_info()

    # 填写对客价
    def fill_client_price(self):
        client_price = self.order['对客价']
        element_tool.fill_inputbox(client_price, element_tool.get_element(self.driver, "对客价"))