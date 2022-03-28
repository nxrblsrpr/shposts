#!/bin/python3
"""
Created on Wed Mar  2 13:03:58 2022

@author: ophidian
"""

import sys
import socket
from datetime import datetime as dt

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments; syntax: python3 scanner.py <IP>")

print("Scanning target "+target+"\nTime started: "+str(dt.now()))

try:
    for port in range(65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target, port))
        if result == 0:
            print(":{} is open" .format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()