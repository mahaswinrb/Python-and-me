import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

Dff = pd.read_excel('gun.xlsx')
Dff.columns = map(str.capitalize, Dff.columns)
print(Dff.head(n=5))

print(Dff.Race.value_counts(ascending=False))
guns = Dff.copy(deep=True)
guns = guns.dropna()

# Intent Donut
Count = pd.DataFrame(guns.Intent.value_counts(ascending=False))
Count = Count.sort_index(axis=0, level=None, ascending=True)
Values = pd.Index.tolist(Count)
Intent = sorted(list(set(guns['Intent'])), key=str.lower)
fig = plt.figure(figsize=(9,6))
plt.pie(Values, labels = Intent, autopct = '%1.1f%%')
plt.legend(title='Intent')
plt.title('Death Reasons', fontsize=20)
plt.axis('equal')
Circle = plt.Circle(xy=(0,0),radius=0.5,facecolor='white')
plt.gca().add_artist(Circle)

# Race Donut
guns['Race'].replace('Native American/Native Alaskan','Native', inplace=True)
guns['Race'].replace('Asian/Pacific Islander','Asian', inplace=True)
Count = pd.DataFrame(guns.Race.value_counts(ascending=False))
Count = Count.sort_index(axis=0, level=None, ascending=True)
Values = pd.Index.tolist(Count)
Race = sorted(list(set(guns['Race'])), key=str.lower)
fig = plt.figure(figsize=(9, 6))
plt.pie(Values, labels = Race, startangle = 120,autopct = '%1.1f%%')
plt.axis('equal')
plt.legend(title='Race')
plt.title('Ethnic Distribution', fontsize=20)
Circle = plt.Circle(xy=(0,0),radius=0.5,facecolor='white')
plt.gca().add_artist(Circle)

# Education/Ethnic Group Bar
Asian = guns[['Race','Education']].copy(deep=True)
Asian = Asian[Asian.Race == 'Asian']
Asian = pd.DataFrame(Asian['Education'].value_counts(ascending=False))
Asian = Asian.sort_index(axis=0, level=None, ascending=True)
Asian = Asian['Education'].values.tolist()
Black = guns[['Race','Education']].copy(deep=True)
Black = Black[Black.Race == 'Black']
Black = pd.DataFrame(Black['Education'].value_counts(ascending=False))
Black = Black.sort_index(axis=0, level=None, ascending=True)
Black = Black['Education'].values.tolist()
White = guns[['Race','Education']].copy(deep=True)
White = White[White.Race == 'White']
White = pd.DataFrame(White['Education'].value_counts(ascending=False))
White = White.sort_index(axis=0, level=None, ascending=True)
White = White['Education'].values.tolist()
Native = guns[['Race','Education']].copy(deep=True)
Native = Native[Native.Race == 'Native']
Native = pd.DataFrame(Native['Education'].value_counts(ascending=False))
Native = Native.sort_index(axis=0, level=None, ascending=True)
Native = Native['Education'].values.tolist()
Hispanic = guns[['Race','Education']].copy(deep=True)
Hispanic = Hispanic[Hispanic.Race == 'Hispanic']
Hispanic = pd.DataFrame(Hispanic['Education'].value_counts(ascending=False))
Hispanic = Hispanic.sort_index(axis=0, level=None, ascending=True)
Hispanic = Hispanic['Education'].values.tolist()

barWidth = 0.15
r1 = np.arange(len(Asian))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
fig = plt.figure(figsize=(9, 6))
plt.bar(r1, Asian, color='blue', width=barWidth, edgecolor='white', label='Asian')
plt.bar(r2, Black, color='yellow', width=barWidth, edgecolor='white', label='Black')
plt.bar(r3, White, color='seagreen', width=barWidth, edgecolor='white', label='White')
plt.bar(r4, Native, color='red', width=barWidth, edgecolor='white', label='White')
plt.bar(r5, Hispanic, color='black', width=barWidth, edgecolor='white', label='Hispanic')
plt.xticks([r + barWidth for r in range(len(Asian))], ['Elementary', '< High','High', '= High', 'Graduate'])
plt.title('Race vs Education', fontsize=20)
plt.legend()

#Age Hist
Age = guns.Age.value_counts()
fig = plt.figure(figsize=(9, 5))
plt.hist(guns['Age'],rwidth = 0.5,color = 'seagreen',alpha=1)
plt.tick_params(axis='both', which='both',length=0)
plt.xlim(xmin=0, xmax=110)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Age distribution', fontsize=20)



