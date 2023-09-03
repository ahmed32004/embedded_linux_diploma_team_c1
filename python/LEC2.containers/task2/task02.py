#!/usr/bin/python3
import requests

x = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print(x.json()['bpi']['USD']['rate'])
