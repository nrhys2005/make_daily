#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 주의사항 : chormedriver와 chrome 버전을 맞춰줘야함. 
#
import config
import requests
import time
from selenium import webdriver
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

etoos_id = config.etoos_id
etoos_pw = config.etoos_pw

today = datetime.today()
#today = datetime(2021,5,5)

#이전 데일리 날짜
find_day = (check_restday(today,0)).strftime("%Y-%m-%d")
#금일 데일리 날짜
today =today.strftime('%Y-%m-%d')

def make_daily(title):
    url = 'https://doc.etoos.com/display/ONLINE/'+today+'+DAILY+'+title
    driver.get(url)

    time.sleep(1)

    menu = driver.find_element_by_xpath ('//*[@id="action-menu-link"]')
    menu.click()

    time.sleep(1)

    copy = driver.find_element_by_xpath ('//*[@id="action-copy-page-link"]')
    copy.click()

    driver.implicitly_wait(30)
    time.sleep(1)

    copy_next = driver.find_element_by_xpath ('//*[@id="copy-dialog-next"]')
    copy_next.click()

    driver.implicitly_wait(30)
    time.sleep(1)

    title = today + " DAILY "+title
    driver.find_element_by_css_selector("input#content-title.text.pagetitle").send_keys(title)

    time.sleep(1)
    driver.implicitly_wait(100)

    make = driver.find_element_by_xpath ('//*[@id="rte-button-publish"]')
    make.click()




# chorme driver
driver = webdriver.Chrome('./chromedriver')

#웹개발팀 confluence 
driver.get('https://doc.etoos.com/display/ONLINE')

#로그인
driver.find_element_by_name('os_username').send_keys(etoos_id)
driver.find_element_by_name('os_password').send_keys(etoos_pw)
driver.find_element_by_id('loginButton').click()

# 데일리생성 - 상품개발팀
make_daily('상품개발팀'.'이상훈')

# 데일리생성 - 시험개발팀
make_daily('시험개발팀')

# 데일리생성 - 학습개발팀
make_daily('학습개발팀')


time.sleep(1)
driver.implicitly_wait(100)

driver.quit()

