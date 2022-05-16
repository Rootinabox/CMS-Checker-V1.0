import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)


red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
Cyan = '\033[36m'
white = '\033[37m'
black = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
  _____             _   _             _               
 |  __ \           | | (_)           | |              
 | |__) |___   ___ | |_ _ _ __   __ _| |__   _____  __
 |  _  // _ \ / _ \| __| | '_ \ / _` | '_ \ / _ \ \/ /
 | | \ \ (_) | (_) | |_| | | | | (_| | |_) | (_) >  < 
 |_|  \_\___/ \___/ \__|_|_| |_|\__,_|_.__/ \___/_/\_\
                                                      
                                                             
 CMS Checker V1.0    |   Priv8 method    | |  Coded by Rootinabox                             
                      
 [+] Telegram : @rootinabox
 [+] Channel  : https://t.me/Rootinabox_Channel

   \033[32m>----------------------------------<
   [-] 1. CMS Wordpress
   [-] 2. CMS Joomla
   [-] 3. CMS Laravel
   [-] 4. CMS  OpenCart
   [-] 5. CMS Drupal
   [-] 6. CMS Prestashop
   [-] 7. CMS Magneto 
   [-] 8. CMS vBulletin
   [-] 9. CMS osCommerce
   [-] 10. Scan All 
   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

rootinabox = raw_input(':~# \033[34mChoose\033[32m Number : ')

users = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

def cms_wordpress(url):
	try:
		cek = requests.get(url+'/xmlrpc.php?rsd', headers=users, timeout=15)
		if 'Wordpress' in cek.text.encode('utf-8'):
			print(yellow + '[Found Cms Wordpress --> ]' + green + url)
			open('cms/wp.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found Cms Wordpress --> ]' + red + url)
	except:
		pass
	pass

def cms_joomla(url):
	try:
		ceks = requests.get(url+'/administrator/index.php', headers=users, timeout=15).text
		if 'Joomla!' in ceks and '/language/en-GB/en-GB.xml' in ceks:
			print(yellow + '[Found Cms Joomla --> ]' + green + url)
			open('cms/joomla.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found Cms Joomla --> ]' + red + url)
	except:
		pass
	pass

def cms_laravel(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'X-XSRF-TOKEN' in get_source and 'XSRF-TOKEN' in get_source:
			print(yellow + '[Found Laravel Cookies --> ]' + green + url)
			open('cms/laravel.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found Laravel Cookies --> ]' + abanb + url)
	except:
		pass
	pass

def cms_opencart(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'index.php?route=common/home' in ceks.text.encode('utf-8'):
			print(yellow + '[Found CMS Opencart --> ]' + green + url)
			open('cms/opencart.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Opencart--> ]' + abanb + url)
	except:
		pass
	pass

def cms_drupal(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'sites/default' in ceks.text.encode('utf-8'):
			print(yellow + '[Found CMS Drupal --> ]' + green + url)
			open('cms/drupal.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Drupal--> ]' + abanb + url)
	except:
		pass
	pass

def cms_prestashop(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'sites/default' in ceks.text.encode('utf-8'):
			print(yellow + '[Found CMS Prestashop --> ]' + green + url)
			open('cms/prestashop.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Prestashop--> ]' + abanb + url)
	except:
		pass
	pass

def cms_magneto(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'Mage.Cookies' in ceks.text.encode('utf-8'):
			print(yellow + '[Found CMS Magneto --> ]' + green + url)
			open('cms/magneto.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Magneto--> ]' + abanb + url)
	except:
		pass
	pass

def cms_vBulletin(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'vBulletin' in ceks.text.encode('utf-8'):
			print(yellow + '[Found CMS vBulletin --> ]' + green + url)
			open('cms/vBulletin.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS vBulletin--> ]' + abanb + url)
	except:
		pass
	pass

def cms_osCommerce(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'osCommerce' in ceks.text.encode('utf-8'):
			print(yellow + '[Found CMS osCommerce --> ]' + green + url)
			open('cms/osCommerce.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS osCommerce--> ]' + abanb + url)
	except:
		pass
	pass

def allgas(url):
	try:
		cms_wordpress(url)
		cms_joomla(url)
		cms_laravel(url)
		cms_opencart(url)
		cms_drupal(url)
		cms_prestashop(url)
		cms_magneto(url)
		cms_vBulletin(url)
		cms_sCommerce(url)
	except:
		pass

def Main():
	try:
		if rootinabox =='1':
			list1 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev1 = open(list1, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_wordpress, rev1)
		if rootinabox =='2':
			list2 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev2 = open(list2, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_joomla, rev2)
		if rootinabox =='3':
			list3 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev3 = open(list3, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_laravel, rev3)
		if rootinabox =='4':
			list4 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev4 = open(list4, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_opencart, rev4)
		if rootinabox =='5':
			list5 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev5 = open(list5, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_drupal, rev5)
		if rootinabox =='6':
			list6 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev6 = open(list6, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_prestashop, rev6)
		if rootinabox =='7':
			list7 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev7 = open(list7, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_magneto, rev7)
		if rootinabox =='8':
			list8 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev8 = open(list8, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_vBulletin, rev8)
		if rootinabox =='9':
			list9 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev9 = open(list9, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_vBulletin, rev9)
		if rootinabox =='10':
			list10 = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev10 = open(list10, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(allgas, rev10)
	except:
		pass

if __name__ == '__main__':
	Main()