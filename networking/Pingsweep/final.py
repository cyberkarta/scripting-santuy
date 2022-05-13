#!/usr/bin/env python3

import asyncio
import subprocess
import ipaddress
import re
import requests
import time

addr = "192.168.10.0/24"
report_file = "report.csv"

async def ping(host):
    host = str(host)
    response = await asyncio.create_subprocess_shell(
                f'ping {host} -c 4',
                stderr=asyncio.subprocess.DEVNULL,
                stdout=asyncio.subprocess.DEVNULL
            )
    stdout, stderr = await response.communicate()
    # if response.returncode == 0:
    #     print(f'{host} is UP')
    # else:
    #     print(f'{host} is No Response')

def find_mac(mac):
    time.sleep(2)
    vendor = requests.get('http://api.macvendors.com/' + mac).text
    return vendor

def gen_report(report_file=report_file):
    hasil = subprocess.run(
    ["arp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
    )
    hasil = hasil.stdout.decode("utf-8")
    hasil = hasil.split("\n")

    with open(report_file, "w") as f:
        for i in hasil:
            if "Address" in i:
                continue
            i = re.split('\s+',i)
            if i == ['']:
                break
            del i[3:]
            del i[1]
            vendor = find_mac(i[1])
            i.append(vendor)
            print(i)
            for j in i :
                f.write(str(j) + ',')
            f.write('\n')



tasks = []

network = ipaddress.ip_network("192.168.100.0/24")
print ("__Ping Sweep Start__")

for host in network.hosts():
    task = ping(host)
    tasks.append(task)

tasks = asyncio.gather(*tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)

gen_report()

print("Completed")