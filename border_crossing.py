from graph import *
from polynomial import *

# reads excel-file into a variable
data_year = Graph('data/crossings_per_year.xlsx')

# insert desired x-axis and y-axis to plot graph
data_year.linear_axis("year", "people_crossing_by_year")

# insert dataset with x-axis as first column and y-axis as last column
data_month = Polynomial('data/crossing_remittance_by_month.xlsx')

# insert polynomial degree
data_month.polynomial_axis(18)


# TODO:
# test different excel-files
# try catch error handling
# add input so user can choose file and x and y axis
