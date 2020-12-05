
"""
Assingment done by Nitanshu Shrivastava
10432297

This program is for calculating top 15 senders and 
create a graph and analyse 
"""
import csv
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
# open the file and read it as a data frame
n= open("H_Clinton-emails.csv")
fr1 = csv.reader(n)
fr1 = pd.read_csv(n)
# creating frame of MetaDataFrom
listMetadataFrom = fr1.MetadataFrom.tolist()
print"\n following is list of senders \n",listMetadataFrom

# creating frame of RawText
listRawText = fr1.RawText.tolist()
print"following is the list of contents \n",listRawText

# Grouping SenderPersonId based on count and sorting it in descending order and selecting top 10 IDs
dataf2 = pd.DataFrame({'count':fr1.groupby(['SenderPersonId']).size()}).reset_index()
dataf1 = dataf2.sort_values('count', ascending = False)[:10].reset_index()
print"\n The top 10 senders are\n ",fr1.MetadataFrom[dataf1.SenderPersonId.tolist()]

# Creating a list of 100 most common words in RawText
listword=[]
for i in listRawText:
    for j in str(i).strip('\n').split(' '):
        listword += j.split('\n')
listword1=[]
for i in Counter(listword).most_common(100):
    if i[0] == None: continue
    listword1.append(str(i[0]))

# Creating a word cloud
wc = WordCloud(background_color="white", max_words=50,stopwords=listword1)
wc.generate(" ".join(listword)); wc.to_file("file1.png")
plt.imshow(wc); plt.axis('off'); plt.show()
'''
# Creating a Scatter plot for top 15 sendors
frequency = dataf1["count"].tolist()
name= dataf1["SenderPersonId"].tolist()
plt.bar(name, frequency, label = "graph of top 15 senders", color = "k")
plt.xlabel("SenderId"); plt.ylabel("frequency of SenderPersonId"); plt.show()
n.close()
'''