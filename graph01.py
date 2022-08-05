import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
ax.plot([1,2,3,4,5,6,7,8,9,10],[10,23,34,21,35,14,38,27,39,45],'ro')
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
plt.show()