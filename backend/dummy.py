#!/usr/bin/python

import requests
import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

if sys.argv < 2:
    print("no args!")