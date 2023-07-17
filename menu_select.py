# 确保已安装必要的第三方库
from selenium.webdriver.common.by import By
import time

import element_tool


# 选择侧边栏一级菜单(先点击订单管理，再点击新建订单)
def menu_select_1(driver,menu_name):
    elements = driver.find_elements(By.CSS_SELECTOR, "div[class='el-submenu__title']")
    for element in elements:
        if element.text == menu_name:
            element_manage_order = element
    element_manage_order.click()
    time.sleep(1)

# 点击“新建订单”
def click_new_order(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, "a[href='/sp-frontend/order/newbook']")
    for element in elements:
        print(element.text)
        if element.text == "新建订单":
            element_new_order = element
    element_new_order.click()
    alert_text = element_tool.get_alert(driver)
    time.sleep(1)
    return alert_text

# 点击“订单概览”
def over_view_order(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, "a[href='/sp-frontend/order/overview']")
    for element in elements:
        print(element.text)
        if element.text == "订单概览":
            element_new_order = element
    element_new_order.click()
    alert_text = element_tool.get_alert(driver)
    time.sleep(1)
    return alert_text