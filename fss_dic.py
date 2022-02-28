import requests

from bs4 import BeautifulSoup

url="http://www.edujin.co.kr/news/articleList.html?view_type=sm"

response=requests.get(url)

if response.status_code==200:
    html=response.content
    soup=BeautifulSoup(html,'html.parser')
    section=soup.find('section')
    print(section)   
    # ul=section.find("ul")
    # h4=ul.find('h4')
    
    # print(h4)
   
   
else: 
    print(response.status_code)
