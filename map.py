"""
Map Definition for A* Algorithm

Authors:
-Nidhi Bhojak
-Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Plotting the final map

fig = plt.figure()
plt.axes()
plt.xlim(-5.1, 5.1)
plt.ylim(-5.1, 5.1)
offset = 5.1
circle1 = plt.Circle((3.1-offset, 2.1-offset), radius=1, fill=False, ec="red")
circle2 = plt.Circle((7.1-offset, 2.1-offset), radius=1, fill=False, ec="red")
circle3 = plt.Circle((5.1-offset, 5.1-offset), radius=1, fill=False, ec="red")
circle4 = plt.Circle((7.1-offset, 8.1-offset), radius=1, fill=False, ec="red")
square1 = plt.Rectangle((2.35-offset, 7.35-offset), width=1.5, height=1.5, fill=False, ec="red")
square2 = plt.Rectangle((0.35-offset, 4.35-offset), width=1.5, height=1.5, fill=False, ec="red")
square3 = plt.Rectangle((8.35-offset, 4.35-offset), width=1.5, height=1.5, fill=False, ec="red")
inner_wall = plt.Rectangle((0.1-offset, 0.1-offset), width=10, height=10, fill=False)
outer_wall = plt.Rectangle((0-offset, 0-offset), width=10.2, height=10.2, fill=False)

plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.gca().add_patch(circle4)
plt.gca().add_patch(square1)
plt.gca().add_patch(square2)
plt.gca().add_patch(square3)
plt.gca().add_patch(inner_wall)
plt.gca().add_patch(outer_wall)
plt.axis("scaled")


plt.grid(color='lightgray',linestyle='--')

