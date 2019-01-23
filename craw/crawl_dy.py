from selenium import webdriver
URL = 'https://movie.douban.com/annual2016/#1'
driver=webdriver.Chrome('E://chromedriver')
driver.get(URL)
el = driver.find_element_by_xpath('//div[@id="app"]/div/div/button')
el.click()
from selenium.webdriver.common.by import  By

el2 = driver.find_element(By.XPATH, '//div[@data-scroll="limited"]/ul')