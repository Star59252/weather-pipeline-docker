import os
import requests
import mysql.connector
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY", "Hyderabad")

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME", "weather_db")
DB_PORT = int(os.getenv("DB_PORT", 3306))

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def transform(data):
    return {
        "city": data.get("name"),
        "temp": data.get("main", {}).get("temp"),
        "humidity": data.get("main", {}).get("humidity"),
        "pressure": data.get("main", {}).get("pressure"),
        "wind": data.get("wind", {}).get("speed"),
        "desc": data.get("weather", [{}])[0].get("description")
    }

def load_db(record):
    conn = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, port=DB_PORT
    )
    cursor = conn.cursor()
    query = """
        INSERT INTO weather_data (city, temperature, humidity, pressure, wind_speed, description)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        record["city"], record["temp"], record["humidity"],
        record["pressure"], record["wind"], record["desc"]
    ))
    conn.commit()
    cursor.close()
    conn.close()

def run_once():
    try:
        data = fetch_weather()
    except Exception as e:
        print("Fetch failed:", e)
        return False
    record = transform(data)
    try:
        load_db(record)
    except Exception as e:
        print("DB insert failed:", e)
        return False
    print(f"Inserted: {record} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    return True

if __name__ == "__main__":
    # If run directly, perform one run
    run_once()
