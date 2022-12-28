from flask import Flask
app = Flask(__name__) #저장되어 있는 위치 지정

#-----------------------------------------------------------------------

#라우트 : 엔드 포인트에 대한 응답 방식

#1. 라우트 추가
@app.route('/')  #'/' : 루트 주소 / 에 접속했을 때 실행
def index():
    return 'Hello World'

#2. 엔드 포인트 변수 받기
@app.route('/index/<item>')
def item_print(item):
    return f'Itme is {item}' 

#3. 초기값 설정
@app.route('/index/', defaults={'item':'none'})
@app.route('/index/<item>')
def item_print(item):
    return f'Itme is {item}' 

#-----------------------------------------------------------------------

#블루프린트 : 외부 라우트

#1. 폴더 구조
'''
app
├── __init__.py
└── routes
    └── user_routes.py
'''

#2-1. 블루프린트 만들기(user_routes.py)
from flask import Blueprint
bp = Blueprint('user', __name__, url_prefix='/user')
    # user : 블루프린트 명칭(url에서의 명칭)
    # __name__ : 블루프린트 import 명칭
    # url_prefix : 해당 블루프린트의 기본 접두어
@bp.route('/')
    # ~~~/user/
def index():
    return 'User Route'

#2-2. 블루프린트 호출(__init__.py 에서)
from app.routes import user_routes
    # 블루프린트 경로               
app.register_blueprint(user_routes.bp) # 블루프린트 라우트

#-------------------------------------------------------------------------

#애플리케이션 팩토리 : 여러개 블루프린트

def app_factory():
    app = Flask(__name__)

    from app.routes import user_routes1
    from app.routes import user_routes2
    app.register_blueprint(user_routes1)
    app.register_blueprint(user_routes2)

    return app

#-------------------------------------------------------------------------

#템플릿 : html파일 호출

#1. 폴더 구조
'''
app
├── __init__.py
├── routes
|   └── user_routes.py
└── templates
    └── index.html
'''

#2. 템플릿 작성(index.html 파일)
<html>
  <head>
    <title>
      New HTML Page
    </title>
  </head>
  <body>
    <h1>I am in templates folder</h1>
    #body에 추가 기능 작성
  </body>
</html>

#3. 템플릿 호출(__init__.py 에서)
from flask import render_template
@app.toute('/')
def index():
    return render_template('index.html')