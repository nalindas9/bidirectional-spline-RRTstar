"""
RRT* for Non-Holonomic Mobile Robot

Authors:
-Nidhi Bhojak
-Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import map
import matplotlib.pyplot as plt
import numpy as np
import utils

def main():
  # Taking inputs from the user
  clearance = eval(input('Please enter the clearance value of the robot from the obstacle:'))
  print('The clearance value you entered is:', clearance)
  print('')
  start_point = eval(input('Please enter the start coordinates for the robot in this format - [X_coord, Y_coord, Theta]:'))
  while not utils.check_node(start_point, clearance):
    start_point = eval(input('Please enter the start coordinates in this format - [X_coord, Y_coord, Theta]:'))
  start_circle = plt.scatter(start_point[0], start_point[1], c = 'b')
  print('The start point you entered is:', start_point)
  print('')  
  goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord]:'))
  while not utils.check_node(goal_point, clearance):
    goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord]:'))
  goal_circle = plt.scatter(goal_point[0], goal_point[1], c = 'y')
  print('The goal point you entered is:', goal_point)
  print('')
  goal_circle = plt.Circle((goal_point[0], goal_point[1]), radius= 0.25,fill=False)
  plt.gca().add_patch(goal_circle)
  rpm = eval(input('Please enter the RPM for both the wheels in this format - [RPM1,RPM2]:'))
  print("The wheel RPM's you entered for both the wheels are:", rpm)
  print('')

  plt.show()
  plt.close()
  
if __name__ == '__main__':
  main()
