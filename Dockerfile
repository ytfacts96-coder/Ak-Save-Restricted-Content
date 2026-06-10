FROM python:3.10.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Create sessions directory
RUN mkdir -p /app/sessions

CMD gunicorn app:app --bind 0.0.0.0:10000 & python3 bot.py & wait
