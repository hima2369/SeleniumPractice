from selenium import webdriver
import time
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://wwww.facebook.com/')
time.sleep(5)

driver.find_element_by_xpath('(//a[@role="button"])[2]').click()
time.sleep(5)

driver.find_element_by_name('firstname').send_keys("himabindu")
time.sleep(3)
driver.find_element_by_name('lastname').send_keys("kollam")
driver.find_element_by_name('reg_email__').send_keys('9703622043')
driver.find_element_by_name('reg_passwd__').send_keys('Bindureddy@45')
time.sleep(3)
select_day=Select(driver.find_element_by_name("birthday_day"))
time.sleep(3)

#print(select_day.options)
#print(option.text)
select_day.select_by_index(5)

#select_day.select_by_value('19')

#select_day.select_by_visible_text('17')

#select_day.deselect_all()
#select_day.deselect_by_index()
#select_day.deselect_by_value()
#select_day.deselect_by_visible_text()
select_month=Select(driver.find_element_by_name("birthday_month"))
time.sleep(5)

#print(select_month.options)
#print(option.text)
#select_month.select_by_index(3)
select_month.select_by_value('4')
#select_month.select_by_visible_text('Apr')
#select_month.deselect_by_value()
#select_month.deselect_all()
#select_month.deselect_by_visible_text()
#select_month.deselect_by_index()

select_year=Select(driver.find_element_by_name("birthday_year"))
time.sleep(5)
print(select_year.options)
#print(option.text)
select_year.select_by_index('10')
time.sleep(3)
select_year.select_by_value('1997')
time.sleep(3)
select_year.select_by_visible_text('1998')
time.sleep(3)

driver.find_element_by_xpath('(//input[@class="_8esa"])[1]').click()


