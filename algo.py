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
import numpy as np

XDIM = 10
YDIM = 10
EPSILON = 0.2
NUMNODES = 1800
plusminus = [1,-1]

explored_nodes1 = dict()
explored_nodes2 = dict()

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

# Function to check if two points can be joined without collision
def valid_joint(p1,p2, clearance):
  delta = np.linspace(0, math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2), num=20) 
  theta = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
  points = []
  for i in delta:
    inter_point = (p1[0] + i*math.cos(theta), p1[1] + i*math.sin(theta))   
    points.append(inter_point)
    if not utils.check_node(inter_point, clearance): 
      return False
  print('Points', points)
  return True
  
# Function to implement rrt algo
# Args: (start point, goal point)
def rrt(start, goal, clearance):
  nodes1 = []
  start1 = tuple(start)
  explored_nodes1[start1] = start1
  nodes1.append(start1)
  
  nodes2 = []
  start2 = tuple(goal)
  explored_nodes2[start2] = start2
  nodes2.append(start2)
  # Running the algo for 'NUMNODES' number of iterations
  for i in range(NUMNODES):
    
    # Tree generation from start node
    rand1 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus) 
    while not utils.check_node(rand1, clearance):
      rand1 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus)
    nearest_node1 = nodes1[0]
    for p1 in nodes1:
      if dist(p1, rand1) < dist(nearest_node1, rand1):
        nearest_node1 = p1
    new_node1 = interpolate(nearest_node1, rand1)
    if utils.check_node(new_node1, clearance):
      explored_nodes1[new_node1] = nearest_node1
      nodes1.append(new_node1)
    
    
    # Check if the new node from tree 1 can be joined to tree 2 
    nearest_node3 = nodes2[0]   
    for p in nodes2:
      if dist(p, new_node1) < dist(nearest_node3, new_node1):
        nearest_node3 = p 
    if valid_joint(new_node1,nearest_node3, clearance):
      print('Joint from tree 1 to tree 2 found!!')
      explored_nodes1[nearest_node3] = new_node1 
      return explored_nodes1, explored_nodes2
    else:
      # Tree generation from goal node
      rand2 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus) 
      while not utils.check_node(rand2, clearance):
        rand2 = random.random()*(XDIM/2)*random.choice(plusminus), random.random()*(YDIM/2)*random.choice(plusminus)
      nearest_node2 = nodes2[0]
      for p2 in nodes2:
        if dist(p2, rand2) < dist(nearest_node2, rand2):
          nearest_node2 = p2
      new_node2 = interpolate(nearest_node2, rand2)
      if utils.check_node(new_node2, clearance):
        explored_nodes2[new_node2] = nearest_node2
        nodes2.append(new_node2)
    
    # Again check if the new node from tree 1 can be joined to tree 2 
    nearest_node3 = nodes2[0]   
    for p in nodes2:
      if dist(p, new_node1) < dist(nearest_node3, new_node1):
        nearest_node3 = p 
    if valid_joint(new_node1,nearest_node3, clearance):
      print('Joint from tree 1 to tree 2 found!!')
      explored_nodes2[nearest_node3] = new_node1 
      return explored_nodes1, explored_nodes2
    """
    # Check if the new node from tree 2 can be joined to tree 1 
    nearest_node4 = nodes1[0]   
    for p in nodes1:
      if dist(p, new_node2) < dist(nearest_node4, new_node2):
        nearest_node4 = p 
    if valid_joint(new_node2,nearest_node4, clearance):
      print('Joint from tree 2 to tree 1 found!!')
      explored_nodes[nearest_node4] = new_node2
      return explored_nodes
    """  
    """
    if ((new_node1[0] - goal[0]) ** 2 + (new_node1[1] - goal[1]) ** 2) <= 0.25 ** 2:
      print('Found the goal!!!')
      final_path = back_track(new_node1, start)
    """
  return explored_nodes1, explored_nodes2
      
          
