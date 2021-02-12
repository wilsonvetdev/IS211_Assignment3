import argparse
import urllib.request
import logging
import ssl
import csv, re
import sys
import pprint

#  url = http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv

def download_data(url):
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        data = response.read()
        
        with open('img_data.csv', 'w') as img_file:
            data = data.decode('utf-8').splitlines()

            writer = csv.writer(img_file, delimiter = '\n')

            for line in data:
            # writerow() needs a list of data to be written, so split at all empty spaces in the line 
                writer.writerow(re.split('\n', line))


data = download_data('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')

with open('img_data.csv', newline='') as img_file:
    data_reader = csv.reader(img_file, delimiter="'")
    for line in data_reader:
        print(line)

# def main(url):
#     print(f"Running main with URL = {url}...")


# if __name__ == "__main__":
#     """Main entry point"""
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
#     args = parser.parse_args()
#     main(args.url)