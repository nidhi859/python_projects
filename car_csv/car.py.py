#!/usr/bin/env python
# coding: utf-8

# # Pandas pyplot

# In[1]:


# import the necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


# load the car.csv dataset
car = pd.read_csv("C:/Users/Nidhi/Downloads/Data Analysis using Python/car.csv")
car.head()


# In[3]:


car.dtypes


# In[4]:


car.columns


# In[5]:


# Analyltical summary of the dataset
car.describe(include = 'all')


# In[6]:


car.hist(figsize=(20,30))


# In[7]:


# relationship between categorical and continuous variable
sns.boxplot(x="Vehicle Size", y = "Engine HP", data = car)


# In[8]:


# Drop irrelevant columns
car = car.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'],axis =1)
car.head(5)


# In[9]:


# Renaming the columns names
car = car.rename(columns={"Engine HP":"HP", "Engine Cylinders":"Cylinders","Transmission Type":"Transmission"})
car.head(5)


# In[10]:


# Total number of rows and columns
car.shape


# In[11]:


# Rows containig duplicate data
duplicate_rows_car = car[car.duplicated()]
print("Number of duplicate rows: ",duplicate_rows_car.shape)


# In[12]:


# Count the rows before removing the data
car.count()


# In[13]:


# Drop the duplicates
car = car.drop_duplicates()
car.count()


# In[14]:


# Find the null values
print(car.isnull().sum())


# In[15]:


# Drop the missing values
car = car.dropna()
car.count()


# In[16]:


print(car.isnull().sum())


# In[17]:


# Finding the outliers
sns.boxplot(x=car['HP'])


# In[18]:


# Ploting a Histogram for number of cars per brand
car.Make.value_counts().nlargest(40).plot(kind='bar',figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel("Number of cars")
plt.xlabel("Make")


# In[19]:


# Find the relations between the variables
plt.figure(figsize=(20,30))
c=car.corr()
sns.heatmap(c,cmap='BrBG',annot=True)
c


# In[ ]:




