from selenium import webdriver

from utilities import ConfigReader


#behave de hook mekanizmasini olusturdugumuz environment.py ile yaptik
#📌 Önemli nokta → Dosya adının mutlaka environment.py olması gerekir.
#Behave bu dosyayı otomatik olarak bulur ve içindeki hook’ları sen hiçbir yerde import etmeden çalıştırır.



def before_scenario(context, scenario):
    browser=ConfigReader.read_configuration("basic info","browser")   #bu kisimda if elif' lerle diger browser'larida acabiliriz
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))

def after_scenario(context, scenario):
    context.driver.quit()