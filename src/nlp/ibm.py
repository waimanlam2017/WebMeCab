import subprocess
import json

class WatsonWrapper():
    def __init__(self):
        pass
    def translate(self, text):
        command = "curl --user apikey:oCO2bYH9NOyLzpqCCi-a0hypOM1hfC1FHwH7Ec-mTWX9 --request POST --header \"Content-Type: application/json; charset=UTF-8\" --data \"{\\\"text\\\":[\\\"" + text +"\\\"],\\\"model_id\\\":\\\"ja-en\\\"}\" \"https://gateway-syd.watsonplatform.net/language-translator/api/v3/translate?version=2018-05-01\""
        
        com = subprocess.run(command, shell=True, stdout= subprocess.PIPE) 
        
        if ( com.returncode == 0 ):
            my_json = com.stdout.decode('utf8')
            data = json.loads(my_json)
            print(data)
            return data
        else:
            return "{'translations': [{'translation': 'Translation Error.'}]"
        
