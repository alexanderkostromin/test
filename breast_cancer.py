# -*- coding: utf-8 -*-
"""Breast Cancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lEWtcOb7F1569UrFmRYjQYgWpv4HGe4d
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

"""### Reading our dataset and dropping junk columns"""

df = pd.read_csv("data.csv")
df.drop(['id','Unnamed: 32'], axis=1, inplace=True)
df.head()

"""### Split the features data and the target """

#Мы будет использовать только эти колонки для обучения
cols = ['concave points_mean','area_mean','radius_mean','perimeter_mean','concavity_mean']

X = df[cols]
y = df['diagnosis']

# Encoding the target value 
y = np.asarray([1 if c == 'M' else 0 for c in y])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=43)
# Разделение данных на обучающую и тестовую выборки

print('Shape training set: X:{}, y:{}'.format(X_train.shape, y_train.shape))
print('Shape test set: X:{}, y:{}'.format(X_test.shape, y_test.shape))

"""### Training Random Forest"""

rfc = RandomForestClassifier()
# Создаем объект класса классификатора случайного леса

rfc.fit(X_train, y_train)
# Выполняем подгонку модели

y_pred = rfc.predict(X_test)
# Предсказываем значения, основываясь на тестовых данных

print('Accuracy : {}'.format(accuracy_score(y_test, y_pred)*100))
# Значение точности модели, процент совпадения истинных и предсказанных значений

"""### Checking Feature Importances"""

f_importance = pd.DataFrame(rfc.feature_importances_*100,index=cols,columns=['Importance'])
f_importance.sort_values(by='Importance',ascending=False,inplace=True)
f_importance

clf_report = classification_report(y_test, y_pred)
print('Classification report')
print(clf_report)

conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)

"""### Saving the model"""

joblib.dump(rfc,"../models/cancer_model.pkl")