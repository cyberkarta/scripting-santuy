#!/usr/bin/env python3

import asyncio
from asyncio import subprocess
import ipaddress

addr = "192.168.100.0/24"

async def ping(host):
    host = str(host)
    response = await asyncio.create_subprocess_shell(
                f'ping {host} -c 1',
                stderr=asyncio.subprocess.DEVNULL,
                stdout=asyncio.subprocess.DEVNULL
            )
    stdout, stderr = await response.communicate()
    if response.returncode == 0:
        print(f'{host} is UP')
    # else:
    #     print(f'{host} is No Response')

tasks = []

network = ipaddress.ip_network("192.168.100.0/24")
print ("__Ping Sweep Start__")

for host in network.hosts():
    task = ping(host)
    tasks.append(task)

tasks = asyncio.gather(*tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)

print("Completed")