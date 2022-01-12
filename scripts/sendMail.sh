#!/bin/bash

echo $(date) : sending mail >> ${CRON_LOG}
python3 ${SCRAPDIR}/sendmail.py
echo $(date) : finished sending mail >> ${CRON_LOG}
