# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:36:30 2020

@author: manoj
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome('C:\Program Files\webdrivers\chromedriver.exe')
browser.maximize_window()
browser.delete_all_cookies()

base_url='https://www.amazon.com'
browser.get(base_url)

#identify the user name text box and enter the value  
#browser.find_element_by_id("identifierId").send_keys("manojthe8055@gmail.com")  
#time.sleep(2)  

#click on the next button  
#browser.find_element_by_xpath("//span[@class='RveJvd snByac'][1]").click()  
#time.sleep(3)  

