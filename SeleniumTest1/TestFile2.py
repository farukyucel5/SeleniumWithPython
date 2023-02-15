from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.amazon.com")

get_url = driver.current_url
get_title = driver.title

if "amazon" in get_url:
    print("we are on Amazon ")
else:
    print("we cannot access to Amazon")


driver.get("https://www.youtube.com/")
get_url = driver.current_url
get_title = driver.title

if "youtube" in get_url:
    print("we are on Youtube ")
    driver.save_screenshot("screenShotYoutube.png")
else:
    print("we cannot access to Youtube")

driver.back()

get_url = driver.current_url
get_title = driver.title

if "amazon" in get_url:
    print("we are on Amazon ")
    driver.save_screenshot("screenShotAmazon.png")
else:
    print("we cannot access to Amazon")

