#!/bin/bash

echo $(date) : sending mail >> ${CRON_LOG}
python3 ${SCRAPDIR}/sendMail.py
echo $(date) : finished sending mail >> ${CRON_LOG}
