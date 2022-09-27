FROM python:3.10

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN python manage.py collectstatic --noinput

CMD uwsgi --module=aikido_cardiff.wsgi --http=0.0.0.0:80
# CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" aikido_cardiff.wsgi
