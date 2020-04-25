"""
Utility Functions

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import numpy as np
import math


# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node, clearance):
  # Checking if point inside map
  if node[0] + clearance >= 5 or node[0] - clearance <= -5  or node[1] + clearance >= 5 or node[1] - clearance <= -5 :
    print('Sorry the point is out of bounds! Try again.')
    return False
  # Checking if point inside circles
  elif (node[0] - (-2) ) ** 2 + (node[1] - (-3)) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 1 obstacle space! Try again')
    return False
  elif (node[0]) ** 2 + (node[1]) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 2 obstacle space! Try again')
    return False
  elif (node[0] - 2) ** 2 + (node[1] - (-3)) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 3 obstacle space! Try again')
    return False
  elif (node[0] - (2)) ** 2 + (node[1] - (3)) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 4 obstacle space! Try again')
    return False
  # Checking if point inside squares
  elif node[0]  >= -4.75 - clearance  and node[0] <= -3.25 + clearance and node[1] >= -0.75 - clearance  and node[1]  <= 0.75 + clearance :
    print('Sorry the point is in the square 1 obstacle space! Try again')
    return False
  elif node[0]  >= -2.75 - clearance  and node[0] <= -1.25 + clearance and node[1] >= 2.25 - clearance  and node[1]  <= 3.75 + clearance :
    print('Sorry the point is in the square 2 obstacle space! Try again')
    return False
  elif node[0]  >= 3.25 - clearance  and node[0] <=  4.75 + clearance and node[1] >= -0.75 - clearance  and node[1]  <= 0.75 + clearance:
    print('Sorry the point is in the square 3 obstacle space! Try again')
    return False
  else:
    return True   
  
