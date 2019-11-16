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
if (crawl):
    crawl = crawl[0]
    flag = False
    crawl_list = list(crawl)
    for index in range(len(crawl)):
        if (crawl[index] == '"' and flag == True):
            flag = False
        elif (crawl[index] == '"' and flag == False):
            flag = True
        if (crawl[index] == "'" and flag == False):
            crawl_list[index] = '"'
    crawl = ''.join(map(str, crawl_list)) 
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
    json_data['Price'] = float(sanitized_price)
    crawl = json.dumps(json_data)
    print(crawl)
else:
    print("ERROR")
sys.stdout.flush()