#!/usr/bin/env python3
"""
Utility Functions

Reference: Spline module taken from Author: Atsushi Sakai(@Atsushi_twi)
(https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/CubicSpline/cubic_spline_planner.py)

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import numpy as np
import math
from scipy import interpolate
import spline
import matplotlib.pyplot as plt

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

def cubic_spline(points):
  x_pts = [x[0] for x in points]
  y_pts = [x[1] for x in points]
  ds = 0.01
  sp = spline.Spline2D(x_pts, y_pts)
  s = np.arange(0, sp.s[-1], ds)
  rx, ry, ryaw, rk = [], [], [], []
  for i_s in s:
    ix, iy = sp.calc_position(i_s)
    rx.append(ix)
    ry.append(iy)
    ryaw.append(sp.calc_yaw(i_s))
    rk.append(sp.calc_curvature(i_s))
  plt.plot(x_pts, y_pts, "xb", label="input")
  plt.plot(rx, ry, "-r", label="spline")
  spline_pts = tuple(zip(rx,ry))
  return spline_pts 
  
def quaternion_to_euler(w, x, y, z):
  """Converts quaternions with components w, x, y, z into a tuple (roll, pitch, yaw)"""
  sinr_cosp = 2 * (w * x + y * z)
  cosr_cosp = 1 - 2 * (x**2 + y**2)
  roll = np.arctan2(sinr_cosp, cosr_cosp)

  sinp = 2 * (w * y - z * x)
  pitch = np.where(np.abs(sinp) >= 1,
               np.sign(sinp) * np.pi / 2,
               np.arcsin(sinp))

  siny_cosp = 2 * (w * z + x * y)
  cosy_cosp = 1 - 2 * (y**2 + z**2)
  yaw = np.arctan2(siny_cosp, cosy_cosp)

  return roll, pitch, yaw
  
  
