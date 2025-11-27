#!/bin/bash
set -e

# create log file
touch /var/log/etl.log
chmod 666 /var/log/etl.log

# add cron job: run at minute 0 every hour
echo "0 * * * * /app/run_etl.sh" > /etc/cron.d/weather_etl_cron

# give execution rights on the cron job
chmod 0644 /etc/cron.d/weather_etl_cron

# apply cron job
crontab /etc/cron.d/weather_etl_cron

# run cron in foreground
cron && tail -F /var/log/etl.log
