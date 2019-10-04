from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Program Files (x86)\drivers\geckodriver.exe")

driver.get("http://www.newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)

time.sleep(5)

ele = driver.find_element_by_name("userName")
print(ele.is_displayed())
print(ele.is_enabled() )

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())


ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

#roundtip = driver.find_element_by_css_selector("input(value=roundtrip)")
print("mjees")
#print(roundtip.is_selected())
time.sleep(5)
driver.close()

