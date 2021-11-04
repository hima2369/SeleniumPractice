from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")

driver.get(r"C:\Users\Manosasi\Desktop\selenium\third2.html")
driver.find_element_by_tag_name('button').click()
time.sleep(5)

alert_obj=driver.switch_to.alert
print(alert_obj.text)
time.sleep(5)

