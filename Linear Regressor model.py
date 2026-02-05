import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"F:\Gen AI & Agentic AI\Gen AI - Jan\Session 38 - Jan 20\Salary_Data.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, train_size=0.8,random_state=0)

from sklearn.linear_model import LinearRegression # LinearRegression is algoritham
regressor = LinearRegression() #regressor is model
regressor.fit(x_train, y_train) #regressor model is applied on the x_train and y_train to fit

y_pred = regressor.predict(x_test)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color ='blue')
plt.title('salary vs experience (Test set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

print(regressor)

m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)

emp_15 = m_slope*15 + c_intercept
print(emp_15)

emp_20 = m_slope*20+ c_intercept
print(emp_20)

