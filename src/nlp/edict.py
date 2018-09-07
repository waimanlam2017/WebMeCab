import sqlite3

class EdictWrapper():
    def __init__(self):
        pass
        
    def create_connection(self, db_file):
        try:
            return sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return None
            
    #def lookup_word(self, word):
    #    c = self.conn.cursor()
    #    c.execute("SELECT def FROM Dict WHERE kanji=?", (word,))
    #    result = c.fetchone()
    #    if ( result is not None ):
    #        return result[0]
    #    return result
        
                
    def parse_mecab_result(self, mecab_result):
        edict_result = []
        for entry in mecab_result:
            word = entry[0]
            pos = entry[1]
            conn = self.create_connection('edict.sqlite')
            cursor = conn.cursor()
            cursor.execute("SELECT def FROM Dict WHERE kanji=?", (word,))
            result = cursor.fetchone()
            if ( result is not None ):
                definition =  result[0]
                edict_result.append( {'name':word, 'pos':pos, 'definition':definition} )
            else:
                edict_result.append( {'name':word, 'pos':pos, 'definition':''} )
        return edict_result
                


    