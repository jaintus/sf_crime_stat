import logging
import pykafka


logging.getLogger("pykafka.broker").setLevel('ERROR')

client = pykafka.KafkaClient(hosts="localhost:9092")

consumer_msgs = client.topics["service-calls"].get_balanced_consumer(
    consumer_group = b'pykafka-1',
    auto_commit_enable = False,
    zookeeper_connect = 'localhost:2181'
)

for msg in consumer_msgs:
    if msg is not None:
        print( msg.value.decode('utf-8') )