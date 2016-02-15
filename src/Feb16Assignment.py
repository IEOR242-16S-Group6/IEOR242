
# coding: utf-8

# In[ ]:

#!/bin/env python
# Feb16_Tokenizing.py
# IEOR242 Applications in Data Analytics 
# Feb 14 2016


# In[2]:

import nltk
from nltk.corpus import stopwords
import pandas as pd


# In[9]:

# Import Dictionary
Library = pd.DataFrame(pd.read_csv("../data/LoughranMcDonald_MasterDictionary_2014.csv"))


# In[6]:

# PATHS to our scrapped 10K files
CP2012_MDNA = "../data/company10k/CP2012_MDNA.txt"
CP2013_MDNA = "../data/company10k/../data/company10k/company10k/CP2013_MDNA.txt"
CP2014_MDNA = "../data/company10k/company10k/CP2014_MDNA.txt"
PG2012_MDNA = "../data/company10k/company10k/PG2012_MDNA.txt"
PG2013_MDNA = "../data/company10k/company10k/PG2013_MDNA.txt"


# In[7]:

MDNA = open(CP2012_MDNA).read()


# In[8]:

# Stemming


# In[ ]:



