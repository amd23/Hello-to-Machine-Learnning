
# coding: utf-8

# In[417]:


import numpy as np
from matplotlib import pyplot as plt
#importing numpy and matpolib
get_ipython().magic('matplotlib inline')


# In[418]:


price = [1, 0.6, 1.4, 1.1,1.4, 1.3, 0.9, 1.1, 1.2, 1.4]
land = [39, 46, 48 , 51, 56, 59, 62, 65, 69, 6.9]
#a sat1ple data set with x price in t1illion and y land it0 sqt1


# In[419]:


# y = mx + b the formula fo straight line
t1 = 0
t0 = 0
y = lambda x : t1*x + t0


# In[420]:



# here I am taking the min and max of the sample data
def centralLine(y, data_points):
    x_values = [i for i in range(int(min(data_points))-1, int(max(data_points))+2)]
    y_values = [y(x) for x in x_values]
    plt.plot(x_values, y_values, 'r')
    


# In[421]:


alpha = 0.01 # if we make it too big we may miss the desired result it is the learning thing in the gradient descent
def summationForThetas(y, price, land):
    thetaZero = 0
    thetaOne = 0
    #summation for cost function
    #plus measuring distance of the dots related to the plotted lines i.e. to the hypothesis predicted
    for i in range(1, len(price)):
        thetaZero += y(price[i]) - land[i]
        thetaOne += (y(price[i]) - land[i])
        
    return thetaZero / len(price), thetaOne / len(price) # dividing by m


# In[422]:


for i in range(200):
    s0, s1 = summationForThetas(y, price, land)
    t1 = t1 - alpha * s1
    t0 = t0 - alpha * s0
    centralLine(y, price)
    plt.plot(price, land, 'gd')


# In[423]:


centralLine(y, price)
plt.plot(price, land, 'gd')


# In[424]:


y(10)


# In[425]:


y(20)


# In[426]:


import pandas as pd
df = pd.read_csv("C:/Users/User/Downloads/housingdata.csv")


# In[427]:


df.head()


# In[428]:


x_points = df['price'].tolist()
y_points = df['land'].tolist()


# In[429]:


plt.plot(x_points, y_points, 'bo')

