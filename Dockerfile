FROM ubuntu:20.04

ENV TZ="Asia/Seoul"
RUN date

RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y wget python3 python3-pip vim cron git-all

RUN apt-get install -y  libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]
