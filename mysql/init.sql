CREATE DATABASE IF NOT EXISTS weather_db;
USE weather_db;

CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    wind_speed FLOAT,
    description VARCHAR(200),
    dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
