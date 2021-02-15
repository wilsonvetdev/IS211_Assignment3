import argparse
import urllib.request
import csv, re
import operator

# url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

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


def process_data(url):

    download_data(url)

    data_list = []

    with open('img_data.csv', newline='') as img_file:
        data_reader = csv.reader(img_file, delimiter= ",")
        for line in data_reader:
            if len(line) == 1:
                changed_line = re.split(r',\s*(?![^()]*\))', line[0])
                data_list.append({"file_path": changed_line[0], "datetime": changed_line[1], "browser": changed_line[2], "status": changed_line[3], "request_size": changed_line[4]})
            else:
                data_list.append({"file_path": line[0], "datetime": line[1], "browser": line[2], "status": line[3], "request_size": line[4]})
    
    return data_list


def calculate_img_hits(processed_data):

    counter = 0

    result = []

    for item in processed_data:
        result.append(re.findall('(jpg|jpeg|png|PNG|gif|GIF)', item["file_path"]))
    
    for item in result:
        if len(item) != 0:
            counter += 1
    
    return f"Image requests account for {counter / len(result) * 100}% of all requests."


def calculate_most_popular_browser(processed_data):

    mozilla = []
    chrome = []
    ie = []
    safari = []

    counter_dict = {
        "firefox": 0,
        "chrome": 0,
        "ie": 0,
        "safari": 0
    }

    for item in processed_data:
        mozilla.append(re.findall("Firefox", item["browser"]))
        chrome.append(re.findall("Chrome", item["browser"]))
        ie.append(re.findall("Internet Explorer", item["browser"]))
        safari.append(re.findall("Safari", item["browser"]))

    for i in range(len(processed_data)):
        if len(mozilla[i]) != 0:
            counter_dict["firefox"] += 1
        elif len(chrome[i]) != 0:
            counter_dict["chrome"] += 1 
        elif len(ie[i]) != 0:
            counter_dict["ie"] += 1 
        elif len(safari[i]) != 0:
            counter_dict["safari"] += 1

    return max(counter_dict.items(), key=operator.itemgetter(1))[0]


def main(url):
    print(f"Running main with URL = {url}...")
    processed_data = process_data(url)
    print(calculate_img_hits(processed_data))
    print(calculate_most_popular_browser(processed_data))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)