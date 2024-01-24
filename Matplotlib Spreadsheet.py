"""
Matplotlib Spreadsheet
@author: Caitlin Miller
"""
import matplotlib.pyplot as mat
import numpy

# The variables below represnt the x (absorbance of caffeine), and the y (concentration of caffeine) axes
C = numpy.array([4, 8, 12, 16, 20])
A = numpy.array([0.150, 0.386, 0.353, 0.501, 0.580])

# Creates a scatter plot from the following data points above
mat.scatter(C, A, color='orange', s=50)

# Finds a best-fit line for the data
slope, intercept = numpy.polyfit(C, A, 1)

# Plots the linear fit line
mat.plot(C, slope*C + intercept, color='green', linewidth=2)

# Labels the y and x axes, and give a plot title
mat.ylabel('C(mg/L)')
mat.xlabel('Absorbance')
mat.title('Absorbance vs Concentration of caffeine (230nm peak)')
# Shows the plot
mat.show()

#prints the extinction coefficient for the caffeine at absorbance of 230nm
print(" ε=",slope,"intercept=",intercept)
