from selenium import webdriver
import time

naver_url='http://www.naver.com'
browser=webdriver.Chrome('')
time.sleep(1)
browser.get(naver_url)
time.sleep(1)

browser.find_element_by_xpath('//*[@id="acount"]/a').click()
time.sleep(1)


browser.find_element_by_xpath('//*[@id="id"]').send_keys('chaossky')

time.sleep(1)


browser.find_element_by_xpath('//*[@id="pw"]').send_keys('winter010!@#')
time.sleep(1)


browser.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(1)