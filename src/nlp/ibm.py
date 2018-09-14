import subprocess

class WatsonWrapper():
    def __init__(self):
        pass
    def translate(self, text):
        command = "curl --user apikey:oCO2bYH9NOyLzpqCCi-a0hypOM1hfC1FHwH7Ec-mTWX9 --request POST --header \"Content-Type: application/json; charset=UTF-8\" --data \"{\\\"text\\\":[\\\"" + text +"\\\"],\\\"model_id\\\":\\\"ja-en\\\"}\" \"https://gateway-syd.watsonplatform.net/language-translator/api/v3/translate?version=2018-05-01\""
        print(command)
        
        subprocess.run(command) 
        
        
        #curl --user apikey:oCO2bYH9NOyLzpqCCi-a0hypOM1hfC1FHwH7Ec-mTWX9 --request POST --header "Content-Type: application/json" --data #"{\"text\":[\"ここは\"],\"model_id\":\"ja-en\"}" "https://gateway-syd.watsonplatform.net/language-translator/api/v3/translate?version=2018-05-01"
        
        #{"text":[""],"model_id":"ja-en"}
        
        
watson = WatsonWrapper()
watson.translate("ここは牛丼がおしいいです。")