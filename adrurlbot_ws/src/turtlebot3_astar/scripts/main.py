#!/usr/bin/env python3
"""
RRT* for Non-Holonomic Mobile Robot

Authors:
-Nidhi Bhojak
-Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import map
import algo
import matplotlib.pyplot as plt
import numpy as np
import utils
import copy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist
from math import atan2
import math
import rospy
import time

x = 0
y = 0
theta = 0

def main():
  rospy.init_node('Adrurlbot_vel_publisher', anonymous=True)
  r = rospy.Rate(4)
  def odom_callback(msg):
    global x
    global y
    global theta
 
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
 
    rot_q = msg.pose.pose.orientation
    #(roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    (roll, pitch, theta) = utils.quaternion_to_euler(rot_q.w, rot_q.x, rot_q.y, rot_q.z)
  sub = rospy.Subscriber("/odom", Odometry, odom_callback)
  pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
  vel_msg = Twist()
  # Taking inputs from the user
  time.sleep(2)
  print('')
  print("************************* Let's move the turtlebot! *******************************")
  print('')
  clearance = eval(input('Please enter the clearance value of the robot from the obstacle:'))
  print('The clearance value you entered is:', clearance)
  print('')
  start_point = eval(input('Please enter the start coordinates for the robot in this format - [X_coord, Y_coord, Theta]:'))
  while not utils.check_node(start_point, clearance):
    start_point = eval(input('Please enter the start coordinates in this format - [X_coord, Y_coord, Theta]:'))
  start_circle = plt.scatter(start_point[0], start_point[1], c = 'b')
  print('The start point you entered is:', start_point)
  print('')  
  goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord, Theta]:'))
  while not utils.check_node(goal_point, clearance):
    goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord, Theta]:'))
  goal_circle = plt.scatter(goal_point[0], goal_point[1], c = 'y')
  print('The goal point you entered is:', goal_point)
  print('')
  goal_circle = plt.Circle((goal_point[0], goal_point[1]), radius= 0.25,fill=False)
  plt.gca().add_patch(goal_circle)
  
  explored1, explored2, final_path1, final_path2 = algo.rrt(start_point, goal_point, clearance)

  final_path2.pop(-1)
  final_path2.reverse()
  final_path1_spline = copy.deepcopy(final_path1)
  final_path1_spline.pop(-1)
  spline_pts1 = utils.cubic_spline(final_path1_spline)
  spline_pts2 = utils.cubic_spline(final_path2)
  final_path = final_path1 + final_path2
  final_spline_path = spline_pts1 + spline_pts2
  print('The final path is:', final_path)
  
  goal = Point()
  for points in final_spline_path:
    goal.x = points[0]
    goal.y = points[1]
    print('Point:', (points[0], points[1]))
    while not rospy.is_shutdown():
      inc_x = goal.x -x
      inc_y = goal.y -y
      
      angle_to_goal = atan2(inc_y, inc_x)
      print('Angle diff:', angle_to_goal - theta)
      if angle_to_goal - theta > 0:
        if abs(angle_to_goal - theta) > 0.05:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.1
        else:
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = 0.0
      else:
        if abs(angle_to_goal - theta) > 0.05:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = -0.1
        else:
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = 0.0
      #print('Distance to next point:', math.sqrt((inc_x)**2 + (inc_y)**2))
      if math.sqrt((inc_x)**2 + (inc_y)**2) < 0.03:
        break 
      pub.publish(vel_msg)
      r.sleep() 
  vel_msg.linear.x = 0.0
  vel_msg.angular.z = 0.0
  pub.publish(vel_msg)    
    
  
  
  # Plotting the explored nodes and final path
  points1x = []
  points1y = []
  points2x = []
  points2y = []
  points3x = []
  points3y = []
  points4x = []
  points4y = []
  points5x = []
  points5y = []
  points6x = []
  points6y = []
  points7x = []
  points7y = []
  points8x = []
  points8y = []
  
  for point in explored1.keys():
    points1x.append(point[0])
    points1y.append(point[1])
    points2x.append(explored1[point][0]-point[0])
    points2y.append(explored1[point][1]-point[1])
  
  for point in explored2.keys():
    points3x.append(point[0])
    points3y.append(point[1])
    points4x.append(explored2[point][0]-point[0])
    points4y.append(explored2[point][1]-point[1])
 
  
  for point in range(len(final_path)):
    if point+1 < len(final_path):
      points5x.append(final_path[point][0])
      points5y.append((final_path[point][1]))
      points6x.append((final_path[point+1][0])-(final_path[point][0]))
      points6y.append((final_path[point+1][1])-(final_path[point][1]))
    else:
      points5x.append(final_path[point][0])
      points5y.append((final_path[point][1]))
      points6x.append((final_path[-1][0])-(final_path[point][0]))
      points6y.append((final_path[-1][1])-(final_path[point][1]))
  """
  for point in range(len(final_path2)):
    if point+1 < len(final_path2):
      points7x.append(final_path2[point][0])
      points7y.append((final_path2[point][1]))
      points8x.append((final_path2[point+1][0])-(final_path2[point][0]))
      points8y.append((final_path2[point+1][1])-(final_path2[point][1]))
    else:
      points7x.append(final_path2[point][0])
      points7y.append((final_path2[point][1]))
      points8x.append((final_path2[-1][0])-(final_path2[point][0]))
      points8y.append((final_path2[-1][1])-(final_path2[point][1]))
  """
  plt.quiver(np.array(points1x), np.array(points1y), np.array(points2x), np.array(points2y), units='xy' ,scale=1, label = 'Explored nodes', color = 'g', width =0.02, headwidth = 1,headlength=0)
  plt.quiver(np.array(points3x), np.array(points3y), np.array(points4x), np.array(points4y), units='xy' ,scale=1, label = 'Explored nodes', color = 'g', width =0.02, headwidth = 1,headlength=0)
  plt.quiver(np.array(points5x), np.array(points5y), np.array(points6x), np.array(points6y), units='xy' ,scale=1, label = 'Final Path', width =0.07, headwidth = 1,headlength=0)  
  #plt.quiver(np.array(points7x), np.array(points7y), np.array(points8x), np.array(points8y), units='xy' ,scale=1, label = 'Final Path', width =0.07, headwidth = 1,headlength=0)  
  
  plt.show()
  plt.close()
  
if __name__ == '__main__':
  main()
