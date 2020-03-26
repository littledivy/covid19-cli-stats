#!/usr/bin/env python3

# Author: Divy Srivastava <dj.srivastava23@gmail.com>

import requests
import re
from bs4 import BeautifulSoup
import subprocess
import time
# Python program to print 
# red text with green background 

from colorama import Fore, Back, Style 

subprocess.run(["clear"])

from yaspin import yaspin
with yaspin(text="Scraping Data", color="yellow") as spinner:
	page = requests.get('https://www.worldometers.info/coronavirus/')
	page_india = requests.get('https://www.worldometers.info/coronavirus/country/india/')

	soup = BeautifulSoup(page.content,"html.parser")
	soup_india = BeautifulSoup(page_india.content, "html.parser")
	spinner.ok("✅ ")
	#finds and prints when this was last updated
	lastupdated = soup.find("div", {"style":"font-size:13px; color:#999; text-align:center"}).get_text()
	lasttimeupdated = str(lastupdated)

	# finds and prints total amount of coronavirus deaths
	casescount = soup.find("span", {"style":"color:#aaa"}).get_text()
	coronaviruscases = "\nTOTAL CASES\n" + str(casescount)

	# finds and prints total amount of people recoverd
	recovercount = soup.find("div", {"style":"color:#8ACA2B "}).get_text()
	coronavirusrecoveries = "\nTOTAL RECOVERED" + str(recovercount)

	# finds and prints total amount of people recoverd
	casesandrecoveredinindia = soup_india.findAll("div", {"class":"maincounter-number"})

	totalindiacases = casesandrecoveredinindia[0].getText()
	totalindiadeaths = casesandrecoveredinindia[1].getText()
	totalindiarecovered = casesandrecoveredinindia[2].getText()


	print("\n"+lasttimeupdated)
	print(coronaviruscases)
	print(coronavirusrecoveries)
	print("TOTAL CASES IN INDIA")
	print(f'{Fore.YELLOW}{str(totalindiacases)}{Style.RESET_ALL}')
	print("TOTAL RECOVERED IN INDIA")
	print(f'{Fore.GREEN}{str(totalindiarecovered)}{Style.RESET_ALL}')
	print("TOTAL DEATHS IN INDIA")
	print(f'{Fore.RED}{str(totalindiadeaths)}{Style.RESET_ALL}')
	print("\nSource: World O' Meter\n")
	time.sleep(20)
	subprocess.run(["clear"])
