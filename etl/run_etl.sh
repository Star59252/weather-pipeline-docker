#!/bin/bash
cd /app
python3 weather_etl.py >> /var/log/etl.log 2>&1