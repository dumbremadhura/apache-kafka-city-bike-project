"""
Kafka consumer script for Citi Bike NYC data.

This script listens to:
- Station information topic (e.g., metadata like location, capacity)
- Station status topic (e.g., available bikes and docks)

...and prints the consumed messages to the console.
"""

from constants import BIKES_STATION_INFORMATION_TOPIC, BIKES_STATION_STATUS_TOPIC
from kafka_consumer import Consumer


class Consume:
    """
    A consumer class that subscribes to Citi Bike Kafka topics and logs messages.
    """
    def __init__(self):
        """
        Initializes a Kafka consumer with a predefined consumer group.
        """
        self.consumer_group = Consumer('city_bike_stations_consumer_group')
    
    def consume(self):
        """
        Subscribes to bike-related Kafka topics and continuously consumes messages.
        Prints metadata and content of each Kafka message.
        """
        while True:
            # Subscribe to and consume from station information topic
            self.consumer_group.subscribe_consumer([BIKES_STATION_INFORMATION_TOPIC])
            for message in self.consumer_group.consumer:
                print(message.topic, message.partition, message.offset)

            # Subscribe to and consume from station status topic
            self.consumer_group.subscribe_consumer([BIKES_STATION_STATUS_TOPIC])
            for message in self.consumer_group.consumer:
                print(message)


# Instantiate and run the consumer
consumer_instance = Consume()
consumer_instance.consume()
