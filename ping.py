import os
os.system("cls")
os.system(f"title ")
import time
import datetime
import socket
import threading
from pystyle import *
import signal
import platform
import subprocess

RED = '\033[1;91m'
WHITE = '\033[0m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
GOLD = '\033[0;33m'
PURPLE = '\033[0;35m'

def signal_handler(sig, frame):
    print()
    print()
    print(f" {PURPLE}[{RED}!{PURPLE}]{RED} Stopped by user{WHITE}")
    time.sleep(1.4)
    exit()

signal.signal(signal.SIGINT, signal_handler)

def custom_ping(host, count=4, interval=1):
    system = platform.system().lower()
    command = None

    if system == "windows":
        command = ["ping", "-n", str(count), "-w", str(interval * 1000), host]
    else:
        command = ["ping", "-c", str(count), "-i", str(interval), host]

    try:
        while True:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout
            current_time = datetime.datetime.now().strftime("%H:%M")
            if result.returncode == 0:
                status = "success"
                time_val = extract_time(output)
            else:
                status = "fail"
                time_val = "N/A"
            print(f" {PURPLE}[ {GOLD}{current_time}{PURPLE} ]{BLUE} {host} {WHITE}is{GREEN} {WHITE}PING > {BLUE}{time_val}ms")
    except Exception as e:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"[{current_time}] Host {host} is error, response time: N/A")

def extract_time(output):
    lines = output.splitlines()
    if platform.system().lower() == "windows":
        for line in lines:
            if "Average =" in line:
                return line.split()[-1].replace("ms", "")
    else:
        for line in lines:
            if "min/avg/max" in line:
                return line.split("/")[1]
    return "N/A"

def wifiCheck():
    try: 
        ip = socket.gethostbyname("www.google.com")
        print()
        print(f"                                                {PURPLE}[{GREEN}!{PURPLE}]{WHITE} Internet : {GREEN}Active{WHITE}")    
    except Exception as e:
        print(f"                                                {PURPLE}[{RED}!{PURPLE}]{WHITE} Internet : {RED}{e}{WHITE}")   
        time.sleep(3.7)
        exit()

art = """
    ____  _____   __________________   
   / __ \/  _/ | / / ____/ ____/ __ \   
  / /_/ // //  |/ / / __/ __/ / /_/ /   
 / _____/ // /|  / /_/ / /___/ _, _/   
/_/   /___/_/ |_/\____/_____/_/ |_|    
"""

print()
print()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(art)))
wifiCheck()
print()
print()

host = input(f" {BLUE}https:// {WHITE}> ")
os.system(f"title PING - [  {host}  ]")
ping_thread = threading.Thread(target=custom_ping, args=(host,))
ping_thread.start()