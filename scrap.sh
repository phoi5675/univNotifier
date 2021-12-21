# remove previous scraped files
find /webScrap/ -type f -name "*.html" -exec rm {} \;

# start web scraping
python3 /webScrap/run.py
exit
