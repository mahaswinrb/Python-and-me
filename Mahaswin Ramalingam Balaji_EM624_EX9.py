from bs4 import BeautifulSoup
import re
import urllib as ur
from operator import itemgetter

dictio = { "A+" : 1, "A" : 0.96, "A-" : 0.92, "B+" : 0.89,
              "B" : 0.86, "B-" : 0.82, "C+" : 0.79, "C" : 0.76, "C-" : 0.72, 
              "D+" : 0.69, "D" : 0.66, "D-" : 0.62}
hypertext = ur.urlopen("https://www.rottentomatoes.com/m/justice_league_2017/reviews/")
soup = BeautifulSoup(hypertext,'lxml')

overallpages = soup.find('span',{'class':re.compile('pageInfo')}).text.strip().split(' ')[3]
page = 1
scorerev = []
while page <= int(overallpages):
    
    hypertext = ur.urlopen("https://www.rottentomatoes.com/m/justice_league_2017/reviews/?page="+
                      str(overallpages))
    soup = BeautifulSoup(hypertext,'lxml')
    reviews = soup.findAll('div',{'class':re.compile('review_desc')})
    for review in reviews:
        rev = review.find('div',{'class':re.compile('the_review')}).text.strip()
        try:
            rating = review.find('div',{'class':re.compile('small subtle')}).text.strip()
            if "Original Score" in rating:
                rating = re.split('[|:/]',rating)
                rating = float(rating[2].strip())/float(rating[3].strip())
            else: continue
        except:
            #print("Rating tag not found")
            continue
        scorerev.append([rev, rating])
    page += 1
rev_score = sorted(scorerev, key=itemgetter(1), reverse = True)
print"\nTop 10 reviews are:\n", scorerev[:10]
rev_score = sorted(rev_score, key=itemgetter(1))
print"\nBottom 10 reviews are:\n", scorerev[:10]

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
f= open("stopwords_en.txt")
df = pd.read_table(f)
f.close()
df = df.iloc[:,0].values.tolist()
wclist=[]
for review in rev_score:
    words = review[0].split(' ')
    for word in words:
        if word not in df:
            wclist.append(word)    
wc = WordCloud(background_color="white", max_words=25,stopwords=df)
wc.generate(" ".join(wclist)); wc.to_file("file1.png")
plt.imshow(wc); plt.axis('off'); plt.show()