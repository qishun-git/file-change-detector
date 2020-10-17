FROM ubuntu:20.04
LABEL name="file-change-detector"
MAINTAINER qishunw "wqs751746269@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /

CMD python3 application.py