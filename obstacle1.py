import matplotlib.pyplot as plt
import numpy as np
from math import pi
from matplotlib.patches import Ellipse

# Plotting the final map

fig = plt.figure()
plt.axes()
plt.xlim(0, 100)
plt.ylim(0, 100)
circle1 = plt.Circle((50, 50), radius=20, facecolor = 'black')
circle2 = Ellipse((15, 25), width=15, height= 10, angle=0, facecolor = 'black')
circle3 = Ellipse((80, 30), width=15, height= 10, angle=0, facecolor = 'black')


plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.axis("scaled")


plt.grid(color='lightgray',linestyle='--')
plt.show()
