# kafka-5709
*  John Caspers
* SENG 5709 Big Data Engineering

First we need to start the Kafka Environment by running these two commands inside the Kafka `src` folder. 
```bash
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

```bash
$ bin/kafka-server-start.sh config/server.properties
```

Now that we have those running. We can start our create our topic by running this command. 
```bash
$ bin/kafka-topics.sh --create --topic sample2 --bootstrap-server localhost:9092
```
Now in this GitHub repo we can run both the consumer and producer python files.
```bash 
$ python consumer.py
```
```bash 
$ python producer.py
```
We should see the output in the consumer terminal of our producer sending messages to the topic we created and the consumer receiving those messages. 
