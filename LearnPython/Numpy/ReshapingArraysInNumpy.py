#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([('Germany','France','Hungary','Austria'),('Berlin','Paris','Budapest','vienna')])


# In[4]:


a


# In[6]:


a.shape


# In[7]:


# flattening the array
# Row major flattening to a 1-D array
a.ravel()


# In[8]:


# Transpose of an array - rows become columns and columns become rows
a.T


# In[9]:


# flatens the array row wise
a.T.ravel()


# In[10]:


a.shape


# In[13]:


a.reshape(4,2)


# In[14]:


a.shape


# In[15]:


np.arange(15).reshape(5,3)


# In[17]:


np.arange(15).reshape(3,5)


# In[24]:


countries = np.array(['Germany','France','asd','dfdf','fdg','hjjk','ioio','tyu','opa'])
countries


# In[25]:


# -1 - Means we dont know what the dimention is
# it is automatically findout the dimention
# Rows are not defined but columns as only 3
countries.reshape(-1,3)
# 3 columns in the result, unknown rows depends on the number of elements in the original array


# In[30]:


#Rows are only 3 but columns are depends (they created by the function)
countries.reshape(3,-1)


# In[ ]:




