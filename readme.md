# Dockerized Weather ETL Pipeline

This project is an automated ETL (Extract, Transform, Load) pipeline that monitors weather conditions for a specific city. It fetches data from the OpenWeatherMap API every hour, stores it in a MySQL database, and visualizes the trends using Grafana.

## 🚀 Features

* **Automated Data Collection:** A Python script runs continuously on a Cron schedule (every hour) to fetch live weather data.
* **Data Persistence:** Stores City, Temperature, Humidity, Pressure, Wind Speed, and Weather Description in a MySQL database.
* **Visualization:** Integrated Grafana dashboard for real-time monitoring.
* **Containerized:** Fully Dockerized environment using Docker Compose for easy deployment.

## 🛠️ Tech Stack

* [cite_start]**Language:** Python 3.11 [cite: 4]
* **Database:** MySQL 8.0
* **Visualization:** Grafana
* **Orchestration:** Docker & Docker Compose
* **API:** OpenWeatherMap

## 📂 Project Structure

```text
.
├── etl/
│   ├── Dockerfile          # Python image configuration
│   ├── weather_etl.py      # Main ETL script
│   ├── run_etl.sh          # Wrapper script for execution
│   ├── entrypoint.sh       # Cron setup and container entrypoint
│   └── requirements.txt    # Python dependencies
├── mysql/
│   └── init.sql            # Database schema initialization
├── docker-compose.yml      # Service orchestration
├── .env                    # Environment variables (Credentials)
└── README.md