
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# In[7]:


path ='DataSet\datasets.csv'
data=pd.read_csv(path)
data.columns=['cropType','cropDays','soilMoisture','temp','humidity','y']
sb.pairplot(data)


# In[9]:


print(data.corr())

