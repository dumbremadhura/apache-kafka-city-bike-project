"""
Contains API endpoints for accessing Citi Bike NYC data.

These constants provide the GBFS (General Bikeshare Feed Specification) endpoints
for station information and station status.
"""

BIKES_STATION_INFORMATION = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'
"""URL to fetch static Citi Bike station metadata (name, location, capacity, etc.)."""

BIKES_STATION_STATUS = 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json'
"""URL to fetch real-time Citi Bike station status (bikes available, docks available, etc.)."""
