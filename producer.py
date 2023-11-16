import json
import time
from kafka import KafkaProducer
import pandas as pd
import re
import requests

links=["https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/1.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/2.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/3.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/4.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/5.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/6.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/7.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/8.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/9.json",
       "https://raw.githubusercontent.com/Swordsec/challenge-questions/master/backend/users/10.json"
       ]

    
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=lambda m: json.dumps(m).encode('utf-8'))
for link in links:
    try:   
        df = pd.read_json(link)
        for i,row in df.iterrows():
            to_json = row.to_dict()
            producer.send('sword2', value=to_json)
            #time.sleep(2)
            producer.flush()
            print("veri gönderildi")
    except :
        url = (link)
        response = requests.get(url)
        json_verisi = response.text
        regex_ifadesi = r'\{[^}]+\}'
        eslesmeler = re.findall(regex_ifadesi, json_verisi)
        duzeltilmis_json = '[' + ','.join(eslesmeler) + ']'
        df = pd.read_json(duzeltilmis_json)
        for i,row in df.iterrows():
            to_json = row.to_dict()
            producer.send('sword2', value=to_json)
            #time.sleep(2)
            producer.flush()
            print("veri gönderildi")
    
    
    
    
    
    
    
    

    
