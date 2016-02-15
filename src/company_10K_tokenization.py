#!/bin/env python
# coding: utf-8
# company_10K_tokenization.py
# IEOR242 Applications in Data Analytics Group 06
# Feb 14 2016

import nltk
from nltk.corpus import stopwords
import re
from collections import Counter

# Tokenization and word count function
def word_tokenization( text_file ):
    raw_text = open(text_file).read().decode('utf8')
    # Stemming
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    non_stop_text = pattern.sub('', raw_text)
    # Tokenize
    word_token = nltk.word_tokenize(non_stop_text)
    # Count the word frequency
    word_count = Counter(word_token)
    return word_count

# The company names and years in use
company_years = ['CP2012', 'CP2013', 'CP2014', 'PG2012', 'PG2013']
# Paths to the MDNA parts from the scrapped company 10K files
MDNA_files = ["../data/company10k/" + company_years[i] + "_MDNA.txt" for i in range(len(company_years))]
# Get word count of all the MDNA files
word_counts = [word_tokenization(MDNA_files[i]) for i in range(len(MDNA_files))]