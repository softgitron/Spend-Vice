#!/usr/bin/python
import sys
import re
import subprocess
import os

if (len(sys.argv) > 1):
    givenURL = sys.argv[1]
else:
    print("No url as input.")
    exit(1)
# Call Crawler script
# https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
cwd=os.path.dirname(os.path.realpath(__file__)) + '/prod_info/'
result = subprocess.run(['scrapy', 'crawl', 'amazon', '-a', 'url=' + givenURL], cwd=cwd, stderr=subprocess.PIPE)
output = result.stderr.decode('utf-8')
crawl = re.findall(r"\{\'Name\'.*?\}", output)
if (crawl):
    crawl = crawl[0].replace("'", '"')
    print(crawl)
else:
    print("ERROR")
sys.stdout.flush()