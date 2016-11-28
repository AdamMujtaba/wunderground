# !/usr/bin/python
# just a simple and quick script shows the temps for a whole year. and puts the data in a CSV file.
import requests
import csv
from datetime import timedelta, date

# define necessary variables
api_key = ''
date_range = []
temp = csv.writer(open('wundergroundv2.csv', 'w'))


# date formatting
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2015, 01, 01)
end_date = date(2015, 12, 31)
for single_date in daterange(start_date, end_date):
    date_range.append('history_' + single_date.strftime("%Y%m%d"))

# URL construction
url = ['http://' + 'api.wunderground.com/api/' + api_key + '/' + dateinput +
       '/q/iq/basrah.json' for dateinput in date_range]
for i in url:
    wunderground = requests.get(i).json()
    for item in wunderground['history']['dailysummary']:
        print item['date']['pretty'] + '--' + item['meantempm']
        temp.writerow([item['date']['pretty'], item['mintempm'], item['maxtempm'], item['meantempm']])

