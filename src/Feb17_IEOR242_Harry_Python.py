#!/usr/bin/env python
# Some exploratory tests
# Harry Sun
# Feb 17 2016

import pandas as pd

# Get the files and import to DataFrames
!wget -c http://funglab.berkeley.edu/pub/tic_company_gics
gics_df = pd.read_table("tic_company_gics")
!wget -c funglab.berkeley.edu/pub/sec.list.txt -o sec_list.txt
sec_list_df = pd.read_table("sec_list.txt", header=None)


sec_list_df.columns = ['Names']

# See if we can get the company names from sec list
sec_list_df['Names'][5]
name5 = sec_list_df['Names'][5]
name5.split('_')
name5.split('_')[4]
name5.split('_')[3]
for i in range(0, 40):
    print sec_list_df['Names'][i].split('_')[3].split('-')[0]

# Save it
sec_company_names = []
for i in range(0, len(sec_list_df)):
    sec_company_names.append(sec_list_df['Names'][i].split('_')[3].split('-')[0])
# Convert to DataFrame
sec_company_names_df = pd.DataFrame(sec_company_names)
sec_company_names_df.columns = ['sec_companies']

# Get all the consumer staples companies from gics
consumer_staples_gics = gics_df[gics_df['gsector']==30]

# Remove all the duplicates
consumer_stapels_gics_nodup = consumer_staples_gics.drop_duplicates()

# Get list of gics company names
consumer_staples_gics_company_names = consumer_stapels_gics_nodup['conm']
# Convert to DataFrame
con_staples_gics_company_names = pd.DataFrame(consumer_staples_gics_company_names)

# Rename them
gics_company_names_staples = con_staples_gics_company_names
gics_company_names_staples.columns = ['gics_companies']


# Save them to lists
list_gics_company_names_staples = gics_company_names_staples['gics_companies'].tolist()
list_sec_company_names = sec_company_names_df['sec_companies'].tolist()
