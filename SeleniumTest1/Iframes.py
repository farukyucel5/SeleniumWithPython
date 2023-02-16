import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
# 1. iframe id
# 2. iframe name
# 3 index (0'dan basliyor')
driver.switch_to.frame("mce_0_ifr")
WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "p")))
gettext = driver.find_element(By.TAG_NAME, "p")
print(gettext.text)
assert "Your content goes here." in gettext.text
time.sleep(2)
# default_content => en ana sayfaya don,, sayfanin aslina don
# parent_frame => bir ustteki frame gecis icin
# 1. ana sayfa
#   2. frame 1
#      3 frame 2
driver.switch_to.default_content()
getHeadLine = driver.find_element(By.TAG_NAME, "h3")
assert getHeadLine.is_displayed()
time.sleep(2)
