"""
RRT Algo 
Reference: rrt.py written by Steve LaValle in May 2011

Authors: 
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import random, math

XDIM = 10
YDIM = 10
EPSILON = 0.2
NUMNODES = 1000

# Function to calculate the Euclidean distance between 2 points
def dist(p1,p2):
  return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

# Function to find the point b/w the random point and the nearest node in the tree
def interpolate(p1,p2):
  if dist(p1,p2) < EPSILON:
    return p2
  else:
    theta = atan2(p2[1]-p1[1], p2[0]-p1[0])
    return p1[0] + EPSILON*cos(theta), p1[1] + EPSILON*sin(theta)  
  
# Function to implement rrt algo
# Args: (start point, goal point)
def rrt(start, goal):
  nodes = []
  nodes.append(start)
  
  # Running the algo for 'NUMNODES' number of iterations
  for i in range(NUMNODES):
    rand = random.random()*XDIM, random.random()*YDIM 
    nearest_node = nodes[0]
    for p in nodes:
      if dist(p, rand) < dist(nearest_node, rand):
        nearest_node = p
    new_node = interpolate(nearest_node, rand)
    nodes.append(new_node)
  
  return nodes
      
          
