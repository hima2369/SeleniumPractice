import time
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.redbus.com/")
driver.maximize_window()
driver.implicitly_wait(50)

driver.find_element_by_xpath('//input[@id="src"]').send_keys("Bengaluru")
driver.find_element_by_xpath('//li[@data-id="122"]').click()
#print(WebDriverWait(driver,15).until(EC.presence_of_element_located(By.XPATH,'//li[@select-id="results[3]"]')).text)
driver.find_element_by_xpath('//input[@id="dest"]').send_keys("rajampet")
#time.sleep(3)
driver.find_element_by_xpath('//li[@data-id="1395"]').click()
#time.sleep(3)

driver.find_element_by_xpath('//label[text()="Onward Date"]').click()
#time.sleep(3)

def select_date(day,month_and_year):
    month_year=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
    if month_year==str(month_and_year):
        #time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[text()=' + '{}'.format(str(day)) + ']').click()
        #driver.find_element_by_xpath("""//div[@class="rb-calendar"]//td[text()='3']""").click()
    else:
        #time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="next"]').click()
        select_date(day,month_and_year)
select_date(3,'Jan 2022')

driver.find_element_by_xpath('//label[@class="db text-trans-uc tal"]').click()
def return_date(day,month_and_year):
    month_year=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
    if month_year==str(month_and_year):
        #time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[text()=' + '{}'.format(str(day)) + ']').click()
    else:
        #time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="next"]').click()
        return_date(day,month_and_year)
return_date(4,'Jan 2022')

driver.find_element_by_xpath('//button[@id="search_btn"]').click()