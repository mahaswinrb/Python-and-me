
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


read = pd.read_csv('guns.csv')
read.columns = map(str.capitalize, read.columns)
print(read.head(n=5))

print(read.Race.value_counts(ascending=False))
gundeath = read.copy(deep=True)
gundeath = gundeath.dropna()


Count = pd.DataFrame(gundeath.Intent.value_counts(ascending=False))
Count = Count.sort_index(axis=0, level=None, ascending=True)
Values = pd.Index(Count).tolist()
Intent = sorted(list(set(gundeath['Intent'])), key=str.lower)
fig = plt.figure(figsize=(9,6))
plt.pie(Values, labels = Intent, autopct = '%1.1f%%')
plt.legend(title='Intention')
plt.title('Cause of deaths', fontsize=20)
plt.axis('equal')
Circle = plt.Circle(xy=(0,0),radius=0.5,facecolor='white')
plt.gca().add_artist(Circle)


gundeath['Race'].replace('Native American/Native Alaskan','Native', inplace=True)
gundeath['Race'].replace('Asian/Pacific Islander','Asian', inplace=True)
Count = pd.DataFrame(gundeath.Race.value_counts(ascending=False))
Count = Count.sort_index(axis=0, level=None, ascending=True)
Values = pd.Index(Count).tolist()
Race = sorted(list(set(gundeath['Race'])), key=str.lower)
fig = plt.figure(figsize=(9, 6))
plt.pie(Values, labels = Race, startangle = 120,autopct = '%1.1f%%')
plt.axis('equal')
plt.legend(title='Race')
plt.title('Ethnic Distribution', fontsize=20)
Circle = plt.Circle(xy=(0,0),radius=0.5,facecolor='white')
plt.gca().add_artist(Circle)


r_a = pd.pivot_table(gundeath,values ='Sex',index=['Age'],columns=['Race'], aggfunc = 'count' )
r_a.plot.area(subplots=True,title = 'Gun Deaths in the US by Race',colormap='coolwarm',stacked=False)


r_a = pd.pivot_table(gundeath,values ='Age',index=['Intent'],columns=['Sex'], aggfunc = 'count' )
r_a.plot.bar(title = 'Gun Deaths in the US (Intention and Sex)',colormap='coolwarm',stacked=True)

r_a = pd.pivot_table(gundeath,values ='Age',index=['Race'],columns=['Intent'], aggfunc = 'count' )
r_a.plot.bar(title = 'Gun Deaths in the US(Intention and Race)',colormap='coolwarm',stacked=True)



intent_edu = gundeath.groupby(['Intent', 'Education'])['Intent'].count().unstack('Education')

edu_legend_labels = ['Less than\nElementry school','Less than \nHigh School', 'Graduated from\nHigh School\nor equivalent', 
                 'Some College', 'At least\ngraduated\nfrom College']


ax = intent_edu.plot(kind='bar', stacked=True, colormap='coolwarm', width=0.5, alpha=0.6)
plt.xticks(rotation=0)
ax.set_xlabel('Intention', fontsize=14)
ax.set_ylabel('No.of.Deaths', fontsize=14)
plt.tick_params(axis='both', which='both',length=0)
ax.legend(edu_legend_labels, ncol=1, frameon=False, prop={'size':10}, loc=0)
plt.ylim(ymin=0, ymax=90000)
plt.title('Educational level vs Intention', fontsize=14, fontweight='bold')

plt.show()

