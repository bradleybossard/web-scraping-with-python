FROM ubuntu:15.04

RUN apt-get update --fix-missing --yes

RUN apt-get install --yes python3 vim python3-bs4

WORKDIR /src
