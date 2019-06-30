
# coding: utf-8

# In[1]:


import findspark
# this is for loading pyspark from home directory
findspark.init('spark24')
#now we can use pyspark

from pyspark import SparkContext  # this is for word count


# In[2]:


# this time we need live data not from csv or xls
from pyspark.streaming import StreamingContext


# In[3]:


# now using sparkcontext
sc = SparkContext("local[2]", "NetworkWordCount")
                 
    


# In[4]:


#to assign edelay in message
ssc = StreamingContext(sc,10)


# In[5]:


# now defining tcp socket ip and port
lines = ssc.socketTextStream("localhost", 9999) # bind the tcp socket


# In[6]:


# above line will take each and every data in lines


# In[7]:


# now splitting lines with space to find the words
words = lines.flatMap(lambda line: line.split(" "))


# In[8]:


# now assigning number 1 to each and every words
pairs = words.map(lambda word: (word, 1))


# In[9]:


# this timw will reduce by words and count it
wordCounts = pairs.reduceByKey(lambda x, y: x + y)


# In[10]:


# to print live streaming data 
wordCounts.pprint()


# In[11]:


# this will start live streaming
ssc.start()


# In[ ]:


ssc.awaitTermination()

