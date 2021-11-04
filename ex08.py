from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://wwww.facebook.com/')

driver.find_elements_by_xpath('//input[@name="email"]')
#//input[@id="email"]
#//input[@type="text"]
#//input[@class="inputtext _55r1 _6luy"]
#//input[@placeholder="Email address or phone number"]

driver.find_elements_by_xpath('//input[@name="pass"]')
#//input[@type="password"]
#//input[@id="pass"]
#//input[@data-testid="royal_pass"]
#//input[@placeholder="Password"]
#//input[@class="inputtext _55r1 _6luy _9npi"]

driver.find_elements_by_xpath('//button[@value="1"]')
#//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]
#//button[@name="login"]
#//button[@data-testid="royal_login_button"]
#//button[@type="submit"]
#//button[@id="u_0_d_i3"]

driver.find_elements_by_xpath('//div[@class="_6ltj"]')  #forgotten password
#//a[contains(text(),'Forgotten password?')]


driver.find_elements_by_xpath('//a[@role="button" and @id="u_0_2_nN"]')
#//a[@id="u_0_2_nN"]
#//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]
#//a[@data-testid="open-registration-form-button"]
#//div[@class="_6ltg"]//a[@role="button"]
#//*[@id="u_1l_2_DI"]

driver.find_elements_by_xpath('//input[@name="firstname"]')
#//input[@type="text" and @class="inputtext _58mg _5dba _2ph-" ]
#//input[@type="text" and @id="u_p_b_9E" ]

driver.find_elements_by_xpath('//input[@name="lastname"]')
#//input[@type="text" and @class="inputtext _58mg _5dba _2ph-" and @id="u_p_d_Qu"]
#//input[@type="text" and @id="u_p_d_Qu"]

driver.find_elements_by_xpath('//input[@name="reg_email__"]')
#//input[@id="u_p_g_Je"]
#(//input[@class="inputtext _58mg _5dba _2ph-"])[3]

driver.find_elements_by_xpath('(//input[@type="password"])[2]')
#//input[@type="password" and @class="inputtext _58mg _5dba _2ph-"]
#//input[@name="reg_passwd__" ]
#//input[@id="password_step_input" ]
#//input[@data-type="password" ]

driver.find_elements_by_xpath('//select[@name="birthday_day"]')
#//select[@id="day" or @title="Day"]
#//select[@class="_9407 _5dba _9hk6 _8esg" and @title="Day"]

driver.find_elements_by_xpath('//select[@name="birthday_month"]')
#//select[@class="_9407 _5dba _9hk6 _8esg" and @title="Month"]
#//select[@id="month" and @title="Month"]

driver.find_elements_by_xpath('//select[@name="birthday_year"]')
#//select[@id="year" and @class="_9407 _5dba _9hk6 _8esg"]
#//select[@id="year" or @title="Year"]

driver.find_elements_by_xpath('//input[@id="u_p_4_aH"]')
#//input[@class="_8esa" and @value="1"]
#//input[@type="radio" and @value="1"]

driver.find_elements_by_xpath('//input[@id="u_p_5_lq"]')
#//input[@type="radio" and @value="2"]
#//input[@class="_8esa" and @value="2"]

driver.find_elements_by_xpath('//input[@id="u_p_6_M6"]')
#//input[@value="-1"]
#//input[@name="sex" and @class="_8esa" and @value="-1"]
#//input[@name="sex" and @class="_8esa" and @id="u_p_6_M6"]

driver.find_elements_by_xpath('//select[@name="preferred_pronoun"]')
#//select[@name="preferred_pronoun"]//option[@value="1"]
#//select[@name="preferred_pronoun"]//option[@value="2"]
#//select[@name="preferred_pronoun"]//option[@value="6"]
#//select[@name="preferred_pronoun"]//option[@selected="1"]

driver.find_elements_by_xpath('//button[@name="websubmit"]')
#//button[@type="submit" and @id="u_p_s_uf"]
#//button[@class="_6j mvm _6wk _6wl _58mi _3ma _6o _6v"]

