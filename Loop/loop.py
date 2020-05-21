from datetime import datetime
import pprint
import os
import requests

import csv
os.chdir('/Users/zerodeg/project/pycharm/HeadFirstPython/Loop')

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {convert2ampm(k): str(v).title() for k, v in flights.items()}

pprint.pprint(flights2)
print()

dests = set(flights2.values())

# print(dests)
#
# west_end = [k for k, v in flights2.items() if v == 'West End']
# treasure_cay = [k for k, v in flights2.items() if v == 'Treasure Cay']
# rock_sound = [k for k, v in flights2.items() if v == 'Rock Sound']
# freeport = [k for k, v in flights2.items() if v == 'Freeport']

when = {dest: [k for k, v in flights2.items() if v == dest] for dest in dests}
pprint.pprint(when)
print()


urls = ('http://naver.com', 'http://oreilly.com', 'http://twitter.com')
print(urls)

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '-> ', resp.status_code, '-> ', resp.url)


# for resp_len, status, url in gen_from_urls(urls):
#     print(resp_len, '-> ', status, '-> ', url)
