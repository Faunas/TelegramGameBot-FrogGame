from selenium import webdriver
import pickle
from time import sleep
import time
from schedule import *
import schedule
from variables_actions import *
from selenium.webdriver.common.by import By


chromedriver = "C:/CH/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver)

browser.get('https://web.telegram.org/k/')
sleep(5)
enter_russian = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/button[1]').click()
sleep(5)
enter_number = browser.find_element_by_css_selector('#auth-pages > div > div.tabs-container.auth-pages__container > div.tabs-tab.page-sign.active > div > div.input-wrapper > div.input-field.input-field-phone > div.input-field-input').send_keys(login)
next_buttn = browser.find_element_by_css_selector('#auth-pages > div > div.tabs-container.auth-pages__container > div.tabs-tab.page-sign.active > div > div.input-wrapper > button.btn-primary.btn-color-primary.rp').click()
code_quest = input('Введи код с телефона: ')
code_site = browser.find_element_by_css_selector('#auth-pages > div > div.tabs-container.auth-pages__container > div.tabs-tab.page-authCode.active > div > div.input-wrapper > div > input').send_keys(code_quest)
sleep(3)
find_dialog = browser.find_element_by_css_selector('#folders-container > div > div.chatlist-top > ul > a:nth-child(1) > div.c-ripple').click()

schedule.every().hour.do(gotojob_kitchen)
schedule.every().hour.do(end_job)
schedule.every().hour.do(eatmyfrog)
schedule.every().hour.do(gotojob_kitchen)
schedule.every().hour.do(gotodetsad_smallfrog)
schedule.every().hour.do(end_job)
schedule.every().hour.do(eatmyfrog)
schedule.every().hour.do(gotojob_kitchen)
schedule.every().hour.do(end_job)
schedule.every().hour.do(eatmyfrog)
schedule.every().hour.do(gotojob_kitchen)
schedule.every().hour.do(takedetsad_smallfrog)
schedule.every().hour.do(end_job)

while True:
    schedule.run_pending()
    time.sleep(5)


