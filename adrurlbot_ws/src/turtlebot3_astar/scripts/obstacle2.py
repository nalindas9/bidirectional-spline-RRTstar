#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Plotting the final map

fig = plt.figure()
plt.axes()
plt.xlim(-5.1, 5.1)
plt.ylim(-5.1, 5.1)
offset = 5.1

square1 = plt.Rectangle((3.0-offset, 0-offset), width=1.5, height=3.0, facecolor="black")
square2 = plt.Rectangle((0.0-offset, 3.5-offset), width=3.0, height=1.5, facecolor="black")
square3 = plt.Rectangle((6.0-offset, 2-offset), width=3.0, height=1.5, facecolor="black")
inner_wall = plt.Rectangle((0.1-offset, 0.1-offset), width=10, height=10, fill=False)
outer_wall = plt.Rectangle((0-offset, 0-offset), width=10.2, height=10.2, fill=False)


plt.gca().add_patch(square1)
plt.gca().add_patch(square2)
plt.gca().add_patch(square3)
plt.gca().add_patch(inner_wall)
plt.gca().add_patch(outer_wall)
plt.axis("scaled")


#plt.grid(color='lightgray',linestyle='--')
plt.show()
