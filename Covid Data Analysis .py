#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


# In[ ]:


corona_dataset_csv = pd.read_csv("")
corona_dataset_csv.head(10)


# In[ ]:


corona_dataset_aggregated = corona_dataset_csv.groupby("").sum()
corona_dataset_aggregated.head()


# In[ ]:


corona_dataset_aggregated.shape


# In[ ]:


# Visualzing data by Country 
corona_dataset_aggregated.loc["Spain"].plot()


# In[ ]:


# First derivate
corona_dataset_aggregated.loc["Spain"].diff().plot()


# In[ ]:


countries = list(corona_dataset_aggregated.index)
max_infection_rate = []

for c in countries:
    max_infection_rate.append(corona_dataset_aggregated.loc["Spain"].diff().max())

