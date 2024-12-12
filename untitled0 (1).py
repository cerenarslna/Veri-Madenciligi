# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bPVXwI3bwr8l6Nyz5Ri5YNZA-HcIZeZ5
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir('/content/drive/My Drive/verimadenciligi/hafta5')
!pwd

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('iris.csv')
df.head()

sns.countplot(x=df['species'])
plt.title("barplot")

plt.scatter(df['petal_length'],df['petal_width'],color='blue')
plt.title('iki değişkenli analiz')
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.show()

plt.figure(figsize=(10,10))
sns.scatterplot(x=df['petal_length'],y=df['petal_width'], marker='s', hue=df['species'])