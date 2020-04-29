"""
RRT Algo 
Reference: rrt.py written by Steve LaValle in May 2011

Authors: 
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import random, math
import utils

XDIM = 10
YDIM = 10
EPSILON = 0.2
NUMNODES = 1800
plusminus = [1,-1]

explored_nodes = dict()

# Function to generate index given a node
def index(node):
  return (node[0], node[1], node[2])

# Function to find the path
def back_track(node_ind, start_node):
    print('Backtracking to find the best possible path ...')
    path = [node_ind]
    while node_ind != index(start_node):
      parent = explored_nodes[node_ind]
      path.insert(0, parent)
      node_ind = parent
    print('The path is:', path)
    print('Backtracking complete.')
    return path

# Function to calculate the Euclidean distance between 2 points
def dist(p1,p2):
  return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

# Function to find the point b/w the random point and the nearest node in the tree
def interpolate(p1,p2):
  if dist(p1,p2) < EPSILON:
    return p2
  else:
    theta = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    return p1[0] + EPSILON*math.cos(theta), p1[1] + EPSILON*math.sin(theta)  

def check_obstacle(p1,p2):
  y = p2[1] + ((p2[1]-p1[1])/(p2[0]-p1[0]))*(x - p1[0])
  for i in range(20)
  
# Function to implement rrt algo
# Args: (start point, goal point)
def rrt(start, goal, clearance):
  nodes1 = []
  nodes2 = []
  start1 = tuple(start)
  start2 = tuple(goal)
  explored_nodes[start1] = start1
  explored_nodes[start2] = start2
  nodes1.append(start1)
  nodes2.append(start2)
  
  # Running the algo for 'NUMNODES' number of iterations
  for i in range(NUMNODES):
    rand1 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus) 
    rand2 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus) 
      
    while not utils.check_node(rand1, clearance):
      rand1 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus)
    while not utils.check_node(rand2, clearance):
      rand2 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus)
      
    nearest_node1 = nodes1[0]
    nearest_node2 = nodes2[0]
    for p in nodes1:
      if dist(p, rand1) < dist(nearest_node1, rand1):
        nearest_node1 = p
    new_node1 = interpolate(nearest_node1, rand1)
    if utils.check_node(new_node1, clearance):
      explored_nodes[new_node1] = nearest_node1
      nodes1.append(new_node1)
    for p in nodes2:
      if dist(p, new_node1) < dist(nearest_node2, new_node1):
        nearest_node2 = p
    internode1 = interpolate(nearest_node2, new_node1)
    if utils.check_node(internode1, clearance):
      explored_nodes[nearest_node2] = new_node1
      final_path = back_track(start2, start1)
      print('Found the path!!!')
      return explored_nodes, final_path
    
    for p in nodes2:
      if dist(p, rand2) < dist(nearest_node2, rand2):
        nearest_node2 = p
    new_node2 = interpolate(nearest_node2, rand2)
    if utils.check_node(new_node2, clearance):
      explored_nodes[nearest_node2] = new_node2
      nodes2.append(new_node2)
    for p in nodes1:
      if dist(p, new_node2) < dist(nearest_node1, new_node2):
        nearest_node1 = p
    internode2 = interpolate(nearest_node1, new_node2)
    if utils.check_node(internode2, clearance):
      explored_nodes[new_node2] = nearest_node1
      final_path = back_track(start2, start1)
      print('Found the path!!!')
      return explored_nodes, final_path
      
          
