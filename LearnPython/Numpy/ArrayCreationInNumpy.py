#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


array_one = np.array([1,2,3,4])
array_one


# In[9]:


a = [1,2,3,4,5,6]
array_two = np.array(a)
array_two


# In[8]:


array_of_zeros = np.zeros((3,4))
array_of_zeros


# In[12]:


array_of_ones = np.ones((3,4))
array_of_ones


# In[17]:


array_empty = np.empty((2,3))
array_empty


# In[20]:


array_eye = np.eye(4)
array_eye


# In[26]:


# To print the Even numbers in array
# 2 - Start element
# 20 - Stop element
# 2 - Step elemrnt 
# There is no end value printing
array_of_evens = np.arange(2,20,2)
array_of_evens


# In[30]:


array_of_floats = np.arange(0,2,0.3)
array_of_floats


# In[31]:


array_2d = np.array([(1,2,3,4),(6,7,8,9)])
array_2d


# In[34]:


array_2d.shape


# In[37]:


np.arange(6)


# In[40]:


array_nd = np.arange(8).reshape(4,2)
array_nd


# In[41]:


array_nd


# In[44]:


# above arra_nd shape but all vaues are one
array_ones = np.ones_like(array_nd)
array_ones


# In[ ]:




