# 确保已安装必要的第三方库
from selenium.webdriver.common.by import By
import time

import element_tool

# 该字典用来维护excel中输入的系统环境与中金应用云中的系统环境名称进行对应
system_dic = {'无双dev':['无双系统'],
              '无双uat':['无双-场外衍生品簿记系统'],
              '金元宝dev':['金元宝-DEV'],
              '金元宝uat':['金元宝-UAT']
              }

# 选择对应的系统
def system_select(driver,system_name,system_env):
    elements = driver.find_elements(By.CSS_SELECTOR,"div[class = 'desktop-item']")
    for element in elements:
        if element.text in system_dic[system_name + system_env]:
            element_jyb_uat = element
            break
    element_jyb_uat.click()
    time.sleep(5)

    # 根据句柄切换当前窗口，切换到金元宝系统中
    for handle in driver.window_handles:
        # 先切换到该窗口
        driver.switch_to.window(handle)
        # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
        if '金元宝' in driver.title:
            # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
            break

    alert_text = element_tool.get_alert(driver)

    return driver,alert_text