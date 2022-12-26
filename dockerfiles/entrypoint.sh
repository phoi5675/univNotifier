#!/bin/bash

# Export environment values to use them in cron.
printenv > /environ
# Set permissions
chmod 0744 ${SCRAPDIR}/scripts/scrap.sh
chmod 0744 ${SCRAPDIR}/scripts/sendMail.sh

# Run cron
cron -f

