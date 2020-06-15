from bokeh_graph import *
from matplotlib_polynomial import *

# Reads excel-file into a variable for Bokeh plot.
data_year = Graph('data/crossings_per_year_people_and_money.xlsx')

# Insert desired x-axis, y-axis and twin y-axis to plot graph.
data_year.linear_axis("year", "people", "money")

# Insert dataset for Matplotlib plot, make sure x-axis is first column and y-axis is last column.
# data_month = Polynomial('data/crossings_per_month_money.xlsx')
data_year_people = Polynomial('data/crossings_per_year_people.xlsx')
data_year_money = Polynomial('data/crossings_per_year_money.xlsx')


# Functions plotting data.
# data_month.polynomial_axis()
data_year_people.polynomial_axis("People", 10000000)
data_year_money.polynomial_axis("Money", 1000000000)
