from src.nlp.mecab_wrapper import PosTagger
from src.nlp.edict import EdictWrapper
import json

class Butler():
    def __init__(self):
        self.mecab = MeCabWrapper()
        self.edict = EdictWrapper()
        
    def ask_mecab(self, text):
        return self.mecab.parse_text(text)
        
    def ask_edict(self, mecab_result):
        return self.edict.parse_mecab_result(mecab_result)
    
    def ask_edict_to_json(self, mecab_result):
        return json.dumps(self.ask_edict(mecab_result))
        