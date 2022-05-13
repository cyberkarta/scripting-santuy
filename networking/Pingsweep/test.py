import subprocess
import re
import requests
import time

csv_file = "test.csv"

def find_mac(mac):
    time.sleep(2)
    vendor = requests.get('http://api.macvendors.com/' + mac).text
    return vendor


#### 


hasil = subprocess.run(
    ["arp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
    )

hasil = hasil.stdout.decode("utf-8")
hasil = hasil.split("\n")

with open("csv_file", "w") as f:
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


        


# for line in hasil:
#     line = line.split(" ")

    

# with open("hasil.csv", "w") as f:

