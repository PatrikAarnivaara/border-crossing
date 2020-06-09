from graph import *
from polynomial import *

# reads excel-file into a variable
data_year = Graph('data/crossings_and_remittance_per_year.xlsx')

# insert desired x-axis and y-axis to plot graph
data_year.linear_axis("year", "people", "money")

# insert dataset with x-axis as first column and y-axis as last column
data_month = Polynomial('data/crossing_remittance_by_month.xlsx')

# insert polynomial degree
data_month.polynomial_axis()

