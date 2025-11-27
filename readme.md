# 🌤️ Dockerized Weather ETL Pipeline (Fully Automated)

> **⚠️ Assessment Note:**
> For the purpose of this assessment review, the `.env` configuration file (containing API keys and Database credentials) is **included** in this repository. 
> The project is configured for **"Zero-Touch" deployment**: Data fetching starts immediately, and Grafana connects to the database automatically.

## ⚡ Quick Start (One Command)

You can run this project locally or in the cloud. No manual configuration is required.

### Option A: Run Locally (Requires Docker)
```bash
# 1. Clone the repository
git clone [https://github.com/Star59252/weather-pipeline-docker.git](https://github.com/Star59252/weather-pipeline-docker.git)
cd weather-pipeline-docker

# 2. Start the application
docker-compose up --build -d
````

### Option B: Run in Browser (No Installation)

1.  Click the green **Code** button \> **Codespaces** \> **Create codespace on main**.
2.  Wait for the terminal to load.
3.  If it doesn't start automatically, run: `docker-compose up --build -d`

-----

## 🖥️ Accessing the Dashboard

Once the containers are running, the services are available immediately:

| Service | URL | Username | Password | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Grafana** | [http://localhost:3000](https://www.google.com/search?q=http://localhost:3000) | `bashansnehith123` | `Sneh!th59252` | **Auto-Connected** ✅ |
| **MySQL** | `localhost:3307` | `root` | `59252` | **Active** ✅ |

  * **Check Logs:** `docker logs -f weather_etl`

-----

## 🚀 Key Features (Automation)

This pipeline is designed to be self-healing and fully automated:

  * **Instant Data Fetch:** The Python script runs **immediately** upon container startup (via `entrypoint.sh`). You do not need to wait for the hourly Cron job to trigger the first data point.
  * **Auto-Provisioned Grafana:** The MySQL connection is **pre-configured** via `config/datasource.yml`. You do not need to manually add the data source in the GUI.
  * **Resilient Scheduling:** After the initial run, a Cron job schedules the script to run at the top of every hour to track long-term trends.

## 📂 Project Structure

```text
.
├── etl/
│   ├── Dockerfile          # Python environment setup
│   ├── weather_etl.py      # Core logic: Fetch API -> Transform -> Load DB
│   ├── run_etl.sh          # Wrapper script for execution
│   ├── entrypoint.sh       # Logic for Cron + Immediate Run
│   └── test_weather.py     # Unit tests
├── config/
│   └── datasource.yml      # Grafana auto-provisioning config
├── mysql/
│   └── init.sql            # Database schema initialization
├── .devcontainer/          # GitHub Codespaces configuration
├── docker-compose.yml      # Service orchestration
├── .env                    # Credentials (Included for review)
└── README.md
```

## 🛠️ Tech Stack

  * **ETL Script:** Python 3.11 (Requests, MySQL Connector)
  * **Database:** MySQL 8.0
  * **Visualization:** Grafana (Provisioned via file)
  * **Orchestration:** Docker Compose
  * **CI/CD:** GitHub Actions & Codespaces

## 📝 Database Schema

The `weather_data` table stores the following metrics for **Phagwara**:

  * `temperature` (°C)
  * `humidity` (%)
  * `pressure` (hPa)
  * `wind_speed` (m/s)
  * `description` (Text)
  * `dt` (Timestamp)

