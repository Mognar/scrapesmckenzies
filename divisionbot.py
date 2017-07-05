
# coding: utf-8

# In[1]:

import requests


# In[2]:

import time


# In[3]:

from time import sleep
import os


# In[4]:


# In[5]:

import tweepy


# In[6]:

consumer_key = os.environ['CONKEY']
consumer_secret = os.environ['CONSEC']
access_token = os.environ['ACCKEY']
access_token_secret = os.environ['ACCSEC']


# In[7]:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[8]:


# In[9]:

from bs4 import BeautifulSoup


# In[10]:

import http.cookiejar


# In[11]:

URL = 'http://parliamentlive.tv/Guide'
#URL = 'http://www.senedd.tv/Meeting/Live'
#URL = 'http://hansard.parliament.uk/search/MemberContributions?memberId=1522&type=Spoken'
#jar = http.cookiejar.CookieJar()
#req = requests.get(URL, cookies=jar)
#req = requests.get(URL, cookies=jar)
#req = requests.get(URL)


# In[12]:

#soup = BeautifulSoup(req.text, "lxml")
r = requests.get(URL)
soup = BeautifulSoup(r.content, "lxml")
eventurl = soup.find("div", {"class":"description"})
urlnew = eventurl.find("a", href=True)
fullurl ='http://parliamentlive.tv' + urlnew['href']
print(fullurl)


# In[ ]:

#textout = soup.find("div", "col-md-10 nopadding")
#textout.h4.unwrap()


# In[ ]:

while True: 
    from datetime import datetime
    timenow= datetime.now()
    jar = http.cookiejar.CookieJar()
    req = requests.get(fullurl, cookies=jar)
    req = requests.get(fullurl, cookies=jar)
    soup = BeautifulSoup(req.text, "lxml")
    textout = soup.find("div", "col-md-10 nopadding")
    textime = soup.find("span","time-code")
    #textout = soup.find_all("li")
    #textout.h4.unwrap()
    textin = str(textout.text)
    textimes = str(textime.text)
    if "Division" in textin:
        #from datetime import datetime
        #timenow= str(datetime.now())
        try:
            api.update_status("Division, started:" + textimes)
        except tweepy.TweepError as e:
            pass 
        print(textin + textimes)
        sleep(60)
    else: 
        time.sleep(20)     
    #textin = str(textout)
    #print (textin)
    #from datetime import datetime
    #timenow= str(datetime.now())
    #print(textin + " " + timenow)
    #time.sleep(30)


# In[ ]:

#from datetime import datetime
#timenow= str(datetime.now())
#print(textin + timenow)
#time.sleep(30)


# In[ ]:

#api.update_status("No. of contribs:" + textin + timenow)
#print(textin + timenow)
#time.sleep(30)


# In[ ]:



