FROM ubuntu:20.04

# Set timezone to make run cron based on GMT+9.
ENV TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Change apt list to mirror in Korea.
RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

# Install packages.
# ARG DEBIAN_FRONTEND=noninteractive
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y \
	libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 firefox \
	wget python3 python3-pip vim cron git-all htop

# Install python packages.
RUN pip3 install --upgrade pip

RUN pip3 install pycairo PyGObject

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Setup cron
ENV SCRAPDIR="/webScrap"
ARG DOCKERFILES_DIR="dockerfiles"

COPY $DOCKERFILES_DIR/cron_webscrap /etc/cron.d/cron_webscrap
RUN chmod 0644 /etc/cron.d/cron_webscrap

RUN touch /var/log/cron.log

RUN service cron start

# Install geckodriver
ADD https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz \
	/geckodriver-v0.30.0-linux32.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver 
RUN mv ./geckodriver /usr/bin/
RUN rm geckodriver*

# Setup cron
RUN apt-get install -y cron
ENV SCRAPDIR="/webScrap"
ENV CRON_LOG="/var/log/cron.log"
ARG DOCKERFILES_DIR="dockerfiles"

RUN touch /var/log/cron.log
RUN chmod 644 /var/log/cron.log

COPY $DOCKERFILES_DIR/cron_webscrap /etc/cron.d/cron_webscrap

# Change CRLF -> LF
RUN sed -i -e 's/\r$//' /etc/cron.d/cron_webscrap

RUN chmod 0644 /etc/cron.d/cron_webscrap

RUN crontab /etc/cron.d/cron_webscrap

# Add entrypoint
COPY $DOCKERFILES_DIR/entrypoint.sh /entrypoint.sh

# Fix permission for entrypoint.sh
RUN chmod 0755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
