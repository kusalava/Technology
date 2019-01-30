#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


angles = np.array([0,30,45,60,90])


# In[4]:


# Converting angles to radians
# pi value available numpy package also
angles_radians = angles * np.pi/180
angles_radians


# In[5]:


print('sine of angles in the array:')
print(np.sin(angles_radians))


# In[6]:


angles_radians = np.radians(angles)
angles_radians


# In[19]:


print('Cosine of angles in the arry:')
print(np.cos(angles_radians))


# In[9]:


print('Tangent of angles in the arry:')
print(np.tan(angles_radians))


# In[11]:


sin = np.sin(angles * np.pi/180)
print('Compute sine inverse of angles. Returned values in radians')
inv = np.arcsin(sin)
print(inv)


# In[12]:


# Converting the to degree
print('Check result by converting to degrees')
print(np.degrees(inv))


# In[16]:


test_scores = np.array([32.32,56.98,21.52,44.32,55.63,13.75,43.47,43.34])


# In[17]:


print('Mean (avg) of the test scores')
print(np.mean(test_scores))


# In[18]:


print('Median test scores  of the students ')
print(np.median(test_scores))


# In[20]:


print('variant of the student data')
print(np.var(test_scores))


# In[28]:


salaries = np.genfromtxt('C:\\home\\uploads\\JISPTbatch\\DATAQ\\OBA_KO-QSI-FCTR_Copy\\LOG\\salary.csv',delimiter=',')


# In[38]:


salaries = salaries.reshape(74,24)


# In[39]:


salaries.shape


# In[41]:


# Removing elipses
np.set_printoptions(threshold = np.nan)


# In[42]:





# In[43]:


mean     = np.mean(test_scores)
median   = np.median(test_scores)
sd       = np.std(test_scores)
variance = np.var(test_scores) 


# In[44]:


print('Mean = %i' %mean)
print('Median = %i'%median)
print()
print('Variance = %i'%variance)


# In[ ]:




