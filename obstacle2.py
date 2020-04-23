import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Plotting the final map

fig = plt.figure()

plt.axes()
plt.xlim(0, 100)
plt.ylim(0, 100)

square1 = plt.Rectangle((30, 0), width=15, height=30, facecolor= 'black')
square2 = plt.Rectangle((0, 35), width=30, height=15, facecolor= 'black')
square3 = plt.Rectangle((60, 20), width=30, height=15, facecolor= 'black')


plt.gca().add_patch(square1)
plt.gca().add_patch(square2)
plt.gca().add_patch(square3)
plt.axis("scaled")


#plt.grid(color='lightgray',linestyle='--')
plt.show()
