from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

data = pd.read_excel('data/crossings_per_year.xlsx')

# add comment here, create class?
x = data["year"]
y = data["people_crossing_by_year"]

# prepare the output file
output_file("line_from_excel.html")

# create a figure object
f = figure()

# create a line plot
f.line(x, y)

# write the graph in the figure object
show(f)

# print(data)
