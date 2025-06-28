# 🚴‍♂️ City Bike Kafka Streaming Project

This project is a hands-on Kafka streaming pipeline built as part of **Darshil Parmar's Apache Kafka course on DataVidhya**. 
It demonstrates how to fetch real-time Citi Bike NYC data from public APIs, produce it to Kafka topics, and consume it using simple Python scripts — helping you understand the core concepts of Kafka in practice.

## 📁 Project Structure
city-bike-project/
│
├── bikes/ # Core logic for fetching and sending bike data
│ └── bikes.py
│
├── kafka_consumer/ # Kafka consumer script
│ └── consumer.py
│
├── kafka_producer/ # Kafka producer script
│ └── producer.py
│
├── services/ # HTTP service wrapper
│ └── http_service.py
│
├── constants/ # API routes and Kafka topic names
│ ├── routes.py
│ └── topics.py
│
├── docker-compose.yml # Docker setup for Kafka and Zookeeper
├── .gitignore # Ignore unneeded files
└── README.md # You're here



## 🔧 Prerequisites

- Docker and Docker Compose installed
- Python 3.7+
- `requests` and `kafka-python` libraries installed for Python scripts

## 🐳 Setup with Docker

1. **Start Kafka and Zookeeper**
   ```bash
   docker-compose up -d

2. **Enter Kafka container**
   ```bash
   docker exec -it <container_id_or_name> bash

***You can find the Kafka container name with:***
   ```bash
   docker ps

3. **Create Kafka Topics**
    ```bash
    kafka-topics.sh --create --topic bikes_station_information --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
    kafka-topics.sh --create --topic bikes_station_status --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

## Run the Project
***Open multiple terminal windows for the following:***
1. **Start Producer script**
    ```bash
    python3 bikes/bikes.py
    # This will fetch data from the Citi Bike API and produce messages to Kafka topics.

2. **Start Consumer script**
    ```bash
    python3 consumer/bike_consumer.py
    # This will consume messages from Kafka and print them to the console.

📚 References
Built for educational purposes as part of Darshil Parmar's Apache Kafka course on https://courses.analyticsvidhya.com/.

Citi Bike NYC GBFS data: https://gbfs.citibikenyc.com/gbfs/en/

👩‍💻 Proj Author
Madhura Dumbre,
Data Engineer
📍 Bengaluru, India
🔗 https://www.linkedin.com/in/madhuradumbre/
