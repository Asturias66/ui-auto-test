import time

from selenium.webdriver.common.by import By

import element_tool
import get_data
from system_select import system_select
from login import login_cicc_cloud
from menu_select import menu_select_1,click_new_order,over_view_order

class Test_review_order():
    @classmethod
    def setup_class(self):
        print('\n *** 初始化-模块 ***')
        # 定义config文件路径
        config_path = 'config/config.json'
        # 获取中金应用云登录账号与登录密码、选择的系统环境
        self.user_account, self.user_password, self.system_name, self.system_env, self.series = get_data.get_config(config_path)


    @classmethod
    def teardown_class(self):
        print('\n ***   清除-模块 ***')

    def test_review_order(self):
        # 登录中金应用云系统
        driver = login_cicc_cloud(self.user_account, self.user_password)
        driver.maximize_window()

        # 设置最长等待时间15秒
        driver.implicitly_wait(15)

        # 选择要使用的系统与环境并进入
        print('尝试进入所选系统')
        driver, alert_text = system_select(driver, self.system_name, self.system_env)
        print('尝试进入所选系统的结果是' + alert_text)
        assert alert_text == 'OK'

        # 选择侧边栏中“订单管理”菜单
        menu_select_1(driver, "订单管理")

        # 点击“订单概览”
        print('尝试进入订单概览页面')
        alert_text = over_view_order(driver)
        print('尝试进入订单概览页面的结果是' + alert_text)
        assert alert_text == '' or alert_text == 'OK'

        # 点击每一页一笔订单
        curent_page_element = driver.find_element(By.CSS_SELECTOR, "ul[class = 'el-pager']>li[class = 'number active']")
        curent_page = int(curent_page_element.text)
        page_element = driver.find_elements(By.CSS_SELECTOR,
                                            "ul[class = 'el-pager']>li[class = 'number']")
        max_page = int(page_element[-1].text)
        while (1):
            check_orders = driver.find_elements(By.XPATH,
                                                "//button[@class = 'el-button el-button--text el-button--small']/span[text()='审阅']")

            for check_order in check_orders:
                print('尝试进入订单')
                driver.execute_script("arguments[0].click();", check_order)
                alert_text = element_tool.get_alert(driver)
                print('尝试进入订单的结果为' + alert_text)
                assert alert_text == '' or alert_text == 'OK'

                time.sleep(2)

                # 获取订单号
                order_id_element = driver.find_element(By.XPATH,
                                                  "//div[@class = 'clearfix']/span[contains(text(),'当前订单')]")

                print(order_id_element.text)

                # 点击返回按钮
                back_button = driver.find_element(By.XPATH,
                                                  "//button[@class = 'el-button el-button--default el-button--mini is-plain']/span[text()=' 返回 ']")
                back_button.click()
                time.sleep(1)

            if curent_page < max_page:
                next_button = driver.find_elements(By.CSS_SELECTOR,
                                                   "button[class = 'btn-next']")
                next_button.click()
                curent_page = curent_page + 1

            if curent_page == max_page:
                break


        time.sleep(5)




