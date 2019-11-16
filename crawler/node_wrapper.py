#!/usr/bin/python
import sys
import re
import subprocess
import os
import json

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
try:
    if (crawl):
        crawl = crawl[0]
        crawl = crawl.replace("'", "")
        crawl = crawl.replace('"', "")
        crawl = crawl.replace("{Name:", '{"Name": "')
        crawl = crawl.replace(", Price:", '", "Price": "')
        crawl = crawl.replace(", Image:", '", "Image": "')
        crawl = crawl[:-1]
        crawl += '"}'
        json_data = json.loads(crawl)
        price = json_data['Price']
        sanitized_price = ""
        for letter in price:
            if (letter == "$" or letter == "€" or letter == " "):
                continue
            if (letter.isdigit() == True or letter == '.'):
                sanitized_price += letter
            else:
                break
        if (sanitized_price.isdecimal()):
            json_data['Price'] = float(sanitized_price)
        else:
            json_data['Price'] = 0
        if ('Name' in json_data):
            json_data['Name'] = json_data['Name'].strip()
        if ('Image' in json_data):
            json_data['Image'] = json_data['Image'].strip()
        crawl = json.dumps(json_data)
        print(crawl)
    else:
        print("ERROR")
    sys.stdout.flush()
except Exception as e: print(e)