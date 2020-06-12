from bokeh_graph import *
from matplotlib_polynomial import *

# Reads excel-file into a variable for Bokeh plot.
data_year = Graph('data/crossings_and_remittance_per_year.xlsx')

# Insert desired x-axis, y-axis and twin y-axis to plot graph.
data_year.linear_axis("year", "people", "money")

# Insert dataset for Matplotlib plot, make sure x-axis is first column and y-axis is last column.
data_month = Polynomial('data/crossing_remittance_by_month.xlsx')
data_year_reg = Polynomial('data/crossings_per_year.xlsx')

# Functions plotting data.
data_month.polynomial_axis()
data_year_reg.polynomial_axis()
