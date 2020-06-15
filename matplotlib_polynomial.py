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

    def polynomial_axis(self, title, const_number):
        x = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, -1].values

        # Callback.
        train_test_visualize(x, y, title, const_number)


def dice(y_array_length):
    # List for appending random numbers and numpy array for converting before returning array.
    dice_list_array = []
    dice_array = np.array

    # Counter.
    i = 0

    # Convert random numbers to six numbers in between -1 and 1
    while i < y_array_length:
        dice_six_sided = np.random.randint(1, 7)
        if dice_six_sided == 1:
            dice_list_array.append(-1)
        elif dice_six_sided == 2:
            dice_list_array.append(-0.6)
        elif dice_six_sided == 3:
            dice_list_array.append(-0.2)
        elif dice_six_sided == 4:
            dice_list_array.append(0.2)
        elif dice_six_sided == 5:
            dice_list_array.append(0.6)
        else:
            dice_list_array.append(1)
        i += 1
        dice_array = np.array(dice_list_array)

    return dice_array


def train_test_visualize(x, y, title, const_number):
    # Random numbers in between -1 and 1.
    random_number = np.random.uniform(low=-1, high=1, size=len(y))

    # Constant.
    const_number = const_number

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
    r_2_score = r2_score(y_test, y_pred)

    # regressor to new variable.
    y_reg = regressor.predict(poly_reg.fit_transform(x))

    # Creates a new array of y-values with random numbers.
    y_error = random_number * const_number
    y_deviation = y_reg + random_number * const_number
    y_dice_reg = y_reg + dice(len(y)) * const_number

    # Visualizing results of the polynomial regression with subplots.
    plt.suptitle("Border Crossings - " + title + " - Polynomial, R2: " + str(r_2_score))
    plt.title(r2_score(y_test, y_pred))

    # Dataset.
    plt.subplot(231)
    plt.plot(x, y, color='red')
    plt.xlabel('Year')

    # Trained dataset regression.
    plt.subplot(232)
    plt.plot(x, y, color='red')
    plt.plot(x, y_reg, color='green')
    plt.xlabel('Year')

    # Dataset with random deviation (0 - 10000000).
    plt.subplot(233)
    plt.plot(x, y, color='red')
    plt.plot(x, y_deviation, color='purple')
    plt.xlabel('Year')

    # Data set with error bars random deviation (0 - 10000000).
    plt.subplot(234)
    plt.plot(x, y, color='red')
    plt.errorbar(x, y, yerr=y_error, fmt='o', ecolor="black", capsize=3, alpha=0.5)
    plt.xlabel('Year')

    # Data set with random deviation by dice.
    plt.subplot(235)
    plt.plot(x, y, color='red')
    plt.plot(x, y_dice_reg, color='yellow')
    plt.xlabel('Year')

    # Plot graph.
    plt.show()
