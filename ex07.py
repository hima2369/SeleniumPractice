from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
#driver.get(r"C:\Users\Manosasi\Desktop\selenium\Ffirst.html")
#driver.maximize_window()
#h1_text=driver.find_element_by_css_selector('#h1Id')
#print(h1_text.text)
#h1_class=driver.find_element_by_css_selector('.h1Class')
#print(h1_class.text)

#print(driver.find_element_by_css_selector('#pId').text)
#print(driver.find_element_by_css_selector('.pClass').text)

#print(driver.find_element_by_css_selector('p[name]').text)
#print(driver.find_element_by_css_selector('p.pClass[name]').text)

driver.get('https://www.google.com/')
driver.find_element_by_name('q').send_keys('india')
time.sleep(3)

suggestions_list=driver.find_elements_by_xpath('//li[@data-view-type="1"]')
for suggestion in suggestions_list:
    print(suggestion.text)

