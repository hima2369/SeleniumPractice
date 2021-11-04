from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get(r"C:\Users\Manosasi\Desktop\selenium\first.html")

#print(driver.current_url)

#anchor_tag=driver.find_element_by_tag_name('h1')
#print(anchor_tag.text)

#id=driver.find_element_by_id('pId')
#print(id.text)

#print(id.get_attribute('id'))

#name=driver.find_element_by_name('nameInput1')
#print(name.get_attribute('value'))

#name=driver.find_element_by_name('nameInput2')
#print(name.get_attribute('placeholder'))

#print(driver.find_element_by_link_text('Google.com').text)

#print(driver.find_element_by_link_text('Gmail.com').text)

#print(driver.find_element_by_partial_link_text('Google').text)

#print(driver.find_element_by_class_name('h1Class').text)


#driver.get('https://www.google.com/')

#curr=driver.current_window_handle
#print('the current window obj is',curr)
#time.sleep(5)

#driver.find_element_by_tag_name('a').click()
#print(driver.window_handles)
#time.sleep(5)

#driver.switch_to.window(window_name=curr)
#time.sleep(5)

#driver.find_element_by_tag_name('a').click()
#print(driver.window_handles)

#print(dir(driver.find_element_by_tag_name('a')))
#driver.set_window_position(0,200)
#driver.set_window_size(0,100)
#time.sleep(5)
#driver.fullscreen_window()
#time.sleep(5)

#a=driver.get_window_position()
#print('bowser position',a)

#b=driver.get_window_rect()
#print('browser,window position',b)

#c=driver.get_window_size()
#print('browser size',c)

