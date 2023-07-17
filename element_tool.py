# 确保已安装必要的第三方库
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#根据标签获取输入框元素
def get_element(driver,label):
    parent_element = driver.find_element(By.XPATH,"//label[@class = 'el-form-item__label'][text()='" + label + "']/..")
    element_selected = parent_element.find_element(By.CSS_SELECTOR, "input[class = 'el-input__inner']")
    # elements = driver.find_elements(By.CSS_SELECTOR, "div[class = 'el-form-item is-required']")
    # for element in elements:
    #     element_label = element.find_element(By.CSS_SELECTOR,"label")
    #     print(element_label.text)
    #     if element_label.text == label:
    #         element_selected = element.find_element(By.CSS_SELECTOR,"input[class = 'el-input__inner']")
    return element_selected

# 点击组件后进行选择（可单选可多选可级联选择）
def select_checkbox(driver,input_values,element):
    # 如果输入值中没有+且类型为str，则表示为单选
    if '+' not in input_values and isinstance(input_values,str):
        # 点击当前元素，打开下拉框
        element.click()
        time.sleep(1)
        # 点击要选择的内容
        choice_elements = driver.find_elements(By.CSS_SELECTOR, "li[class = 'el-select-dropdown__item']")
        for choice_element in choice_elements:
            if choice_element.text != '' and choice_element.text in input_values:
                element_selected = choice_element
                element_selected.click()
                time.sleep(0.5)
    # 级联选择
    elif '+' in input_values:
        value_list = input_values.split('+')
        for value in value_list:
            # 点击当前元素，打开下拉框
            element.click()
            time.sleep(4)
            # 点击要选择的内容
            choice_elements = driver.find_elements(By.CSS_SELECTOR, "li[class = 'el-cascader-node']")
            for choice_element in choice_elements:
                if choice_element.text != '' and choice_element.text in value:
                    element_selected = choice_element
                    # 此处需要js注入执行点击，否则多选时不能选择连续的选项（原因未知）
                    driver.execute_script("arguments[0].click();", element_selected)
                    time.sleep(0.5)
                    element = choice_element
    # 多选
    else:
        # 点击当前元素，打开下拉框
        element.click()
        time.sleep(4)
        # 点击要选择的内容
        choice_elements = driver.find_elements(By.CSS_SELECTOR, "li[class = 'el-select-dropdown__item']")
        for choice_element in choice_elements:
            if choice_element.text != '' and choice_element.text in input_values:
                element_selected = choice_element
                # 此处需要js注入执行点击，否则多选时不能选择连续的选项（原因未知）
                driver.execute_script("arguments[0].click();", element_selected)
                time.sleep(0.5)


# 选择日历
def select_calender(driver,input_values,element):
    # 获取年月日
    input_year = int(input_values.split('/')[0])
    input_month = int(input_values.split('/')[1])
    input_day = input_values.split('/')[2]

    # 点击当前元素，打开下拉框
    element.click()
    time.sleep(0.5)

    # 获取当前日期选择器的时间
    date_elements = driver.find_elements(By.CSS_SELECTOR, "span[class = 'el-date-picker__header-label']")
    current_year = ''
    current_month = ''
    for date_element in date_elements:
        if '年' in date_element.text:
            current_year = date_element.text
            current_year = int(current_year[:-1])
            continue
        if '月' in date_element.text:
            current_month = date_element.text
            current_month = int(current_month[:-1])
            continue

    # 获取变更年与月的单击按钮元素
    next_year_element = None
    last_year_element = None
    next_month_element = None
    last_month_element = None

    next_year_elements = driver.find_elements(By.CSS_SELECTOR, "button[aria-label = '后一年']")
    for element in next_year_elements:
        if element.size['height'] != 0:
            next_year_element = element
            break
    last_year_elements = driver.find_elements(By.CSS_SELECTOR, "button[aria-label = '前一年']")
    for element in last_year_elements:
        if element.size['height'] != 0:
            last_year_element = element
            break
    next_month_elements = driver.find_elements(By.CSS_SELECTOR, "button[aria-label = '下个月']")
    for element in next_month_elements:
        if element.size['height'] != 0:
            next_month_element = element
            break
    last_month_elements = driver.find_elements(By.CSS_SELECTOR, "button[aria-label = '上个月']")
    for element in last_month_elements:
        if element.size['height'] != 0:
            last_month_element = element
            break

    # 将日期选择器调整到需要的年月
    while(1):
        if current_year < input_year:
            next_year_element.click()
            current_year = current_year + 1

        if current_year > input_year:
            last_year_element.click()
            current_year = current_year - 1

        if current_month < input_month:
            next_month_element.click()
            current_month = current_month + 1

        if current_month > input_month:
            last_month_element.click()
            current_month = current_month - 1

        if current_year == input_year and current_month == input_month:
            break

    # 选择对应的日
    time.sleep(0.5)
    day_elements = driver.find_elements(By.XPATH, "//td[@class = 'available']/div/span[text()={input_day}]".format(input_day = input_day))
    for day_element in day_elements:
        if day_element.size['height'] != 0:
            day_element.click()
            break

# 填写输入框
def fill_inputbox(input_values,element):
    # 如果输入框中原本有数据，则清除
    element.clear()
    element.send_keys(input_values)

# 填写模糊搜索下拉框
def fill_input_search(driver,input_values,element):
    # 如果输入框中原本有数据，则清除
    element.clear()
    element.send_keys(input_values)

    time.sleep(3)

    item_element = driver.find_element(By.CSS_SELECTOR, "li[role = 'option']")

    item_element.click()

# 获取弹出框内容
def get_alert(driver):
    try:
        time.sleep(1)
        element = driver.find_element(By.XPATH, "//div[@role = 'alert']/p")
        alert_text = element.text
    except:
        alert_text = ''
    return alert_text
