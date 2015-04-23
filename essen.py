# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import urllib.request
from bs4 import BeautifulSoup
from collections import OrderedDict

page = urllib.request.urlopen('http://oracle-web.zfn.uni-bremen.de/essen/mensa').read()

soup = BeautifulSoup(page)
soup.prettify()
menuItems = soup.findAll('font',{'color':'RED'}) # Identify today's Menu

for br in soup.findAll('br'): # Replace the break tags with a dash
	br.replaceWith(" - ")

# Create a header list
menuKeys=['Heute','Essen 1', 'Essen 2', 'Vegetarisch', 'Wok und Pfanne',
'Aufläufe und Gratin', 'Pizza, Suppen und Co.', 'Beilagen']

menuValues=[] #An empty list for the menu items
for eachItem in menuItems:
	stringItem = ' '.join(eachItem.findAll(text=True)) # Ext.text
	data = stringItem.strip('&nbsp;') # Remove nbsp tags
	data = data.replace('\n',' ') # Replace newline with comma
	data = re.sub(' +', ' ', data) # Replace dbl space with single

	menuValues.append(data) # Add to list

menu = OrderedDict(zip(menuKeys,menuValues)) # Merge list to dict

print ("\n------------")

for key,val in menu.items():
	print (key,"\n",val,"\n------------\n")
