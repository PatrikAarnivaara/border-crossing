import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


class Polynomial:

    def __init__(self, filepath):
        self.filepath = filepath
        self.dataset = pd.read_excel(filepath)

    def polynomial_axis(self):
        x = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, -1].values

        # Insert x and y
        train_test_visualize(x, y)


def train_test_visualize(x, y):

    # Split dataset into Train and Test set
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

    # Train the Polynomial model on Training set
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X_train)
    regressor = LinearRegression()
    regressor.fit(X_poly, y_train)

    # Predicting Test result
    y_pred = regressor.predict(poly_reg.transform(X_test))
    np.set_printoptions(precision=2)

    # Evaluate the R2-value of model
    print(r2_score(y_test, y_pred))

    # Visualising the Polynomial Regression results
    plt.plot(x, y, color='red')
    plt.scatter(x, regressor.predict(poly_reg.fit_transform(x)), color='blue')
    plt.suptitle('R2: ' + str(r2_score(y_test, y_pred)))
    plt.title('Border Remittance Polynomial')
    plt.xlabel('Year')
    plt.ylabel('Money Remittance')
    plt.show()
