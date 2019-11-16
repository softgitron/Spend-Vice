#!/usr/bin/python
import sys
import json

givenURL = sys.argv[1]
#Save the generated ean to "generatedEAN" and print it!
#generatedEAN = 430303030
x = {
    "Price":420,
    "Image":"https://image.businessinsider.com/59974812b0e0b595758b5449?width=1100&format=jpeg&auto=webp",
    "Name":"Essential Phone"
}
y = json.dumps(x)
print(y)
#print(generatedEAN)
sys.stdout.flush()