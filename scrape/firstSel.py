#!/usr/bin/env python
from selenium import webdriver

query=input("enter your search query: ")

driver= webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.youtube.com')

(driver.find_element_by_xpath('//*[@id="search-form"]')).click()
(driver.find_elements_by_xpath('//*[@id="search"]'))[2].send_keys(query)
(driver.find_elements_by_xpath('//*[@id="search-icon-legacy"]'))[0].click()


