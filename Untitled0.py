
# coding: utf-8

# In[1]:

import requests


# In[2]:

from time import sleep


# In[3]:

get_ipython().system(u'pip install tweepy')


# In[15]:

import tweepy


# In[16]:

consumer_key = 'X1VdJN3XZE0qaoBjrAWTf0zBC'
consumer_secret = 'NMTltKlA2Rd0926YRNLII5bAHVExm9s1ZGLAqsfrLEphcHvCQM'
access_token = '854276747096973313-sKvvt5r0vPbFdpDmH6c81bxxvlULNcM'
access_token_secret = 'fvWM3NCtIiq0ox3qyFRqEyKdYtE1LlYFCYRY45wF16cQ6'


# In[17]:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[18]:

get_ipython().system(u'pip install beautifulsoup4')


# In[19]:

from bs4 import BeautifulSoup


# In[20]:

import http.cookiejar


# In[21]:

URL = 'http://hansard.parliament.uk/search/MemberContributions?memberId=1522&type=Spoken'
jar = http.cookiejar.CookieJar()
req = requests.get(URL, cookies=jar)
req = requests.get(URL, cookies=jar)


# In[22]:

soup = BeautifulSoup(req.text, "lxml")


# In[26]:

textout = soup.find("p", "pagination-total")


# In[27]:

textin = str(textout)
print (textin)


# In[28]:

api.update_status("No. of contribs:" + textin + '.')


# In[ ]:

sleep(900)

