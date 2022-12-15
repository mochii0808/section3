# csv 파일 옮기기

import psycopg2 #저장소 통신 라이브러리

host = '호스트 주소를 입력해주세요'
user = '유저 이름을 입력해주세요'
password = '비밀번호를 입력해주세요'
database = '데이터베이스 이름을 입력해주세요'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

import csv #csv 읽기 라이브러리

with open('titanic.csv', mode='r') as f: 
#open, close : 파일 입출력
#with : close 누락 방지
  reader = csv.reader(f)
  next(reader)
  ind = 0 #Id에 넣을 값, 0부터 시작, csv에 없음
  for row in reader:
    cur.execute(
      """
      INSERT INTO passenger (Id, Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) 
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
      """,
      [ind] + row #0부터 정수 + csv 데이터
    )
    ind += 1

connection.commit()
connection.close()