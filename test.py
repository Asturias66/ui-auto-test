import pandas as pd
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import element_tool
import get_data
import new_order
from series_project.xinan import XinAn
from system_select import system_select
from login import login_cicc_cloud
from menu_select import menu_select_1,click_new_order,over_view_order

# 定义config文件路径
config_path = 'config/config.json'
# 获取中金应用云登录账号与登录密码、选择的系统环境
user_account, user_password, system_name, system_env, series = get_data.get_config(config_path)

xinan_data_path = 'data/鑫安.csv'
xintou_data_path = 'data/鑫投.csv'
changying_data_path = 'data/长赢.csv'
ruichi_data_path = 'data/瑞驰.csv'

data_orders = get_data.get_orders(ruichi_data_path)
print(data_orders)

# 登录并打开新建订单页面
driver = new_order.open_new_order(user_account, user_password, system_name, system_env)

for index, order in data_orders.iterrows():
    flag = new_order.new_order(driver,order)
    assert flag == True

# # 设置最长等待时间15秒
# driver.implicitly_wait(15)
#
# # 选择要使用的系统与环境并进入
# driver, alert_text = system_select(driver, system_name, system_env)
# print('尝试进入所选系统')
# assert alert_text == 'OK'
# print('尝试进入所选系统的结果是' + alert_text)
#
# # 选择侧边栏中“订单管理”菜单
# menu_select_1(driver, "订单管理")
#
# # 点击“订单概览”
# alert_text = over_view_order(driver)
# assert alert_text == '' or alert_text == 'OK'
#
# # 点击每一页一笔订单
# curent_page_element = driver.find_element(By.CSS_SELECTOR, "ul[class = 'el-pager']>li[class = 'number active']")
# curent_page = int(curent_page_element.text)
# page_element = driver.find_elements(By.CSS_SELECTOR,
#                                     "ul[class = 'el-pager']>li[class = 'number']")
# max_page = int(page_element[-1].text)
# while (1):
#     check_orders = driver.find_elements(By.XPATH,
#                                         "//button[@class = 'el-button el-button--text el-button--small']/span[text()='审阅']")
#
#     for check_order in check_orders:
#         driver.execute_script("arguments[0].click();", check_order)
#         alert_text = element_tool.get_alert(driver)
#         assert alert_text == '' or alert_text == 'OK'
#
#         time.sleep(2)
#
#         # 点击返回按钮
#         back_button = driver.find_element(By.XPATH,
#                              "//button[@class = 'el-button el-button--default el-button--mini is-plain']/span[text()=' 返回 ']")
#         back_button.click()
#         time.sleep(1)
#
#
#     if curent_page < max_page:
#         next_button = driver.find_elements(By.CSS_SELECTOR,
#                                            "button[class = 'btn-next']")
#         next_button.click()
#         curent_page = curent_page + 1
#
#     if curent_page == max_page:
#         break
#
# time.sleep(5)