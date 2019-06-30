
# coding: utf-8

# In[1]:


my_list =[1,2,3]


# In[47]:


import numpy as np
import pandas as pd


# In[5]:


arr = np.array(my_list)

arr
# In[19]:


arr.dtype


# In[7]:


my_mat = [[1,2,300],[34,23,41],[78,34,87]]


# In[8]:


np.array(my_mat)


# In[9]:


np.arange(0,10)


# In[10]:


np.arange(0,11,3)


# In[11]:


np.ones(5)


# In[12]:


np.zeros(5)


# In[13]:


np.linspace(0,10,10)


# In[14]:


np.linspace(0,10,100)


# In[15]:


np.eye(5)


# In[16]:


np.random.rand(9)


# In[18]:


np.random.randn(8,8,6)


# In[20]:


a = np.arange(0,10)


# In[21]:


a


# In[22]:


a[0:5]


# In[23]:


a[5:]


# In[24]:


a[:]


# In[25]:


a[:5]


# In[26]:


arr1 = [[1,2,3],[5,32,67],[87,12,9]]


# In[27]:


arr1


# In[33]:


arr2 = np.array(arr1)


# In[34]:


arr2


# In[35]:


arr2[:2]


# In[36]:


arr2[0:]


# In[37]:


arr2[1:]


# In[38]:


arr2[1: ,1:]


# In[40]:


p =arr2[1: ,1:]


# In[41]:


p


# In[42]:


p[1: ]


# In[43]:


p[1: ,1:]


# In[44]:


arr_2d = np.arange(50).reshape(5,10)


# In[45]:


arr_2d


# In[46]:


arr_2d[1:3 , 3:5]


# In[48]:


clear


# In[58]:


labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = { 'a' : 10 , 'b' : 20 , 'c' :30 }


# In[51]:


my_data
   


# In[52]:


arr


# In[53]:


d


# In[54]:


pd.Series(data = my_data)


# In[55]:


pd.Series(my_data,labels)


# In[56]:


pd.Series(arr)


# In[59]:


pd.Series(d)


# In[61]:


pd.Series(data=[sum,print,len])


# In[64]:


ser1 = pd.Series([1,2,3],['USA','Germany','Japan'])


# ser1

# In[65]:


ser1


# In[66]:


ser1[1]


# In[67]:


ser1['USA']


# In[68]:


ser2 = pd.Series(data= labels)


# In[69]:


ser2[0]


# In[70]:


ser2


# In[71]:


ser1 + ser2


# # Pandas - DataFrames

# In[72]:


from numpy.random import randn


# In[74]:


a = np.random.seed(101)


# In[92]:


randn(2)


# In[93]:


df = pd.DataFrame(randn(6,4),['A','B','C','D','E','F'],['W','X','Y','Z'])


# In[94]:


df


# In[95]:


df['W']


# In[96]:


type(df['W'])


# In[97]:


type(df)


# In[98]:


df.W


# In[99]:


df.X


# In[101]:


df[['W','Z']]


# In[103]:


df['new'] = df['W'] + df['Y']


# In[104]:


df


# In[111]:


#df.drop('new',axis=1,inplace=True)


# In[112]:


df.drop('E')


# In[113]:


df.shape


# df

# In[115]:


df[['Z']]


# In[116]:


#ROWS


# In[117]:


df


# In[118]:


df.loc['A']


# In[119]:


df.iloc[2]


# In[120]:


df


# In[121]:


df.loc['E','Z']


# In[122]:


df.loc[['A','B'],['W','Y']]


# In[126]:


booldf = df > 0


# In[127]:


booldf


# In[128]:


df


# In[129]:


df[booldf]


# In[130]:



df 


# In[131]:


df[df['Z'] < 0]


# In[133]:


df[df['Z'] < 0] [['X']]


# In[134]:


df['W'] >0


# In[139]:


df[(df['W']>0) & (df['Z']>1)]


# In[138]:


df


# In[140]:


df.reset_index()


# In[141]:


newind = 'CA NY WY OR CO'.split()


# In[142]:


newind


# In[151]:


df('States')=newind


# In[ ]:





# In[150]:


df


# In[147]:


df.set_index('States')


# In[152]:


d = { 'A':[1,2,np.nan],'B ':[5,np.nan,np.nan],'c':[1,2,3]}


# In[153]:


df1 = pd.DataFrame(d)


# In[154]:


df1


# In[158]:


df1.dropna(axis=1)


# In[163]:


df1.dropna(thresh=1)


# In[164]:


df1.fillna(value='FILL VALUEEE')


# In[165]:


df1['A']


# In[167]:


df1['A'].fillna(value=df1['A'].mean())

