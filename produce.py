"""
Main script to fetch Citi Bike station data and produce it to Kafka topics.

This script repeatedly fetches:
- Station metadata (location, capacity, etc.)
- Station status (availability of bikes/docks)

...and publishes each record to its corresponding Kafka topic using the `Bikes` class.
"""

from bikes import Bikes
from constants import BIKES_STATION_INFORMATION, BIKES_STATION_STATUS

# Infinite loop to continuously fetch and produce bike data
while True:
    bikes = Bikes()
    
    # Fetch and produce station information to Kafka
    bikes.get_bikes_station_information(BIKES_STATION_INFORMATION, {}) 
    
    # Fetch and produce station status to Kafka
    bikes.get_bikes_station_status(BIKES_STATION_STATUS, {})       
