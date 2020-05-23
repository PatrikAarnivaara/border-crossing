from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd


class Plot:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_excel(filepath)

    def axis(self, x, y):
        x = self.data[x]
        y = self.data[y]

        # prepare the output file
        output_file("line_from_excel.html")

        # create a figure object
        f = figure()

        # create a line plot
        f.line(x, y)

        # write the graph in the figure object
        show(f)
