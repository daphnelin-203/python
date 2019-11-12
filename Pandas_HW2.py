#!/usr/bin/env python
# coding: utf-8

# In[36]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[37]:


df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00484/tripadvisor_review.csv")


# ## TripAdvisor 十個旅遊地評論 Average user feedback

# In[38]:


df.head(11)


# ## 更改表頭名

# In[39]:


df.rename(columns={'Category 1':'art galleries','Category 2':'dance clubs','Category 3':'juice bars','Category 4':'restaurants','Category 5':'museums','Category 6':'resorts','Category 7':'parks/picnic spots','Category 8':'beaches','Category 9':'theaters','Category 10':'religious institutions',}, inplace = True)


# In[44]:


A = df.head(11)


# In[58]:


A


# In[62]:


B = A.drop(['User ID'], axis=1)


# In[63]:


B


# In[68]:


B.plot()

