from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome("C:\\Users\\J\\AppData\\Roaming\\Microsoft\\Windows\\Network Shortcuts\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/")
srchtxtbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
srchtxtbox.click()
time.sleep(5)
srchtxtbox.send_keys('messi')
srchtxtbox.send_keys(Keys.ENTER)

res = driver.find_elements(By.TAG_NAME,'a' )
print(len(res))
cnt = len(res)
def test_searchresults():
    expectedvalue = 5
    actualvalue = cnt
    assert expectedvalue == actualvalue
