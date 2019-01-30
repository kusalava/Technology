#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.arange(9)


# In[3]:


x


# In[4]:


print('Split the array in 3 equal-sized sunarrays')
np.split(x,3)


# In[6]:


#np.split(x,4)


# In[ ]:


print('Split the array at position indicated in 1-D array:')
np.split(x,[3,4])

