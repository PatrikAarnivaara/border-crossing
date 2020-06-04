from ploter import *
from polynomial import *

# reads excel-file into a variable
data_year = Linear('data/crossings_per_year.xlsx')

# insert desired x-axis and y-axis to plot graph
data_year.linear_axis("year", "people_crossing_by_year")

data_month = Polynomial('data/crossing_remittance_by_month.xlsx')




# TODO:
# test different excel-files
# try catch error handling
# add input so user can choose file and x and y axis
