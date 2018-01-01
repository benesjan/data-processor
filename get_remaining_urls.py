import json
import sys

if len(sys.argv) != 4:
    print("Not enough input arguments")
    sys.exit(1)

crawled_urls = set()
with open(sys.argv[1], 'r') as data_file:
    for line in data_file:
        product = json.loads(line)
        crawled_urls.add(product['product_url'])

with open(sys.argv[2], 'r') as input_file, open(sys.argv[3], 'w') as output_file:
    for line in input_file:
        if line.strip() not in crawled_urls:
            output_file.write(line)
