#!/usr/bin/python
import sys
import json

givenURL = sys.argv[1]
#Save the generated ean to "generatedEAN" and print it!
#generatedEAN = 430303030
if (givenURL === "https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B0756CYWWD?_encoding=UTF8&%2AVersion%2A=1&%2Aentries%2A=0"){
    x = {
        "Price": 349,
        "Image":"https://images-na.ssl-images-amazon.com/images/I/51sAtKgDkDL.jpg",
        "Name":"Bose Quite Comfort Headphones"
    };
} else if (givenURL === "https://www.amazon.com/Sandisk-128GB-Flash-Memory-Drive/dp/B00P8XQPY4/ref=sr_1_27?qid=1573973513&sr=8-27&srs=18332380011"){
    x = {
        "Price":18.92,
        "Image":"https://images-na.ssl-images-amazon.com/images/I/51dudPA-u4L._SL1100_.jpg",
        "Name":"Sandisk Flash Memory Drive"
    };
} else if (givenURL === "https://www.amazon.com/AmazonBasics-Hardside-Spinner-Luggage-20-Inch/dp/B071VG5N9D?pf_rd_p=8eb011f8-a9f1-4c31-a254-7a5f8477042c&pd_rd_wg=XWO5U&pf_rd_r=66M6HZ2P9QTK992J5CXE&ref_=pd_gw_unk&pd_rd_w=Potrc&pd_rd_r=87982f33-2aad-465a-85ca-70104eac5d22"){
    x = {
        "Price":49.99,
        "Image":"https://images-na.ssl-images-amazon.com/images/I/91SJsAkdZDL._UX679_.jpg",
        "Name":"Amazon Basics Hardside Luggage"
    };
} else {
    x = {
        "Price":420,
        "Image":"https://image.businessinsider.com/59974812b0e0b595758b5449?width=1100&format=jpeg&auto=webp",
        "Name":"Essential Phone"
    };
}

y = json.dumps(x)
print(y)
#print(generatedEAN)
sys.stdout.flush()