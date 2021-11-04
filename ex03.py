from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get(r"C:\Users\Manosasi\Desktop\selenium\first.html")

print(driver.current_url)

print(driver.current_window_handle)
driver.find_element_by_tag_name('a').click()
time.sleep(5)
print(driver.current_window_handle)
print(driver.window_handles)
time.sleep(5)

#driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(window_name=driver.window_handles[1])
#time.sleep(5)

driver.find_element_by_name('q').send_keys('india',Keys.ENTER)
time.sleep(5)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(3)
print(driver.find_element_by_xpath("//span[normalize-space()='Next']").click())

driver.find_element_by_xpath("//h3[@class='LC20lb DKV0Md']").click()