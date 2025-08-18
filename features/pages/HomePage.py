from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver



    my_account_option_xpath="/html/body/nav/div/div[2]/ul/li[2]/a/span[1]"

    def click_on_my_account(self): # bu method direk burda olusturulup home page de my account butonuna tiklattirilabilir
        self.driver.find_element(By.XPATH.self.my_account_option_xpath).click()