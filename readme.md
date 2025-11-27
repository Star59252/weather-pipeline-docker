# Dockerized Weather ETL Pipeline
📖 Project Overview
This project is an automated ETL (Extract, Transform, Load) pipeline that monitors real-time weather conditions. It is fully containerized using Docker, ensuring it runs consistently in any environment.

Extract: A Python script fetches live weather data for Phagwara from the OpenWeatherMap API every hour.

Transform: The data is processed to extract key metrics (Temperature, Humidity, Wind Speed).

Load: Cleaned data is stored in a MySQL database.

Visualize: A Grafana dashboard connects to the database to visualize weather trends over time.

> **⚠️ Assessment Note:**
> For the purpose of this assessment review, the `.env` configuration file (containing API keys and Database credentials) has been **included** in this repository. 
> You can simply clone this repo and run it immediately without extra configuration.

## ⚡ Quick Start (For Reviewers)

To see the pipeline in action on your machine, follow these two steps:

### 1. Run the Application
```bash
# Clone the repository
git clone [https://github.com/Star59252/weather-pipeline-docker.git](https://github.com/Star59252/weather-pipeline-docker.git)
cd weather-pipeline-docker

# Start the application (using the included .env config)
docker-compose up --build

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
│   ├── Dockerfile          # Python environment setup
│   ├── weather_etl.py      # Main script to fetch & store data
│   ├── run_etl.sh          # Execution wrapper
│   ├── entrypoint.sh       # Cron job scheduler
│   └── test_weather.py     # Unit tests for CI pipeline
├── mysql/
│   └── init.sql            # Database schema initialization
├── .github/
│   └── workflows/          # CI/CD Pipeline configuration
├── docker-compose.yml      # Orchestration of all services
├── .env                    # Credentials (Included for assessment)
└── README.md

📝 Database Schema
The system automatically initializes a table named weather_data with the following columns:

id: Primary Key

city: Target city (Phagwara)

temperature: Temperature in Celsius

humidity: Humidity percentage

pressure: Atmospheric pressure

wind_speed: Wind speed

description: Weather condition description

dt: Timestamp of record
