from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/create')
def create():
    return 'create'

@app.route('/read/<id>')
def read(id):
    return 'read' + id

app.run(debug=True)