# 确保已安装必要的第三方库
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# 定义中金应用云初始链接
url_cicc_cloud = r'https://eappuat.cicc.group/selfcare/#/index/selfcare/my'

# 存储cookie文件的路径
cookie_path = "cookie/cookie.json"

#登录中金应用云平台
def login_cicc_cloud(user_account,user_password):
    # 指定浏览器为chrome，需先把selenium的chromeDriver放在python安装目录
    driver = webdriver.Chrome()
    driver.get(url_cicc_cloud)
    time.sleep(2)

    # # 若cookie有效，则直接登入系统，不需要输入用户名与密码
    # verify_flag,driver = verify_cookies(driver)
    # if verify_flag == True:      # 若cookie有效，则直接返回driver
    #     print("cookie有效，直接进入系统")
    #     return driver

    # 点击“账号登录”按钮
    elements = driver.find_elements(By.CSS_SELECTOR, ".para-btn-login")
    for element in elements:
        print(element.text)
        if element.text == "账号登录":
            element_login_by_account = element
    element_login_by_account.click()
    time.sleep(1)

    # 输入账号与密码

    # 获取账号输入框组件，填写账号
    elements = driver.find_elements(By.CSS_SELECTOR,
                                    "#username > div.content-box > div:nth-child(1) "
                                    "> div.para-input-content > div > input[type=text]")
    input_account = elements[0]
    input_account.send_keys(user_account)

    # 获取密码输入框组件，填写密码
    elements = driver.find_elements(By.CSS_SELECTOR,
                                    "#username > div.content-box > div:nth-child(2) "
                                    "> div.para-input-content > div > input[type=password]")
    input_password = elements[0]
    input_password.send_keys(user_password)

    # 点击“账号登录”按钮
    elements = driver.find_elements(By.CSS_SELECTOR, "#username > button")
    for element in elements:
        print(element.text)
        if element.text == "账号登录":
            element_login_by_account = element
    element_login_by_account.click()
    time.sleep(3)

    # 获取本次登录的cookie
    cookie_login = driver.get_cookies()

    print("登陆后获取的cookie %s" % cookie_login)

    # 存储本次登录的cookie
    # save_cookies(cookie_login)

    return driver


# 校验cookie
def verify_cookies(driver):
    # 打开cookie存储的json文件
    json_file = open("cookie/cookie.json", "r")

    # 获取文件中存储的cookie
    cookies = json.load(json_file)

    # 清空已有的cookie
    driver.delete_all_cookies()


    for cookie in cookies:
        cookie_list = {
            'domain': 'eappuat.cicc.group',
            'name': cookie["name"],
            'value': cookie["value"],
            "expires": "",
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False,
        }

        # 向浏览器中添加cookie
        print("添加cookie： %s  ： %s  ： %s" % (cookie["name"], cookie["value"], cookie["domain"]))
        driver.add_cookie(cookie)

    # 关闭json文件
    json_file.close()

    # 打开中金应用云网页
    driver.get(url_cicc_cloud)
    time.sleep(2)

    # 若cookie有效，则直接登入系统，不需要输入用户名与密码
    if 'login' not in driver.current_url:
        return True,driver
    else:
        return False,driver


# 存储cookie到json文件
def save_cookies(cookie_login):
    # 打开cookie存储的json文件
    json_file = open("cookie/cookie.json", "w")

    cookie_list = []

    for cookie in cookie_login:
        print("添加cookie： %s  ： %s  ： %s" % (cookie["name"], cookie["value"], cookie["domain"]))

        cookie_list.append(cookie)

    # 将cookie写入json文件中
    json.dump(cookie_list, json_file)

    # 关闭json文件
    json_file.close()