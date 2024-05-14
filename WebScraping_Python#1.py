# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:33:26 2022

@author: santi
"""

import requests as r
from bs4 import BeautifulSoup
import csv
import random as rand
import time

url = 'http://drd.ba.ttu.edu/isqs3358/hw/hw1/'
fp = 'C:\\Users\\santi\\Downloads\\'
filename = 'Homework1ISQS3358.csv'
low = 1
high = 5
interval = rand.randint(low,high)+rand.random()

resparent = r.get(url)
parentsoup = BeautifulSoup(resparent.text,'lxml')
scoreboardgeneral = parentsoup.find('div',attrs={'id':'UsrIndex'})


scoreboardstatss = scoreboardgeneral.find_all('tr')
#Demostrates all the tr's
#print(scoreboardstatss)

#When I use this it works, but it still does not work the scoreboardstat.find('a')
#scorebaorddiff= scoreboardstatss[1:]


with open(fp + filename,'w') as dataout:
    datawriter = csv.writer(dataout, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    #write header row
    datawriter.writerow(['Rank', 'user_id', 'fname', 'lname', 'avg_water', 'avg_sleep', 'avg_step', 'day', 'day_water_amt', 'day_sleep_amt', 'day_step_amt', 'metric'])  
   
    for z in scoreboardstatss:
        #Demonstrates that there are no td's
        #print(z)
        scoreboardstats =z.find_all('td')
        #print(len(scoreboardstats))
        if len(scoreboardstats) ==7:
            indurl =scoreboardstats[0].find('a')
            print(indurl)
            href = indurl['href']
            get = r.get(url +href)
            print(url+href)
            soup = BeautifulSoup(get.text,'lxml')
            indiv = soup.find('div',attrs={'id':'UsrDetail'})
            namegeneral = soup.find('div', attrs={'id':'UsrPrimary'})
            indivname = soup.find_all('span', attrs={'class':'val'})
            fname = indivname[0].text
            lname = indivname[1].text
            rank = indivname[2].text
            print(fname)
            print(lname)
            print(rank)
            print(href)
            link = href.split('=')[1]
            print(link)
            indivchar = soup.find_all('tr')
            print(indivchar)
            len(indivchar)
            for i in indivchar:
                attr = i.find_all('td')
                len(attr)
                print(attr)
                if len(attr) ==4:
                    datawriter.writerow([rank,link,fname,lname,scoreboardstats[4].text,scoreboardstats[3].text,scoreboardstats[5].text,
                    attr[0].text, attr[2].text, attr[1].text, attr[3].text,scoreboardstats[6].text]) #metrics
                   
        time.sleep(interval)