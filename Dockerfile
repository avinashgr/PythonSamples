FROM ubuntu:latest
LABEL maintainer="dmadad@icloud.com"

RUN apt update && apt -y upgrade  && apt-get update 

RUN apt-get install -y --fix-missing python3 && apt install -y --fix-missing python3-pip 

RUN apt install -y build-essential libssl-dev libffi-dev python3-dev && apt install -y python3-venv

RUN apt-get install -y --fix-missing wget

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb --fix-missing; apt-get -fy install

RUN  mkdir -p environments/development/python/notebook && cd environments/development/python/notebook && python3 -m venv jupyterenv && . jupyterenv/bin/activate && pip install jupyter

EXPOSE 8888