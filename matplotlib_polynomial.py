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
    # random numbers in between -1 and 1
    y_random = np.random.uniform(low=-1, high=1, size=len(y))

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

    # Refactor, 1 betyder - 1.0, 2 betyder -0.6, 3 betyder -0.2, 4 betyder +0.2, 5 betyder +0.6, 6 betyder +1
    # snurrar ett roulette hjul 1000 gånger
    # för statisktik på vilka nummer ni får... blir de jämt fördelade? Om man kastar tärningen 100000 gånger?
    # om man snurrar rouletten 1 miljon gånger

    xyz = regressor.predict(poly_reg.fit_transform(x))
    a = xyz + (y_random * 5000000)
    standard_deviation = xyz.std()
    print(y_random)
    print(y)
    print(xyz)
    print(standard_deviation)

    # Visualising the Polynomial Regression results
    plt.plot(x, y, color='red')
    plt.plot(x, a, color='blue')
    plt.suptitle('R2: ' + str(r2_score(y_test, y_pred)))
    plt.title('Border Remittance Polynomial')
    plt.xlabel('Year')
    plt.ylabel('Money Remittance')
    plt.show()
