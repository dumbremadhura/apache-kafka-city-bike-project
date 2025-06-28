"""
Kafka producer module for sending messages to a specified Kafka topic.

This module wraps the KafkaProducer from the `kafka-python` library to simplify
sending JSON-serialized messages to a local Kafka cluster.
"""

import json
from kafka import KafkaProducer

class Producer:
    """
    Kafka JSON producer for publishing messages to Kafka topics.

    Initializes a Kafka producer with JSON serialization.
    """

    def __init__(self):
        """
        Sets up the Kafka producer with a local Kafka broker and JSON value serializer.
        """
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda m: json.dumps(m).encode('utf-8')
        )

    def data_producer(self, topic, message):
        """
        Sends a JSON-serialized message to a specified Kafka topic.

        Args:
            topic (str): Name of the Kafka topic.
            message (dict): Data to be sent to the topic.
        """
        self.producer.send(topic, message)
