"""
Fetches Citi Bike station information and status from the public NYC GBFS API
and publishes the data to corresponding Kafka topics.

This module integrates HTTP service calls and Kafka production logic to handle
real-time bike data streaming.
"""

from services.http_service import HttpService
from kafka_producer import Producer
from constants.routes import BIKES_STATION_INFORMATION, BIKES_STATION_STATUS
from constants.topics import BIKES_STATION_INFORMATION_TOPIC, BIKES_STATION_STATUS_TOPIC


class Bikes:
    """
    Bikes data handler that fetches bike station data and publishes it to Kafka topics.
    """

    def __init__(self):
        """
        Initializes HTTP client and Kafka producer.
        """
        self.http_service = HttpService()
        self.producer = Producer()

    def get_bikes_station_information(self, url, params):
        """
        Fetches station metadata (e.g., location, capacity) from the Citi Bike API
        and sends each station's data to the `bikes_station_information` Kafka topic.

        Args:
            url (str): API endpoint for station information.
            params (dict): Optional parameters for the GET request.
        """
        response = self.http_service.get(url, params=params).json()
        for message in response['data']['stations']:
            print('BIKES_STATION_INFORMATION : ', message)
            self.producer.data_producer(BIKES_STATION_INFORMATION_TOPIC, message)

    def get_bikes_station_status(self, url, params):
        """
        Fetches real-time station status (e.g., available bikes, docks) from the Citi Bike API
        and sends each station's data to the `bikes_station_status` Kafka topic.

        Args:
            url (str): API endpoint for station status.
            params (dict): Optional parameters for the GET request.
        """
        response = self.http_service.get(url, params=params).json()
        for message in response['data']['stations']:
            print('BIKES_STATION_STATUS : ', message)
            self.producer.data_producer(BIKES_STATION_STATUS_TOPIC, message)
