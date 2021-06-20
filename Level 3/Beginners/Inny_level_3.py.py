#!/usr/bin/env python
# coding: utf-8

# Numpy exercises 

# In[9]:


import numpy as np


# In[13]:


a= np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])
print(a)
a= a.reshape(5,2)
print(a)


# In[14]:


SampleArray= np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(SampleArray)
print(SampleArray[0:,2])


# In[15]:


ArrayOne = np.array([[5, 6, 9], [21, 18, 27]])
ArrayTwo = np.array([[15, 33, 24],[4, 7, 1]])
ArrayAddition = ArrayOne + ArrayTwo
print(ArrayAddition)
Square= np.square(ArrayAddition)
print(Square)


# Panda exercises

# In[16]:


import pandas as pd


# In[17]:


df = pd.read_csv('Automobile_data.csv')


# In[18]:


print(df.head(5))


# In[19]:


print(df.tail(5))


# In[20]:


df.isnull()


# In[21]:


df.fillna("NaN")


# In[22]:


df.describe


# In[23]:


df.groupby("company").price.max()


# In[ ]:


df.

