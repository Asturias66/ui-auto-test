# 确保已安装必要的第三方库
import time

from selenium.webdriver.common.by import By
import pandas as pd

# 导入元素选择填充工具函数
import element_tool

# 导入父类
from series_project.series import Series

class RuiChi(Series):
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

        self.fill_rate()
        self.element_blank.click()

        super().fill_client_info()

    # 填写费率相关要素
    def fill_rate(self):
        package_price = self.order['业绩计提基准']
        element_tool.fill_inputbox(package_price, element_tool.get_element(self.driver, "业绩计提基准"))

        subscription_rate = self.order['认购费率']
        element_tool.fill_inputbox(subscription_rate, element_tool.get_element(self.driver, "认购费率"))

        fixed_IA_fee_rate = self.order['基础投顾费率']
        element_tool.fill_inputbox(fixed_IA_fee_rate, element_tool.get_element(self.driver, "基础投顾费率"))

        fixed_sales_fee_rate = self.order['销售部门分摊基础投顾费比例']
        element_tool.fill_inputbox(fixed_sales_fee_rate, element_tool.get_element(self.driver, "销售部门分摊基础投顾费比例"))

        surplus_IA_fee_rate = self.order['超额投顾费比例']
        element_tool.fill_inputbox(surplus_IA_fee_rate,
                                   element_tool.get_element(self.driver, "超额投顾费比例"))

        surplus_sales_fee_rate = self.order['销售部门分摊超额投顾费比例']
        element_tool.fill_inputbox(surplus_sales_fee_rate,
                                   element_tool.get_element(self.driver, "销售部门分摊超额投顾费比例"))




