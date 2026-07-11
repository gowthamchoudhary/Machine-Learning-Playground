
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("ronaldo_mock_match_dataset.csv")
df.head()

print(df["Competition"].value_counts())

df = pd.get_dummies(df, columns=["Competition"], dtype=int)

X = df.drop("Goals",axis=1)
Y = df["Goals"]

"""lets split the data"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,Y_train)

print(model.intercept_)
print(model.coef_)

coefficients = pd.DataFrame(
    {
        "Features":X.columns,
        "Coefficients":model.coef_
    }
)
print(coefficients)

y_pred = model.predict(X_test)
print(y_pred.shape)

print(X_train.shape)
print(X_test.shape)

print(Y_train.shape)
print(Y_test.shape)

comparison = pd.DataFrame({
    "Actual Goals": Y_test,
    "Predicted Goals": y_pred
})


comparison["Error"] = (comparison["Actual Goals"] - comparison["Predicted Goals"]).abs()
print(comparison.head(10))
MAE = comparison["Error"].mean()
print("Mean Absolute Error (MAE):", MAE)

plt.figure(figsize=(6,6))
plt.scatter(Y_test,y_pred)
plt.title("Goal Record")
plt.xlabel("Actual Goals")
plt.ylabel("Predicted Goals")
plt.grid(True, linestyle='-', alpha=1)
plt.show()

