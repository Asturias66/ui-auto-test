# 确保已安装必要的第三方库
from selenium.webdriver.common.by import By
import pandas as pd

# 导入元素选择填充工具函数
import element_tool

# 导入父类
from series_project.series import Series

class ChangYing(Series):
    def __init__(self, order, driver):
        super().__init__(order, driver)
        self.order = order
        self.driver = driver
        # 获取页面空白处元素,方面之后操作进行点击
        self.element_blank = driver.find_element(By.XPATH, "//body")

    def fill_order(self):
        # 调用父类方法填写交易要素
        super().fill_transaction_elements()

        sale_incentive = self.order['销售激励']
        # 填写销售激励
        element_tool.fill_inputbox(sale_incentive, element_tool.get_element(self.driver, "销售激励"))
        self.element_blank.click()

        self.fill_option()

        super().fill_client_info()

    # 填写长赢期权相关内容
    def fill_option(self):
        option_structure_type = self.order['期权结构']

        element_tool.select_checkbox(self.driver, option_structure_type,
                                     element_tool.get_element(self.driver, "期权结构"))

        if option_structure_type == '鲨鱼鳍':
            barrier_type = self.order['障碍类型']

            element_tool.select_checkbox(self.driver, barrier_type,
                                         element_tool.get_element(self.driver, "障碍类型"))

            if barrier_type == '单鲨':
                option_exercise_type = self.order['行权方向']
                element_tool.select_checkbox(self.driver, option_exercise_type,
                                             element_tool.get_element(self.driver, "行权方向"))
            else:
                pass

        option_start_date = self.order['标的期初价格观察日']
        element_tool.select_calender(self.driver, option_start_date,
                                                     element_tool.get_element(self.driver, "标的期初价格观察日"))

        option_end_date = self.order['标的期末价格观察日']
        element_tool.select_calender(self.driver, option_end_date,
                                                     element_tool.get_element(self.driver, "标的期末价格观察日"))

        knockout_type = self.order['敲出观察频率']
        element_tool.select_checkbox(self.driver, knockout_type,
                                     element_tool.get_element(self.driver, "敲出观察频率"))

        ticker_name = self.order['挂钩标的']
        element_tool.fill_input_search(self.driver,ticker_name,
                                       element_tool.get_element(self.driver, "挂钩标的"))

        price_type = self.order['价格类型']
        element_tool.select_checkbox(self.driver, price_type,
                                     element_tool.get_element(self.driver, "价格类型"))

        # price_trigger_type = self.order['价格比较方式']
        # element_tool.select_checkbox(self.driver, price_trigger_type,
        #                              element_tool.get_element(self.driver, "价格比较方式"))

        basis = self.order['基准收益率']
        element_tool.fill_inputbox(basis, element_tool.get_element(self.driver, "基准收益率"))

        participate_rate = self.order['参与率']
        element_tool.fill_inputbox(participate_rate, element_tool.get_element(self.driver, "参与率"))

        knockout_price = self.order['敲出价格']
        element_tool.fill_inputbox(knockout_price, element_tool.get_element(self.driver, "敲出价格"))

        exercise_price = self.order['执行价格']
        element_tool.fill_inputbox(exercise_price, element_tool.get_element(self.driver, "执行价格"))

        knockout_intere_rate = self.order['敲出收益率']
        element_tool.fill_inputbox(knockout_intere_rate, element_tool.get_element(self.driver, "敲出收益率"))

        minimum_benchmark = self.order['最低参考业绩比较基准']
        element_tool.fill_inputbox(minimum_benchmark, element_tool.get_element(self.driver, "最低参考业绩比较基准"))

        maximum_benchmark = self.order['潜在最高参考业绩比较基准']
        element_tool.fill_inputbox(maximum_benchmark, element_tool.get_element(self.driver, "潜在最高参考业绩比较基准"))

        is_interest_rate_annualized = self.order['是否年化收益率']
        element_tool.select_checkbox(self.driver, is_interest_rate_annualized,
                                     element_tool.get_element(self.driver, "是否年化收益率"))

        if not pd.isnull(is_interest_rate_annualized):
            interest_rate = self.order['计息基准']
            element_tool.select_checkbox(self.driver,interest_rate,
                                         element_tool.get_element(self.driver, "计息基准"))



