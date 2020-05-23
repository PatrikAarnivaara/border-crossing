from ploter import *

# reads excel-file into a variable
data_year = Plot('data/crossings_per_year.xlsx')

# insert desired x-axis and y-axis to plot graph
data_year.axis("year", "people_crossing_by_year")

# TODO:
# test different excel-files
# try catch error handling
# add input so user can choose file and x and y axis
