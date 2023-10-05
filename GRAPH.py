#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
import matplotlib.pyplot as plt 
 
# data to be plotted
x = np.arange(1, 11) 
y = x * x * x
 
# plotting
plt.title("Line graph") 
plt.xlabel("X axis") 
plt.ylabel("Y axis") 
plt.plot(x, y, color ="red") 
plt.show()


# In[6]:


plt.bar(x,y,color = 'green')
plt.show()


# In[24]:


plt.hist(x,y,color = 'blue')
plt.show()


# In[19]:


plt.bar([0.25,2.25,3.25,5.25,7.25],[300,400,200,600,700],
label="Carpenter",color='b',width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[50,30,20,50,60],
label="Plumber", color='g',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Wage')
plt.title('Details')

# Print the chart
plt.show()


# In[26]:


x1 = [1, 2.5,3,4.5,5,6.5,7]
y1 = [1,2, 3, 2, 1, 3, 4]
x2=[8, 8.5, 9, 9.5, 10, 10.5, 11]
y2=[3,3.5, 3.7, 4,4.5, 5, 5.2]
plt.scatter(x1, y1, label = 'high bp low heartrate', color='c')
plt.scatter(x2,y2,label='low bp high heartrate',color='g')
plt.title('Smart Band Data Report')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Print the chart
plt.show()


# In[ ]:




