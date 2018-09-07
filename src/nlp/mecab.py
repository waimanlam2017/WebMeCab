import MeCab

#No unit test for this class, it just call MeCab without special logic

class MeCabWrapper():
    def __init__(self):
        self.m = MeCab.Tagger("-Ochasen")

    def parse_text(self, text):
        self.m.parse("")
        parsed = self.m.parseToNode(text)
        components = []
        while parsed:
            word = parsed.surface
            pos = parsed.feature.split(',')[0]
            tp = (word, pos)
            components.append(tp)
            parsed = parsed.next
        return components