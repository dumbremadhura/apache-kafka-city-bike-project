"""
Provides a lightweight HTTP client wrapper around the `requests` library.

This service is used to make GET requests to external APIs (e.g., Citi Bike GBFS feeds)
using a persistent session for performance and connection reuse.
"""

import requests


class HttpService:
    """
    A simple HTTP service using a persistent `requests.Session`.

    Methods:
        get(url, params={}): Sends a GET request to the specified URL with optional query parameters.
    """
    
    def __init__(self):
        """Initializes the HTTP session."""
        self.http_conn = requests.Session()
    
    def get(self, url, params={}):
        """
        Sends a GET request to the provided URL with optional query parameters.

        Args:
            url (str): The URL to send the GET request to.
            params (dict, optional): Dictionary of query parameters. Defaults to empty dict.

        Returns:
            Response: A `requests.Response` object containing the server's response.
        """
        return self.http_conn.get(url, params=params)
