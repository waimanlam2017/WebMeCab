#!flask/bin/python
from flask import Flask
from flask import request
from flask_cors import CORS
from src.request.butler import Butler
app = Flask(__name__)
CORS(app)


butler = Butler()
@app.route('/tokenize', methods=['POST'])
def tokenize():
    content = request.get_json()
    mecab_result = butler.ask_mecab(content['text'])
    return butler.ask_edict(mecab_result)

@app.route('/translate', methods=['POST'])
def translate():
    content = request.get_json()
    text =content['text']
    return butler.ask_watson(text)



app.run(host='0.0.0.0', port=19999)