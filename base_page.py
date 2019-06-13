from common.find_element import Read_ini
import time
class Base():
    def __init__(self,browser):
        self.browser = browser
        self.cong = Read_ini()

    def find_ele(self,option,section='LoginElement'):
        method = self.cong.get_method(section,option)
        values = self.cong.get_ele(section,option)
        return self.browser.find_element(method,values)

    def login_action(self,username,password):
        time.sleep(2)
        self.find_ele('login_loginbtn').click()
        time.sleep(2)
        self.find_ele('user_name').send_keys(username)
        time.sleep(2)
        self.find_ele('password').send_keys(password)
        time.sleep(3)
        self.find_ele('login_submit').click()



