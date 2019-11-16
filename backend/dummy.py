#!/usr/bin/python
import sys
import json

givenURL = sys.argv[1]
#Save the generated ean to "generatedEAN" and print it!
#generatedEAN = 430303030
x = {
    "Price":300,
    "Image":"https://images.unsplash.com/photo-1504148455328-c376907d081c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1143&q=80",
    "Name":"Epic Product"
}
y = json.dumps(x)
print(y)
#print(generatedEAN)
sys.stdout.flush()