#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.arange(6)


# In[3]:


print(a)


# In[5]:


b = np.arange(12).reshape(4,3)


# In[6]:


print(b)


# In[7]:


c= np.arange(24).reshape(2,3,4)


# In[8]:


print(c)


# In[11]:


print(np.arange(10000).reshape(100,100))


# In[13]:


# For no summarisation
# No elipses (....)
''' threshold specifies the total number of array elements which trigger summarization - here we dont wat 
    any summarization'''
np.set_printoptions(threshold = np.nan)


# In[15]:


large_matrix = np.arange(10000).reshape(100,100)
print(large_matrix)


# In[ ]:




