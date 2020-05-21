
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rnd


# In[13]:


data = pd.read_csv('lalvslac.csv')


# In[14]:


data


# In[20]:


laldf = data[data.Tm == 'LAL']
lacdf = data[data.Tm == 'LAC']


# In[123]:


laldf.PTS.hist(color = 'gold')
lacdf.PTS.hist(color = 'red')
plt.title('Points per game',fontsize=14)
plt.legend(['Lakers', 'Clippers'])


# In[124]:


laldf.OPTS.hist(color = 'gold')
lacdf.OPTS.hist(color = 'red')
plt.title('Opponent Points per game',fontsize=14)
plt.legend(['Lakers', 'Clippers'])


# In[56]:


lalmeanpts = laldf.PTS.mean()
lalsdpts = 12.020
lacmeanpts = lacdf.PTS.mean()
lacsdpts = 14.121
lalmeanopts = laldf.OPTS.mean()
lalsdopts = 12.0521
lacmeanopts = lacdf.OPTS.mean()
lacsdopts = 11.851


print("Lakers Average Points per game is ", lalmeanpts)
print("Clippers Average Points per game is ", lacmeanpts)
print("Lakers Average Opponent Points per game is ", lalmeanopts)
print("Clippers Average Opponent Points per game is ", lacmeanopts)


# In[118]:


rnd.gauss(lalmeanpts, lalsdpts)


# In[91]:


def gameSim():
    LALScore = (rnd.gauss(lalmeanpts, lalsdpts)+ rnd.gauss(lacmeanopts, lacsdopts))/2
    LACScore = (rnd.gauss(lacmeanpts, lacsdpts)+ rnd.gauss(lalmeanopts, lalsdopts))/2
    if int(round(LALScore)) > int(round(LACScore)):
        return "Lakers Win"
    elif int(round(LALScore)) < int(round(LACScore)):
        return "Clippers Win" 
    else: return 'Tie'


# In[132]:


gameSim()

