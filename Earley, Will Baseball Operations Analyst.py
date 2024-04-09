#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## We begin by importing the data into a Data Frame. We explore the data using the describe command for statistical information and the isnull command to see if there are any null values. 

# In[15]:


# Reading in the csv file, making sure to correctly identify the index column
hitter = pd.read_csv('/Users/williamearley/Jobs/Detroit Tigers/Baseball Operations Analyst/AnalyticsQuestionnaireHitData.csv', index_col=0)


# In[16]:


# Making sure we can see all of the columns
pd.set_option('display.max_columns', None)


# In[17]:


# Taking a look at the data
hitter.head(3)


# In[12]:


# Using describe to get a sense of all the numerical columns here.
hitter.describe()


# In[ ]:


# Always good to check for null values in a dataset, given a longer breakdown I would do some imputation or
# fill in the missing values. I am not going to print out these results at this time but there are some
# null values.
hitter.isnull().sum()


# ### Creating visualizations to communicate data and tell the story is one of my absolute favorite things to do. I kept it simple here because sometimes less is more. I am letting these stats speak for themselves in a clear, straightforward, and understandable way. This helps when breaking down data for decision makers who are less familiar with quantitative methods. 

# In[21]:


# Batted Ball Outcomes
batted_ball_outcomes = hitter['PitchCall'].value_counts()
plt.figure(figsize=(12, 8))
batted_ball_outcomes.plot(kind='bar', color='skyblue')
plt.title('Batted Ball Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[23]:


# Pitch Type Distribution
pitch_type_distribution = hitter['PitchType'].value_counts()
plt.figure(figsize=(8, 6))
pitch_type_distribution.plot(kind='bar', color='lightgreen')
plt.title('Pitch Type Distribution')
plt.xlabel('Pitch Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[28]:


# Handedness Matchups
handedness_matchups = hitter.groupby('BatterSide')['PitchCall'].value_counts().unstack()
handedness_matchups.plot(kind='bar', figsize=(12, 6))
plt.title('Handedness Matchups')
plt.xlabel('Batter Side')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Pitch Call')
plt.tight_layout()
plt.show()


# ### Given more time, I would lean on the pybaseball package to really bring these visualizations to life.

# In[27]:


from pybaseball import statcast

