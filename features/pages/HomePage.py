from selenium.webdriver.common.by import By

# self → class içindeki değişkenlere/metodlara erişmek için kullanılır.

class HomePage:
    def __init__(self,driver):
        self.driver=driver

#amac locate ve bu locate'i nerde kullandiysak bunun methodunu hazirlayip ,step lerde bu methodu cagirmak

    my_account_option_xpath="/html/body/nav/div/div[2]/ul/li[2]/a/span[1]"
    login_option_link_teext="Login"



    def click_on_my_account(self): # bu method direk burda olusturulup home page de my account butonuna tiklattirilabilir
        self.driver.find_element(By.XPATH.self.my_account_option_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_link_teext).click()