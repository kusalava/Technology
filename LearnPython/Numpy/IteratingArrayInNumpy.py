#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.arange(11)**2


# In[3]:


a


# In[7]:


for i in a:
    print(i**(1/2))


# In[10]:


students = np.array([['Alice','Beth','cathy','Dorothy'],['65','78','90','81'],['71','82','79','92']])


# In[11]:


for i in students:
    print('i==',i)


# In[13]:


# Printing all row elements in sequentially
# flatten is in-built function in numpy
for elements in students.flatten():
    print(elements)


# In[14]:


# Printing all column wise elements in sequentially
# flatten is in-built function in numpy
for elements in students.flatten(order='F'):
    print(elements)


# In[16]:


z = np.arange(12).reshape(3,4)
z


# In[17]:


# It prints the row format
for i in np.nditer(z):
    print(i)


# In[18]:


# flattern - Actually returns a result array
# nditer - Just allows you to iterate over elements
for i in np.nditer(z,order='F'):
    print(i)


# In[19]:


# For Iterating column-wise-each column is a 1-D array
for i in np.nditer(z,order='F',flags = ['external_loop']):
    print(i)


# In[20]:


# elements iteration itself
# multiplying the value itself
# elipses (...) are used to iterate current elements of the array 
for arr in np.nditer(z,op_flags = ['readwrite']):
    arr[...] = arr*arr
z


# In[22]:


z


# In[ ]:




