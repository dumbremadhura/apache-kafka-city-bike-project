"""
Kafka topic names used in the Citi Bike streaming pipeline.

These constants define the Kafka topics where different types of Citi Bike data
(station metadata and station status) are produced and consumed.
"""

BIKES_STATION_INFORMATION_TOPIC = 'bikes_station_information'
"""Kafka topic for station metadata such as location, name, and capacity."""

BIKES_STATION_STATUS_TOPIC = 'bikes_station_status'
"""Kafka topic for real-time station availability including bikes and docks."""
