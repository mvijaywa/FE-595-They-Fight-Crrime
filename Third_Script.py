
# coding: utf-8

# In[ ]:


from textblob import TextBlob
import pandas as pd


# In[ ]:


df1 = pd.DataFrame()
#df2 = pd.DataFrame()
with open('merged.txt') as fp:
    for line in fp:
        line = line.replace('They fight crime!','')
        if("She's" in line):
            line = line.split("She's")[1]
            df1 = df1.append({'Character':line,'Polarity':TextBlob(line).sentiment.polarity}, ignore_index=True)
        if("he's" in line):
            line = line.split("he's")[1]
            df1 = df1.append({'Character':line,'Polarity':TextBlob(line).sentiment.polarity}, ignore_index=True)
x = df1['Character'].value_counts().index.tolist()[0:10]
print(x)

