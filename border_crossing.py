from ploter import *

# reads excel-file into variable data
data_year = Plot('data/crossings_per_year.xlsx')

# insert x-axis and y-axis to plot graph
data_year.axis("year", "people_crossing_by_year")
