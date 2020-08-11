# bidirectional-spline-RRTstar
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/nalindas9/bidirectional-spline-RRTstar/blob/master/LICENSE)

## About
This is the repository for the project - Implementation of Bidirectional Spline RRT* for a Non-holonomic Mobile Robot. Implemented the Bidirectional Spline RRT* for path Planning for the Turtlebot3 robot. Though on the application of spline-based smoothing the path length increases fractionally, the smoothened trajectory is much more feasible for the robot to follow.

## 2D Obstacle Space

### System and library requirements.
 - Python3
 - Numpy
 - matplotlib
 - math
 - Scipy
 
### How to Run
1. Clone this repo or extract the "proj5_Nalin_Nidhi.zip" file. <br>
2. Navigate to the folder "Code/2D_Obstacle_space" <br>
3. To run the code, from the terminal, run the command `python3 main.py` <br>
4. The program will ask for the clearance (in meters) from the obstacles, provide input in 'float' format. For eg: 0.2<br>
5. Next program will ask for start point, provide input in [x,y,theta] format. For eg: [-4,3,0]. If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.<br>
6. Next program will ask for goal point, provide input in [x,y,theta] format. For eg: [4,-3, 0].
If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.<br>
7. To view the simulation video for the following parameters - 
Start : (-4, 4, 0)
Goal : (4, -4, 0)
Clearance : 0.1 meters
Navigate to the folder "Outputs/2D_Obstacle_space". Open the video "testcase3.avi"<br>

The blue circle is the start point, and the yellow circle is the goal with threshold radius of 0.25 meters. The green color is for the explored nodes, while the black color signifies the final path. The red color is after spline smoothing has been applied.

## 3D Obstacle Space

## System and library requirements.
 - Python3
 - Numpy
 - matplotlib
 - math
 - Scipy
 - ROS Kinetic (Ubuntu 16.04)
 - Gazebo 7.0.0
 
## How to Run
1. Clone this repo or extract the "proj5_Nalin_Nidhi.zip" file. <br>
2. Navigate to the folder "Code/2D_Obstacle_space" <br>
3. To run the simulation, firstly navigate to the "adrurlbot_ws" folder. <br>
4. Enter the command "catkin_make" inside this folder to initialize it as a ROS workspace.
Once you have done this, go back to home and then source this ROS workspace using "source <path to setup.bash>"
5. Once this is done, you can run the turtlebot 3 Gazebo world simulation using the command - "roslaunch turtlebot3_astar turtlebot3_gazebo_astar.launch x_pos:=0.0 y_pos:=-3.0 yaw:=0.0". Here you can set the start point for the robot to spawn. x_pos --> x-coordinate, y_pos --> y-coordinate, yaw --> Initial orientation of robot w.r.t world x-axis. Ensure that the start point you give here is the same start point you give later when asked again.
6. The program will ask for the clearance (in meters) from the obstacles, provide input in 'float' format. For eg: 0.2<br>
5. Next program will ask for start point, provide input in [x,y,theta] format. For eg: [-4,3,0]. If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.<br>
6. Next program will ask for goal point, provide input in [x,y,theta] format. For eg: [4,-3, 0].
If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.<br>
7. Voila! You should see the Turtlebot 3 follow the planned path to reach the goal and stop.
8.  To view the simulation video for the following parameters - 
Start : (-4, 4, 0)
Goal : (4, -4, 0)
Clearance : 0.1 meters
Navigate to the folder "Outputs/3D_Obstacle_space". Open the video "testcase1.avi"<br>


