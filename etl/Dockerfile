FROM python:3.9

RUN apt update && apt -y upgrade && apt install -y python3-setuptools netcat
RUN pip install pipenv

RUN mkdir /app
WORKDIR /app/
COPY / /app/

RUN pipenv install --system --deploy --skip-lock

ENTRYPOINT ["python", "/app/main.py"]