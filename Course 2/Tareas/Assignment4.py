
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Bogotá, Bogota D.C., Colombia**, or **Colombia** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Bogotá, Bogota D.C., Colombia** to Ann Arbor, USA. In that case at least one source file must be about **Bogotá, Bogota D.C., Colombia**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Bogotá, Bogota D.C., Colombia** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')

#Read Datasets
file = 'Colombia.csv'
df = pd.read_csv(file,sep=';')
file2 = 'All London 2012 athletes - ALL ATHLETES.csv'
df2 = pd.read_csv(file2)


# In[4]:

#Work on dataset 1
# Filter for Colombian athletes
newdf=df.loc[(df.NOC=='COL')]

#Select the data to plot
Women=newdf.loc[(newdf.Sex=='F')]
Men=newdf.loc[(newdf.Sex=='M')]

# Set up values
X=Men.Age.value_counts()
Y=Women.Age.value_counts()
Y1=Y.index.values
A=[]
for i in Y1:
    b=int(i)
    A.append(b)
B=Y.values
X1=X.index.values
C=[]
for i in X1:
    d=int(i)
    C.append(d)
D=X.values

#Plot
plt.figure()
plt.title("Histogram of Ages by Gender of Olympic Colombian Athletes", loc='center', alpha=0.8,fontsize=14)
plt.bar(C, D, alpha=0.5, label='Men')
plt.bar(A, B, alpha=0.9, label='Women')
plt.axvline(x=np.array(A).mean(), zorder=1, color='k', ls='--',label='Mean Men')
plt.axvline(x=np.array(C).mean(), zorder=1, color='k', ls='-.', label='Mean Women')
plt.xlabel('Age')
plt.ylabel('Count')
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]
plt.legend(loc=7, frameon=False)
Wmean='Mean women = '+str(round(np.array(A).mean(),0))
Mmean='Mean men = '+str(round(np.array(C).mean(),0))
plt.text(16, 84.5, Wmean, fontsize=7, alpha=0.9)
plt.text(33, 84.5, Mmean, fontsize=7, alpha=0.9)


# In[5]:

#Work on dataset 2
lon= df2.loc[(df2.Country=='Colombia')]
Womenlon=lon.loc[(lon.Sex=='F')]
Menlon=lon.loc[(lon.Sex=='M')]

# Set up values
Xlon=Menlon.Age.value_counts()
Ylon=Womenlon.Age.value_counts()
Y1lon=Ylon.index.values
Alon=[]
for i in Y1lon:
    b=int(i)
    Alon.append(b)
Blon=Ylon.values
X1lon=Xlon.index.values
Clon=[]
for i in X1lon:
    d=int(i)
    Clon.append(d)
Dlon=Xlon.values

#Plot
plt.figure()
plt.title("Histogram of Ages by Gender of Olympic\n Colombian Athletes in London 2012", loc='center', alpha=0.8,fontsize=14)
plt.bar(Alon, Blon, alpha=0.5, label='Women')
plt.bar(Clon, Dlon, alpha=0.9, label='Men')
plt.axvline(x=np.array(Alon).mean(), zorder=1, color='k', ls='--', label='Mean Women')
plt.axvline(x=np.array(Clon).mean(), zorder=1, color='k', ls='-.',label='Mean Men')
plt.xlabel('Age')
plt.ylabel('Count')
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]
plt.legend(loc=7, frameon=False)
Wmean='Mean women = '+str(round(np.array(Alon).mean(),0))
Mmean='Mean men = '+str(round(np.array(Clon).mean(),0))
plt.text(19, 8, Wmean, fontsize=7, alpha=0.9)
plt.text(28, 8, Mmean, fontsize=7, alpha=0.9)


# In[ ]:



