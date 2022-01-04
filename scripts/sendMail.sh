#!/bin/bash

cronfile="/var/log/cron.log"

echo $(date) : sending mail >> ${cronfile}
python3 ${SCRAPDIR}/sendmail.py
echo $(date) : finished sending mail >> ${cronfile}
