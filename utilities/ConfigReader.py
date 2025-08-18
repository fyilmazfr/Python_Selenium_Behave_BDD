from configparser import ConfigParser

"""
Ne işe yarar?

config.ini dosyasında ayarlar tutulur (örneğin URL, browser tipi, kullanıcı adı, şifre).

category = dosyada bölüm adı olur ([default], [browser] gibi).

key = o bölüm altındaki anahtar adı olur (url, username, password).

config.get(category, key) = değeri string olarak döndürür.
"""


def read_configuration(category,key):
    config=ConfigParser()                      # ConfigParser sınıfından bir nesne oluşturuyor
    config.read("configurations/config.ini")    # config.ini dosyasını okuyor
    return config.get(category,key)             # Dosyadaki ilgili bölüm (category) ve anahtar (key) değerini döndürüyor


"""
Kullanım:

url = read_configuration("default", "url")  
print(url)   # https://example.com

user = read_configuration("credentials", "username")
print(user)  # test_user



"""
