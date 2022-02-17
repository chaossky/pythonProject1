# from bs4 import BeautifulSoup
# import urllib.request
# OUTPUT_FILE_NAME='output.txt'
# import selenium
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = 'http://www.edujin.co.kr/news/articleList.html?view_type=sm'
#
# driver = webdriver.Chrome(executable_path='chromedriver')
# driver.get(url=URL)
#
# driver.find_element_by_id('ke_kbd_btn').click()
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome("chromedriver.exe")
#driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://finance.naver.com/item/main.nhn?code=005930"
url='https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

#driver.get(url)
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    print(title.get_text())

else:
    print(status_code)

# id_name = "tab_con1"
# elem = driver.find_element(By.ID, id_name)
#
#
# print(elem.text)
#s_content > div.section > ul > li:nth-child(1) > dl > dt > a