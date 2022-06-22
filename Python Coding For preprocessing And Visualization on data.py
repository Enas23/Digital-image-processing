#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import scipy as sp
import seaborn as sns 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


# In[50]:


df=pd.read_csv("D:/Task1/Retailers History.csv")


# In[87]:


df.head()


# In[88]:


df.tail()


# In[6]:


df.size


# In[89]:


df.describe()


# In[8]:


df.info()


# In[90]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[11]:


duplicateRowsDF=df[df.duplicated()] #find all duplicate data 


# In[12]:


print(duplicateRowsDF)


# In[13]:


duplicateRowsDF4=df[df.duplicated(['order_month'])]


# In[14]:


print(duplicateRowsDF4)


# In[15]:


duplicateRowsDF.plot()


# In[16]:


plt.figure(figsize=(20,12))
sns.set_context('notebook',font_scale = 1.3)
sns.heatmap(df.corr(),annot=True,linewidth =2) # correlation to know relation between features 
plt.tight_layout()


# In[17]:


df.plot()


# In[91]:


df.dropna()


# In[83]:


print(df11)


# In[92]:


df.drop(df.index[[20,21,22,23,24]])


# In[21]:


print(df1)


# In[81]:


df1.dropna()


# In[35]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt





# In[53]:


 
    #df1.to_excel(writer, sheet_name="Sheet1")  
    #df2.to_excel(writer, sheet_name="Sheet2")  


# In[54]:


df1=df.head()
df2=df.tail()


# In[86]:


with pd.ExcelWriter("task3.xlsx") as writer:
    df9.to_excel(writer, sheet_name="Sheet4")  
    df2.to_excel(writer, sheet_name="Sheet3")
    df4.to_excel(writer, sheet_name="Sheet5")
    df5.to_excel(writer, sheet_name="Sheet6")
    df6.to_excel(writer, sheet_name="Sheet7")
    df8.to_excel(writer, sheet_name="Sheet8")
    df11.to_excel(writer, sheet_name="Sheet9")
    
    
    
    


# In[ ]:




