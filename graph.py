import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import Range1d, LinearAxis
from bokeh.plotting import figure


class Graph:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_excel(filepath)

    def linear_axis(self, x, y, y2):
        x = self.data[x]
        y = self.data[y]
        y2 = self.data[y2]

        # prepare the output file
        output_file("legend_labels.html")

        # create a figure object
        f = figure(title='Border Crossings - People and Money', y_range=(300000000, 380000000))
        f.extra_y_ranges = {"y2": Range1d(start=20000000000, end=40000000000)}
        f.add_layout(LinearAxis(y_range_name="y2", axis_label="Money"), 'right')

        # create a line plot
        f.line(x, y, legend_label="people", color="red")
        f.line(x, y2, legend_label="money", color="green", y_range_name="y2")
        f.xaxis.axis_label = "Year"
        f.legend.location = "bottom_right"

        # write the graph in the figure object
        show(f)
