import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(x)
print(y)

# prepare the output file
output_file("line.html")

# create a figure object
f = figure()

# create a line plot
f.line(x, y)

print("Border Crossing")

# Testing
with open("./data/wonderland.txt", 'r') as crossings:
    lines = crossings.readlines()
for line in lines:
    print(line, end='')

# # prepare some data
# df = pd.read_excel("/data/crossings_per_year.xlsx")
# x = df["month"]
# y = df["people_crossing_by_month"]
#
# # prepare the output file
# output_file("line_from_excel.html")
#
# # create a figure object
# f = figure()
#
# # create a line plot
# f.line(x, y)
#
# # write the graph in the figure object
# show(f)
