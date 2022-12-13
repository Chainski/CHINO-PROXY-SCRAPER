# https://github.com/chainski

import os
import time
import requests
import pystyle
import random
import sys
from pystyle import *

def sendRequest(s): 
    try: 
        return requests.get(s).content
    except Exception:
        pass

def saveFile(f,w):
    try:
        f.write(sendRequest(w))
    except Exception:
        pass 

os.system('cls')
os.system('mode con: cols=120 lines=50')

banner = '''
╔═══╗╔╗ ╔╗╔══╗╔═╗ ╔╗╔═══╗    ╔═══╗╔═══╗╔═══╗╔═╗╔═╗╔╗  ╔╗    ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
║╔═╗║║║ ║║╚╣╠╝║║╚╗║║║╔═╗║    ║╔═╗║║╔═╗║║╔═╗║╚╗╚╝╔╝║╚╗╔╝║    ║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔══╝║╔═╗║
║║ ╚╝║╚═╝║ ║║ ║╔╗╚╝║║║ ║║    ║╚═╝║║╚═╝║║║ ║║ ╚╗╔╝ ╚╗╚╝╔╝    ║╚══╗║║ ╚╝║╚═╝║║║ ║║║╚═╝║║╚══╗║╚═╝║
║║ ╔╗║╔═╗║ ║║ ║║╚╗║║║║ ║║    ║╔══╝║╔╗╔╝║║ ║║ ╔╝╚╗  ╚╗╔╝     ╚══╗║║║ ╔╗║╔╗╔╝║╚═╝║║╔══╝║╔══╝║╔╗╔╝
║╚═╝║║║ ║║╔╣╠╗║║ ║║║║╚═╝║    ║║   ║║║╚╗║╚═╝║╔╝╔╗╚╗  ║║      ║╚═╝║║╚═╝║║║║╚╗║╔═╗║║║   ║╚══╗║║║╚╗
╚═══╝╚╝ ╚╝╚══╝╚╝ ╚═╝╚═══╝    ╚╝   ╚╝╚═╝╚═══╝╚═╝╚═╝  ╚╝      ╚═══╝╚═══╝╚╝╚═╝╚╝ ╚╝╚╝   ╚═══╝╚╝╚═╝
                                           
                        ╔══════════════════════════════════════════════╗
                        ║         CHINO PROXY SCRAPER 1.0.0.2          ║
                        ║              coded by CHINOTECH              ║
                        ║        For Educational Purposes Only         ║
                        ║      PROTOCOLS: HTTP/S | SOCKS4 | SOCKS5     ║
                        ╚══════════════════════════════════════════════╝                                           
'''
print(Colorate.Horizontal(Colors.purple_to_red, Center.XCenter(banner)))

os.system(f'title CHINO Proxy Scraper - Made By: Chainski Tools')
print()
Write.Print("[+] This program will autoscrape proxies into separate files", Colors.red_to_yellow, interval=0.01)
print()
Write.Print("\n[+] Scraping Proxies Please Wait . . . \n", Colors.red_to_purple, interval=0)

http = open('http.txt','wb')
socks4 = open('socks4.txt','wb')
socks5 = open('socks5.txt','wb')
allp = open('all.txt','wb')

# HTTP Proxies Sources
http_ = ["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt","https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all","https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt","https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt","https://www.proxy-list.download/api/v1/get?type=http","https://www.proxy-list.download/api/v1/get?type=https","https://www.proxyscan.io/download?type=http","https://www.proxyscan.io/download?type=https","https://api.openproxylist.xyz/http.txt","https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt","https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all","https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt","https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt"]

for h in http_:
    saveFile(http, h)

Write.Print("[!] Successfully Scraped And Saved HTTP Proxies!\n", Colors.white_to_red, interval=0)
time.sleep(1)

# SOCKS4 Proxies Sources
socks4_ = ["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all","https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt","https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt","https://www.proxy-list.download/api/v1/get?type=socks4","https://www.proxyscan.io/download?type=socks4","https://api.openproxylist.xyz/socks4.txt","https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt","https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt","https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt","https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt"]

for s in socks4_:
    saveFile(socks4, s)

Write.Print("[!] Successfully Scraped And Saved SOCKS4 Proxies!\n", Colors.white_to_red, interval=0)
time.sleep(1)

# SOCKS5 Proxies Sources
socks5_ = ["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all","https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt","https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt","https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt","https://www.proxy-list.download/api/v1/get?type=socks5","https://www.proxyscan.io/download?type=socks5","https://api.openproxylist.xyz/socks5.txt","https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt","https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt","https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt","https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"]

for s5 in socks5_:
    saveFile(socks5, s5)

Write.Print("[!] Successfully Scraped And Saved SOCKS5 Proxies!\n", Colors.white_to_red, interval=0)
time.sleep(1)


# All Proxies Sources
all_ = ["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt","https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt", "http://hack-hack.chat.ru/proxy/allproxy.txt", "http://hack-hack.chat.ru/proxy/p1.txt", "http://hack-hack.chat.ru/proxy/p2.txt", "http://hack-hack.chat.ru/proxy/p3.txt", "http://hack-hack.chat.ru/proxy/p4.txt", "http://olaf4snow.com/public/proxy.txt", "http://alexa.lr2b.com/proxylist.txt", "http://inav.chat.ru/ftp/proxy.txt","https://cyber-hub.pw/statics/proxy.txt","https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/all.txt"]

for a in all_:
    saveFile(allp, a)

Write.Print("[!] Successfully Scraped And Saved 'ALL' Proxies!\n\n", Colors.white_to_red, interval=0)
time.sleep(1)

# Closing Files
http.close()
socks4.close()
socks5.close()
allp.close()

# Done!
time.sleep(1)
Write.Print("Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.06)
Write.Print("Press any key to continue . . .", Colors.white_to_red, interval=0)
input()