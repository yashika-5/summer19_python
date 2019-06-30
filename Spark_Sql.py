
# coding: utf-8

# In[1]:


import findspark
findspark.init('spark24')
from pyspark.sql import SQLContext
from pyspark.sql import DataFrameNaFunctions
from pyspark import SparkConf
from pyspark import SparkContext
conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


# In[2]:


sqlContext = SQLContext(sc)


# In[3]:


# supervised algo 
df = sqlContext.read.format("csv").option("header", "true").load("/home/yashika/Decision-Tree-Through-Spark-master/daily_weather.csv")


# In[4]:


display(df)


# In[5]:


df.show()


# In[6]:


df.columns


# In[7]:


featureColumns = ['air_pressure_9am','air_temp_9am','avg_wind_direction_9am','avg_wind_speed_9am',
        'max_wind_direction_9am','max_wind_speed_9am','rain_accumulation_9am',
        'rain_duration_9am']


# In[8]:


df = df.drop('number')


# In[9]:


df = df.na.drop()


# In[10]:


df


# In[11]:


df.show()


# In[12]:


df.count()


# In[13]:


from pyspark.ml.feature import Binarizer


# In[14]:


binarizer = Binarizer(threshold=24.99999,inputCol="relative_humidity_3pm",outputCol="label")


# In[15]:


# trasnfrom for adding column to table

binarizerDF = binarizer.transform(df)

