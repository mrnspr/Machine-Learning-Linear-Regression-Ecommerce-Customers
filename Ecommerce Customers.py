#!/usr/bin/env python
# coding: utf-8

# # Linear Regression Project 
# An E-Commerce company based in New York City sells clothes online. But they also have in-store style and clothing consultations. Customers come into the store, have appointments/meetings with a personal stylist, then can go home and order the clothes they want on a mobile app or website.
# 
# The company is trying to decide whether to focus its efforts on its mobile app experience or its website.
# 
# Just follow the steps below to analyze customer data

# In[26]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # Get the Data
# We'll work with the Ecommerce Customers csv file from the company. It has Customer info, such as <u>Email</u>, <u>Address</u>, and their color <u>Avatar</u>. Then it also has numerical value columns:
# 
# <b>Avg. Session Length</b>: Average session of in-store style advice sessions.<br>
# <b>Time on App</b>: Average time spent on App in minutes<br>
# <b>Time on Website</b>: Average time spent on Website in minutes<br>
# <b>Length of Membership</b>: How many years the customer has been a member.<br>
# ** Read in the Ecommerce Customers csv file as a DataFrame called customers.**

# In[27]:


customers = pd.read_csv("Ecommerce Customers")


# In[28]:


customers.head()


# In[29]:


customers.describe()


# In[30]:


customers.info()


# # Exploratory Data Analysis
# 
# For the rest of the exercise we'll only be using the numerical data of the csv file.
# ___
# **Use seaborn to create a jointplot to compare the "<u>Time on Website</u>" and "<u>Yearly Amount Spent</u>" columns. Does the correlation make sense?**

# In[31]:


# More time on site, more money spent.
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)


#  ** Do the same but with the Time on App column instead. **

# In[32]:


sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)


# Let's explore these types of relationships across the entire data set. Use pairplot to recreate the plot below.

# In[33]:


sns.pairplot(customers)


# Based off this plot what looks to be the most correlated feature with Yearly Amount Spent? Length of Membership

# **Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of Membership. **

# In[34]:


sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)


# # Training and Testing Data
# Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets. ** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **

# In[35]:


y = customers['Yearly Amount Spent']


# In[36]:


X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]


# ** Use model_selection from sklearn to split the data into training and testing sets.**

# In[37]:


from sklearn.model_selection import train_test_split


# In[38]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# # Training the Model
# Now its time to train our model on our training data!
# 
# ** Import LinearRegression from sklearn.linear_model **

# In[39]:


from sklearn.linear_model import LinearRegression


# Create an instance of a LinearRegression() model named lm.

# In[40]:


lm = LinearRegression()


# ** Train/fit lm on the training data.**

# In[41]:


lm.fit(X_train,y_train)


# Print out the coefficients of the model

# In[42]:


# The coefficients
print('Coefficients: \n', lm.coef_)


# # Predicting Test Data
# Now that we have fit our model, let's evaluate its performance by predicting off the test values!
# 
# ** Use lm.predict() to predict off the X_test set of the data.**

# In[45]:


predictions = lm.predict( X_test)


# ** Create a scatterplot of the real test values versus the predicted values. **

# In[46]:


plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')


# # Evaluating the Model
# Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).
# 
# ** Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. Refer to the lecture or to Wikipedia for the formulas**

# In[47]:


# calculate these metrics by hand!
from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# # Residuals
# You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data.
# 
# Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().

# In[24]:


sns.distplot((y_test-predictions),bins=50);


# # Conclusion
# We still want to figure out the answer to the original question, do we focus our efforts on mobile app or website development? Or maybe that doesn't even really matter, and Membership Time is what is really important. Let's see if we can interpret the coefficients at all to get an idea.
# 
# ** Recreate the dataframe below. **

# In[48]:


coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients


# ** How can you interpret these coefficients? **

# Interpreting the coefficients:
# 
# - Holding all other features fixed, a 1 unit increase in **Avg. Session Length** is associated with an **increase of 25.98 total dollars spent**.
# - Holding all other features fixed, a 1 unit increase in **Time on App** is associated with an **increase of 38.59 total dollars spent**.
# - Holding all other features fixed, a 1 unit increase in **Time on Website** is associated with an **increase of 0.19 total dollars spent**.
# - Holding all other features fixed, a 1 unit increase in **Length of Membership** is associated with an **increase of 61.27 total dollars spent**.

# Do you think the company should focus more on their mobile app or on their website?
# 
# This is tricky, there are two ways to think about this: Develop the Website to catch up to the performance of the mobile app, or develop the app more since that is what is working better. This sort of answer really depends on the other factors going on at the company, you would probably want to explore the relationship between Length of Membership and the App or the Website before coming to a conclusion!
