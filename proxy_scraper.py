import os
from time import sleep
import requests
import random
import string
from colorama import Fore
import webbrowser


os.system('cls')

logo = '''

   ██████  ▄████▄  ██▀███   ▄▄▄      ██▓███  ▓█████ ██▀███  
 ▒██    ▒ ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██ ▓█   ▀▓██ ▒ ██▒
 ░ ▓██▄   ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒▒███  ▓██ ░▄█ ▒
   ▒   ██▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒▒▓█  ▄▒██▀▀█▄  
 ▒██████▒▒▒ ▓███▀ ░██▓ ▒██▒ ▓█   ▓██▒██▒ ░  ░░▒████░██▓ ▒██▒
 ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█▒▓▒░ ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
 ░ ░▒  ░    ░  ▒    ░▒ ░ ▒░  ░   ▒▒ ░▒ ░      ░ ░    ░▒ ░ ▒░
 ░  ░  ░  ░          ░   ░   ░   ▒  ░░          ░     ░   ░ 
       ░  ░ ░        ░           ░              ░     ░     
'''

info = '''
+----------------------------------------------------------------------------+
| EPHBOMB PROXY SCRAPER                                                         |                      
+----------------------------------------------------------------------------+
'''

print(Fore.RED+logo)
print(Fore.RED+info)

print()
ready = input(f'{Fore.RED} This program will autoscrape (HTTP,SOCKS4,SOCK5) proxies into separate files {Fore.YELLOW} (Hit "ENTER" To Continue) ')

url = 'https://api.openproxylist.xyz/http.txt'
r = requests.get(url)
results = r.text
with open ("http.txt", "w") as file:
 file.write(results)
 
url = 'https://api.openproxylist.xyz/socks4.txt'
r = requests.get(url)
results = r.text
with open ("socks4.txt", "w") as file:
 file.write(results)
 
url = 'https://api.openproxylist.xyz/socks5.txt'
r = requests.get(url)
results = r.text
with open ("socks5.txt", "w") as file:
 file.write(results)