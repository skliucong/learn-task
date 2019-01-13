# coding = utf-8
from time import sleep
from selenium import webdriver

browser = webdriver.chrome("D:\chromedriver.exe")

browser.get(r"http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_id("su").click()
sleep(5)
browser.quit()