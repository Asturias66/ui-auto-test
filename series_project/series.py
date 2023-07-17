# 确保已安装必要的第三方库
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 导入元素选择填充工具函数
import element_tool

class Series:
    def __init__(self,order,driver):
        self.order = order
        self.driver = driver
        # 获取页面空白处元素,方面之后操作进行点击
        self.element_blank = driver.find_element(By.XPATH, "//body")

    # 填写交易要素
    def fill_transaction_elements(self):
        # 获取表格中的订单数据
        salers = self.order['销售人员'].split('、')
        product_type = self.order['业务类型']
        series_and_product = self.order['产品名称']
        calendar = self.order['交易日历']
        ccy = self.order['结算货币']
        raise_start_date = self.order['募集起始日']
        raise_end_date = self.order['募集结束日']
        value_date = self.order['成立日']
        due_date = self.order['到期日']
        trade_days = self.order['期限']
        sales_channel = self.order['认购方式']
        raise_start_point = self.order['散户募集起征点/元']
        code = self.order['代码']
        remark = self.order['备注']
        client_pay_day = self.order['客户打款日']
        risk_rank = self.order['风险等级']

        # 对于销售人员进行选择
        element_tool.select_checkbox(self.driver,salers,element_tool.get_element(self.driver,"销售人员"))
        self.element_blank.click()

        if not pd.isnull(code):
            # 填写代码
            element_tool.fill_inputbox(code, element_tool.get_element(self.driver, "代码"))

        if not pd.isnull(risk_rank):
            # 选择风险等级
            element_tool.select_checkbox(self.driver, risk_rank, element_tool.get_element(self.driver, "风险等级"))

        if not pd.isnull(remark):
            # 填写备注
            element_tool.fill_inputbox(remark, element_tool.get_element(self.driver, "备注"))

        # 选择业务类型
        element_tool.select_checkbox(self.driver,product_type,element_tool.get_element(self.driver,"业务类型"))

        # 选择产品名称
        element_tool.select_checkbox(self.driver,series_and_product, element_tool.get_element(self.driver,"产品名称"))

        # 选择交易日历
        element_tool.select_checkbox(self.driver, calendar, element_tool.get_element(self.driver,"交易日历"))

        # 选择结算货币
        element_tool.select_checkbox(self.driver, ccy, element_tool.get_element(self.driver, "结算货币"))

        if product_type == '募集':
            # 选择募集起始日
            element_tool.select_calender(self.driver, raise_start_date, element_tool.get_element(self.driver, "募集起始日"))

            # 选择募集结束日
            element_tool.select_calender(self.driver, raise_end_date, element_tool.get_element(self.driver, "募集结束日"))

            # 填写散户募集起征点
            element_tool.fill_inputbox(raise_start_point, element_tool.get_element(self.driver, "散户募集起征点/元"))
            self.element_blank.click()

        if product_type == '定制':
            # 选择客户打款日
            element_tool.select_calender(self.driver, client_pay_day,
                                         element_tool.get_element(self.driver, "客户打款日"))

        # 选择成立日
        element_tool.select_calender(self.driver, value_date, element_tool.get_element(self.driver, "成立日"))

        # 选择到期日
        if not pd.isnull(due_date):
            element_tool.select_calender(self.driver, due_date, element_tool.get_element(self.driver, "到期日"))

        # 填写期限
        if not pd.isnull(trade_days):
            element_tool.fill_inputbox(trade_days, element_tool.get_element(self.driver, "期限"))
            self.element_blank.click()

        # 选择认购方式
        element_tool.select_checkbox(self.driver, sales_channel, element_tool.get_element(self.driver, "认购方式"))




    # 填写客户信息
    def fill_client_info(self):
        product_type = self.order['业务类型']
        target_raise_amount = self.order['预计募集规模上限']
        renewal_amount = self.order['源自续期金额']

        client_name = self.order['客户全称']

        if not pd.isnull(self.order['资金账户']):
            account = str(int(self.order['资金账户']))
        else:
            account = None

        client_amount = self.order['新认购金额']

        sequel_choice = self.order['续作标志']
        rate_pay_choice = self.order['利息支付标志']
        sale_dep = self.order['销售部门']
        sale_province = self.order['销售省份']
        distinct_business = self.order['地区/营业部(仅供参考)']
        IC_contact = self.order['IC联系人']
        IC_email = self.order['邮箱']



        if product_type == '募集':
            # 填写预计募集规模上限
            element_tool.fill_inputbox(target_raise_amount, element_tool.get_element(self.driver, "预计募集规模上限"))


        if product_type == '定制':
            # 填写客户全称
            element_tool.fill_input_search(self.driver,client_name,element_tool.get_element(self.driver, "客户全称"))

            # 选择资金账户
            element_tool.select_checkbox(self.driver, account, element_tool.get_element(self.driver, "资金账户"))

            # 填写新认购金额
            element_tool.fill_inputbox(client_amount,element_tool.get_element(self.driver, "新认购金额"))

        # 填写源自续期金额
        element_tool.fill_inputbox(renewal_amount, element_tool.get_element(self.driver, "源自续期金额"))

        if not pd.isnull(sequel_choice):
            # 填写续作标志
            element_tool.select_checkbox(self.driver,sequel_choice,element_tool.get_element(self.driver, "续作标志"))

        if not pd.isnull(rate_pay_choice):
            # 填写利息支付标志
            element_tool.select_checkbox(self.driver, rate_pay_choice,
                                         element_tool.get_element(self.driver, "利息支付标志"))

        # 填写销售部门
        element_tool.select_checkbox(self.driver, sale_dep, element_tool.get_element(self.driver, "销售部门"))

        if not pd.isnull(sale_province):
            # 销售省份
            element_tool.select_checkbox(self.driver,sale_province,element_tool.get_element(self.driver, "销售省份"))

        if not pd.isnull(distinct_business):
            # 地区/营业部
            element_tool.select_checkbox(self.driver, distinct_business, element_tool.get_element(self.driver, "地区/营业部(仅供参考)"))

        if not pd.isnull(IC_contact):
            # 填写IC联系人
            element_tool.fill_inputbox(IC_contact, element_tool.get_element(self.driver, "IC联系人"))

        if not pd.isnull(IC_email):
            # 填写邮箱
            element_tool.fill_inputbox(IC_email, element_tool.get_element(self.driver, "邮箱"))

    # 提交订单
    def save_order(self,choice):
        button_element = self.driver.find_element(By.XPATH,"//button[@class = 'el-button diy-margin-top save-button el-button--primary el-button--small']/span[text()='验证后提交']")
        button_element.click()
        time.sleep(2)

        if choice == 'draft':
            draft_button_element = self.driver.find_element(By.XPATH,
                                                            "//button[@class = 'el-button el-button--info el-button--mini']/span[text()='暂存为草稿']")
            draft_button_element.click()

        if choice == 'submit':
            draft_button_element = self.driver.find_element(By.XPATH,
                                                            "//button[@class = 'el-button el-button--info el-button--mini']/span[text()='提交到FIOP复核']")
            draft_button_element.click()

