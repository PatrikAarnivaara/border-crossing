from ploter import *

# reads file into variable data
data_year = Plot('data/crossings_per_year.xlsx')

# x-axis plots year, y-axis plots sum of people per year
data_year.axis("year", "people_crossing_by_year")
