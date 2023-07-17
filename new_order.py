from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import get_data
from login import login_cicc_cloud
from menu_select import menu_select_1, click_new_order
from system_select import system_select
from series_project.ruichi import RuiChi
from series_project.xinan import XinAn
from series_project.xintou import XinTou
from series_project.changying import ChangYing

# 打开新建菜单页面
def open_new_order(user_account,user_password,system_name,system_env):
    # 登录中金应用云系统
    driver = login_cicc_cloud(user_account, user_password)
    driver.maximize_window()

    # 选择要使用的系统与环境并进入
    print('尝试进入所选系统')
    driver, alert_text = system_select(driver, system_name, system_env)
    print('尝试进入所选系统的结果是' + alert_text)
    assert alert_text == 'OK' or alert_text == ''

    # 选择侧边栏中“订单管理”菜单
    menu_select_1(driver, "订单管理")

    # 点击“新建订单”
    print('尝试进入新建订单页面')
    alert_text = click_new_order(driver)
    print('尝试进入新建订单页面的结果是' + alert_text)
    assert alert_text == '' or alert_text == 'OK'

    return driver

# 添加订单方法
def new_order(driver,order):
    # 获取当前测试的订单数据
    print(order)

    # 初始化类
    if '鑫安' in order['产品名称']:
        booking_order = XinAn(order, driver)
    if '鑫投' in order['产品名称']:
        booking_order = XinTou(order, driver)
    if '长赢' in order['产品名称']:
        booking_order = ChangYing(order, driver)
    if '瑞驰' in order['产品名称']:
        booking_order = RuiChi(order, driver)

    # 填写订单
    booking_order.fill_order()
    # 提交订单
    booking_order.save_order('submit')

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,
                                                                      "//button[@class = 'el-button el-button--primary el-button--small is-plain']/span[text()=' 新建订单 ']")))

    # 判断是否回到概览页面决定提交是否成功
    try:
        print("新建订单成功")
    except:
        print("新建订单失败")
        return False

    new_order_button = driver.find_element(By.XPATH,
                                           "//button[@class = 'el-button el-button--primary el-button--small is-plain']/span[text()=' 新建订单 ']")

    driver.execute_script("arguments[0].click();", new_order_button)

    return True