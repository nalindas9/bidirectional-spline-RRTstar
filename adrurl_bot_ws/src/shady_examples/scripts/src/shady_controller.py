#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from numpy import inf
from std_msgs.msg import String

distance = 0
def velocity_publisher(distance):

  # Velocity publisher
  vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  rospy.init_node('shady_robot_velocity_publisher', anonymous=True)
  
  if distance >= 6:
	  msg = Twist()

	  msg.linear.x = 0.5
	  msg.linear.y = 0
	  msg.linear.z = 0
	  msg.angular.x = 0
	  msg.angular.y = 0
	  msg.angular.z = 0
  else:
	  msg = Twist()

	  msg.linear.x = -0.5
	  msg.linear.y = 0
	  msg.linear.z = 0
	  msg.angular.x = 0
	  msg.angular.y = 1
	  msg.angular.z = 0

  rate = rospy.Rate(10) # 10hz
  
  while not rospy.is_shutdown():
    vel_pub.publish(msg)
    print('The given velocities are::', msg)
    rate.sleep()

def callback(msg):
	print ('The distance from the left is:', msg.ranges[0], 'The distance from the front is:',     msg.ranges[360],'The distance from the right is:', msg.ranges[719])
	distance = msg.ranges[360]
		
	#dist = str(distance)
	#callback_pub.publish(dist)
	


if __name__ == '__main__':
  if len(sys.argv) == 1:
    try: 
      sub = rospy.Subscriber('/shady/laser/scan', LaserScan, callback)
  
      velocity_publisher(distance)
    except rospy.ROSInterruptException:
      print('Shutting down the velocity publisher. Have a nice day!')
      pass
  else:
    print("Usage: rosrun shady_examples shady_obstacle_avoider.py")

