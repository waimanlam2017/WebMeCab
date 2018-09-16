from src.nlp.mecab import MeCabWrapper
from src.nlp.edict import EdictWrapper
from src.nlp.ibm import WatsonWrapper
import json

class Butler():
    def __init__(self):
        self.mecab = MeCabWrapper()
        self.edict = EdictWrapper()
        self.ibm = WatsonWrapper()
        
    def ask_mecab(self, text):
        return self.mecab.parse_text(text)
        
    def ask_edict(self, mecab_result):
        return json.dumps(self.edict.parse_mecab_result(mecab_result))
    
    def ask_watson(self, text):
        return json.dumps(self.ibm.translate(text))
        