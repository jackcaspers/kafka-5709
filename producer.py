from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sample2', b'Hello, World!')
producer.send('sample2', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()