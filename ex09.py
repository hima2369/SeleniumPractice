import time
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.redbus.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//input[@id="src"]').send_keys("Bengaluru")
time.sleep(5)
driver.find_element_by_xpath('//li[@data-no="3"]//i[@class="icon solr-icon icon-ic-city"]').click()
#driver.find_element_by_xpath('//li[@data-id="122" and text()="Bengaluru"]').click()
time.sleep(5)
driver.find_element_by_xpath('//input[@id="dest"]').send_keys("rajampet")
time.sleep(3)
driver.find_element_by_xpath('//li[@data-id="1395"]').click()
time.sleep(3)
driver.find_element_by_xpath('//label[text()="Onward Date"]').click()
time.sleep(3)
#driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="next"]').click()
#month_year=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
#print(month_year)

#date=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="wd day" and text()=6]').click()

def select_date():
    month_year=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
    if month_year=='Jan 2022':
        time.sleep(3)
        driver.find_element_by_xpath("""//div[@class="rb-calendar"]//td[text()='3']""").click()
    else:
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="next"]').click()
        select_date()
select_date()

driver.find_element_by_xpath('//label[@class="db text-trans-uc tal"]').click()
#Returnmonth_year=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
#print(Returnmonth_year)
#driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="wd day" and text()="4"]').click()

def select_date():
    month_year=driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
    if month_year=='Jan 2022':
        time.sleep(3)
        driver.find_element_by_xpath("""//div[@class="rb-calendar"]//td[text()='4']""").click()
    else:
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="next"]').click()
        select_date()
select_date()

time.sleep(5)
driver.find_element_by_xpath('//button[@id="search_btn"]').click()