
# coding: utf-8

# In[18]:


import findspark
import time
findspark.init('spark24')
import matplotlib.pyplot as plt


# In[2]:


# now calling spark
from pyspark import SparkContext
sc=SparkContext()


# In[3]:


# loading file
frdd=sc.


# In[5]:


data


# In[6]:


frdd


# In[7]:


[i for i in dir(frdd) if 'flat' in i]


# In[8]:


# splitting in line

linesplit=frdd.flatMap(lambda line:line.split(" "))
             # for line in frdd.flatMap
            # line.split(" ")


# In[9]:


#applying mapping
#dir(linesplit)
mapping=linesplit.map(lambda word: (word,1))


# In[10]:


#now apply reduce

count = mapping.reduceByKey(lambda a,b:a+b)


# In[12]:


data = count.collect()


# In[15]:


list1=[]
list2=[]
for i in data :
    #print(i)
    #time.sleep(1)
    list1.append(i[0])
    list2.append(i[1])


# In[24]:


#list2
# plot graph
plt.figure(figsize=(16,15))
plt.xlabel('words')
plt.ylabel('count')
plt.grid()
plt.bar(list1,list2)

