import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://herokuapp.com/yeni-sekme.html")
driver.find_element(By.ID, "facebook").click()
driver.find_element(By.ID, "twitter").click()
driver.find_element(By.ID, "instagram").click()
time.sleep(2)


def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break


sekme_degistir("facebook")
print("facebook: " + driver.title)

sekme_degistir("twitter")
print("twitter: " + driver.title)

sekme_degistir("instagram")
print("instagram: " + driver.title)

sekme_degistir("selenium")
print("anasayfa: " + driver.title)

driver.quit()
