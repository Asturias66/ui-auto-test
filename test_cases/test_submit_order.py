import get_data
import new_order

class Test_submit_order():
    @classmethod
    def setup_class(self):
        print('\n *** 初始化-模块 ***')
        # 定义订单数据文件路径
        self.xinan_data_path = 'data/鑫安.csv'
        self.xintou_data_path = 'data/鑫投.csv'
        self.changying_data_path = 'data/长赢.csv'
        self.ruichi_data_path = 'data/瑞驰.csv'

        # 定义config文件路径
        config_path = 'config/config.json'
        # 获取中金应用云登录账号与登录密码、选择的系统环境
        self.user_account, self.user_password, self.system_name, self.system_env, self.series = get_data.get_config(config_path)

    @classmethod
    def teardown_class(self):
        print('\n ***   清除-模块 ***')

    # 测试新增鑫安订单
    def test_submit_xinan_order(self):
        data_orders = get_data.get_orders(self.xinan_data_path)
        print(data_orders)

        # 登录并打开新建订单页面
        driver = new_order.open_new_order(self.user_account, self.user_password, self.system_name, self.system_env)

        for index, order in data_orders.iterrows():
            flag = new_order.new_order(driver,order)
            assert flag == True

    # 测试新增鑫投订单
    def test_submit_xintou_order(self):
        data_orders = get_data.get_orders(self.xintou_data_path)
        print(data_orders)

        # 登录并打开新建订单页面
        driver = new_order.open_new_order(self.user_account, self.user_password, self.system_name, self.system_env)

        for index, order in data_orders.iterrows():
            flag = new_order.new_order(driver, order)
            assert flag == True

    # 测试新增长赢订单
    def test_submit_changying_order(self):
        data_orders = get_data.get_orders(self.changying_data_path)
        print(data_orders)

        # 登录并打开新建订单页面
        driver = new_order.open_new_order(self.user_account, self.user_password, self.system_name, self.system_env)

        for index, order in data_orders.iterrows():
            flag = new_order.new_order(driver, order)
            assert flag == True


    # 测试新增瑞驰订单
    def test_submit_ruichi_order(self):
        data_orders = get_data.get_orders(self.ruichi_data_path)
        print(data_orders)

        # 登录并打开新建订单页面
        driver = new_order.open_new_order(self.user_account, self.user_password, self.system_name, self.system_env)

        for index, order in data_orders.iterrows():
            flag = new_order.new_order(driver, order)
            assert flag == True



