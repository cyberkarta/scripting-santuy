import requests

mac = "cc:2d:e0:74:0b:90"

vendor = requests.get('http://api.macvendors.com/' + mac).text
print(mac, vendor)