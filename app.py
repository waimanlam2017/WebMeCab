#!flask/bin/python
from flask import Flask
from flask import request
from flask_cors import CORS
from src.request.butler import Butler
app = Flask(__name__)
CORS(app)


butler = Butler()
@app.route('/postjson', methods=['POST'])
def post():
    print("Is Request JSON:", request.is_json)
    print("Request:", request)
    content = request.get_json()
    print("The data from request:" , content['text'])
    print("What is return from mecab:" , butler.ask_mecab(content['text']))
    return butler.ask_mecab(content['text'])

app.run(host='0.0.0.0', port=19999)