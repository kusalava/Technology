#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.arange(11)**2


# In[3]:


a


# In[4]:


a[2]


# In[5]:


a[-2]


# In[6]:


a[2:7]


# In[7]:


a[2:-2]


# In[8]:


a[:2]


# In[9]:


a[2:]


# In[10]:


a[:7]


# In[11]:


# Step through an elemrnts
# Starting to 11 elemnts but stepping 2
a[:12:2]


# In[15]:


# Step to reverse stepping
# Reverse direction
# Stepping the -1 - means backward
a[::-1]


# In[16]:


# skipping the one element backward
a[::-2]


# In[18]:


# There is no need to all elemrnts in same data type
students = np.array([['Alice','Beth','cathy','Dorothy'],['65','78','90','81'],['71','82','79','92']])


# In[21]:


# symbol '<' - Little endian
# symbol '>' Big endian
# symblo 'U' Unicode
students


# In[23]:


# First Row of the array
students[0]


# In[24]:


# second Row of the array
students[1]


# In[25]:


# Last elements in the array
students[-1]


# In[26]:


students[0,1]


# In[29]:


students[0:2,2:4]


# In[30]:


students[:,1:2]


# In[36]:


students[:,0:1]


# In[37]:


students[:1,0:1]


# In[40]:


students[-1,:-2]


# In[41]:


students[0,...]


# In[43]:


students[1,]


# In[44]:


students[0,]


# In[45]:


students[...,1]


# In[ ]:




