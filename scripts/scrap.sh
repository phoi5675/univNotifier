#!/bin/bash

# Change CRLF -> LF
sed -i -e 's/\r$//' ${SCRAPDIR}/*.*

# remove previous scraped files
find ${SCRAPDIR}/ -type f -name "*.html" -exec rm {} \;
echo $(date) : started scraping >> ${CRON_LOG}

# start web scraping
python3 ${SCRAPDIR}/run.py
echo $(date) : finished scraping >> ${CRON_LOG}