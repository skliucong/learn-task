# coding = utf-8
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

browser.get("http://search.people.com.cn/cnpeople/news/noNewsResult.jsp")
browser.find_element_by_id("keyword").send_keys("富强")
browser.find_element_by_class_name("tt03").find_element_by_xpath("//table/tbody/tr/td[2]/img").click()

