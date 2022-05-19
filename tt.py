import time
import random
import string

LicenseKey = input("Input License Key: ")
print("Checking if Key is Valid...")
time.sleep(1)
print("Key is Valid")
Wallet = input("Wallet: ")
print("Checking if Wallet exists... ")
time.sleep(1)
print("Wallet Found!")
time.sleep(0.2)
print("Setup up workspace for you...")
time.sleep(3)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while(True):
    if(tries > random.randint(10000, 100000)): # chance to get fake btc
        print("[-] bc1" + id_gen() + " | Valid |  " + "0.0335 BTC")
        print("Withdrawing to your Wallet...")
        time.sleep(10)
        tries = 0
        print("Done!")
        time.sleep(1)
    else:
        print("[-] bc1" + id_gen() + " | Invalid | " + "0.0000 BTC")
        tries += 1
