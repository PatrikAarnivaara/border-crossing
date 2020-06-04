import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def polynomial_axis(dataset):
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    # Split dataset into Train and Test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    # Train the Polynomial model on Training set
    poly_reg = PolynomialFeatures(degree=16)
    x_poly = poly_reg.fit_transform(x_train)
    regressor = LinearRegression()
    regressor.fit(x_poly, y_train)

    # Predicting Test result
    y_pred = regressor.predict(poly_reg.transform(x_test))
    np.set_printoptions(precision=2)

    # Evaluate the model
    print(r2_score(y_test, y_pred))

    # Visualising the Polynomial Regression results
    plt.plot(x, y, color='red')
    plt.plot(x, regressor.predict(poly_reg.fit_transform(x)), color='blue')
    plt.suptitle('R2: ' + str(r2_score(y_test, y_pred)))
    plt.title('Border Remittance Polynomial')
    plt.xlabel('Year')
    plt.ylabel('Money Remittance')
    plt.show()


class Polynomial:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_excel(filepath)
