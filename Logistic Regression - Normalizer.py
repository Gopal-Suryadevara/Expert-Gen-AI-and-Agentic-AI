import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"F:\Gen AI & Agentic AI\Gen AI - Jan\Session 45 - Jan 28\logit classification.csv")

x = dataset.iloc[:, [2,3]] #independent attribute
y = dataset.iloc[:, -1] #dependent attribute

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state=0)

from sklearn.preprocessing import Normalizer 
nr = Normalizer()
x_train = nr.fit_transform(x_train)
x_test = nr.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print (ac)

from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)

bias = classifier.score(x_train, y_train)
print(bias)

variance = classifier.score(x_test, y_test)
print(variance)