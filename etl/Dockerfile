FROM python:3.11-slim

# install cron and required packages
RUN apt-get update && apt-get install -y cron gcc g++ --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy files
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY weather_etl.py /app/
COPY run_etl.sh /app/
COPY entrypoint.sh /app/

RUN chmod +x /app/run_etl.sh /app/entrypoint.sh

ENV PYTHONUNBUFFERED=1

CMD ["/app/entrypoint.sh"]
