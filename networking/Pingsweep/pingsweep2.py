#!/usr/bin/env python3

import subprocess
import ipaddress

network = ipaddress.ip_network("192.168.100.0/24")

print ("__Ping Sweep Start__")

for host in network.hosts():
    host = str(host)
    response = subprocess.run(
        ['ping', host, '-c', '1'],
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL
    )
    
    # print(response.read())
    if response.returncode == 0:
        print(f'{host} is UP')
    else:
        print(f'{host} is No Response')

print("Completed")