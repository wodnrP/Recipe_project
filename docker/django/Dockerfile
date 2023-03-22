# base image
FROM python:3.9.6-slim-buster

# set working directory
WORKDIR /app
# copy project files
COPY ./  /app
# copy requirements.txt
COPY requirements.txt /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt -y install default-libmysqlclient-dev && \ 
    /py/bin/pip install --use-pep517 -r /app/requirements.txt 


# COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf
# COPY ./docker/django/entrypoint.sh /entrypoint.sh

# expose port
EXPOSE 80

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["/py/bin/"]
# run entrypoint.sh
ENTRYPOINT gunicorn -w 4 manage:app -b 0.0.0.0:8000