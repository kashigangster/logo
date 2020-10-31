#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦
\033[1;96m          _____                     _ _ 
\033[1;96m         / ____|                   | (_) ⚡
\033[1;96m        | (___  _ __   ___  ___  __| |_  
\033[1;96m         \___ \| '_ \ / _ \/ _ \/ _` | | 
\033[1;96m         ____) | |_) |  __/  __/ (_| | |
\033[1;96m        |_____/| .__/ \___|\___|\__,_|_|
\033[1;96m               | |                      
\033[1;96m               |_|   Kashi  Updated 0.3                   
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
                                                                          Updated✔   
  _  __              _____   _    _   _____ 
 | |/ /     /\      / ____| | |  | | |_   _|
 | ' /     /  \    | (___   | |__| |   | |  
 |  <     / /\ \    \___ \  |  __  |   | |  
 | . \   / ____ \   ____) | | |  | |  _| |_ 
 |_|\_\ /_/    \_\ |_____/  |_|  |_| |_____|
                                            
                                            
                                            
"""

jalan("\033[1;97m•◈•───────•◈ NOT A NAME ITS BRAND •◈•───────•◈•")  


jalan("\033[1;96m•◈•   _____ _____  ______ ______ _____ _____ ")
jalan("\033[1;96m•◈•  / ____|  __ \|  ____|  ____|  __ \_   _|")
jalan("\033[1;97m•◈• | (___ | |__) | |__  | |__  | |  | || |  ")
jalan("\033[1;96m•◈•  \___ \|  ___/|  __| |  __| | |  | || |  ")
jalan("\033[1;96m•◈•  ____) | |    | |____| |____| |__| || |_ ")
jalan("\033[1;96m•◈• |_____/|_|    |______|______|_____/_____|")
 
jalan("   \033[1;91m INDAIN USERZ USE ANY PROXY ")	
jalan("   \033[1;91m WIFI USERZ USE ANY PROXY ")
jalan("   \033[1;93m Welcome to Kashi Teaches ")
jalan("   \033[1;91m Whtsapp Num +923062045786 ")	

jalan("\033[1;97m•◈•──────────•◈•\033[1;96mKashi Love Sidra\033[1;96m•◈•──────────•◈•")

CorrectUsername = "Speedi"
CorrectPassword = "Kashi"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;97mUSER NAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mPASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')

def menu():
    print(f"{G}1{r} Crack From Friendlist")
    print(f"{G}2{r} Crack From Likes On Post,PUBG")
    print(f"{G}3{r} Crack By Search Name")
    print(f"{G}4{r} Crack From Group (Only Takes 100 User)")
    print(f"{G}5{r} Crack From Friend Friendlist")
    print(f"{G}6{r} Crack From Hashtag")
    print(f"{G}7{r} Crack Re-check Result")
