#!/usr/bin/python3
"""Requests data and API"""

import requests
from sys import argv

url_base = 'https://jsonplaceholder.typicode.com/users/'


def get_data():
    """This function gets data of API"""
    name = requests.get(url_base + argv[1]).json()
    todos = requests.get(url_base + argv[1] + '/todos/').json()
    count = 0
    title = ""

    for item in todos:
        if item['completed'] is True:
            title += "\t {}\n".format(item['title'])
            count += 1

    print("Employee {} is done with tasks({}/20):\n{}".format(name['name'],
                                                              count, title),
          end='')


if __name__ == '__main__':
    get_data()
