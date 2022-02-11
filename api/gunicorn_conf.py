import os

loglevel = os.getenv("LOGLEVEL", "DEBUG")
errorlog = '/usr/local/var/log/gunicorn/gunicorn-error.log'
accesslog = '/usr/local/var/log/gunicorn/gunicorn-access.log'

bind = ['0.0.0.0:5000']
