
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


x=(5,6)
y=(7,2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim(0,10)
plt.ylim(0,10)


# In[3]:


plt.grid(color='red')


# In[4]:


plt.legend()


# In[5]:


plt.plot(x,y,label="x-axis")


# In[6]:


plt.plot(x,y,label="water")


# In[7]:


plt.legend()


# In[8]:


x1=(5,9)
y1=(4,3)
plt.plot(x1,y1,label='land')
plt.legend()


# In[9]:


plt.plot(x,y,label="water")


# In[10]:


plt.plot(x,y,label="water")
plt.legend()


# In[11]:


player=['virat','msd','rohit','abd']
player1=['virat1','msd1','rohit1','abd1']
runs=[120,130,90,30]
runs1=[20,30,90,30]
plt.bar(player,runs)


# In[12]:


plt.xlabel('players')
plt.ylabel('runs')


# In[13]:


player=['virat','msd','rohit','abd']
player1=['virat1','msd1','rohit1','abd1']
runs=[120,130,90,30]
runs1=[20,30,90,30]
plt.bar(player,runs)
plt.bar(player1,runs1)


# In[14]:


player=['virat','msd','rohit','abd']
player1=['virat1','msd1','rohit1','abd1']
runs=[120,130,90,30]
runs1=[20,30,90,30]
plt.bar(player,runs)
plt.bar(player1,runs1)
plt.show()

