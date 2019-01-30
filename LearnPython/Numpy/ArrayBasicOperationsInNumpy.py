#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np


# In[2]:


# array operations
a = np.array([10,10,10,10])
b = np.array([5,5,5,5])


# In[3]:


a+b


# In[4]:


a - b


# In[5]:


a*b


# In[6]:


a/b


# In[7]:


a%3


# In[8]:


a < 35


# In[9]:


a>25


# In[11]:


A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print('A:\n',A)
print('B:\n',B)


# In[12]:


A+B


# In[13]:


# Matrix Multiplication
A.dot(B)


# In[14]:


# Anotheer method for matrix multiplication
np.dot(A,B)


# In[19]:


a *= 3
a


# In[18]:


b += a
b


# In[20]:


# we can sum all elements in array
# we can findout min and max values
ages = np.array([1,2,3,4,5,6])


# In[21]:


ages.sum()


# In[22]:


ages.min()


# In[23]:


ages.max()


# In[28]:


numbers = np.arange(12).reshape(3,4)
numbers


# In[29]:


# sum of all column values
numbers.sum(axis=0)


# In[30]:


#for summing all rows values to  use axis = 1
numbers.sum(axis=1)


# In[31]:


# finding minimum element in a row
numbers.min(axis=1)


# In[32]:


# finding minimum element in a column
numbers.min(axis=0)


# In[33]:


numbers.max(axis=0)


# In[35]:


numbers.max(axis=1)


# In[ ]:




