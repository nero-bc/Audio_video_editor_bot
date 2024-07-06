FROM python:3.9-slim

RUN apt-get update && apt-get install -y ffmpeg sqlite3 libsqlite3-dev

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "start.py"]
