
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import findspark
findspark.init('spark24')


# In[2]:


# web scrapping
#load url
web=requests.get('https://php.net/')


# In[4]:


# loading text data only for html
htmldata=web.text


# In[7]:


# now applying bs
soup=BeautifulSoup(htmldata,'html5lib')
text_only=soup.get_text() # string


# In[8]:


# storing data permanently
'''f=open('php.txt','w+')
f.write(text_only)
f.close()'''



# In[11]:


#!cat php.txt
newdata = [i for i in text_only.split()]  # list


# In[13]:


with open('php.txt','w+') as f:
    f.write(str(newdata))


# In[1]:


get_ipython().system('cat php.txt')


# In[16]:


f = open('php.txt','w')
for j in newdata:
    f.write(j)
    f.write('\n')
f.close()


# In[ ]:


u

