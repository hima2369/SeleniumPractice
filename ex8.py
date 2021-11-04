from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://wwww.facebook.com/')

driver.find_elements_by_xpath('//input[@name="email"]')
driver.find_element_by_name('email').send_keys('choppanagesh421@gmail.com')
time.sleep(3)

driver.find_elements_by_xpath('//input[@name="pass"]')
driver.find_element_by_name('pass').send_keys('9703622043')
time.sleep(5)

#driver.find_element_by_xpath('//button[@value="1"]').click()


#driver.find_element_by_xpath('(//a[@role="button"])[2]').click()

driver.find_element_by_xpath('//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()


