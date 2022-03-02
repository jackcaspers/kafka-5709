from kafka import KafkaConsumer
print('running')
consumer = KafkaConsumer('sample2')
for message in consumer:
    print (message)

