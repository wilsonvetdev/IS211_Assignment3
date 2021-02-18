# IS211_Assignment3

# Spring 2021 IS 211 Course Assignment Three

### Setup - Python 3.9.1

1. Git clone this repository onto local environment
2. cd into the repo ** delete img_data.csv for testing purpose. 
  * Run below command to ensure Python 3 environment, and not the Python that comes installed with your local machine.
  * $ python3 -m venv env
  * $ source env/bin/activate
3. run 'python assignmnet3.py --url 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
  * downloads the image data from the above URL
  * creates a file called img_data.csv to store data line by line
4. outputs on terminal the most frequently used browser, and also image requests out of all data.
