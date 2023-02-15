import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
driver.save_screenshot("herukuapp.png")
dropdown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropdown)
odeme_tipleri = odeme.options # web element listesi, her bir option tagi

for tip in odeme_tipleri:
    print(tip.text)
time.sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
time.sleep(2)
odeme.select_by_index(3)
time.sleep(2)