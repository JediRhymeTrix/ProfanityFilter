# nginx-gunicorn-flask with python2.7

FROM python:2.7

RUN apt update
RUN apt install -y nginx supervisor
RUN pip install gunicorn

ENV PYTHONIOENCODING=utf-8

# Build folder
RUN mkdir -p /deploy/app
WORKDIR /deploy/app
COPY app /deploy/app
RUN pip install -r /deploy/app/requirements.txt
# remove this line if not required:
RUN python ./utils/prep.py

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY configs/nginx_flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx_flask.conf /etc/nginx/sites-enabled/nginx_flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY configs/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

CMD ["/usr/bin/bash"]
