import time
import random
import string
import os
from colorama import init, Fore
import subprocess
import requests

init(convert=True)

PASTE_BIN_URL = "https://pastebin.com/jURv2gNG"

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get(PASTE_BIN_URL)

try:
    if hardwareid in site.text:
        pass
    else:
        print("You are not Whitelisted!")
        print(f"Your HWID is {hardwareid}")
        print("Setup a pastebin with your HWID and replace the example link in line 9 with yours!")
        time.sleep(30)
        input()
        exit(0)
except:
    print("Failed to connect to database")
    input()
    exit(0)

license_key = input(Fore.RED + 'Input License Key: ')
if license_key == "123":
    print(Fore.GREEN + "Key is Valid!")
    time.sleep(0.5)
else:
    print(Fore.RED + "Invalid Key!")
    print(Fore.RED + "Press Enter to quit!")
    input("")
    exit(0)

os.system("cls")
wallet = input(Fore.RED + "Wallet: ")
print(Fore.CYAN + "Checking if Wallet exists... ")
time.sleep(1)
print("Wallet found")

time.sleep(0.2)
