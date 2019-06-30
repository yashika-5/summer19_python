
# coding: utf-8

# In[1]:


import pandas as pd
import findspark
findspark.init('spark24')
from pyspark.sql import SparkSession
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


reviews = pd.read_csv("/home/yashika/Downloads/zomato.csv")
reviews.head(3)
  


# In[3]:


#pd.show_versions()
#reviews.value_counts()


# In[4]:


reviews['location'].value_counts().head(10).plot.bar()


# In[5]:


len(reviews)


# In[6]:


#reviews['votes']
reviews['votes'].value_counts().head(10).sort_index().plot.bar()


# In[7]:


df = pd.DataFrame(np.random.rand(10,4))


# In[8]:


df.cumsum()
df.plot()


# In[9]:


#pd.Series(np.random.rand(10))
ts = pd.Series(np.random.rand(100))


# In[10]:


#ts.cumsum()


# In[11]:


plt.figure(figsize=(10,5))
ts.plot()
#plt.plot()


# In[12]:


len(df)


# In[13]:


list(range(len(df)))


# In[14]:


df[0] = pd.Series()


# In[16]:


#df.plot(0)


# In[19]:


df3 = pd.DataFrame(np.random.randn(10, 2))
                   


# In[38]:


df3.plot()
#columns=['B', 'C']
df3['A'] = pd.Series(list(range(len(df))))
#df3['A']=pd.Series(len(df))


# In[39]:


df3.plot()


# In[40]:


df3.plot()


# In[41]:


df3['A']


# In[43]:


df.iloc[5]


# In[44]:


df = pd.DataFrame(np.random.rand(10,4))


# In[45]:





# In[46]:


df


# In[50]:


df.iloc[4].plot(kind='bar')


# In[54]:


plt.axhline(3, color='red');


# In[55]:


df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])


# In[56]:


df2


# In[57]:


df2.plot()


# In[59]:


df2.plot.bar(stacked=True);


# In[60]:


df2.plot.hist(stacked=True);


# In[63]:


data = { 'Company' :['Hello','heyy','Good','bad'], 'Person' :['Parsang','Yashika','Payal','Parsika'] ,'Sales' :[200,300,100,500]}


# In[64]:


df4=pd.DataFrame(data)


# In[65]:


df4


# In[67]:


df4.plot.hist()


# In[79]:


by = df4.groupby('Sales')


# In[81]:


by.min()


# In[72]:


by.std()


# In[74]:


by.sum().loc['Good']


# In[84]:


reviews.head(5)

