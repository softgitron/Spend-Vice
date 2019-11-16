How to Run?

pip install -r `requirements.txt`

scrapy crawl amazon -a url=<product_url>

Example: scrapy crawl amazon -a url=https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B0756CYWWD/https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B0756CYWWD/

Result: {'Name': 'Bose QuietComfort 35 II Wireless Bluetooth Headphones, Noise-Cancelling, with Alexa voice control, enabled with Bose AR – Black', 'Price': '$299.88', 'Image': 'https://images-na.ssl-images-amazon.com/images/I/51sAtKgDkDL._SY300_QL70_.jpg'}
