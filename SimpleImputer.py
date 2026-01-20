import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = pd.read_csv(r"F:\Gen AI & Agentic AI\Gen AI - Jan\Session 37 - Jan 19\12th, 19th - ML\5. Data preprocessing\Data.csv")

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer()
#imputer = SimpleImputer(strategy='median') -- changing from mean to median

imputer=imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
