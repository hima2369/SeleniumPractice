from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(r"C:\Users\Manosasi\Desktop\selenium\third1.html")
time.sleep(3)
driver.find_element_by_tag_name('button').click()
alert_obj=driver.switch_to.alert
print(alert_obj.text)