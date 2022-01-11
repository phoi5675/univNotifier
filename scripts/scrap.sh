#!/bin/bash

cron_log="/var/log/cron.log"

# Change CRLF -> LF
sed -i -e 's/\r$//' ${SCRAPDIR}/*.*

# remove previous scraped files
find ${SCRAPDIR}/ -type f -name "*.html" -exec rm {} \;
echo $(date) : started scraping >> ${cron_log}

# start web scraping
python3 ${SCRAPDIR}/run.py
echo $(date) : finished scraping >> ${cron_log}