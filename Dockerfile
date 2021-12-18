FROM ubuntu

RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get update
RUN apt-get install -y python3 python3-pip vim cron git-all firefox

ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]
