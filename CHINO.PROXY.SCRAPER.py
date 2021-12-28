import os
from time import sleep
import requests
import random
import string
from colorama import Fore
import webbrowser

webbrowser.open('https://www.youtube.com/channel/UCR55c-mtcH86O-QvOQC_oFg')

os.system('cls')

logo = '''

 ▄████▄   ██░ ██   ██ ███▄    █  ▒█████        ██████  ▄████▄  ██▀███   ▄▄▄      ██▓███  ▓█████ ██▀███  
▒██▀ ▀█ ▒▓██░ ██ ▒▓██ ██ ▀█   █ ▒██▒  ██▒    ▒██    ▒ ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██ ▓█   ▀▓██ ▒ ██▒
▒▓█    ▄░▒██▀▀██ ░▒██▓██  ▀█ ██▒▒██░  ██▒    ░ ▓██▄   ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒▒███  ▓██ ░▄█ ▒
▒▓▓▄ ▄██ ░▓█ ░██  ░██▓██▒  ▐▌██▒▒██   ██░      ▒   ██▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒▒▓█  ▄▒██▀▀█▄  
▒ ▓███▀  ░▓█▒░██▓ ░██▒██░   ▓██░░ ████▓▒░    ▒██████▒▒▒ ▓███▀ ░██▓ ▒██▒ ▓█   ▓██▒██▒ ░  ░░▒████░██▓ ▒██▒
░ ░▒ ▒    ▒ ░░▒░▒ ░▓ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░     ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█▒▓▒░ ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
  ░  ▒    ▒ ░▒░ ░  ▒ ░ ░░   ░ ▒░  ░ ▒ ▒░     ░ ░▒  ░    ░  ▒    ░▒ ░ ▒░  ░   ▒▒ ░▒ ░      ░ ░    ░▒ ░ ▒░
░         ░  ░░ ░  ▒    ░   ░ ░ ░ ░ ░ ▒      ░  ░  ░  ░          ░   ░   ░   ▒  ░░          ░     ░   ░ 
░ ░       ░  ░  ░  ░          ░     ░ ░            ░  ░ ░        ░           ░              ░     ░     
'''

info = '''
╔═════════════════════════════════════════════╗
║CHINO PROXY SCRAPER V1.0                     ║
║coded by CHINOTECH                           ║
║For Educational Purposes Only                ║
║Telegram Channel : https://t.me/chinotech    ║
╚═════════════════════════════════════════════╝
'''

print(Fore.LIGHTBLUE_EX+logo)
print(Fore.RED+info)

print()
ready = input(f'{Fore.YELLOW} This program will autoscrape (HTTP,SOCKS4,SOCK5) proxies into separate files (Hit "ENTER" To Continue) ')

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