import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load data
data = pd.read_csv('taxi.csv')
# print(data.head())

# split data into target/ouput and feature/input variable means independent and dependent varible

data_x = data.iloc[:, 0:-1]  # -1 exclude the last columns
# print(data_x)

data_y = data.iloc[:, -1]  # -1 include the last column only
# print(data_y)

# split the data into traing and testing data

X_train, X_test, y_train, y_test = train_test_split(
    data_x, data_y, test_size=0.3, random_state=0)

# calling linear regression
reg = LinearRegression()
reg.fit(X_train, y_train)

print("Train Score:", reg.score(X_train, y_train))
print("Test Score:", reg.score(X_test, y_test))

# create a model which is used in  development
pickle.dump(reg, open('taxi.pkl', 'wb'))

model = pickle.load(open('taxi.pkl', 'rb'))


# testing result 80, 1770000, 6000, 85 this are the input value

print(model.predict([[80, 1770000, 6000, 85]]))
