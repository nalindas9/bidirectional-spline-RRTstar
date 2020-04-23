import numpy as np
import math


# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node, clearance):
  offset = 5.1
  # Checking if point inside map
  if node[0] + clearance >= 10.1-offset or node[0] - clearance <= 0.1-offset  or node[1] + clearance >= 10.1-offset  or node[1] - clearance <= 0.1-offset :
    print('Sorry the point is out of bounds! Try again.')
    return False
  # Checking if point inside squares
  elif node[0] + clearance >= 3.0-offset  and node[0] - clearance <=4.5-offset  and node[1] + clearance>= 0.0-offset  and node[1] - clearance< 3.0-offset :
    print('Sorry the point is in the square 1 obstacle space! Try again')
    return False
  elif node[0] + clearance >= 0.0-offset  and node[0] - clearance <= 3.0-offset  and node[1] + clearance>= 3.5-offset  and node[1] - clearance <= 5.0-offset :
    print('Sorry the point is in the square 2 obstacle space! Try again')
    return False
  elif node[0] + clearance >= 6.0-offset  and node[0] - clearance <= 9.0-offset  and node[1] + clearance>= 2.0-offset  and node[1] - clearance <= 3.5-offset :
    print('Sorry the point is in the square 3 obstacle space! Try again')
    return False
  else:
    return True   

