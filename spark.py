
# coding: utf-8

# In[1]:


import findspark


# In[2]:


import findspark


# In[3]:





# In[23]:


import findspark
import time


# In[2]:


findspark.init('spark24')


# In[3]:


#import pyspark not a good pra


# In[4]:


from pyspark import SparkContext  # spark basic ops


# In[5]:


# how to read data from a file ---  json , csv , text , xls


# In[6]:


x= SparkContext()


# In[15]:


frdd = x.textFile('/home/yashika/Desktop/a.txt') # creating first RDD


# In[ ]:


frdd.collect()

# only read first line


# In[ ]:


frdd


# In[ ]:


fldd = frdd.first()


# In[10]:


fldd = frdd.first()


# In[11]:


frdd


# In[12]:


fldd


# In[27]:


data = frdd.take(1) # top 3 lines read


# In[28]:


data
list1=[]
list2=[]
import matplotlib.pyplot as plt


# In[29]:


# printing each lines in a gap of 2 sec
for i in data :
    print(i)
    time.sleep(2)

# sep words of line by space  
    for j in i.split():
        count=i.count(j)
        list1.append(j)
        list2.append(count)
plt.xlabel('words')
plt.ylabel('count')
plt.bar(list1,list2)





