from flask import Flask

app = Flask(__name__) # __name__은 Python에서 자동으로 정의되는 특별한 변수로, 현재 모듈의 이름을 나타냄

@app.route('/')
def index():
    return 'hello'

app.run(debug=True) # 'debug=True'는 브라우저를 새로고침 했을 때 수정한 내용이 자동으로 반영되도록 함 