
# coding: utf-8

# In[7]:


import requests
from  bs4 import BeautifulSoup


# In[8]:


r = requests.get('https://www.wikipedia.org/')


# In[3]:


r = requests.get('https://www.wikipedia.org/')


# In[4]:


r


# In[5]:


html = r.text


# In[9]:


html


# In[10]:


soup = BeautifulSoup(html,"html5lib")


# In[11]:


soup


# In[19]:


#get the text out of the soup and print it

text = soup.get_text()
data1 = soup.select('p')


# In[13]:


text


# In[20]:


# create tokenizer
import re
data1


# In[36]:


for i in data1:
    new=i.text


# In[39]:


import re
ps = '\w+'


# In[40]:



res = re.findall(ps,new)


# In[41]:


res


# In[44]:


f={}
for i in data1:
   count = f.get(i,0)
   f[i] = count + 1
    
frequency_list = f.keys()

for j in frequency_list:
   print(j, f[j])

