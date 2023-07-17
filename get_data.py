import json
import pandas as pd

# 获取配置信息
def get_config(config_path):
    # 打开json文件
    json_file = open(config_path, "r",encoding='utf-8')
    # 获取文件中存储的信息
    config_data = json.load(json_file)

    #获取用户账户
    user_account = config_data['用户账户']

    # 获取用户密码
    user_password = config_data['用户密码']

    # 获取系统名称
    system_name = config_data['系统名称（金元宝或无双）']

    # 获取系统环境
    system_env = config_data['系统环境（uat或dev）']

    # 获取选择系列
    series = config_data['选择新建订单系列']

    return user_account,user_password,system_name,system_env,series

def get_orders(data_path):
    # 读取excel中的订单数据
    raw_data = pd.read_csv(data_path, encoding='gbk')

    # # 获取订单数据
    # data_orders = raw_data.iloc[3:,:]
    # # 设置新的表头
    # data_orders_header = raw_data.values.tolist()[2]
    # data_orders.columns = data_orders_header
    # # 重置索引
    # data_orders = data_orders.reset_index(drop=True)

    return raw_data
