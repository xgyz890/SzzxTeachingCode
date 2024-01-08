#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:40:07 2020

@author: Yang
"""
#%% 2
import requests
import re

def get_challenge(s):
    return requests.get("http://www.pythonchallenge.com/pc/"+s).text

src=get_challenge("def/ocr.html")
text=re.compile("<!--((?:[^-]+|-[^-]|--[^>])*)-->", re.S).findall(src)[-1]
# text=re.findall(".*?<!--.*-->.*<!--(.*)-->",src,re.S)
counts={}
for c in text:
    counts[c]=counts.get(c,0)+1
for items in counts:
    print(items,counts[items])
    
#%% 3
import requests
import re

def get_challenge(s):
    return requests.get("http://www.pythonchallenge.com/pc/"+s).text

src=get_challenge("def/equality.html")
text=re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",src)
print("".join(text))

#%% 4
import requests
import re

page=requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345").text
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
count=0
while True:
    try:
        next_id=re.search("\d+",page).group()
        count+=1
        next_id=int(next_id)
    except:
        print("The last url is: ",next_url)
        break
    next_url=url+str(next_id)
    print("url {:2d}: {}".format(count,next_url))
    page=requests.get(next_url).text
    
#%% 5





