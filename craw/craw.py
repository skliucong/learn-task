# coding = utf-8
from time import sleep
from selenium import webdriver
page=0

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

browser.get("http://search.people.com.cn/cnpeople/news/noNewsResult.jsp")
browser.find_element_by_id("keyword").send_keys("富强")
browser.find_element_by_class_name("tt03").find_element_by_xpath("//table/tbody/tr/td[2]/img").click()


for j in range(100):
    if page==0:
        ullis = browser.find_element_by_class_name("w800").find_elements_by_xpath("//ul")
        for i in range(len(ullis)):
            pass

    alis=browser.find_element_by_class_name("show_nav_bar").find_element_by_xpath(".//a[last()]").click()


