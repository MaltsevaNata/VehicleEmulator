FROM python:3.9

RUN apt update && apt -y upgrade && apt install -y python3-setuptools netcat
RUN pip install pipenv

RUN mkdir /app
WORKDIR /app/
COPY / /app/

RUN pipenv install --system --deploy --skip-lock
RUN mkdir -p /usr/local/var/log/gunicorn/

ENTRYPOINT ["gunicorn", "-c", "gunicorn_conf.py", "main:web_app", "--reload", "--worker-class", "aiohttp.GunicornWebWorker"]