# base image
FROM python:3.96

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]