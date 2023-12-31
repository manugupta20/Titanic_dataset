# -*- coding: utf-8 -*-
"""Copy of Prediction Titanic Data

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CBnw2kH3GO0NgRVh0lqvZ25hUGynsmLW
"""



"""# DATA PREPROCCESING"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv("/content/train.csv")
df_test = pd.read_csv("/content/test.csv")

df_train.head(10)

df_train.info()

df_train.describe()

df_train.columns

l1 = ['PassengerId', 'Name','Ticket' ]

df_train.drop(l1, axis = 1, inplace= True)
df_test.drop(l1, axis = 1, inplace= True)

df_train.head()

df_train.nunique()

df_train['Embarked']. unique()

df_train.isnull()

df_train.isnull().sum()

df_train.shape

l2 = ['Cabin']
df_train.drop(l2, axis = 1, inplace= True)
df_test.drop(l2, axis = 1, inplace= True)

df_train.head()

df_train["Age"]

df_train['Age'].mean()

df_train['Age'].fillna(df_train['Age'].mean(), inplace = True)
df_test['Age'].fillna(df_test['Age'].mean(), inplace = True)

df_train.isnull().sum()

df_train['Embarked'].mode()

df_train.dropna(inplace= True)
df_test.dropna(inplace= True)

df_train.isnull().sum()

df_test.isnull().sum()

df_train.head()

df_train[df_train['Survived'] == 1]

df_train[df_train['Survived'] == 1]['Sex'] #specific column

def graph(s) :
    sur = df_train[df_train['Survived'] == 1][s].value_counts()
    passed = df_train[df_train['Survived'] == 0][s].value_counts()

    df = pd.DataFrame([sur , passed])
    df.plot(kind = 'bar')
    #print(df.head()) #for print value

graph("Sex")

df_train[df_train['Survived'] == 1]['Sex']. value_counts()

graph("Embarked")

df_train.columns

graph("SibSp")

"""# Lable Encoding

"""

df_train.head()

from sklearn.preprocessing import LabelEncoder
le_S = LabelEncoder()
le_E = LabelEncoder()

df_train['Sex'] = le_S.fit_transform(df_train['Sex'])
df_train['Embarked'] = le_E.fit_transform(df_train['Embarked'])

df_train.head()

df_test['Sex'] = le_S.transform(df_test['Sex'])
df_test['Embarked'] = le_E.transform(df_test['Embarked'])

df_test.head()

df_train.head()

le_S.classes_

le_E.classes_

X_train = df_train.iloc[:, 1: ].values
Y_train = df_train.iloc[:, 0 ].values
X_test = df_test.values

X_train.shape, Y_train.shape, type(X_train)

print(X_train[:10, :])

from sklearn.preprocessing import StandardScaler
scale_x = StandardScaler()
X_train = scale_x.fit_transform(X_train)
X_test = scale_x.fit_transform(X_test)

X_train[:10, :]

"""#Model Filting"""

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()
clf.fit(X_train, Y_train)

pred = clf.predict(X_train)

pred[:10], Y_train[:10]

(pred == Y_train).sum()/pred.shape

Y_train.shape, pred.shape

