import time
import re
import sys
import requests
from datetime import datetime
from datetime import timedelta
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pandas as pd
import os
import nltk
from collections import Counter

date_start = sys.argv[1]
date_stop = sys.argv[2]
date_start = datetime.strptime(date_start,"%d-%m-%Y") #Date de début du scraping, à passer en arguments quand on lance le script
date_stop = datetime.strptime(date_stop,"%d-%m-%Y") #date de fin

def extract_links(page):
	soup = BeautifulSoup(page.content)
	links = soup.find_all("a",{"class":"teaser__link"})
	return [link["href"] for link in links]



dates = np.arange(date_start,date_stop,timedelta(days=1))
matrix = pd.DataFrame(columns = ["n","gram","annee","mois","jour"])
Matrix = []
for i in range(5):
	Matrix.append(matrix.copy())
tokenizer = nltk.RegexpTokenizer(r"[a-zà-ÿ']+") 



### On génère la liste de tous les articles
for date in dates:
	date = date.astype("object")
	page = requests.get(f"https://www.lemonde.fr/archives-du-monde/{date.day}-{date.month}-{date.year}/")
	nb_page = str(page.content).count("river__pagination river__pagination--page")
	links = []
	links += extract_links(page)
	if nb_page > 1:
		for i in range(nb_page-1):
			page = requests.get(f"https://www.lemonde.fr/archives-du-monde/{date.day}-{date.month}-{date.year}/{i+1}/")
			links += extract_links(page)

options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
driver = webdriver.Firefox(profile,options=options)
driver.get("https://www.lemonde.fr")	
webElem = driver.find_element("css selector","#js-body > div.gdpr-lmd-wall > div > footer > button")
webElem.click()
webElem = driver.find_element("css selector","#Header > header > div.right > div > a.Header__connexion.js-header-login.js-header-login-staled > span.login-info")
webElem.click()
time.sleep(2)
webElem = driver.find_element("css selector","#email")
mot1= ###Put login here
webElem.send_keys(mot1)
webElem = driver.find_element("css selector","#password")
mot1= ##Put password here
webElem.send_keys(mot1)
webElem = driver.find_element("css selector","div.checkbox:nth-child(4) > label:nth-child(2)")
webElem.click()
webElem = driver.find_element("css selector","input.button")
webElem.click()


### On scrape et on 
for url in links:
	print(url)
	text = ""
	if "http" not in url:
		continue
	driver.get(url)
	page = driver.page_source
	###Sauvergarder le texte à ce stade si tu veux tout le html
	### Si tu veux scraper le texte (titre, corps de l'article, légende des photos...)
	### ...tu continues le code et tu sauvegardes à la fin
	pageSoup = BeautifulSoup(page, 'html.parser')
	title = pageSoup.find("title")
	if title is not None:
		text += title.text.replace("’","'") + "\n"
	sous_titre = pageSoup.find("p",{"class":"article__desc"})
	if sous_titre is not None:
		text += re.split("[<>]",str(sous_titre))[-3].replace("’","'") + "\n"
	legendes_photo = pageSoup.find_all("figure",{"class":"article__media"})
	if legendes_photo is not None:
		text += "\n".join([i.img["alt"].replace("’","'") for i in legendes_photo])
	if "live" in url:
		a = pageSoup.find_all("p",{"class":"post__live-container--answer-text post__space-node"})
	else:
		a = pageSoup.find_all("p", {"class": "article__paragraph"})
	text += '\n'.join([z.text for z in a]) + "\n"
	##Save the text somewhere