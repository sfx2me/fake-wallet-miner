import time
import random
import string
import os
from colorama import init, Fore
init(convert=True)
import subprocess, requests

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get("https://pastebin.com/raw/XXXXX")

try:
    if hardwareid in site.text:
        pass
    else:
        print("You are not Whitelisted!")
        print(f"Your HWID is {hardwareid}")
        input()
        exit(123)
except:
    print("Failed to connect to database")
    input()
    exit(123)

LicenseKey = input(Fore.RED + 'Input License Key: ')
if LicenseKey == "123":
    print(Fore.GREEN + "Key is Valid!")
    time.sleep(0.5)
else:
    print(Fore.RED + "Invalid Key!")
    print(Fore.RED + "Press Enter to quit!")
    input("")
    exit(123)

os.system("cls")
wallet = input(Fore.RED + "Wallet: ")
print(Fore.CYAN + "Checking if Wallet exists... ")
time.sleep(1)
walletCheck = requests.get("https://blockchain.info/q/addressbalance/" + wallet)
if walletCheck.status_code == 200:
    print("Wallet found!")
else:
    print("Invalid Wallet")
    exit(123)

time.sleep(0.2)
print(Fore.BLUE+ "Setting up workspace for you...")
time.sleep(3)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while(True):
    if(tries > random.randint(10000, 100000)): # chance to get fake btc
        print(Fore.CYAN +"[-]"+ Fore.RED + " bc1" + id_gen() + Fore.GREEN +" |  Valid  |  " + str(round(random.uniform(0,2), 4)), "BTC")
        print(Fore.GREEN +"Withdrawing to your Wallet...")
        time.sleep(10)
        tries = 0
        print(Fore.GREEN + "Done!")
        time.sleep(1)
    else:
        print(Fore.CYAN +"[-]"+ Fore.RED + " bc1" + id_gen() + Fore.CYAN +" | InValid |  " + "0.0000 BTC")
        tries += 1
