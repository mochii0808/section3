#변수 선언


#requests : 페이지에 정보 요청하기
import requests

#beautifulsoup4 : 받은 응답 내용에서 정보 찾기
from bs4 import BeautifulSoup

###requests로 받고 -> beautifulsoup로 변환


url = 'https://google.com'


#.get : 해당 url과 연결
page = requests.get(url)

#.content : 받은 내용을 문자열로 변환
#html.parser : 파싱 방법(파싱 : HTML,XML -> 파이썬 변환)
soup = BeautifulSoup(page.content, 'html.parser')

#----------------------------------------------------------------------------------


#요소 찾기
#find : 태그(이름, 속성) 이용
#select : CSS selector(#, .) 이용


#find, select_one : 한개
#id로 찾기
dog = soup.find(id = 'dog')
dog = soup.select_one('#dog')

#===============================


#find_all, select : 여러개
#class로 찾을 시 class_(파이썬의 class와 차별)
cat = soup.find_all(class_ = 'cat')
cat = soup.select('.cat')
#div태그의 cat클래스
cat = soup.find_all('div', class_='cat')
cat = soup.select('div.cat')
#하위경로 태그
#리스트로 저장되므로 주의!!!
cat = soup.find_all('div', class_='cat').find('li')
cat = soup.select('div > li')
#하위경로 클래스
cat = soup.find('div').find('ul').find_all('li', class_='fish') 
cat = soup.select('div > ul > li.fish')
