import requests
import datetime

dt_now=datetime.datetime.now()
today=str(dt_now.date())
tistory_url = 'https://www.tistory.com/apis/post/write?'
title = '[테스트]' + today + ' 글 올리기'
access_token = '0ddf3743905dcad393e5fb9f5a57053a_5b699edc7d8f95aba6482440d4bbf676'
parameters = {
    'access_token': access_token,
    'blogName':'gongsipass2020',
    'title': title,
    'content': "열심히 올려보세요.",
    'visibility': '1',
    'category': '955791',
    'tag': '공무원,공무원시험,9급공무원,7급공무원,에듀윌,추천인아이디',
    'acceptComment': '1'
    }

response = requests.post(tistory_url, params=parameters)
print(response.text)


전기 기사 시작하시는 분들
전기 기사 빨리 합격하려면 참고!
전기 기사 공부할때 확인할 것
#에듀윌전기기사 #에듀윌전기공사기사 #에듀윌전기산업기사 #에듀윌합격률 #에듀윌필기노트 #전기기사무료자료 #전기기사인강