"""
Kafka consumer module for reading messages from specified Kafka topics.

Wraps the KafkaConsumer from the `kafka-python` library and provides 
simple subscribe and unsubscribe functionality.
"""

import json
from kafka import KafkaConsumer

class Consumer:
    """
    Kafka JSON consumer for subscribing to and reading messages from topics.

    Args:
        group_id (str): The consumer group ID used to manage offsets and group coordination.
    """

    def __init__(self, group_id):
        """
        Initializes the Kafka consumer with JSON deserialization and offset reset strategy.
        """
        self.consumer = KafkaConsumer(
            bootstrap_servers='localhost:9092',
            group_id=group_id,
            auto_offset_reset='earliest',
            value_deserializer=lambda m: json.loads(m)
        )

    def subscribe_consumer(self, topic):
        """
        Subscribes the consumer to a specified Kafka topic.

        Args:
            topic (str): Name of the Kafka topic to subscribe to.
        """
        self.consumer.subscribe(topic)

    def unsubscribe_consumer(self):
        """
        Unsubscribes the consumer from all currently subscribed topics.
        """
        self.consumer.unsubscribe()
