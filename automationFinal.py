import sys 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get('https://google.com')

driver.find_element_by_id('gb_70').click()
driver.find_element_by_id('identifierId').click()
driver.find_element_by_id('identifierId').send_keys('gabriellepinheiro96@gmail.com')

driver.find_element_by_id('identifierNext').click()


driver.find_element_by_name('password').click()
driver.find_element_by_name('password').send_keys('Gabrielle150796')

driver.find_element_by_id('passwordNext').click()
