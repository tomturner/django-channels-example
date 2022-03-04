FROM python:3.9
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code/

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin git ffmpeg postgresql-client-13

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt
ADD . /code/

