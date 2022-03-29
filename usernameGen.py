# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:18:26 2022

@author: ophidian
"""
#!/bin/python3
import sys

if len(sys.argv) != 2:
    f=open(sys.argv[1], "rt") #Open up the file listed in the first argument, works w/ a path too ofc
    n=open("combList", "x") #Creates a new file for the appended usernames

else:#Syntax checker, will tell you if you're possibly missing something
    print("might wanna check that syntax homie, you missed something.\nTry this: $sudo python3 usernameGen.py <wordlist/wordlist path> @email.com\n\n\n")

try:
    for x in f:
        x=x.rstrip("\n") #Strips the newline character at the end of a line
        n.write(x + sys.argv[2] + "\n") #Appends the email handle to a username

except KeyboardInterrupt:
    print("\n\nExiting program.")
    sys.exit()

f.close()
n.close()