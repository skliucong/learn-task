# coding=utf-8
from selenium import webdriver
import time
import json
import requests
from requests import session
URL = 'http://www.ygdy8.com/html/gndy/jddy/index.html'
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get(URL)
movies=[]
error=[]
numpage=0
f = open('ssssssssssss_movies.csv', 'w')
error_f = open('ssssssss_movies.csv', 'w')
while True:
    numpage=numpage+1
    print(u"第"+str(numpage)+u"页++++++++++++++++++++++++++++++++++++++++++++++++++")
    try:
        kl = driver.find_element_by_xpath('//div[@class="co_content8"]')
    except:
        URL = 'http://www.ygdy8.com/html/gndy/jddy/index.html'
        driver = webdriver.Chrome('E://chromedriver')
        driver.get(URL)
        movies = []
        error = []
        numpage = 0
        f.close()
        f = open('ssssssssssss_movies.csv', 'w')
        numpage = numpage + 1
        print(u"第" + str(numpage) + u"页++++++++++++++++++++++++++++++++++++++++++++++++++")
        kl = driver.find_element_by_xpath('//div[@class="co_content8"]')



    kllist = kl.find_elements_by_xpath('ul/table')
    if kllist==None:
        break



    for item in kllist:
        print(u"电影数量" + str(len(movies) + 1))
        elem=item.find_elements_by_xpath('tbody/tr')
        elem1=elem[1].find_elements_by_xpath('td')
        elem2=elem1[1].find_element_by_xpath('b/a')
        biaoti=elem2.text
        link=elem2.get_attribute('href')

        js='window.open("'+link+'")'
        driver.execute_script(js)
        driver.switch_to_window(driver.window_handles[1])
        neirongs=driver.find_elements_by_xpath('//td[@style="WORD-WRAP: break-word"]')
        if len(neirongs)==0  and '3GP-MP4' not in biaoti:    #忽略掉3gp-mp4
            for getneirongs_i in range(5):
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
                time.sleep(2)

                js = 'window.open("' + link + '")'
                driver.execute_script(js)
                driver.switch_to_window(driver.window_handles[1])
                neirongs = driver.find_elements_by_xpath('//td[@style="WORD-WRAP: break-word"]')
                if len(neirongs) !=0:
                    break

        neirong=[]
        for neirongs_item in  neirongs:
            try:
                neirong_a=neirongs_item.find_element_by_xpath('a')
                if 'ftp://' in neirong_a.text:
                    neirong.append(neirong_a.text)
                else:
                    neirong.append(neirong_a.get_attribute('href'))
            except:
                neirong_a=neirongs_item
                if 'ftp://' in neirong_a.text:
                    neirong.append(neirong_a.text)
                else:
                    try:
                        neirong.append(neirong_a.get_attribute('href'))
                    except:
                        continue




        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        if len(neirong)!=0:
            movies.append(1)
            #movies.append({'biaoti':biaoti,'neirong':neirong})
            data_json = json.dumps({'biaoti':biaoti,'neirong':neirong})
            f.write(data_json+'\n')
        else:
            error_json=json.dumps({'biaoti':biaoti,'link':link})
            error_f.write(error_json+'\n')
            error.append(biaoti)
        print (biaoti)
        print (neirong)
        print ('####################################################################')










    next_= kl.find_elements_by_xpath('div/a')
    nextpage = next_[-2]
    if nextpage.text==u'下一页':
        time.sleep(0.1)
        nextpage.click()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
    else:
        break
f.close()
error_f.close()