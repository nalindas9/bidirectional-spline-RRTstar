#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
 


rospy.init_node('distance_scan_values')
print('Laser Scanner Started!')

if __name__ == '__main__':
	
	
	rospy.spin()




