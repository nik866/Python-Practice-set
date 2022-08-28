#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
with open('D:\Food Quantium.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# In[7]:


import csv
with open('D:\Food Quantium.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# In[ ]:




