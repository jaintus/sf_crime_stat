# SF Crime Stats


## Beginning the Project

This project requires creating topics, starting Zookeeper and Kafka server, and your Kafka bootstrap server. Use the commands below to start Zookeeper and Kafka server.

```
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```
You can start the server using this Python command:

`python producer_server.py`

## Step 1
To see if the server is correctly implemented, use the command:
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <your-topic-name> --from-beginning
```


## Step 2
Apache Spark already has an integration with Kafka Brokers, hence we will not need a separate Kafka Consumer.
Features are implemented in `data_stream.py`.
Do a spark-submit using this command: 
```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0 --master local[4] data_stream.py```


## Step 3
Run `consumer_server.py` to see if `producer_server.py` is working properly.