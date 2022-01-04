#!/bin/bash

cronfile="/var/log/cron.log"

# Change CRLF -> LF
sed -i -e 's/\r$//' *.*

# remove previous scraped files
find ${SCRAPDIR}/ -type f -name "*.html" -exec rm {} \;
echo $(date) : started scraping >> ${cronfile}

# start web scraping
python3 ${SCRAPDIR}/run.py
echo $(date) : finished scraping >> ${cronfile}