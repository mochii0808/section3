#MongoDB URI 양식
HOST = ''
USER = ''
PASSWORD = ''
DATABASE_NAME = ''
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"
                            #유저   비밀번호    호스트      DB 이름

#----------------------------------------------------------------------------------------------------------

#변수 설정


#mongodb import
from pymongo import MongoClient


#MongoDB 계층
#Database -> Collection(테이블) -> Documents(행) -> Fields(열)

#1. 클라이언트 
#소유 client에 연결
client = MongoClient(MONGO_URI)

#2. database
#client가 가진 DB호출
database = client[DATABASE_NAME]

#3. collection
#DB내부 table 호출
COLLECTION_NAME = ''
collection = database[COLLECTION_NAME]

#----------------------------------------------------------------------------------------------------------

#데이터 입력


#1-1. json형식의 단일 데이터(딕셔너리)
json_data = {
    "A" : {
        "a" : "1"
    },
    "B" : {
        "b" : "2"
    },
    "C" : "3",
    "D" : 4
    }

#1-2. json형식 다중 데이터(리스트)
json_data_many = [
    json_data, 
    json_data
    ]


#2-1. insert_one : json데이터 하나 입력
collection.insert_one(json_data)

#2-2. insert_many : json데이터 여러개 입력
collection.insert_many(json_data_many)

#----------------------------------------------------------------------------------------------------------

#데이터 조회


#find : 모든 document 조회
collection.find()
collection.find().pretty() #깔끔한 출력

#find query적용
collection.find({"a" : "1"}) #a : 1인 document
collection.find({"D" : {$lte: 30}}) #D가 5이하인 document


#find_one : 첫번째 document만 조회
collection.find_one()