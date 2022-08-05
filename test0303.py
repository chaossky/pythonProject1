import numpy as np
from scipy.interpolate import splprep, splev
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

N = 500
t = np.linspace(0, 80 * np.pi, N)
r = 0.01*t
x, y = r *np.cos(t), r * np.sin(t)
#x,y=r*np.cos(t),r*r*np.sin(t)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()