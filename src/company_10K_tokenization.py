#!/bin/env python
# coding: utf-8
# company_10K_tokenization.py
# IEOR242 Applications in Data Analytics Group 06
# Feb 14 2016

import nltk
from nltk.corpus import stopwords
from nltk import stem
import re
from collections import Counter


# Tokenization and word count function
def word_tokenization(text_file):
    stemmer = stem.PorterStemmer()
    raw_text = open(text_file).read().decode('utf8')
    raw_text = raw_text.encode('ascii', 'ignore')
    # Removing numbers and characters
    letters_only = re.sub("[^a-zA-Z]", " ", raw_text)
    # Converting to lowercase
    letters_only = letters_only.lower()
    # Tokenization
    word_token = nltk.word_tokenize(letters_only)
    # Removing Stop Words
    word_token = [w for w in word_token if not w in stopwords.words("english")]
    # Stemming
    word_token_final = []
    for word in word_token:
        try:
            word_token_final.append(stemmer.stem(word))
        except:
            word_token_final.append(word)
    # Word frequency
    word_count_final = Counter(word_token_final)
    return word_count_final


def main():
    # Company names and years in use
    company_years = ['CP2012', 'CP2013', 'CP2014', 'PG2012', 'PG2013']
    # Paths to the MDNA parts from the scrapped company 10K files
    MDNA_files = ["../data/company10k/" + company_years[i] +
                  "_MDNA.txt" for i in range(len(company_years))]
    # Word counts of all the MDNA files
    word_counts = [word_tokenization(MDNA_files[i])
                   for i in range(len(MDNA_files))]
    print word_counts

if __name__ == '__main__':
    main()
