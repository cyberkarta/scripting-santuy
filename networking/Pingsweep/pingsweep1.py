#!/usr/bin/env python3

import os

# windows= ping -n 1 
response = os.popen('ping -c 5 192.168.100.1')
# print(response.read())
for i in response.readlines():
    print(i)