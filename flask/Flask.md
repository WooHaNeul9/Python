### Flask

- Flask
사용자 요청이 들어왔을 때 파이썬을 이용해서 코드를 동적으로 생성하고 그것을 응답해주는 것을 편리하게 해줌

***

- 터미널에서 flask 설치
pip install flask

- 터미널에서 server 실행
python 파일명

***

### 라우팅

- 요청을 누가 담당하고 요청을 어떤 함수가 응답할 것인지 연결해주는 것

```
@app.route('/')
def index():
    return 'Index Page'
```
```
@app.route('/hello')
def hello():
    return 'Hello, World'
```

***