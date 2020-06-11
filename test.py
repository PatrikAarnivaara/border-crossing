# Import libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# % matplotlib notebook

# First dataset
City_A = [36, 37, 36, 34, 39, 33, 30, 30, 32, 31, 31, 32, 32, 33, 35]

# Second dataset
City_B = [41, 35, 28, 29, 25, 36, 36, 32, 38, 40, 40, 34, 31, 28, 30]

# Caluclate the mean of datasets
Mean_City_A = np.mean(City_A)
Mean_City_B = np.mean(City_B)

# Caluclate the standard deviation of datasets
STDV_City_A = np.std(City_A)
STDV_City_B = np.std(City_B)

# Create a figure with customized size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Set the axis lables
ax.set_xlabel('Day', fontsize=18)
ax.set_ylabel('Temperature', fontsize=18)

# X axis is day numbers from 1 to 15
xaxis = np.array(range(1, 16))

# Line color for error bar
color_City_A = 'red'
color_City_B = 'darkgreen'

# Line style for each dataset
lineStyle_City_A = {"linestyle": "--", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}
lineStyle_City_B = {"linestyle": "-", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}

# Create an error bar for each dataset
line_City_A = ax.errorbar(xaxis, City_A, yerr=STDV_City_A, **lineStyle_City_A, color=color_City_A, label='City A')
line_City_B = ax.errorbar(xaxis, City_B, yerr=STDV_City_B, **lineStyle_City_B, color=color_City_B, label='City B')

# Label each dataset on the graph, xytext is the label's position
for i, txt in enumerate(City_A):
    ax.annotate(txt, xy=(xaxis[i], City_A[i]), xytext=(xaxis[i] + 0.03, City_A[i] + 0.3), color=color_City_A)

for i, txt in enumerate(City_B):
    ax.annotate(txt, xy=(xaxis[i], City_B[i]), xytext=(xaxis[i] + 0.03, City_B[i] + 0.3), color=color_City_B)

# Draw a legend bar
plt.legend(handles=[line_City_A, line_City_B], loc='upper right')

# Customize the tickes on the graph
plt.xticks(xaxis)
plt.yticks(np.arange(20, 47, 2))

# Customize the legend font and handle length
params = {'legend.fontsize': 13,
          'legend.handlelength': 2}
plt.rcParams.update(params)

# Customize the font
font = {'family': 'Arial',
        'weight': 'bold',
        'size': 12}
matplotlib.rc('font', **font)

# Draw a grid for the graph
ax.grid(color='lightgrey', linestyle='-')
ax.set_facecolor('w')

plt.show()
