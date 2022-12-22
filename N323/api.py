import requests
#json : python객체 -> json데이터
import json

#openweather에서 받은 api key
API_KEY = '58f0a9261dc135f4478747e1c6709c58'
#도시 : 서울
city_name = 'seoul'
#openweather API 주소
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'


#연결
resp = requests.get(url)
#json.loads : 문자열 데이터(python객체)를 json데이터로
current_weather = json.loads(resp.text) #=>딕셔너리 형태