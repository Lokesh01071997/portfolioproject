#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[83]:


URL = 'https://www.amazon.in/Park-Avenue-Livewire-Premium-Perfume/dp/B0BBH3HYC8/ref=pd_bxgy_img_sccl_2/262-3039640-1859610?pd_rd_w=9eCYa&content-id=amzn1.sym.2f895d58-7662-42b2-9a98-3a18d26bef33&pf_rd_p=2f895d58-7662-42b2-9a98-3a18d26bef33&pf_rd_r=7NGG7MTR314J6ZQ81368&pd_rd_wg=U1CiF&pd_rd_r=0b2e2b53-9338-4765-860f-e6999f666ba1&pd_rd_i=B0BBH3HYC8&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL,headers=headers)
soup1 = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id='productTitle').get_text()
price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()

print(title)
print(price)






# In[68]:


print(title)


# In[86]:


print(price)


# In[84]:


price = price.strip()[33:36]
title = title.strip()

print(title)
print(price)


# In[88]:


import datetime

today = datetime.date.today()

print(today)


# In[101]:


import csv

header = ['TITLE','PRICE','Date']
data = [title,price,today]

#with open('amazonwebscrapping.csv', 'w', newline='', encoding='UTF8') as A:
 #   writer = csv.writer(A)
  #  writer.writerow(header)
   # writer.writerow(data)



# In[106]:


import pandas as pd

df = pd.read_csv(r'C:\Users\HP\amazonwebscrapping.csv')

print(df)



# In[105]:


with open('amazonwebscrapping.csv', 'a+', newline='', encoding='UTF8') as A:
    writer = csv.writer(A)
    writer.writerow(data)


# In[113]:


def check_price():
    URL = 'https://www.amazon.in/Park-Avenue-Livewire-Premium-Perfume/dp/B0BBH3HYC8/ref=pd_bxgy_img_sccl_2/262-3039640-1859610?pd_rd_w=9eCYa&content-id=amzn1.sym.2f895d58-7662-42b2-9a98-3a18d26bef33&pf_rd_p=2f895d58-7662-42b2-9a98-3a18d26bef33&pf_rd_r=7NGG7MTR314J6ZQ81368&pd_rd_wg=U1CiF&pd_rd_r=0b2e2b53-9338-4765-860f-e6999f666ba1&pd_rd_i=B0BBH3HYC8&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL,headers=headers)
    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()

    price = price.strip()[33:36]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['TITLE','PRICE','Date']
    data = [title,price,today]
    
    with open('amazonwebscrapping.csv', 'a+', newline='', encoding='UTF8') as A:
        writer = csv.writer(A)
        writer.writerow(data)




# In[ ]:


while(True):
    check_price()
    time.sleep(43200)


# In[ ]:




