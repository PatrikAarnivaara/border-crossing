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

        # Function callback.
        train_test_visualize(x, y)


def train_test_visualize(x, y):
    # Random numbers in between -1 and 1.
    random_number = np.random.uniform(low=-1, high=1, size=len(y))

    # Split dataset into train and test set.
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

    # Train the polynomial model on training set.
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X_train)
    regressor = LinearRegression()
    regressor.fit(X_poly, y_train)

    # Predicting test results.
    y_pred = regressor.predict(poly_reg.transform(X_test))
    np.set_printoptions(precision=2)

    # Evaluate the R2-value of model.
    print(r2_score(y_test, y_pred))

    # Extra random generator based on a six-sided dice.
    # Refactor, 1 betyder - 1.0, 2 betyder -0.6, 3 betyder -0.2, 4 betyder +0.2, 5 betyder +0.6, 6 betyder +1
    # Implement roulette wheel one million times statistic on spread of numbers, how?

    # Creates a new array with random numbers.
    y_reg = regressor.predict(poly_reg.fit_transform(x))
    y_deviation = y_reg + (random_number * 5000000)
    standard_deviation = y_reg.std()

    # Print arrays and random number.
    print(y)
    print(y_reg)
    print(random_number)
    print(standard_deviation)

    # Visualizing results of the polynomial regression.
    plt.plot(x, y, color='red')
    plt.plot(x, y_deviation, color='blue')
    plt.plot(x, y_reg, color='green')
    plt.suptitle('R2: ' + str(r2_score(y_test, y_pred)))
    plt.title('Border Remittance Polynomial')
    plt.xlabel('Year')
    plt.ylabel('Money Remittance')
    plt.show()
