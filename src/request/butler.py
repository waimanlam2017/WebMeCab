from src.nlp.mecab_wrapper import PosTagger
import json

class Butler():
    def __init__(self):
        self.mecab = PosTagger()
        
    def ask_mecab(self, text):
        return json.dumps(self.mecab.parse_text(text))
        