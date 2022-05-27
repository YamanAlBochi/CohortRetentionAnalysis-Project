#!/usr/bin/env python
# coding: utf-8

# # Importing all the necessary libraries for our Project:

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# # Uploading our Dataset:

# In[3]:


df = pd.read_excel("Online Retail.xlsx")


# # Performing Data Exploration:

# In[5]:


df.info()


# In[6]:


df.head()


# In[7]:


df.describe()


# After Exploration we need to Focus on ccustomers with ID to perform our Analysis

# # Data Cleaning:

# In[9]:


df = df.dropna(subset=['CustomerID'])
df.info()


# Now we have the same Non-Null values for our Data

# # Lets create a function so we can see our Cohort invoice months.

# In[10]:


#function for invoice month
import datetime as dt
#function for month
def get_month(x):
    return dt.datetime(x.year, x.month, 1)
#Applying the function
df['InvoiceMonth'] = df['InvoiceDate'].apply(get_month)
df.tail()


# We'll use this later to create our Cohort months

# # Lets create a column index with the minimum invoice date for our first customer acquired

# In[12]:


df['Cohort Month'] = df.groupby('CustomerID')['InvoiceMonth'].transform('min')
df.tail(30)


# Now we're able to see the diferrence in Cohorts from the Invoice month and the cohort months

# # Let's create a data element function to get a series for subtraction 

# In[13]:


# create a date element function to get a series for subtraction
def get_date_elements(db, column):
    day = db[column].dt.day
    month = db[column].dt.month
    year = db[column].dt.year
    return day, month, year


# In[15]:


# get date elements for our cohort and invoice columns
_,Invoice_month,Invoice_year =  get_date_elements(df,'InvoiceMonth')
_,Cohort_month,Cohort_year =  get_date_elements(df,'Cohort Month')


# In[16]:


#check the series 
Cohort_year[:10]


# In[19]:


df.head()


# In[20]:


#create a cohort index 
year_diff = Invoice_year -Cohort_year
month_diff = Invoice_month - Cohort_month
df['CohortIndex'] = year_diff*12+month_diff+1
df.tail()


# In[22]:


#count the customer ID by grouping by Cohort Month  and Cohort Index 
cohort_df = df.groupby(['Cohort Month','CohortIndex'])['CustomerID'].apply(pd.Series.nunique).reset_index()
cohort_df


# In[24]:


# create a pivot table 
cohort_table = cohort_df.pivot(index='Cohort Month', columns=['CohortIndex'],values='CustomerID')
cohort_table


# In[27]:


#change index
#cohort_table.index = cohort_table.index.strftime('%B %Y')
#visualize our results in heatmap
plt.figure(figsize=(21,10))
sns.heatmap(cohort_table,annot=True,cmap='Greens')


# In[28]:


#cohort table for percentage
new_cohort_table = cohort_table.divide(cohort_table.iloc[:,0],axis=0)
new_cohort_table


# In[29]:


#create a percentages visual
plt.figure(figsize=(21,10))
sns.heatmap(new_cohort_table,annot=True,fmt='.0%')


# # The end

# In[ ]:




