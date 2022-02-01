from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome("C:\\Users\\J\\AppData\\Roaming\\Microsoft\\Windows\\Network Shortcuts\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com/")
srchtxtbox = driver.find_element_by_xpath( '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' )
srchtxtbox.click()
srchtxtbox.send_keys('elements on google webpage')
srchtxtbox.send_keys(Keys.ENTER)

links= driver.find_elements(By.TAG_NAME,'a' )

def test_searchresults():

    expectedvalue = 10
    actualvalue = len(links)
    assert expectedvalue == actualvalue


