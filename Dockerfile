# base image
FROM python:3.9.6

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app  /app

# set working directory
WORKDIR /app

# expose port
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

#RUN pip install gunicorn
# set environment variables
ENV PATH="/py/bin:$PATH"
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

