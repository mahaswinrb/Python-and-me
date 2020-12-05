import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


Clinton_dtf = pd.read_csv('guns.csv')
 
senderlist = Clinton_dtf['MetadataFrom']
contentlist = Clinton_dtf['RawText']

listofsender = list(senderlist)
sender_topten = Counter(listofsender).most_common(10)
print '\nThe top 10 senders are:\n', sender_topten


gp = pd.DataFrame({'count':Clinton_dtf.groupby(['SenderPersonId']).size()}).reset_index()
sort = gp.sort_values('count', ascending = False)[:10].reset_index()

frequency = sort["count"].tolist()
names = sort["SenderPersonId"].tolist()
plt.bar(names, frequency, label = "The graph of top 10 senders", alpha = 0.5, align = 'center', color = 'red')
plt.xlabel("Sender ID")
plt.ylabel("Frequency of sender ID")
plt.show()

list_wcl=[]
for i in contentlist:
    for j in str(i).strip('\n').split(' '):
        list_wcl += j.split('\n')
list_wc1=[]
for i in Counter(list_wcl).most_common(25):
    if i[0] == None: continue
    list_wc1.append(str(i[0]))

# Creating a word cloud for most common words
wrdc = WordCloud(background_color="black", max_words=10,stopwords=list_wc1)
wrdc.generate(" ".join(list_wcl)); wrdc.to_file("file1.png")
plt.imshow(wrdc); plt.axis('off'); plt.show()
