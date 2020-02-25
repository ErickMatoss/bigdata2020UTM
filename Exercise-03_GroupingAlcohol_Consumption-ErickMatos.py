#!/usr/bin/env python
# coding: utf-8

# # Ex - GroupBy

# ### Introduction:
# 
# GroupBy can be summarized as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)  
# ### Step 1. Import the necessary libraries

# In[2]:


#With this command we import the pandas library
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 

# ### Step 3. Assign it to a variable called drinks.

# In[3]:


#We import a csv database and assign it to a variable
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()


# ### Step 4. Which continent drinks more beer on average?

# In[4]:


#With this command we list the continents and their beer consumption rate to know which one they drink more on average
drinks.groupby('continent').beer_servings.mean()


# ### Step 5. For each continent print the statistics for wine consumption.

# In[5]:


#With this command we print the statistics of wine consumption of each continent.
drinks.groupby('continent').wine_servings.describe()


# ### Step 6. Print the mean alcohol consumption per continent for every column

# In[6]:


#With this command we can print the mean alcohol consumption per continent for every column
drinks.groupby('continent').mean()


# ### Step 7. Print the median alcohol consumption per continent for every column

# In[7]:


#With this command we can print the median alcohol consumption per continent for every column
drinks.groupby('continent').median()


# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# In[8]:


#With this command we can print the mean, min and max values for spirit consumption
drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])


# In[ ]:




