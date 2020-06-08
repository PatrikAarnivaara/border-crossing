import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import column


class Graph:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_excel(filepath)

    def linear_axis(self, x, y):
        x = self.data[x]
        y = self.data[y]

        # prepare the output file
        output_file("line_from_excel.html")

        # random value in range

        # create a figure object
        f1 = figure()
        f2 = figure()

        # create a line plot
        f1.line(x, y)
        f2.line(x, y)

        # write the graph in the figure object
        show(column(f1, f2))
