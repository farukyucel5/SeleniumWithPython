from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.amazon.com")

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Nutella")
driver.find_element(By.ID,"nav-search-submit-button").click()

page_title=driver.title

print(page_title)


