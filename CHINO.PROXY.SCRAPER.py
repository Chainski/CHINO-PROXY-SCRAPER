# https://github.com/chainski

import os
import time
import requests
import pystyle
import random
import sys
from pystyle import *


test_url = r'https://www.youtube.com/channel/UCR55c-mtcH86O-QvOQC_oFg?sub_confirmation=1'

with open('Subscribe.url','w') as f:
    f.write(f"""[InternetShortcut]
URL={test_url}
""")


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
h = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt")
h1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt")
h2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
h3 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt")
h4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt")
h5 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
h6 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt")
h7 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
h8 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
h9 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
h10 = requests.get("https://www.proxyscan.io/download?type=http")
h11 = requests.get("https://www.proxyscan.io/download?type=https")
h12 = requests.get("https://api.openproxylist.xyz/http.txt")
h13 = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt")
h14 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
h15 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
h16 = requests.get("https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt")
h17 = requests.get("https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt")


# SOCKS4 Proxies Sources
s41 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
s42 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt")
s43 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt")
s44 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
s45 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
s46 = requests.get("https://www.proxyscan.io/download?type=socks4")
s47 = requests.get("https://api.openproxylist.xyz/socks4.txt")
s48 = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt")
s49 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt")
s50 = requests.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt")
s51 = requests.get("https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt")
s52 = requests.get("https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt")
s53 = requests.get("https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt")
s54 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt")

# SOCKS5 Proxies Sources
s51 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
s52 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt")
s53 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt")
s54 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
s55 = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt")
s56 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
s57 = requests.get("https://www.proxyscan.io/download?type=socks5")
s58 = requests.get("https://api.openproxylist.xyz/socks5.txt")
s59 = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt")
s510 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt")
s511 = requests.get("https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt")
s512 = requests.get("https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt")
s513 = requests.get("https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt")
s514 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt")

# All Proxies Sources
all1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt")
all2 = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt")
all3 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt")
all4 = requests.get("http://hack-hack.chat.ru/proxy/allproxy.txt")
all5 = requests.get("http://hack-hack.chat.ru/proxy/p1.txt")
all6 = requests.get("http://hack-hack.chat.ru/proxy/p2.txt")
all7 = requests.get("http://hack-hack.chat.ru/proxy/p3.txt")
all8 = requests.get("http://hack-hack.chat.ru/proxy/p4.txt")
all9 = requests.get("http://olaf4snow.com/public/proxy.txt")
all10 = requests.get("http://alexa.lr2b.com/proxylist.txt")
all11 = requests.get("http://inav.chat.ru/ftp/proxy.txt")
all12 = requests.get("https://cyber-hub.pw/statics/proxy.txt")
all13 = requests.get("https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/all.txt")

Write.Print(f"[!] Finished Scraping Proxies!\n", Colors.white_to_red, interval=0)
time.sleep(1)
Write.Print("[+] Writing Proxies In Files . . .\n", Colors.red_to_purple, interval=0)
time.sleep(1)

# Writing Proxies In Their Respective Files
# Writing HTTP Proxies
http.write(h.content)
http.write(h1.content)
http.write(h2.content)
http.write(h3.content)
http.write(h4.content)
http.write(h5.content)
http.write(h6.content)
http.write(h7.content)
http.write(h8.content)
http.write(h9.content)
http.write(h10.content)
http.write(h11.content)
http.write(h12.content)
http.write(h13.content)
http.write(h14.content)
http.write(h15.content)
http.write(h16.content)
http.write(h17.content)

# Writing SOCKS4 Proxies
socks4.write(s41.content)
socks4.write(s42.content)
socks4.write(s43.content)
socks4.write(s44.content)
socks4.write(s45.content)
socks4.write(s46.content)
socks4.write(s47.content)
socks4.write(s48.content)
socks4.write(s49.content)
socks4.write(s50.content)
socks4.write(s51.content)
socks4.write(s52.content)
socks4.write(s53.content)
socks4.write(s54.content)

# Writing SOCKS5 Proxies
socks5.write(s51.content)
socks5.write(s52.content)
socks5.write(s53.content)
socks5.write(s54.content)
socks5.write(s55.content)
socks5.write(s56.content)
socks5.write(s57.content)
socks5.write(s58.content)
socks5.write(s59.content)
socks5.write(s510.content)
socks5.write(s511.content)
socks5.write(s512.content)
socks5.write(s513.content)
socks5.write(s514.content)

# Writing All Proxies 
allp.write(all1.content)
allp.write(all2.content)
allp.write(all3.content)
allp.write(all4.content)
allp.write(all5.content)
allp.write(all6.content)
allp.write(all7.content)
allp.write(all8.content)
allp.write(all9.content)
allp.write(all10.content)
allp.write(all11.content)
allp.write(all12.content)
allp.write(all13.content)

Write.Print("[!] Finished Writing Proxies In Files!\n", Colors.white_to_red, interval=0)
time.sleep(1)
Write.Print("[+] Closing Files . . .\n", Colors.red_to_purple, interval=0)
time.sleep(1)

# Closing Files
http.close()
socks4.close()
socks5.close()
allp.close()

# Done!
Write.Print("[!] Successfully Scraped And Saved Proxies!\n\n", Colors.white_to_red, interval=0)
time.sleep(1)
Write.Print("Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.06)
Write.Print("Press any key to continue . . .", Colors.white_to_red, interval=0)
input()