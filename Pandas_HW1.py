#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00488/Live.csv")


# ## Facebook Live Sellers in Thailand

# In[4]:


df


# ## 依照 reaction 次數排列

# In[8]:


df_sorted = df.sort_values(by=["num_reactions"], ascending=False)


# In[9]:


df_sorted


# In[10]:


df.num_reactions.plot()

