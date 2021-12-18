#!/bin/bash

# to change CRLF -> LF
sed -i -e 's/\r$//' *.*

# remove geckodriver if exists
rm geckodriver*

# setup geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
tar -xvzf geckodriver*

chmod +x geckodriver

mv ./geckodriver /usr/bin/