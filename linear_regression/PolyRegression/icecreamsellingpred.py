
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score,mean_squared_error

"""Load the dataset"""

data = pd.read_csv("Ice_cream selling data.csv")
data.head()

data.tail()

data.info()

data.describe()

data.isnull().sum()

X=data["Temperature (°C)"]
Y=data.drop("Temperature (°C)",axis=1)
Y

sns.pairplot(data)
plt.show()

X_test,X_train,Y_test,Y_train = train_test_split(X,Y,test_size=0.25,random_state=42)
X_test.min()

poly = PolynomialFeatures(degree = 2)
X_train_poly = poly.fit_transform(X_train.values.reshape(-1,1))
X_test_poly = poly.transform(X_test.values.reshape(-1,1))
model = LinearRegression()
model.fit(X_train_poly,Y_train)
Y_predict = model.predict(X_test_poly)
r2_score(Y_test,Y_predict)

X_grid = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
X_grid_poly = poly.transform(X_grid)
plt.scatter(X,Y)
plt.plot(X_grid, model.predict(X_grid_poly), color='red')
plt.xlabel("Temperature")
plt.ylabel("Revenue")
plt.show()

