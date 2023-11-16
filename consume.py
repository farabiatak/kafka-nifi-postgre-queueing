import json
from kafka import KafkaConsumer
import time 
consumer = KafkaConsumer(
    'sword2', bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: m.decode('utf-8'),group_id='kafka-nifi-deneme'
    )

for msg in consumer:
    #time.sleep(2)
    data = msg.value
    to_json = json.loads(data)
    print(msg.value)

    
    