#!/bin/python3
"""
Created on Wed Mar  2 13:44:05 2022

@author: ophidian
"""
import ipaddress
import os
import sys
from datetime import datetime as dt

netw=sys.argv[1]
net = str(netw)
print(net[:len(net)-1]+str(2))
cidrMask=sys.argv[2]

network=ipaddress.ip_network("{}/".format(netw)+str(cidrMask)+"")

print("Scanning for hosts on {}...\nTime started: ".format(netw)+str(dt.now())+"")

for i in network.hosts():
    response = os.system("ping "+str(i)+" -c 1")
    
    if response == 0:
        print(str(i)+" is Up")
    else:
        print("No response from "+str(i))